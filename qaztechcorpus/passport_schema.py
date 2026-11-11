# -*- coding: utf-8 -*-
"""
QazTechCorpus: OntoTech Digital Technology Passport Schema, TechNER Entity Validator,
ISO 16290 TRL Evidence Auditor, and Hybrid Lexical-Vector-Graph Retrieval Scoring.

Authors:
    Bulbul D. Karbozova (b.karbozova@satbayev.university)
    Emir Y. Toksanov (emirtoxsanov45@gmail.com)
Institution:
    Satbayev University (Almaty, Kazakhstan)
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Sequence
import math


class TechNERLabel(str, Enum):
    """Ten domain-specific named entity classes extracted by the TechNER module."""

    TECH_ARTIFACT = "TECH_ARTIFACT"
    TECH_METHOD = "TECH_METHOD"
    QUANT_PARAM = "QUANT_PARAM"
    MATERIAL = "MATERIAL"
    EQUIPMENT = "EQUIPMENT"
    SOFTWARE_STACK = "SOFTWARE_STACK"
    DOMAIN = "DOMAIN"
    IP_STD = "IP_STD"
    TRL_EVIDENCE = "TRL_EVIDENCE"
    ORG = "ORG"


class LicensingMode(str, Enum):
    """Supported transfer and licensing protocols."""

    CLICK_TO_LICENCE_ACADEMIC = "Click-to-Licence (Academic Use)"
    CLICK_TO_LICENCE_COMMERCIAL = "Click-to-Licence (Commercial Use)"
    EXPRESS_PATH_STARTUP = "Harvard ExpressPath Startup License"
    SPONSORED_RESEARCH = "Sponsored R&D Contract"
    RESTRICTED_ENDA_DATAROOM = "Virtual Data Room under e-NDA"


@dataclass(frozen=True)
class ExtractedEntity:
    """Single span or structured entity extracted from a trilingual R&D document."""

    label: TechNERLabel
    surface_form: str
    normalized_stem: str
    language: str  # 'kk', 'ru', or 'en'
    confidence: float
    page_number: int


@dataclass(frozen=True)
class TRLEvidenceCitation:
    """Verifiable documentary citation supporting an ISO 16290 TRL assessment."""

    claimed_trl: int
    artifact_type: str  # e.g., 'analytical_calc', 'lab_protocol', 'patent', 'pilot_act'
    verbatim_quote: str
    page_reference: str
    verified_by_auditor: bool


@dataclass
class DigitalTechnologyPassport:
    """
    Six-block faceted Digital Technology Passport governed by the OntoTech OWL 2 ontology.
    """

    # Block 1: Identification
    passport_id: str
    doi_or_handle: str
    project_registration_number: str
    title_kk: str
    title_ru: str
    title_en: str
    version: str = "1.0.0"
    linked_publications: List[str] = field(default_factory=list)

    # Block 2: Engineering and Industry Taxonomy
    ipc_cpc_codes: List[str] = field(default_factory=list)
    oecd_fos_codes: List[str] = field(default_factory=list)
    industrial_tags: List[str] = field(default_factory=list)

    # Block 3: Technical Specification and Open Abstract
    non_confidential_abstract_en: str = ""
    engineering_problem_solved: str = ""
    quantitative_parameters: Dict[str, str] = field(default_factory=dict)
    hardware_software_stack: List[str] = field(default_factory=list)

    # Block 4: ISO 16290:2013 Maturity Verification (TRL 1 to 9)
    assessed_trl: int = 1
    trl_probabilities: Dict[int, float] = field(default_factory=dict)
    trl_evidence_citations: List[TRLEvidenceCitation] = field(default_factory=list)

    # Block 5: Legal Status and IP Protection
    ip_object_type: str = "R&D Report"
    patent_registry_number: Optional[str] = None
    rightsholder_organization: str = "Satbayev University"
    author_orcids: List[str] = field(default_factory=list)

    # Block 6: Transfer and Licensing Profile
    licensing_modes: List[LicensingMode] = field(default_factory=list)
    enda_required_for_dossier: bool = True

    def validate_iso_16290_consistency(self) -> bool:
        """
        Deterministic production rule check for ISO 16290 TRL consistency (Axiom set X).
        """
        if not (1 <= self.assessed_trl <= 9):
            return False
        if self.assessed_trl >= 4:
            has_lab_or_higher = any(
                c.verified_by_auditor and c.claimed_trl >= 4
                for c in self.trl_evidence_citations
            )
            if not has_lab_or_higher:
                return False
        return True


def macro_f1_score(
    precisions: Sequence[float], recalls: Sequence[float]
) -> float:
    """
    Computes macro-averaged F1 across K = 10 TechNER entity classes (Equation 2).
    """
    if len(precisions) != len(recalls) or not precisions:
        raise ValueError("Precision and recall sequences must be non-empty and of equal length.")
    k = len(precisions)
    total = 0.0
    for p_k, r_k in zip(precisions, recalls):
        if p_k + r_k > 0:
            total += (2.0 * p_k * r_k) / (p_k + r_k)
    return total / float(k)


def cosine_similarity(v_q: Sequence[float], v_d: Sequence[float]) -> float:
    """Computes cosine similarity between dense cross-lingual embeddings."""
    dot = sum(a * b for a, b in zip(v_q, v_d))
    norm_q = math.sqrt(sum(a * a for a in v_q))
    norm_d = math.sqrt(sum(b * b for b in v_d))
    if norm_q == 0.0 or norm_d == 0.0:
        return 0.0
    return dot / (norm_q * norm_d)


def hybrid_retrieval_score(
    s_bm25: float,
    v_q: Sequence[float],
    v_d: Sequence[float],
    s_graph: float,
    alpha: float = 0.35,
    beta: float = 0.45,
    gamma: float = 0.20,
) -> float:
    """
    Computes the linear combination ranking score S(q, d) (Equation 3):
        S(q, d) = alpha * S_BM25(q, d) + beta * cos(v_q, v_d) + gamma * S_graph(q, d)
    where alpha + beta + gamma = 1.
    """
    if not math.isclose(alpha + beta + gamma, 1.0, rel_tol=1e-5):
        raise ValueError("Weights alpha, beta, gamma must sum to 1.0")
    cos_sim = cosine_similarity(v_q, v_d)
    return alpha * s_bm25 + beta * cos_sim + gamma * s_graph


if __name__ == "__main__":
    sample_passport = DigitalTechnologyPassport(
        passport_id="QTC-2026-0001",
        doi_or_handle="10.5281/zenodo.qaztechcorpus.0001",
        project_registration_number="BR2026-SATBAYEV-01",
        title_kk="Технологиялардың цифрлық корпусы мен онтологиялық репозитарийі",
        title_ru="Цифровой корпус и онтологический репозиторий технологий",
        title_en="Digital Corpus and Ontological Repository of Technologies (QazTechCorpus)",
        ipc_cpc_codes=["G06F 16/36", "G06N 5/02"],
        oecd_fos_codes=["1.2 Computer and information sciences"],
        assessed_trl=4,
        trl_evidence_citations=[
            TRLEvidenceCitation(
                claimed_trl=4,
                artifact_type="lab_protocol",
                verbatim_quote="Validated on 5,000 trilingual scientific documents with macro-F1 >= 0.86.",
                page_reference="Section 5, p. 11",
                verified_by_auditor=True,
            )
        ],
        author_orcids=["0000-0002-9287-5319"],
        licensing_modes=[LicensingMode.CLICK_TO_LICENCE_ACADEMIC],
    )
    assert sample_passport.validate_iso_16290_consistency()
    print(f"Passport {sample_passport.passport_id} validated successfully (TRL {sample_passport.assessed_trl}).")
