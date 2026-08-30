# AI/ML Engineering Roadmap — v1.0

**Target:** broad AI/ML engineer, with an early employment bias toward Applied AI/LLM Engineering. **Pacing:** mastery-based; roughly 12–18+ months for the broad core at high availability.

| Phase | Typical effort | Capability outcome | Gate |
|---|---:|---|---|
| 0 Orientation & Diagnostic | 2–4 days | understand field, setup, learning/AI rules, baseline skill map | Entry plan |
| 1 Mathematics for ML | 4–6 weeks | algebra/functions, linear algebra, probability/statistics, calculus/optimization connected to ML | Math Ready |
| 2 Scientific Python & Data | 3–4 weeks | NumPy, data cleaning/EDA, SQL, reproducible analysis | Data Ready |
| 3 Classical ML | 6–8 weeks | frame, baseline, train/validate, compare, debug and explain predictive models | **ML Foundation Ready** |
| 4 Deep Learning & PyTorch | 8–10 weeks | build/debug neural networks and complete PyTorch training systems | Deep Learning Builder |
| 5 Vision + NLP Foundations | 4–6 weeks | understand major representation/model ideas that lead into transformers | Representation Ready |
| 6 Transformers & LLM Foundations | 6–8 weeks | understand tokenization, attention, transformers, inference, adaptation | LLM Foundations Ready |
| 7 Applied LLM Engineering | 6–8 weeks | build evaluated RAG/LLM systems with grounding, security, cost/latency controls | **Junior Applied AI Ready** |
| 8 Agents & AI Systems | 4–6 weeks | controlled tool-using systems with state, approvals, recovery and evaluation | Agent Systems Ready |
| 9 MLOps & Production AI | 6–8 weeks | test, package, serve, containerize, observe and reproduce AI/ML services | **AI/ML Engineer Ready** |
| 10 AI System Design | 4–6 weeks | choose appropriate AI architecture and defend tradeoffs | System Design Ready |
| 11 Career Engineering | continuous | portfolio, open source, interview, application and specialization strategy | Employment campaign |

## Phase progression

### 0. Orientation & Diagnostic
Learn the role map, development environment, Git/evidence habits, AI-assistance policy and your actual starting gaps.

### 1. Mathematical Foundations
Rebuild algebra and functions, then vectors/matrices/linear algebra, probability/statistics, derivatives/gradients and optimization. Formalism serves intuition and application; the phase is not a proof marathon.

### 2. Scientific Python & Data
NumPy, vectorization, pandas/dataframes, missing/categorical/time data, joins, EDA/visualization, SQL and reproducible data analysis. Flagship: messy-data investigation.

### 3. Classical Machine Learning
Problem framing, baselines, splits, regression/classification, regularization, metrics, pipelines, feature engineering, cross-validation, leakage, trees/ensembles, boosting, KNN/SVM intuition, imbalance/calibration, clustering/PCA, interpretability/error analysis and experiment design. Flagship: unfamiliar tabular problem from raw data to defensible report.

### 4. Deep Learning & PyTorch
Neural networks, losses, backprop, autograd, optimization, initialization, regularization, normalization, data pipelines, GPU execution, reproducibility and debugging. Boss fight: repair a deliberately broken training system.

### 5. Vision + NLP Foundations
CNN/vision fundamentals plus pre-transformer NLP, embeddings and sequence-model context. The purpose is broad representation intuition, not premature specialization.

### 6. Transformers & LLM Foundations
Subword tokenization, embeddings, self-attention/QKV, multi-head attention, positional information, transformer blocks, encoder/decoder families, language-model objectives, decoding, context/inference, Hugging Face workflows, fine-tuning/PEFT and a small transformer implementation lab.

### 7. Applied LLM Engineering
Problem framing and baselines, structured output, embeddings/search, RAG, chunking, metadata, hybrid retrieval/reranking, evaluation datasets, retrieval/generation evaluation, grounding/citations, model selection, cost/latency/caching/routing, prompt injection/data boundaries. Flagship: evaluated knowledge/decision-support system.

### 8. Agents & AI Systems
Workflow vs agent, tool schemas, state, control loops, planning boundaries, human approval, memory, persistence, recovery, MCP, frameworks after fundamentals, trajectory evaluation and observability. Flagship: controlled tool-using system that survives injected failures.

### 9. MLOps & Production AI
Reproducible environments, tracking/lineage, data/model versioning, testing, packaging, FastAPI, Docker, CI/CD, monitoring/drift, GenAI tracing/evaluation, batch/online inference, queues/background work, cloud foundations and open-model serving. Flagship: productionized AI service.

### 10. AI System Design
Requirements and success metrics, rules vs ML vs LLM, data architecture, batch/realtime choices, latency/throughput/cost, reliability, privacy/security/risk, human oversight, architecture communication and ADRs. Boss fight: defend an architecture for an ambiguous business problem.

### 11. Career Engineering
Turn skill into evidence: project quality, technical writing, open source, unfamiliar repositories, research/paper literacy, coding/debugging/ML/applied-AI interviews, no-degree evidence strategy, regional/global applications, and specialization selection.

## Specialization forks
After the broad trunk, choose one primary direction: Applied AI/LLM, ML Engineering, Computer Vision, NLP, MLOps/ML Platform, or Research Engineering. Maintain broad competence; deepen selectively.

## Portfolio standard before serious applications
Aim for **3–5 serious repositories**, not 20 tutorial clones: classical ML, deep learning, evaluated applied-LLM, controlled agent/tool system, and production/deployment evidence. Each should document decisions, experiments/evals, failure cases, tests, limitations and reproducibility.
