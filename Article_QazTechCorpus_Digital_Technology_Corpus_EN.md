# METHODOLOGY FOR BUILDING A DIGITAL CORPUS AND ONTOLOGICAL REPOSITORY OF TECHNOLOGIES BASED ON CORPUS LINGUISTICS AND KNOWLEDGE GRAPHS

**Abstract:** This paper presents a corpus-linguistic and ontological methodology for designing a national digital corpus and repository of technologies (QazTechCorpus) by adapting structural principles from computational corpus linguistics to scientific and technical knowledge engineering. Grounded in the three-level architecture of the National Corpus of the Kazakh Language (qazcorpus.kz) and an empirical statistical baseline of 170,747 running word tokens (23,383 distinct surface word forms) drawn from Kazakh technical texts, we extend subcorpus segmentation, metadata markup, and morphosyntactic normalization to organize unstructured outputs from state-funded research and development (R&D) projects. To establish functional requirements, we benchmark six university technology transfer and repository platforms across the United States and Europe: Stanford University, Harvard University, the University of Oxford, Charles University, the Massachusetts Institute of Technology (MIT), and the Czech Technical University in Prague (CVUT). We then specify a five-layer software architecture that integrates metadata harvesting via OAI-PMH 2.0, agglutinative stem normalization, trilingual named entity extraction across ten technical classes (TechNER) using encoder baselines alongside long-context foundation models (Gemini 4 Carbon and Argon) in a multi-agent workflow, evidence-based verification of Technology Readiness Levels (TRL 1 to 9) under ISO 16290, and a Neo4j knowledge graph governed by the OWL 2 ontology OntoTech.

**Keywords:** corpus linguistics; specialized technical corpus; Kazakh language morphology; ontological engineering; knowledge graph; named entity recognition; technology readiness level.


## 1. Introduction

Universities and national research institutes generate substantial volumes of specialized scientific and technical texts during state-funded and grant-supported research and development (R&D) projects. These outputs include final technical reports, patent specifications, utility model filings, software documentation, and laboratory test protocols. In Kazakhstan, more than 50,000 such historical and ongoing technical records are stored across fragmented registries or local archives as unstructured PDF documents written in Kazakh, Russian, and English. Because these text collections lack a unified corpus annotation schema and machine-readable domain metadata, domain experts cannot systematically search for engineering solutions by quantitative operating parameters, research administrators struggle to verify technology maturity from primary textual evidence, and industrial partners face high transaction barriers when licensing academic inventions.

Applied corpus linguistics offers well-established principles for turning unstructured text archives into structured, queryable linguistic resources (Biber, Conrad, & Reppen, 1998; McEnery & Hardie, 2012; Friginal & Hardy, 2014). Recent studies in *Applied Corpus Linguistics* have demonstrated both the practical utility of compiling specialized domain corpora (Chua, 2022) and the methodological potential of combining traditional corpus-assisted analysis with Large Language Models (LLMs) and automated annotation pipelines (Crosthwaite & Baisa, 2023; Curry, Baker, & Brookes, 2024; Uchida, 2024). In Kazakhstan, foundational work in computational and corpus linguistics has centered on the National Corpus of the Kazakh Language (qazcorpus.kz), which integrates 13 specialized subcorpora, a multi-attribute metadata markup window, and dedicated morphological and lexicographical software modules (Zhubanov, 2014; Pirmanova & Karbozova, 2022; National Corpus of the Kazakh Language, 2026). In parallel, recent statistical lexicography of Kazakh engineering discourse has quantified the distribution of 170,747 word tokens and 23,383 unique surface word forms across technical university texts (Karbozova, 2024). However, while general, literary, and pedagogical Kazakh corpora have matured rapidly, a dedicated trilingual corpus and ontological repository tailored to engineering R&D reports, patents, and technology transfer has not yet been constructed.

The objective of this study is to develop an architectural and ontological methodology for a national digital corpus and repository of technologies (QazTechCorpus) by uniting applied corpus linguistics, OWL 2 knowledge graphs (Khoroshevsky, 2008; World Wide Web Consortium, 2012), multi-agent LLM annotation workflows, and institutional repository practices from leading North American and European universities. Specifically, we address four research tasks: (1) establishing methodological continuity between the three-level linguistic architecture of qazcorpus.kz, empirical frequency distributions of Kazakh technical word forms, and the proposed technical repository; (2) conducting a comparative analysis of six international university repository and technology transfer platforms; (3) formalizing the OntoTech ontology, the morphosyntactic normalization and 10-class TechNER extraction pipeline, the ISO 16290 TRL verification protocol, and the hybrid retrieval ranking model; and (4) defining a staged validation roadmap and corpus evaluation protocol from TRL 2 to TRL 7.


## 2. Empirical Baseline and Methodological Continuity with Corpus Linguistics Architecture

Our methodology builds directly on two domestic empirical foundations: the software and subcorpus architecture of the National Corpus of the Kazakh Language (qazcorpus.kz) (Zhubanov, 2014; Pirmanova & Karbozova, 2022) and the statistical analysis of Kazakh technical discourse compiled in the *Frequency Dictionary of Word Forms in Kazakh Technical Texts* (Karbozova, 2024).

In the database and resource manager architecture described by Pirmanova and Karbozova (2022) and implemented in qazcorpus.kz (National Corpus of the Kazakh Language, 2026), text organization operates across three interconnected levels. At the first level, the macro-structure partitions the corpus into 13 functional and thematic subcorpora, including Main, Terminological, Scientific, Educational, Parallel, Historical, Dialectal, and Spoken collections. At the second level, a structured metadata markup window assigns document-level extralinguistic attributes (author, title, functional style, publication chronology, target audience, medium, and domain rubric) alongside word-level morphological tags. At the third level, specialized software utilities handle optical character recognition for Kazakh diacritics (`tbiocr`), electronic terminological dictionaries (`tbisozdik`), lexical card indices (`tbikartoteka`), concordance generation, and word-form frequency calculation.

Extending this linguistic infrastructure to engineering R&D documentation requires addressing the specific statistical and morphosyntactic properties of technical Kazakh. In an empirical study of technical texts used across engineering universities in Kazakhstan, Karbozova (2024) analyzed a corpus of $N = 170,747$ running word tokens, identifying $V = 23,383$ distinct surface word forms. This yields an overall Type-Token Ratio (TTR) of:

$$TTR = \frac{V}{N} = \frac{23,383}{170,747} \approx 0.1370 \quad (13.70\%)$$

Two corpus-linguistic phenomena explain this high surface-form diversity in Kazakh scientific and technical texts. First, because Kazakh is a rich agglutinative language, a single technical stem or compound noun productively attaches sequences of plural, possessive, case, and relational suffixes, generating dozens of low-frequency surface word forms from one underlying terminological concept. Second, statistical comparison against the national terminology database (`termincom.kz`) reveals widespread lexical variation, including morphological and phonetic doublets (*zharyspaly sozder*), calques from Russian and English technical nomenclature, and homonymous analytical units whose domain meaning depends strictly on collocation context (Karbozova, 2015, 2023, 2024).

Table 1 summarizes how the proposed QazTechCorpus methodology adapts each architectural layer of qazcorpus.kz to overcome these challenges in a trilingual (Kazakh, Russian, English) engineering environment.


### Table 1 - Structural comparison between the linguistic corpus qazcorpus.kz and the proposed technical corpus QazTechCorpus

| Architectural Element | Implementation in Linguistic Corpus (qazcorpus.kz) | Adaptation in Proposed Technical Corpus (QazTechCorpus) |
| --- | --- | --- |
| Primary storage unit | Annotated text, sentence, and surface word token linked to a morphological lemma (Pirmanova & Karbozova, 2022) | Unified Digital Technology Passport linking an R&D report, patent specification, software repository, CAD drawing, and test protocol |
| Subcorpus segmentation | 13 linguistic subcorpora: Main, Terminological, Scientific, Parallel, Educational, Historical, Dialectal, etc. | 6 technical subcorpora: R&D and grant reports, patents and utility models, physical prototypes, software and AI models, datasets, industry R&D queries |
| Metadata markup schema | Author, title, functional style, audience, creation date, source type, thematic rubric (Zhubanov, 2014) | Authors (ORCID), rightsholder organization, IPC/CPC and OECD codes, maturity level TRL 1 to 9 (ISO, 2013), IP protection status, licensing terms |
| Lexical normalization | Morphological analyzer, frequency dictionary of 23,383 technical word forms (Karbozova, 2024), `tbisozdik` | Agglutinative stemmer, doublet resolver (*zharyspaly sozder*), and cross-lingual alignment (Kazakh, Russian, English) mapped to `termincom.kz` |
| Search engine core | Lexico-grammatical concordancer, query by word form, lemma, affix chain, and metadata filters | Hybrid retrieval engine combining BM25 lexical matching, dense cross-lingual embeddings (Wang et al., 2024), and Cypher / SPARQL graph queries |
| Service and processing modules | OCR module `tbiocr`, dictionary database `tbisozdik`, card index `tbikartoteka`, frequency analyzer | Scientific OCR cleaner, 10-class TechNER extractor (encoder baselines and Gemini 4 workflow), multi-agent TRL auditor, and license generator |


To illustrate how morphological normalization stabilizes technical entity extraction prior to neural processing, Table 2 presents examples of complex agglutinative Kazakh technical word forms drawn from metallurgy, chemical engineering, and computing documentation, showing their morpheme-by-morpheme breakdown, normalized stem, and cross-lingual equivalents.


### Table 2 - Morphosyntactic segmentation and lemma normalization of agglutinative Kazakh technical word forms prior to TechNER extraction

| Surface Word Form in Kazakh R&D Text (Latin Transliteration) | Morpheme Segmentation and Grammatical Gloss | Normalized Technical Lemma (Kazakh) | Russian and English Terminological Equivalents | Mapped TechNER Class |
| --- | --- | --- | --- | --- |
| *gidrometallurgiialyq qondyrghylardaghy* | *gidrometallurgiia-lyq* (ADJ) *qondyrghy-lar-da-ghy* (stem-PL-LOC-REL) | *gidrometallurgiialyq qondyrghy* | gidrometallurgicheskaia ustanovka / hydrometallurgical installation | `EQUIPMENT` |
| *avtoklavtyq shaiushy eritindilerding* | *avtoklav-tyq* (ADJ) *shai-u-shy* (PTCP) *eritindi-ler-ding* (stem-PL-GEN) | *avtoklavtyq shaiushy eritindi* | rastvor avtoklavnogo vyshchelachivaniia / autoclave leaching solution | `MATERIAL` |
| *kontsentrattyng taza shyghymy 94,5%-gha* | *kontsentrat-tyng* (GEN) *taza* (ADJ) *shyghym-y* (POSS.3) *94,5%-gha* (DAT) | *kontsentrattyng taza shyghymy (94,5%)* | chistyi vykhod kontsentrata (94,5%) / net concentrate yield (94.5%) | `QUANT_PARAM` |
| *neirondyq zhelilerdi oqytu algoritmderimen* | *neiron-dyq* (ADJ) *zheli-ler-di* (PL-ACC) *oqyt-u* (VN) *algoritm-der-i-men* (PL-POSS.3-INS) | *neirondyq zhelini oqytu algoritmi* | algoritm obucheniia neironnoi seti / neural network training algorithm | `TECH_METHOD` |
| *tote litsenziialau sharttarynda* | *tote* (ADJ) *litsenziia-la-u* (VN) *shart-tar-y-nda* (PL-POSS.3-LOC) | *tote litsenziialau sharty* | dogovor priamogo litsenzirovaniia / direct licensing agreement | `IP_STD` |


By stripping inflectional suffix chains (*-lar-da-ghy*, *-ler-ding*, *-der-i-men*) and mapping morphological doublets to canonical entries in the 23,383-form technical frequency dictionary (Karbozova, 2024) and `tbisozdik`, the preprocessor reduces vocabulary out-of-vocabulary (OOV) rates and ensures that Kazakh, Russian, and English mentions of the same engineering concept project onto identical nodes in the knowledge graph.


## 3. Comparative Analysis of University Technology Transfer Platforms and Repositories

To ground the functional and metadata design of QazTechCorpus in international practice, we examined six university repository and technology transfer infrastructures across the United States, the United Kingdom, and the European Union: Stanford University, Harvard University, the University of Oxford, Charles University, the Massachusetts Institute of Technology (MIT), and the Czech Technical University in Prague (CVUT). This sample captures both high-volume Anglo-American patent licensing portals and European systems that link institutional text repositories directly to national Current Research Information Systems (CRIS).

At Stanford University, the digital backbone of the Office of Technology Licensing (Stanford OTL) is the Stanford TechFinder portal (`techfinder.stanford.edu`) (Stanford Office of Technology Licensing, 2026). Every invention submitted via an Invention Disclosure Form (IDF) is published as a structured Non-Confidential Abstract that communicates the engineering problem, technical advantages, and target applications without disclosing patent-sensitive implementation formulas. Faceted domain taxonomies connect each record to investigator profiles and relationship graphs in Visible Legacy. Stanford OTL manages an active portfolio of 1,014 revenue-generating technologies, processing 541 new invention disclosures and executing up to 152 licensing or option agreements per year (Stanford Office of Technology Licensing, 2026).

Harvard University divides its infrastructure into two specialized digital contours (King, 2007; Harvard Office of Technology Development, 2026). The commercial contour, managed by the Office of Technology Development (Harvard OTD, `otd.harvard.edu`), oversees 5,710 active patents and 970 industry licenses across 670 corporate partners, supporting 90 spin-off startups over a five-year window. A key procedural innovation at Harvard OTD is the ExpressPath license template suite covering Engineering and Physical Sciences, Medical Devices, and Software, which provides standardized, non-negotiable financial terms with deferred upfront fees for academic startups. The scholarly data contour operates on Harvard Dataverse (King, 2007), an open repository framework that assigns persistent DataCite DOIs at both the dataset and individual file levels in strict compliance with FAIR data principles.

At the Massachusetts Institute of Technology (MIT), open scholarly archiving and commercial IP management operate in tandem through DSpace@MIT and the MIT Technology Licensing Office (TLO) showcase (Smith et al., 2003). Built on the OAI-PMH 2.0 harvesting protocol and Qualified Dublin Core metadata, DSpace@MIT curates more than 60,000 technical reports, theses, and working papers generating over 1 million monthly downloads (Smith et al., 2003), while the MIT TLO catalog links published research papers to granted patent families. Similarly, the University of Oxford, operating through Oxford University Innovation (OUI), maintains the Click-to-Licence portal and the OUI Software Store (`process.innovation.ox.ac.uk`) (Oxford University Innovation, 2026). This system separates distribution into zero-cost Academic Use licenses and automated Commercial Use transactions for research software, trained computational models, and linguistic corpora.

In Central Europe, the Czech Technical University in Prague (CVUT) operates its digital library (`dspace.cvut.cz`) on DSpace-CRIS with bidirectional synchronization to the Czech national R&D registry (V3S) under the OpenAIRE 3.0+ metadata standard (Czech Technical University in Prague, 2026). Alongside peer-reviewed articles, the CVUT repository indexes utility models (*uzitny vzor*), certified methodologies, and functional engineering prototypes (*funkcni vzorek*). Charles University in Prague pairs its academic Centre for Knowledge and Technology Transfer (CPPT UK) with a commercial subsidiary, Charles University Innovations Prague (CUIP a.s.) (Charles University, 2026), deploying faculty Innovation Scouts to identify and document early Proof-of-Concept outputs at TRL 3 to 5 before formal patent filing.


![Figure 1](Figures/Figure_1_Benchmark.png)
*Figure 1 - Quantitative indicators of university technology transfer (a) and functional coverage of university platforms across six architectural criteria (b)*

As shown in Figure 1 and Table 3, comparing these six university infrastructures exposes a structural divide between two software classes that rarely interoperate. Open scholarly repositories (DSpace@MIT, Harvard Dataverse, DSpace-CRIS CVUT) provide OAI-PMH metadata harvesting, Dublin Core / DataCite schemas, and persistent DOI identifiers, yet lack automated mechanisms for assessing ISO 16290 TRL maturity or executing licensing contracts. Conversely, commercial technology transfer showcases (Stanford TechFinder, Harvard OTD, Oxford Click-to-Licence) streamline marketing and licensing workflows, but rely on manual curation by patent managers and display only a small subset of university R&D outputs. Unifying both contours within a single corpus architecture driven by automated linguistic and LLM extraction resolves this limitation.


### Table 3 - Comparative analysis of architectural mechanisms across US and European university platforms

| Platform and University | Core Technical and Procedural Mechanism | Functional Limitations | Adaptation in Proposed Technical Corpus |
| --- | --- | --- | --- |
| Stanford OTL & TechFinder (Stanford, USA) | Open Non-Confidential Abstracts, faceted taxonomy, Visible Legacy relationship graphs | Manual abstract drafting by OTL staff; no OAI-PMH harvesting or automated TRL scoring | Dual-contour technology passport: open abstract generated by NLP/LLM pipeline and restricted dossier under e-NDA |
| Harvard OTD & ExpressPath (Harvard, USA) | Standardized non-negotiable ExpressPath licenses across 3 industry tracks with deferred fees | No direct software link to primary R&D reports or source code repositories | Built-in generator for standardized licensing agreements covering software, instruments, and engineering methods |
| Harvard Dataverse (Harvard, USA) | Virtual institutional collections, dataset- and file-level DOI registration, FAIR compliance | Focused on open research data without know-how protection or commercial licensing workflows | Isolated virtual subcorpora for research institutes with DataCite DOI support for open test protocols |
| DSpace@MIT & MIT TLO (Cambridge, USA) | OAI-PMH 2.0 protocol, Qualified Dublin Core metadata, archive of 60,000+ reports and theses | Separation between open text archive in DSpace and commercial patent catalog in TLO | Automated OAI-PMH harvesting of university repositories with end-to-end links across paper, report, patent, and prototype |
| OUI Click-to-Licence (Oxford, UK) | Online OUI Software Store splitting Academic Use and Commercial Use licensing in one click | Applicable mainly to transferable digital assets (software, databases, assessment scales) | Dedicated module for instant licensing of scientific software, trained AI weights, and digital corpora |
| DSpace-CRIS CVUT & CPPT/CUIP UK (Prague, Czechia) | Repository integration with CRIS V3S (OpenAIRE), utility model tracking, faculty scouts, and PoC monitoring | Confined to a single institution; no neural full-text extraction of engineering parameters | Innovation scout workspace and early-stage R&D tracking (TRL 3 to 5) with automated passport pre-filling |


## 4. Architectural-Ontological Model and Hybrid Corpus Annotation Pipeline

The proposed QazTechCorpus platform follows a five-layer microservice architecture (Figure 2) that manages the complete document lifecycle from harvesting raw unstructured PDFs to executing hybrid semantic queries and generating digital license agreements. Layer 1 handles asynchronous data ingestion orchestrated by Apache Airflow. It combines OAI-PMH 2.0 harvesters for polling university DSpace and Dataverse archives (Smith et al., 2003; King, 2007), parsers for national and international patent registries, bibliometric connectors (CrossRef, OpenAlex, ORCID), and a scientific OCR cleaning module that adapts the Kazakh diacritic, table, and formula recognition rules of the `tbiocr` utility (Pirmanova & Karbozova, 2022; National Corpus of the Kazakh Language, 2026).


![Figure 2](Figures/Figure_2_Architecture.png)
*Figure 2 - Five-layer software architecture of the digital corpus and ontological repository of technologies*

Layers 2 and 3 convert normalized trilingual text streams into a formal knowledge graph (Khoroshevsky, 2008). The semantic core of the repository is the domain ontology OntoTech, specified in OWL 2 DL (World Wide Web Consortium, 2012) as an ordered five-tuple:

$$\mathcal{O} = \langle C, R, A, I, X \rangle, \quad (1)$$

where $C$ denotes the finite set of domain concept classes (`TechnologyPassport`, `RnDReport`, `PatentDocument`, `SoftwareModule`, `TestProtocol`, `Researcher`, `Organization`, `Equipment`, `IndustryDomain`, `TRLLevel`); $R$ defines the set of directed object properties linking classes (`developedAt`, `authoredBy`, `protectedByDocument`, `documentedInReport`, `verifiedByProtocol`, `hasReadinessLevel`, `applicableInIndustry`); $A$ specifies the set of typed data attributes (`doiIdentifier`, `stateRegistrationIndex`, `ipcCode`, `oecdFosCode`, `nonConfidentialAbstractEN`, `trlScore`, `trlConfidence`, `orcidId`); $I$ represents the set of concrete passport and entity instances stored in the corpus; and $X$ contains description logic axioms enforced by the OWL 2 reasoner to verify metadata consistency upon ingestion.

Under the OntoTech ontology, every engineering development in the corpus is represented by a unified Digital Technology Passport structured into six faceted metadata blocks (Table 4). This design merges bibliographic metadata standards (Dublin Core, DataCite 4.5) with patent and subject classifications (IPC/CPC, OECD Fields of Science) and transactional attributes adapted from Stanford TechFinder, Harvard ExpressPath, and Oxford Click-to-Licence.


### Table 4 - Structure of the six faceted metadata blocks of the Digital Technology Passport in the OntoTech ontology

| Passport Facet Block | Key Metadata Attributes and Entities | Supported Standards and Protocols |
| --- | --- | --- |
| 1. Identification block | Persistent passport identifier (DOI / Handle), R&D project registration number, trilingual title (Kazakh, Russian, English), record version, linked publications | DataCite Metadata Schema 4.5, Qualified Dublin Core, OAI-PMH 2.0 (Smith et al., 2003; King, 2007) |
| 2. Engineering and industry taxonomy | International and Cooperative Patent Classification codes (IPC / CPC), OECD Fields of Science (FOS) rubrics, applied industrial domain tags | WIPO IPC / CPC, OECD Frascati Manual classification, OWL 2 RDF Schema (World Wide Web Consortium, 2012) |
| 3. Technical specification and open abstract | Non-confidential summary, engineering problem solved, quantitative physical or algorithmic performance metrics, hardware and software stack | Stanford TechFinder Non-Confidential Abstract model (Stanford Office of Technology Licensing, 2026) |
| 4. Maturity verification (TRL) | Assessed readiness level from TRL 1 to TRL 9, confidence score, direct citations to supporting evidence (calculation, bench prototype, lab test protocol) | ISO 16290:2013 international standard (TRL 1 to 9 scale) (International Organization for Standardization, 2013) |
| 5. Legal status and IP protection | IP object type (invention patent, utility model, software or database certificate, trade secret), registry number, rightsholders, and authors (ORCID) | WIPO ST.9 bibliographic patent data standards |
| 6. Transfer and licensing profile | Available transfer mode: academic or commercial Click-to-Licence, ExpressPath startup package, sponsored research contract, e-NDA data room mode | Oxford OUI Software Store and Harvard ExpressPath protocols |


To automate corpus annotation and draft passport synthesis at Layer 2 across unstructured Kazakh, Russian, and English R&D documents, we combine fine-tuned encoder baselines with a multi-agent LLM workflow. Building on recent methodological findings in *Applied Corpus Linguistics* demonstrating that LLMs perform most reliably when constrained by explicit linguistic schemas and human-verified taxonomies (Crosthwaite & Baisa, 2023; Curry, Baker, & Brookes, 2024; Uchida, 2024), our pipeline first applies morphosyntactic stem normalization using the 23,383-form technical frequency dictionary (Karbozova, 2024) and `tbisozdik` (Table 2). Next, token-level span extraction baselines using multilingual XLM-RoBERTa (Conneau et al., 2020) and scientific SciBERT (Beltagy, Lo, & Cohan, 2019) with a Conditional Random Field (CRF) layer are paired with long-context foundation models (Google Gemini 4 Carbon and Gemini 4 Argon). While encoder baselines provide rapid baseline tagging on abstracts, Gemini 4 models ingest complete 50- to 100-page R&D reports, experimental tables, and patent claims in a single context window to output schema-validated JSON records conforming to OntoTech. Table 5 defines the ten target entity classes of the TechNER annotation scheme alongside representative trilingual corpus spans.


### Table 5 - Taxonomic specification of the 10-class TechNER corpus annotation scheme with trilingual examples

| TechNER Class Code | Semantic Definition in OntoTech | Representative Corpus Span (Kazakh / Russian / English) | Target Passport Block |
| --- | --- | --- | --- |
| `TECH_ARTIFACT` | Created device, substance, alloy, catalyst, or software system | *nanokurylymdy sorbent* / *nanostrukturnyi sorbent* / *nanostructured sorbent* | Block 1 & Block 3 |
| `TECH_METHOD` | Technological process, synthesis route, or computational algorithm | *avtoklavtyq shaiu adisi* / *metod avtoklavnogo vyshchelachivaniia* / *autoclave leaching method* | Block 3 |
| `QUANT_PARAM` | Numerical operating parameter, yield, purity, latency, or bound | *shyghymy 94,5%, T = 180 C* / *vykhod 94,5%, T = 180 C* / *yield 94.5% at 180 C* | Block 3 & Block 4 |
| `MATERIAL` | Raw ore, chemical reagent, precursor, or input linguistic dataset | *polimetalldy ken* / *polimetallicheskaia ruda* / *polymetallic ore* | Block 3 |
| `EQUIPMENT` | Laboratory instrument, reactor, sensor, or compute cluster | *rentgendik difraktometr* / *rentgenovskii difraktometr* / *X-ray diffractometer* | Block 3 & Block 4 |
| `SOFTWARE_STACK` | Programming language, neural architecture, database, or protocol | *Neo4j graf bazasy, OWL 2* / *grafovaia SUBD Neo4j* / *Neo4j graph database, OWL 2* | Block 3 & Block 6 |
| `DOMAIN` | Industrial application sector aligned with OECD FOS and IPC/CPC | *tusti metallurgiia* / *tsvetnaia metallurgiia* / *non-ferrous metallurgy* | Block 2 |
| `IP_STD` | Patent number, state registration index, GOST/ISO standard, license | *KR Patenti No. 35841, ISO 16290* / *Patent RK No. 35841* / *KZ Patent No. 35841* | Block 1 & Block 5 |
| `TRL_EVIDENCE` | Documentary proof of maturity (lab protocol, bench act, pilot test) | *zertkhanalyq synaq aktisi* / *akt laboratornykh ispytanii* / *laboratory test protocol* | Block 4 |
| `ORG` | University, research institute, funding body, or industrial partner | *Satbayev University* / *KazNITU im. K.I. Satpaeva* / *Satbayev University* | Block 1 & Block 5 |


Multi-class extraction accuracy across the $K = 10$ entity categories is evaluated on held-out expert-annotated documents using macro-averaged $F_1$:

$$F_1 = \frac{1}{K} \sum_{k=1}^{K} \frac{2 \cdot P_k \cdot R_k}{P_k + R_k}, \quad (2)$$

where $P_k$ and $R_k$ denote Precision and Recall for the $k$-th entity class.

To eliminate subjective self-reporting of technology maturity along the nine-level ISO 16290 scale (TRL 1 to 9) (International Organization for Standardization, 2013), we combine deterministic OWL 2 production rules with an adversarial multi-agent verification workflow powered by Gemini 4 Carbon. First, deterministic rules check whether the mandatory documentary evidence spans (`TRL_EVIDENCE`) required for a claimed level are present in the corpus record (analytical calculations for TRL 2 to 3, laboratory test protocols and bench setups for TRL 4, patent filings and relevant-environment test acts for TRL 5 to 6, and industrial pilot acts for TRL 7). Second, an independent Evidence Auditor agent cross-examines the extracted claims against quantitative tables in the primary PDF report, generating a calibrated probability distribution over TRL 1 to 9 together with verbatim quotes and page citations.

At Layer 3, storage is partitioned across three engines: Neo4j stores semantic triples governed by OntoTech, OpenSearch indexes normalized full texts and 1024-dimensional cross-lingual embeddings from Multilingual-E5 (Wang et al., 2024), and PostgreSQL paired with S3/MinIO manages user accounts, file versions, and licensing audit trails. Candidate technology passports are ranked for a user query $q$ via a weighted linear combination:

$$S(q, d) = \alpha \cdot S_{\text{BM25}}(q, d) + \beta \cdot \cos(\mathbf{v}_q, \mathbf{v}_d) + \gamma \cdot S_{\text{graph}}(q, d), \quad (3)$$

where $S_{\text{BM25}}(q, d)$ captures exact lexical and morphological matches for nomenclature codes, IPC classes, and chemical formulas; $\cos(\mathbf{v}_q, \mathbf{v}_d)$ measures dense cross-lingual semantic similarity between Kazakh, Russian, and English queries and documents; and $S_{\text{graph}}(q, d)$ quantifies structural connectivity in Neo4j (such as verified test protocols and linked patents), with non-negative weights satisfying $\alpha + \beta + \gamma = 1$.

To protect unpublished trade secrets prior to patenting, Layers 4 and 5 enforce two-tier access control. The public portal displays only sanitized Non-Confidential Abstracts modeled on Stanford TechFinder (Stanford Office of Technology Licensing, 2026), whereas complete technical dossiers (raw laboratory logs, blueprints, and source code) reside in a virtual data room gated by an electronic non-disclosure agreement (e-NDA), coupled with automated Click-to-Licence and ExpressPath contract generators. The reference implementation of the six-block passport schema, the `TechNER` validator, the deterministic ISO 16290 consistency checker, and the hybrid scoring function is publicly available in our open repository ([Anonymized Repository Link for Peer Review]).


## 5. Staged Development Roadmap and Corpus Validation Protocol

Practical implementation and empirical validation of QazTechCorpus are structured into six interconnected modules (Modules 1 to 6) across three sequential stages, advancing the platform from an initial methodological specification (TRL 2) to an operationally validated repository prototype (TRL 7 under ISO 16290) (Figure 3).


![Figure 3](Figures/Figure_3_Roadmap.png)
*Figure 3 - Staged research and development roadmap (Modules 1 to 6) and system maturity trajectory (TRL 2 to TRL 7)*

Stage I (TRL 2 to TRL 4, Modules 1 to 3) formalizes the OntoTech ontology in Protege (over 250 classes and 80 object properties in OWL 2 DL), integrates the 23,383-word-form Kazakh technical frequency dictionary (Karbozova, 2024) and `tbisozdik` stemmer into the ingestion pipeline, deploys OAI-PMH 2.0 harvesters, and compiles an initial verified trilingual subcorpus of 15,000 R&D reports and patent specifications inside the containerized tri-modal cluster (Neo4j, OpenSearch, PostgreSQL, S3), reaching 25,000 nodes and 120,000 semantic triples with query latency under 150 ms.

Stage II (TRL 4 to TRL 5, Module 4) executes a rigorous corpus-linguistic validation protocol. A team of computational linguists and domain engineers annotates an open gold benchmark dataset of 5,000 scientific and technical texts in Kazakh, Russian, and English across the 10 TechNER entity classes and ISO 16290 TRL levels. To ensure annotation reliability in line with corpus linguistics standards (McEnery & Hardie, 2012; Friginal & Hardy, 2014), dual independent human annotation is evaluated using Cohen's kappa ($\kappa \ge 0.80$) for token-level entity spans and Krippendorff's alpha ($\alpha \ge 0.78$) for document-level TRL assignments. Fine-tuned encoder baselines (XLM-RoBERTa, SciBERT-CRF) are then benchmarked against the multi-agent Gemini 4 Carbon and Argon workflow, targeting a macro-averaged $F_1 \ge 0.86$ on TechNER extraction and $\ge 0.82$ accuracy on automated TRL verification.

Stage III (TRL 5 to TRL 7, Modules 5 and 6) launches the trilingual web portal featuring faceted concordancing and semantic search, interactive subgraph visualization, innovation scout workspaces (adapted from Charles University), e-NDA virtual data rooms, and one-click academic/commercial licensing modules, scaling the national repository to 50,000 Digital Technology Passports and 250,000 semantic triples integrated with university CRIS platforms.


## 6. Conclusions

1. By uniting computational corpus linguistics with OWL 2 knowledge engineering, this study establishes a replicable methodology for constructing a national digital corpus and ontological repository of technologies (QazTechCorpus). Grounding the text preprocessing pipeline in the three-level architecture of the National Corpus of the Kazakh Language (qazcorpus.kz) and an empirical statistical baseline of 170,747 running tokens (23,383 unique surface word forms) from Kazakh technical texts effectively resolves agglutinative suffix sparsity and terminological doublet variation across trilingual R&D documentation.

2. Comparative evaluation of six university platforms (Stanford, Harvard, Oxford, Charles University, MIT, and CVUT) reveals a persistent divide between open scholarly archives (OAI-PMH, FAIR, DataCite DOI) and commercial licensing portals (Non-Confidential Abstracts, ExpressPath, Click-to-Licence). Our five-layer architecture and two-tier Digital Technology Passport bridge both contours within a single system while safeguarding pre-patent know-how under electronic NDA.

3. The formal OWL 2 ontology OntoTech, the 10-class TechNER annotation taxonomy combining encoder baselines with multi-agent long-context reasoning (Gemini 4 Carbon and Argon), the deterministic and neural ISO 16290 TRL auditing protocol, and the hybrid lexical-vector-graph ranking model provide a complete technical blueprint advancing from TRL 2 to TRL 7 alongside an open 5,000-document trilingual benchmark for the applied corpus linguistics community.


## References

Beltagy, I., Lo, K., & Cohan, A. (2019). SciBERT: A pretrained language model for scientific text. In *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)* (pp. 3615-3620). Association for Computational Linguistics. https://doi.org/10.18653/v1/D19-1371

Biber, D., Conrad, S., & Reppen, R. (1998). *Corpus linguistics: Investigating language structure and use*. Cambridge University Press. https://doi.org/10.1017/CBO9780511804489

Charles University. (2026). *Centre for Knowledge and Technology Transfer of Charles University (CPPT UK) and Charles University Innovations Prague (CUIP)*. https://cppt.cuni.cz/CPPTNEN-79.html

Chua, S.-M. (2022). Compiling and analysing a large corpus of online discussions to explore users' interactions. *Applied Corpus Linguistics*, *2*(2), Article 100017. https://doi.org/10.1016/j.acorp.2022.100017

Conneau, A., Khandelwal, K., Goyal, N., Chaudhary, V., Wenzek, G., Guzman, F., Grave, E., Ott, M., Zettlemoyer, L., & Stoyanov, V. (2020). Unsupervised cross-lingual representation learning at scale. In *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)* (pp. 8440-8451). Association for Computational Linguistics. https://doi.org/10.18653/v1/2020.acl-main.747

Crosthwaite, P., & Baisa, V. (2023). Generative AI and the end of corpus-assisted data-driven learning? Not so fast! *Applied Corpus Linguistics*, *3*(3), Article 100066. https://doi.org/10.1016/j.acorp.2023.100066

Curry, N., Baker, P., & Brookes, G. (2024). Generative AI for corpus approaches to discourse studies: A critical evaluation of ChatGPT. *Applied Corpus Linguistics*, *4*(1), Article 100082. https://doi.org/10.1016/j.acorp.2023.100082

Czech Technical University in Prague. (2026). *Digital Library of the Czech Technical University in Prague (DSpace CVUT) and CTU Open Science Strategy*. https://dspace.cvut.cz/

Friginal, E., & Hardy, J. A. (2014). *Corpus-based sociolinguistics: A guide for students*. Routledge. https://doi.org/10.4324/9780203114827

Harvard Office of Technology Development. (2026). *Harvard ExpressPath licenses and available technologies*. https://otd.harvard.edu/researchers/licensing-startup-formation/harvard-expresspath-licenses/

International Organization for Standardization. (2013). *Space systems: Definition of the Technology Readiness Levels (TRLs) and their criteria of assessment* (ISO Standard No. 16290:2013).

Karbozova, B. (2015). Research of structural and semantic meanings of homonymous units. *The Social Sciences*, *10*(6), 1072-1075. https://doi.org/10.3923/sscience.2015.1072.1075

Karbozova, B. D. (2023). Omonimderdi oqytu tekhnologiiasynda qazaq tili zhiilik sozdikterining mani [The significance of frequency dictionaries of the Kazakh language in the technology of teaching homonyms]. *Foundations and Trends in Modern Learning*, (1), 14-21.

Karbozova, B. D. (2024). *Qazaq tekhnikalyq matinder sozformalarynyng zhiilik sozdigi* [Frequency dictionary of word forms in Kazakh technical texts]. Jogary bilim.

Khoroshevsky, V. F. (2008). Knowledge spaces on the Internet and Semantic Web. *Artificial Intelligence and Decision Making*, (1), 80-97.

King, G. (2007). An introduction to the Dataverse Network as an infrastructure for data sharing. *Sociological Methods & Research*, *36*(2), 173-199. https://doi.org/10.1177/0049124107306660

McEnery, T., & Hardie, A. (2012). *Corpus linguistics: Method, theory and practice*. Cambridge University Press. https://doi.org/10.1017/CBO9780511981395

National Corpus of the Kazakh Language. (2026). *Subcorpus structure, metadata markup window, and software modules (qazcorpus.kz)*. https://qazcorpus.kz/indexru.php

Oxford University Innovation. (2026). *Click-to-Licence portal and OUI Software Store*. https://process.innovation.ox.ac.uk/software/

Pirmanova, K. K., & Karbozova, B. D. (2022). O programmnom obespechenii bazy dannykh elektronnogo korpusa kazakhskikh tekstov [On the database software for an electronic corpus of Kazakh texts]. *Foundations and Trends in Research*, (9), 45-53. https://ojs.publisher.agency/index.php/FTR/issue/view/9

Smith, M., Barton, M., Bass, M., Branschofsky, M., McClellan, G., Stuve, D., Tansley, R., & Walker, J. H. (2003). DSpace: An open source dynamic digital repository. *D-Lib Magazine*, *9*(1), 1-14. https://doi.org/10.1045/january2003-smith

Stanford Office of Technology Licensing. (2026). *Stanford OTL annual report and TechFinder portal*. https://techfinder.stanford.edu/

Uchida, S. (2024). Using early LLMs for corpus linguistics: Examining ChatGPT's potential and limitations. *Applied Corpus Linguistics*, *4*(1), Article 100089. https://doi.org/10.1016/j.acorp.2024.100089

Wang, L., Yang, N., Huang, X., Yang, L., Majumder, R., & Wei, F. (2024). Multilingual E5 text embeddings: A technical report. *arXiv preprint arXiv:2402.05672*. https://doi.org/10.48550/arXiv.2402.05672

World Wide Web Consortium. (2012). *OWL 2 Web Ontology Language document overview (Second Edition)*. W3C Recommendation. https://www.w3.org/TR/owl2-overview/

Zakharov, V. P., & Bogdanova, S. Y. (2020). *Korpusnaia lingvistika* [Corpus linguistics] (3rd ed.). St. Petersburg State University Press.

Zhubanov, A. K. (2014). Korpusnaia lingvistika kak novoe napravlenie v kazakhskom iazykoznanii [Corpus linguistics as a new direction in Kazakh linguistics]. *Bulletin of KazNU. Philological Series*, *149*(3), 18-24.
