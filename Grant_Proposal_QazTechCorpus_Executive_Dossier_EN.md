# EXECUTIVE GRANT PROPOSAL DOSSIER
## Development of the National Digital Corpus and Ontological Repository of Technologies (QazTechCorpus) Using Multi-Agent Scientific Reasoning and Knowledge Graphs

**Host Institution:** Satbayev University (Almaty, Kazakhstan)
**Principal Investigator:** Dr. Bulbul D. Karbozova, PhD, Associate Professor (`b.karbozova@satbayev.university`)
**Co-Investigator / Technical Lead:** Emir Y. Toksanov (`emirtoxsanov45@gmail.com`)
**Project Duration:** 36 Months (3 Stages, Modules 1 to 6, advancing from TRL 2 to TRL 7)
**Target Compute & AI Framework:** Google Antigravity Science (`google-deepmind/science-skills`), Gemini 4 Carbon & Argon API, Neo4j, OpenSearch, Kubernetes

---

### 1. Executive Summary

Over 50,000 scientific research reports, dissertations, patents, and engineering test protocols produced across universities and research institutes in Kazakhstan are stored as static, unstructured PDF files. Because these materials lack unified semantic markup, verified maturity scores, and cross-lingual indexing, valuable laboratory breakthroughs remain invisible to both international scientists and industrial engineers.

**QazTechCorpus** bridges computational corpus linguistics and neuro-symbolic artificial intelligence to convert passive archives into an active, machine-readable knowledge graph. Building on the structural heritage of the National Corpus of the Kazakh Language (`qazcorpus.kz`), the project introduces:
1. **OntoTech Ontology (OWL 2 DL):** A formal domain ontology (`O = <C, R, A, I, X>`) comprising over 250 classes and 80 object property types, aligned with DataCite 4.5, Qualified Dublin Core, WIPO ST.9, IPC/CPC, and OECD Frascati taxonomies.
2. **Digital Technology Passport:** A unified six-block faceted data structure that links R&D reports, patents, source code repositories, CAD blueprints, and empirical test protocols under two-tier access control (public Non-Confidential Abstracts modeled on Stanford TechFinder and restricted technical dossiers under electronic NDA).
3. **Multi-Agent Extraction and TRL Auditing Pipeline (Gemini 4 Carbon & Argon):** A four-agent workflow in Google Antigravity that combines morphological normalization for agglutinative Kazakh with long-context foundation models to extract 10 technical entity classes (`TechNER`) and verify Technology Readiness Levels (TRL 1 to 9 under ISO 16290:2013) with explicit documentary citations.
4. **Tri-Modal Hybrid Search Engine:** A retrieval architecture integrating BM25 lexical matching for chemical formulas and nomenclature codes, 1024-dimensional cross-lingual vector embeddings in OpenSearch, and multi-hop Cypher / SPARQL reasoning in Neo4j.

---

### 2. Multi-Agent Architecture in Google Antigravity

Rather than relying solely on short-context encoder models or manual curation by technology transfer staff, QazTechCorpus uses an autonomous multi-agent pipeline (`/swarm`) orchestrated in Google Antigravity:

| Agent Role | Model / Tooling | Core Scientific Responsibility | Output Artifact |
|---|---|---|---|
| **1. Harvester & OCR Cleaner** | Apache Airflow, `tbiocr`, OAI-PMH 2.0 | Polls university DSpace/Dataverse archives and patent registries; repairs Kazakh diacritics, tables, and formulas in scanned PDFs. | Normalized full-text document stream + morphological stems (`tbisozdik`). |
| **2. TechNER & Passport Synthesizer** | **Gemini 4 Argon & Carbon** + XLM-R / SciBERT baselines | Ingests full 50- to 100-page R&D reports in a single context window; extracts 10 entity classes (`TECH_ARTIFACT`, `QUANT_PARAM`, `TRL_EVIDENCE`, etc.). | Schema-validated JSON draft passport conforming to the 6 OntoTech facet blocks. |
| **3. ISO 16290 Evidence Auditor** | **Gemini 4 Carbon** (Long-horizon reasoning) | Adversarially audits the draft passport against raw experimental protocols and tables; verifies TRL 1 to 9 thresholds with verbatim page quotes. | Calibrated probability distribution over TRL 1 to 9 + audit trail of evidence spans. |
| **4. Knowledge Graph & Sanitization Agent** | OWL 2 Reasoner, Neo4j, Gemini 4 Argon | Checks description logic axioms (`X`), strips unpublished trade secrets from public fields, and writes trilingual abstracts (KZ, RU, EN). | Verified Non-Confidential Abstract + RDF/Cypher triples in Neo4j. |

---

### 3. Scientific Novelty and Open Science Contributions

1. **Cross-Domain Transfer from Corpus Linguistics to Knowledge Engineering:** First formal adaptation of the three-level linguistic architecture of `qazcorpus.kz` (subcorpus segmentation, metadata window, morphological processors) to engineering and R&D documentation.
2. **Open 5,000-Document Trilingual Gold Benchmark:** Creation and public release of an expert-annotated dataset of 5,000 scientific texts in Kazakh, Russian, and English labeled across 10 engineering entity classes and 9 ISO 16290 maturity levels.
3. **Neuro-Symbolic TRL Verification:** Combining deterministic documentary rules with long-context LLM evidence auditing to eliminate subjective self-reporting of technology readiness levels.
4. **Hybrid Lexical-Vector-Graph Retrieval (`S(q, d)`):** Empirical calibration of combined BM25, dense cross-lingual vector similarity, and Neo4j structural connectivity for sub-150 ms technical search.

---

### 4. Implementation Roadmap and Measurable Milestones

- **Stage I (Months 1 to 12, TRL 2 -> TRL 4, Modules 1 & 2):**
  - Formal specification of the `OntoTech` OWL 2 ontology in Protege (250+ classes, 80+ object properties).
  - Deployment of OAI-PMH 2.0 harvesters and scientific OCR cleaning (`tbiocr`); compilation of an initial verified trilingual corpus of **15,000 R&D documents and patents**.
  - Deployment of the containerized tri-modal storage cluster (Neo4j, OpenSearch, PostgreSQL, S3/MinIO) with **25,000 nodes and 120,000 semantic triples** (Module 3).
- **Stage II (Months 13 to 24, TRL 4 -> TRL 5, Module 4):**
  - Annotation and public release of the **5,000-document trilingual Gold Benchmark**.
  - Benchmarking fine-tuned encoders (XLM-RoBERTa, SciBERT-CRF) against Gemini 4 Carbon and Argon multi-agent workflows; achieving **TechNER macro-F1 >= 0.86** and **TRL classification accuracy >= 0.82**.
- **Stage III (Months 25 to 36, TRL 5 -> TRL 7, Modules 5 & 6):**
  - Launch of the trilingual web portal featuring faceted search, interactive subgraph visualization, innovation scout workspaces, e-NDA virtual data rooms, and Click-to-Licence / ExpressPath generators.
  - Scaling the repository to **50,000 Digital Technology Passports and 250,000 semantic triples**, with Open API integration across university CRIS systems and industrial R&D partners.

---

### 5. Justification of Compute Budget for Google Antigravity Science Grant

In our national grant proposal, substantial funds were originally earmarked for purchasing local on-premise GPU servers and commercial API quotas. Receiving the **Google Antigravity Science 6-month Highest Usage Tier grant (Gemini 4 Carbon and Argon)** directly replaces local hardware bottlenecks and enables immediate execution of Stage I and Stage II experiments:
- **Batch ingestion of 50,000 full-text reports:** ~2.0 billion input tokens and ~150 million structured output tokens for end-to-end OntoTech passport generation and trilingual summarization.
- **Multi-agent adversarial TRL auditing:** ~500 million reasoning tokens on Gemini 4 Carbon to cross-examine experimental tables, patent claims, and ISO 16290 criteria across the 5,000-document gold benchmark and full repository.
