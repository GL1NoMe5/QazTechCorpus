# RESEARCH STATEMENT
## Building an Open Multilingual Scientific Knowledge Graph and Multi-Agent TRL Verification System (QazTechCorpus)

**Applicants:**
- **Principal Investigator:** Dr. Bulbul D. Karbozova, PhD, Associate Professor, Satbayev University (Kazakh National Research Technical University named after K.I. Satpayev), Almaty, Kazakhstan (`b.karbozova@satbayev.university`)
- **Co-Investigator / Research Lead:** Emir Y. Toksanov, Undergraduate Researcher, Satbayev University (`emirtoxsanov45@gmail.com`)

**Institution:** Satbayev University (Non-profit public research university)
**Research Nature:** 100% Non-commercial academic research and Open Science infrastructure
**Primary Disciplines:** Computational Linguistics, Natural Language Processing, Knowledge Graphs (OWL 2 / GraphRAG), Automated Scientific Reasoning

---

### 1. Research Problem and Scientific Motivation

Across Central Asia, more than 50,000 completed research and development (R&D) project reports, doctoral dissertations, patent specifications, and laboratory test protocols remain locked inside fragmented institutional archives as unstructured, often scanned PDF documents written in a mix of Kazakh, Russian, and English. Because these records lack machine-readable semantic markup, researchers and engineers cannot search past experimental findings by quantitative physical or algorithmic parameters, cannot automatically verify the empirical maturity of a reported technology under the ISO 16290:2013 Technology Readiness Level (TRL 1 to 9) standard, and frequently duplicate prior laboratory work.

Building an automated extraction and verification system for this corpus presents two fundamental computer science challenges:
1. **Low-resource agglutinative morphology in technical domains:** In Kazakh technical writing, domain terms undergo extensive suffixation (case, possessive, and plural morphemes attached to multi-word engineering compounds), causing severe token sparsity for standard subword encoders such as XLM-RoBERTa or SciBERT.
2. **Long-horizon document reasoning for empirical maturity verification:** Determining whether a technology has genuinely reached TRL 4 (laboratory validation) or TRL 6 (prototype tested in a relevant environment) cannot be solved by sentence-level classification. It requires cross-referencing claims in the executive summary against mathematical derivations, CAD schematics, tables of experimental measurements, and signed test protocols spread across 50- to 120-page technical reports.

---

### 2. Proposed Methodology and Role of Google Antigravity and Gemini 4 Carbon

Our project, **QazTechCorpus**, extends the structural principles of the National Corpus of the Kazakh Language (`qazcorpus.kz`) into an open neuro-symbolic repository governed by the **OntoTech** ontology (over 250 OWL 2 DL classes and 80 object properties stored in Neo4j).

To overcome the context-length and reasoning limitations of legacy encoder models, we use **Google Antigravity** and **Gemini 4 Carbon** as the core multi-agent scientific reasoning engine across a four-agent pipeline (`/swarm` architecture):

1. **Multimodal Ingestion and Morphological Normalization Agent:** Processes multi-page scanned R&D reports, cleans OCR artifacts on Kazakh diacritics and chemical/mathematical formulas (`tbiocr`), and normalizes agglutinative stems using the `tbisozdik` terminological base.
2. **Long-Context TechNER and Schema Synthesis Agent (Gemini 4 Carbon + Argon):** Ingests full-length R&D reports (40,000 to 100,000 tokens per document) in a single context window to extract ten classes of technical entities (`TECH_ARTIFACT`, `TECH_METHOD`, `QUANT_PARAM`, `MATERIAL`, `EQUIPMENT`, `SOFTWARE_STACK`, `DOMAIN`, `IP_STD`, `TRL_EVIDENCE`, and `ORG`) and emit schema-validated JSON technology passports conforming to the six faceted blocks of OntoTech, DataCite 4.5, and Qualified Dublin Core.
3. **Adversarial ISO 16290 TRL Evidence Auditor Agent (Gemini 4 Carbon):** Acts as an independent scientific verifier. Given a draft passport and the source report, the agent checks whether claimed readiness levels are backed by explicit documentary proof (e.g., matching numerical efficiency or purity figures in laboratory tables against TRL 4 to 7 thresholds), flagging unsupported claims and citing exact page and table evidence.
4. **Open Science Sanitization and Trilingual Synthesis Agent:** Separates proprietary pre-patent details from public scientific data to generate verified Non-Confidential Abstracts in Kazakh, Russian, and English, alongside consistent RDF/Neo4j semantic triples (`O = <C, R, A, I, X>`).

---

### 3. Why Gemini 4 Carbon and Antigravity Science Access Are Needed

Running multi-step verification and structured extraction over a 50,000-document trilingual archive is not feasible under standard consumer rate limits:
- **Full-corpus long-context processing:** Extracting structured OntoTech passports and auditing TRL evidence across 50,000 full-text R&D reports (~40,000 tokens average length) requires processing roughly **2.0 billion input tokens** and **150 million structured output tokens**.
- **Adversarial multi-agent verification (`/swarm`):** Our experimental design compares single-pass extraction against multi-agent verification where a Gemini 4 Carbon verifier critiques and corrects extractions made by lighter models (Gemini 4 Argon and fine-tuned XLM-RoBERTa/SciBERT baselines).
- **Benchmarking frontier reasoning on low-resource scientific text:** Access to Gemini 4 Carbon allows us to run systematic ablation studies comparing classical encoder+CRF pipelines against frontier reasoning models on agglutinative Kazakh and code-switched Russian/Kazakh technical prose.

---

### 4. Twelve-Month Research Plan and Open Science Deliverables

- **Months 1 to 3 (Ontology and Gold Benchmark Construction):** Release the formal `OntoTech` OWL 2 ontology (250+ classes) on GitHub and compile an expert-annotated Gold Benchmark of **5,000 trilingual scientific and technical documents** labeled for 10 TechNER entity classes and ISO 16290 TRL levels.
- **Months 4 to 6 (Multi-Agent Pipeline and Ablation Experiments):** Implement the 4-agent extraction and TRL auditing workflow in Google Antigravity; benchmark Gemini 4 Carbon and Argon against XLM-RoBERTa-large and SciBERT-CRF (target macro-F1 >= 0.86 for TechNER and >= 0.82 accuracy for TRL verification).
- **Months 7 to 12 (Corpus Scaling and Public Repository Release):** Process the 50,000-document archive into the tri-modal backend (Neo4j knowledge graph with 250,000+ semantic triples, OpenSearch vector index, PostgreSQL) and publish the open datasets, evaluation code, and research findings at top peer-reviewed NLP and Semantic Web venues (ACL, EMNLP, LREC-COLING, ISWC).

All code, ontology specifications (`OntoTech`), evaluation scripts, and the 5,000-document annotated trilingual benchmark will be released publicly under open academic licenses (Apache 2.0 / CC-BY 4.0).

---

### 5. Ready-to-Paste Short Answers for the Google Form (`https://forms.gle/WvmBbPvRbpKG1BPn9`)

- **Organization / Institution:** Satbayev University (Kazakh National Research Technical University named after K.I. Satpayev)
- **Institutional Email:** `b.karbozova@satbayev.university`
- **Role:** Principal Investigator / Professor (Dr. Bulbul Karbozova) & Undergraduate Researcher (Emir Toksanov)
- **Research Field:** Computer Science & AI / Computational Linguistics, Knowledge Graphs, and Scientific Information Extraction
- **Research Methodology:** Computational / Dry Lab
- **Short Project Description (for 1-paragraph form field):**
  We are building QazTechCorpus, the first open trilingual (Kazakh, Russian, English) scientific knowledge graph and automated Technology Readiness Level (TRL 1 to 9) verification benchmark at Satbayev University. The project processes 50,000 unstructured R&D reports, dissertations, and patents into formal OWL 2 ontologies (OntoTech) and Neo4j knowledge graphs. We use Google Antigravity's multi-agent `/swarm` workflows and Gemini 4 Carbon's long-context reasoning to ingest 50- to 100-page technical reports in a single pass, extract 10 classes of engineering entities (TechNER) in agglutinative Kazakh and Russian, and run adversarial evidence auditing against ISO 16290 maturity criteria. All ontology schemas, multi-agent evaluation harnesses, and a 5,000-document expert-annotated gold benchmark will be released as open-source resources for the scientific community.
