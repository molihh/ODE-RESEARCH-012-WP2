"""Unified Oracle Envelope for WP2 four-mode factory."""
from __future__ import annotations
import hashlib, json
from dataclasses import dataclass, field, replace

STATUSES = {"VALID", "CONFLICT", "INSUFFICIENT_EVIDENCE", "INVALID", "REVIEW_REQUIRED"}
MODES = {"A", "B", "C", "D"}

def canonical(value) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def sha(value) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    source_uri: str
    locator: str
    quote: str
    source_sha256: str
    kind: str = "official"
    def body(self):
        return {"evidence_id": self.evidence_id, "source_uri": self.source_uri,
                "locator": self.locator, "quote": self.quote,
                "source_sha256": self.source_sha256, "kind": self.kind}

@dataclass
class OracleEnvelope:
    oracle_id: str
    oracle_version: str
    task_id: str
    task_type: str
    method_id: str
    oracle_mode: str
    construction_strategy: str
    asset_id: str
    asset_version: str
    asset_sha256: str
    claims: dict
    evidence: list[Evidence]
    constraints: list[str] = field(default_factory=list)
    provenance: dict = field(default_factory=dict)
    independence: dict = field(default_factory=dict)
    validation: dict = field(default_factory=dict)
    status: str = "VALID"
    content_hash: str = ""
    schema_version: str = "ode.oracle-envelope/1"

    def __post_init__(self):
        self.evidence = [Evidence(**e) if isinstance(e, dict) else e for e in self.evidence]
        if self.oracle_mode not in MODES:
            raise ValueError("ORACLE_MODE_INVALID")
        if self.status not in STATUSES:
            raise ValueError("ORACLE_STATUS_INVALID")
        if not self.oracle_id or not self.task_id or not self.asset_id:
            raise ValueError("ORACLE_IDENTITY_MISSING")
        ids = [e.evidence_id for e in self.evidence]
        if len(set(ids)) != len(ids):
            raise ValueError("ORACLE_EVIDENCE_DUPLICATE")
        if self.status == "VALID" and not self.evidence:
            raise ValueError("ORACLE_EVIDENCE_REQUIRED")
        if self.status == "VALID" and not isinstance(self.claims, dict):
            raise ValueError("ORACLE_CLAIMS_INVALID")

    def private(self):
        return {
            "schema_version": self.schema_version,
            "oracle_id": self.oracle_id, "oracle_version": self.oracle_version,
            "task_id": self.task_id, "task_type": self.task_type,
            "method_id": self.method_id, "oracle_mode": self.oracle_mode,
            "construction_strategy": self.construction_strategy,
            "asset_id": self.asset_id, "asset_version": self.asset_version,
            "asset_sha256": self.asset_sha256, "claims": self.claims,
            "evidence": [e.body() for e in self.evidence],
            "constraints": list(self.constraints),
            "provenance": dict(self.provenance), "independence": dict(self.independence),
            "validation": dict(self.validation), "status": self.status,
        }

    def public(self):
        """Metadata safe for TE/UI; claims are replaced by a hash, never exposed."""
        value = self.private(); value.pop("claims")
        value["claims_sha256"] = sha(self.claims)
        value["content_hash"] = self.content_hash
        return value

    def evaluation(self):
        value = self.private(); value["content_hash"] = self.content_hash
        return value

    def compute_hash(self):
        return sha(self.private())

    def seal(self):
        self.content_hash = self.compute_hash()
        return self

    def verify_hash(self):
        return bool(self.content_hash) and self.content_hash == self.compute_hash()

    def transition(self, status, *, reason=""):
        if status not in STATUSES:
            raise ValueError("ORACLE_STATUS_INVALID")
        self.status = status
        self.validation = dict(self.validation, reason=reason)
        return self
