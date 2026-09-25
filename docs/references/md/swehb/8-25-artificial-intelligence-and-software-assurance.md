# 8.25 - Artificial Intelligence And Software Assurance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 184320002. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance

8.25 - Artificial Intelligence And Software Assurance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/184320002/8.25+-+Artificial+Intelligence+And+Software+Assurance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=184320002)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=184320002&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Generative AI Metrics](#tabs-2)
* [3. Resources](#tabs-3)

# 1.0 Introduction

As NASA organizations use Artificial Intelligence (AI) to make decisions, the need for robust Software Assurance (SA) becomes important.Artificial Intelligence (AI) will be increasingly embedded in NASA software systems and decision workflows. AI’s probabilistic behavior, dependence on data, and susceptibility to drift and supply‑chain changes introduce assurance challenges that differ from conventional software. This Topic defines **software assurance (SA)** expectations across the AI system lifecycle, expanding prior guidance on **data quality, continuous testing, documentation, security, bias, and V&V** with **first‑class evaluation, uncertainty management, safety engineering, architectural resilience, human oversight, and continuous change management**.

**Applicability.** Until Agency policy evolves, projects are **recommended to limit AI use to non‑safety‑critical applications unless a documented AI safety case and risk controls are approved by the appropriate authority.**

# 2.0 Scope

This Topic applies to **machine learning (ML), foundation‑model applications (including LLMs), fine‑tuned or open‑weight models, retrieval‑augmented systems, compound AI systems**, and **agentic systems** that plan and take actions using tools. It covers **development, integration, deployment, operation, monitoring, and retirement**.

# 3.0 Key Definitions

* **AI system:** Software that uses data‑driven models to produce predictions, classifications, generations, recommendations, or actions.
* **Foundation model:** Large pre‑trained multi‑task model consumed via API or fine‑tuning.
* **Compound AI system:** Architecture orchestrating multiple AI and non‑AI components (e.g., retrieval, guardrails, models, tools).
* **Agentic system:** AI that plans, uses tools, and takes actions autonomously within defined authority.
* **Data drift / Concept drift:** Changes in input distributions or input–output relationships that degrade performance.
* **Uncertainty calibration:** Correspondence between expressed confidence and probability of correctness.

# 4.0 Policy Statement

Projects that incorporate AI **should** implement Software Assurance practices that:

1. treat **evaluation** as a first‑class engineering activity;
2. ensure **traceability** across all AI artifacts;
3. design **human oversight** appropriate to risk;
4. address **security** across the full AI threat surface;
5. manage **uncertainty** and communicate it to users;
6. architect for **modularity and resilience**;
7. apply **safety engineering** tailored to AI; and
8. plan for **continuous change** in models, data, and dependencies.

# 5.0 Roles and Teaming

Projects **should** form cross‑functional teams that include **domain experts, SA/IV&V, AI evaluation specialists, data engineers, prompt/retrieval engineers, platform/MLOps, and system architects**; and provide **AI literacy** to all stakeholders who interact with AI outputs.

# 6.0 Assurance Requirements and Activities

**6.1 Evaluation as a First‑Class Activity**

**Rationale.** Evaluation determines whether the AI system works as intended before and after deployment. It must detect **drift, safety violations, invalid outputs, and behavior changes**.

**Software Assurance Expectations**

* **Pre‑deployment evaluation plans** should define success criteria, curated benchmarks, probabilistic acceptance thresholds, and human‑judgment workflows for ambiguous tasks (**evaluation‑driven development**).
* **Production evaluation** should implement lightweight monitoring, failure‑mode detection, alerting, and regression tracking distinct from lab tests.
* Evaluation datasets, metrics, and results **should** be version‑controlled and traceable (see §6.8).
* Link to Handbook testing practices (**SWE‑066, SWE‑068, SWE‑193**) for planning, execution, and acceptance criteria.

**6.2 Data Lifecycle Quality and Drift Management**

**Rationale.** AI behavior is shaped by **training data, fine‑tuning sets, retrieval sources, prompts/in‑context examples, guardrail data, and evaluation benchmarks**—not just training datasets.

**Software Assurance Expectations**

* **Data provenance** (source, licensing, representativeness) should be documented for **every** dataset and retrieval corpus; configuration‑managed per **SWE‑070**.
* Implement **drift detection** (data and concept drift) with defined thresholds and retraining/refresh criteria.
* **Synthetic data** use should include validation for relevance and bias; limitations must be documented.
* Extend existing **data‑quality checks** (accuracy, completeness, timeliness, relevance, bias) to **retrieval pipelines and prompt exemplars**.

**6.3 Security: Threats, Supply Chain, and Red Teaming**

**Rationale.** AI expands the attack surface: model poisoning, adversarial inputs, compromised model weights/APIs, prompt injection, excessive agency, and embedding/vector weaknesses.

**Software Assurance Expectations**

* **AI supply chain assurance**: verify provenance of models/components, cryptographically sign artifacts, audit dependencies; define incident response for compromised components.
* Assess **OWASP GenAI** risks (prompt injection, system prompt leakage, excessive agency) and implement guardrails and input/output filtering.
* Conduct **AI red‑teaming** integrated with threat modeling; track findings to closure under **SWE‑156** (security risks).

**6.4 Safety Engineering**

**Rationale.** AI can cause harm via confidently wrong outputs, unpredictable behavior on novel inputs, or autonomous actions. Safety engineering complements security.

**Software Assurance Expectations**

* Produce an **AI Safety Case** documenting hazards (e.g., hallucinations, unsafe tool use, drift failures), mitigations, operating conditions, and residual risk; review at KDPs.
* Implement runtime safety monitoring (e.g., flagged content rates, refusal/abstention metrics, confidence distributions) and **circuit breakers** for violations.
* Align testing with hazard scenarios under **SWE‑066/SWE‑068/SWE‑193**.

**6.5 Model Uncertainty and Reliability**

**Rationale.** Generative models produce fluent outputs that may be incorrect; uncertainty must be **quantified, detected, and communicated**.

**Software Assurance Expectations**

* Implement **confidence/uncertainty indicators**, **consistency checks** (e.g., multiple generations), **retrieval grounding**, and **abstention rules** for low confidence.
* Define escalation paths: return top‑N candidates with confidence, route to human review, or **decline to answer** below thresholds.
* Verify uncertainty handling in requirements V&V (**SWE‑066/SWE‑068/SWE‑193**) acknowledging probabilistic acceptance criteria.

**6.6 Human‑AI Interaction and Oversight**

**Rationale.** Effective oversight depends on **risk level, tempo, autonomy**, and mitigation of **automation bias/cognitive surrender**.

**Software Assurance Expectations**

* Select oversight mode (**in‑loop, on‑loop, out‑of‑loop**) with documented authority boundaries and escalation for out‑of‑scope situations; required approval gates for **agentic actions**.
* Measure oversight effectiveness (override rate, time‑on‑task) and adjust interaction design to support critical evaluation (context, uncertainty cues).

**6.7 Architecture: Modularity, Substitutability, and Operational Resilience**

**Rationale.** Compound systems accumulate hidden dependencies; design must isolate components and make model/provider substitution routine.

**Software Assurance Expectations**

* Decompose systems into **loosely coupled modules** (retrieval, inference, guardrails, tools, orchestration) with explicit interface contracts and **observable behaviors**.
* Maintain **model routing and version isolation** to swap models/APIs without systemic regressions; define rollback procedures.
* Monitor performance time‑series, drift indicators, and safety metrics; promote/rollback based on **evaluation signals** (§6.1).

**6.8 Documentation and Traceability**

**Rationale.** Debugging and accountability require traceability across **models, data, prompts, retrieval configs, guardrails, tool definitions, evaluation assets, and third‑party dependencies**.

**Software Assurance Expectations**

* Version and configuration‑manage **all AI artifacts**; maintain experiment tracking across datasets, prompts, hyperparameters, and results.
* Ensure reproducibility for **model recreation** per **SWE‑070**; record rationale for configuration choices.

**6.9 Continuous Change and Sustainment**

**Rationale.** AI systems exist in continuous change: **data shifts, model updates, API/pricing changes, infrastructure scaling, and team upskilling**.

**Software Assurance Expectations**

* Budget and plan for **monitoring, retraining/fine‑tuning, retrieval refresh, evaluation updates, provider/API migrations**, and **FinOps for AI** (cost observability and optimization).
* Maintain **deprecation/retirement plans** for models and dependencies; define migration triggers and contingencies.

**6.10 Core Data Quality Principles (Expanded and Integrated)**

**Rationale.**  
Data quality is one of the most critical determinants of AI system performance and reliability. Because AI models infer behavior from data, **even minor inaccuracies or biases can propagate into significant operational errors**. High‑quality data is essential across the full lifecycle—training, testing, fine‑tuning, retrieval pipelines, prompt exemplars, guardrails, and evaluation datasets.

**6.10.1 Core Quality Dimensions**

SA should ensure that all data used across the AI lifecycle adheres to the following dimensions:

* **Accuracy** – Data must correctly represent ground truth; even small inaccuracies can materially distort predictions.
* **Completeness** – Missing or partial data must be detected, addressed, or mitigated.
* **Consistency** – Data must be coherent across sources, formats, and time.
* **Timeliness** – Data must reflect the current operational environment and be refreshed as conditions evolve.
* **Relevance** – Data must be appropriate for the target task and domain.
* **Representativeness & Fairness** – Data must reflect deployment contexts and be assessed for hidden biases to prevent discriminatory outcomes.

**6.10.2 Expanded SA Responsibilities for Data Quality**

**a. Provenance and Licensing**

SA should ensure documentation of:

* data origin
* ownership and licensing
* usage rights and restrictions
* representativeness relative to deployment environments

All datasets and retrieval indexes must be configuration‑controlled per related SWE requirements.

**b. Data Security and Configuration Control**

SA should ensure appropriate **security controls, access restrictions, and configuration management** for all data used in training, testing, or inference. Retrieval pipelines must be monitored for ingestion of untrusted or unsafe content.

**c. Data Drift and Concept Drift Management**

Projects should implement mechanisms to detect:

* **data drift** (input distribution changes)
* **concept drift** (changes in input‑to‑output relationships)

Thresholds, alerting processes, and retraining or refresh triggers must be documented.

**d. Retrieval and Context Data Quality**

For retrieval‑augmented systems, SA should evaluate:

* retrieval ranking quality
* index update frequency
* context noise levels
* prompt exemplar accuracy, representativeness, and relevance

**e. Synthetic Data Validation**

If used, synthetic data must be validated for:

* representativeness
* bias or leakage
* compatibility with real‑world conditions
* potential for harmful model overfitting or artifact introduction

**f. Evaluation Data Quality**

Evaluation datasets must follow the same quality principles as training data and must remain relevant as environments evolve.

**6.10.3 Key Considerations for Software Assurance of AI Models**

SA should:

* evaluate and approve all data preparation and validation processes
* ensure data is representative of expected operational distributions
* identify and mitigate data and model bias sources
* analyze edge‑case scenarios to detect data gaps
* ensure all data pipelines feeding AI systems are monitored, secured, documented, and under configuration control

**6.10.4 Integration with Other SA Functions**

This section directly supports and should be applied in conjunction with:

* §6.2 Data Lifecycle and Drift Management
* §6.1 Evaluation (evaluation data quality)
* §6.5 Uncertainty Management
* §6.7 Architecture Resilience (retrieval dependencies)
* SWE‑070, SWE‑156, and related SWE requirements

# 7.0 Integration with Existing SWEHB Requirements

Topic 8.25 links to and extends the following Handbook entries:

* **SWE‑033** (Acquisition vs. Development Assessment), **SWE‑034** (Acceptance Criteria), **SWE‑066** (Perform Testing), **SWE‑068** (Evaluate Test Results), **SWE‑070** (Models, Simulations, Tools), **SWE‑086** (Continuous Risk Management), **SWE‑146** (Auto‑generated Source Code), **SWE‑151** (Cost Estimate Conditions), **SWE‑156** (Evaluate Systems for Security Risks), **SWE‑193** (Acceptance Testing for Affected System and Software Behavior), **SWE‑205** (Determination of Safety‑Critical Software), **SWE‑211** (Test Levels of Non‑Custom Developed Software).

# 8.0 Documentation Artifacts (Minimum Set)

Projects **should** produce and maintain:

1. **AI Suitability Assessment** (includes NIST AI RMF “Map” considerations and error‑tolerance/interpretability needs).
2. **Evaluation Plan and Benchmarks** (lab and production).
3. **Data Provenance & Quality Reports** (training/fine‑tuning/retrieval/prompt exemplars/synthetic data).
4. **AI Safety Case** (hazards, mitigations, operating envelope).
5. **Security Threat Model & Red‑Team Findings** (including GenAI risks).
6. **Architecture Contracts & Substitution Plan** (model/provider swap readiness).

**What Software Managers Need to Know:**

* **AI/ML = statistical, data‑driven systems**, not explicitly programmed code. Behavior depends on training data and modeling assumptions.
* **Use AI/ML only when rules cannot be coded deterministically** or problem is inherently statistical. Not needed when explicit logic suffices.
* **Data quality drives correctness.** AI/ML output is only as good as the training/testing data. Poor, incomplete, or biased data leads to erroneous results.
* **Explainability is required.** Models and data must be transparent, traceable, and testable for V&V and safety investigations.
* **Security risks expand.** Data files, off‑the‑shelf AI libraries, and model inputs introduce new attack vectors. Treat AI/ML data as safety‑critical when used in critical systems.
* **AI/ML still must satisfy all NPR 7150.2 SWEs.** Requirements, architecture, design, test, V&V, cybersecurity, and configuration management all apply.
* **Data management becomes part of the software product.** Must archive, version, validate, and document all training/testing datasets, model weights, and assumptions. (SWE‑042, SWE‑206, SWE‑196).
* **Testing is harder.** Traditional code coverage does not apply; need to show each neural‑network component affects outputs (SWE‑219). Validation must use data beyond training/test sets. (SWE‑055).
* **Model‑of‑model risk.** Using simulation‑generated data compounds approximation error; must ensure simulation assumptions aren’t lost.
* **Operational confidence remains limited.** No provable means yet exists to certify AI/ML for safety‑critical roles; must maintain human oversight and independent verification.

**Software Management Expectations & Software Assurance Focus Areas:**

* **Define and verify quality criteria.** AI requires explicit measures for performance, risk, robustness, and compliance. SA validates these criteria and ensures improvements over time.
* **Balance quality with schedule and cost.** SA helps identify the most critical vulnerabilities and risks when trade‑offs are necessary.
* **Use AI/ML tools to improve SA.** Automated static analysis and other tools can detect defects, security issues, and coverage gaps more efficiently. SA must validate tool usage and results.
* **Support verification & validation of** **probabilistic** **systems.** AI is not fully deterministic; SA must help define V&V criteria appropriate for probabilistic, learning systems.
* **Ensure privacy, security, and ethical compliance.** Protection of training data, configuration control, and ethical considerations (fairness, transparency, risk) are now integral responsibilities for management.
* **Define and verify quality criteria.** AI requires explicit measures for performance, risk, robustness, and compliance. SA validates these criteria and ensures improvements over time.
* **Balance quality with schedule and cost.** SA helps identify the most critical vulnerabilities and risks when trade‑offs are necessary.
* **Use AI/ML tools to improve SA.** Automated static analysis and other tools can detect defects, security issues, and coverage gaps more efficiently. SA must validate tool usage and results.
* **Support verification & validation of** **probabilistic** **systems.** AI is not fully deterministic; SA must help define V&V criteria appropriate for probabilistic, learning systems.
* **Ensure privacy, security, and ethical compliance.** Protection of training data, configuration control, and ethical considerations (fairness, transparency, risk) are now integral responsibilities for management.

You can use AI as safety critical code but the project needs to develop and vet the plan and approach for development, training, and testing. The project needs to be able to explain why we are using AI in safety critical applications and if the AI is going to generate actions with or without any other checks.

# Appendix A — Assurance Checklist

* **Suitability:** Is AI the right approach for the problem and context? (Document rationale.)
* **Data:** Are provenance, licensing, representativeness documented for training/retrieval/prompt exemplars? Are drift monitors deployed?
* **Evaluation:** Are lab and production evaluations defined with probabilistic criteria and human‑judgment workflows?
* **Security:** Have GenAI risks and supply‑chain threats been assessed and red‑teamed?
* **Safety:** Is there a safety case and runtime safeguards/circuit breakers?
* **Uncertainty:** Are confidence/abstention mechanisms implemented and communicated to users?
* **Oversight:** Are autonomy boundaries, approval gates, and escalation paths defined and measured?
* **Architecture:** Are components modular with substitution/rollback plans?
* **Traceability:** Are models, prompts, data, guardrails, tools, and evaluations versioned and reproducible (see SWE‑070)?
* **Sustainment:** Are budgets/plans in place for monitoring, retraining, provider/API changes, and retirement?

## Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-3) in the Resources tab.

# **2. Generative AI Metrics**

Defining metrics for the complexity of generative AI models requires tailoring your evaluation to the unique characteristics of these systems—such as their architecture, size, computational requirements, capabilities, and usability. Unlike traditional software complexity metrics (e.g., cyclomatic complexity), generative AI complexity is often evaluated through model-specific engineering, mathematical, and operational characteristics.

Projects **should** tailor metrics to architecture, computational footprint, operational context, and safety requirements.

**Architectural & Computational**

* Layers/parameters, attention heads, embedding dimensions; FLOPs, memory, latency, and **power consumption**.

**Representational & Output**

* Expressive power, output entropy/diversity; sequence length; long‑range **coherence scores**; temperature and sampling diversity.

**Training & Adaptation**

* Dataset size/quality, convergence iterations, optimizer configuration; **parameters adapted** (PEFT vs. full fine‑tuning); data requirements for domain generalization.

**Interpretability & Safety**

* Explainability indicators (saliency/attention analysis), **bias/fairness audits**, safety‑violation rates, abstention/refusal rates.

**Deployment & Operations**

* Scalability, end‑to‑end latency, API integration complexity, **robustness to adversarial inputs**, drift indicators, and **operational cost** (inference/training).

Below is a comprehensive guide to key metrics that you can use:

## **2.1 Architectural Complexity**

**Metrics**:

* **Number of Layers:** The depth or number of layers in the neural network architecture (e.g., 12 layers for GPT-2, 96 layers for GPT-4).
* **Parameters:** Total number of trainable parameters (e.g., billions for most large language models).
* **Attention Heads:** In transformer models, attention heads drive complexity. Evaluate the number of heads per layer and their interactions.
* **Non-Linearity:** Measure the types and number of activation functions (e.g., ReLU, GELU).

**Why Important**:

These metrics indicate the model's capacity to learn complex patterns. Larger and deeper architectures typically have higher expressivity but come with increased computational cost.

## **2.2 Computational Complexity**

**Metrics**:

* **Floating-Point Operations per Second (FLOPs):** The number of computations required to perform training and inference.
* **Memory Requirements:** GPU or RAM usage during training and inference—especially significant for deployment on constrained systems.
* **Inference Time:** Latency in generating outputs. Faster inference models are considered less complex and more efficient.
* **Power Consumption:** Energy required for training and inference, relevant for sustainable AI practices.

**Why Important**:

These metrics determine the model's scalability and operational costs for deployment and training. For example, models with high FLOPs and memory requirements are often harder to scale.

## **2.3 Model Representational Complexity**

**Metrics**:

* **Expressive Power:** The ability of the model to learn and represent complex functions or dynamics.
* **Entropy of Outputs:** Capturing the diversity and unpredictability of model outputs during inference.
* **Embedding Space Size:** The dimensionality of the embeddings used internally (e.g., 768 for GPT-2, 4096 for GPT-4).

**Why Important**:

These metrics highlight how effectively the model can generalize across diverse tasks and inputs while maintaining rich representations.

## **2.4 Training Complexity**

**Metrics**:

* **Dataset Size:** The volume of training data required (e.g., tokens or examples in billions for large models).
* **Training Iterations:** Number of epochs or updates needed to achieve convergence.
* **Learning Rate Dynamics:** The adaptation of learning rates during training, which impacts convergence speed.
* **Optimization Complexity:** Evaluate the type of optimizer used (e.g., Adam vs. AdaFactor) and its configuration.

**Why Important**:

High training complexity can imply longer development times and greater hardware requirements to train a model properly.

## **2.5 Fine-Tuning and Adaptation Complexity**

**Metrics**:

* **Number of Parameters Adapted:** How much of the model can or must be fine-tuned for specific tasks (e.g., fine-tuning full models vs. adapter layers in PEFT [Parameter-Efficient Fine-Tuning]).
* **Data Requirements for Fine-Tuning:** The amount of task-specific data required to adapt the model.
* **Domain Generalization:** The model’s ability to generalize across new domains without full retraining.

**Why Important**:

Assessing fine-tuning complexity helps determine the model’s usability for downstream applications.

## **2.6 Output Complexity**

**Metrics**:

* **Sequence Length:** The maximum number of tokens or characters the model can process or generate in a single inference step.
* **Coherence Score:** How logically connected the outputs are over long sequences (subjective or algorithmic measures).
* **Temperature and Diversity:** Configurations used during inference and their influence on creativity or randomness of generative outputs.

**Why Important**:

Output complexity impacts the quality and usability of generative and conversational results, especially for tasks requiring coherence, relevance, or creativity.

## **2.7 Interpretability Complexity**

**Metrics**:

* **Explainability:** How easy it is to understand the internal workings of the model (e.g., decision-making pathways or attention distributions).
* **Saliency Maps:** Highlights in the input that influence the outputs, which are useful for interpretability tools.
* **Layer Contribution Analysis:** Understanding which layers contribute most to model performance.
* **Bias and Fairness Audits:** The complexity of detecting and mitigating bias in the model outputs.

**Why Important**:

Interpretability metrics are crucial for ethical AI deployment and trust-building in sensitive applications.

## **2.8 Real-World Deployment Complexity**

**Metrics**:

* **Scalability:** How easy it is to scale up or down the model architecture for different hardware configurations.
* **Latency:** The time taken for the model to respond or process input in real-world usage scenarios.
* **API Complexity:** The ease or difficulty of integrating the model into applications (e.g., REST APIs vs. custom libraries).
* **Security and Robustness:** Complexity of ensuring the model is robust to adversarial attacks or misuse.

**Why Important**:

Deployment complexity plays a significant role in practical utility, customer satisfaction, and security of generative AI solutions.

## **2.9 Best Practices for Defining Metrics**

1. **Task-Specific Design:** Tailor metrics to your specific use case, whether it's text generation, image generation, or conversational AI.
2. **Benchmarking:** Use standard benchmarks such as GLUE, SuperGLUE, BLEU, ROUGE, or human evaluation to assess performance alongside complexity.
3. **Holistic View:** Combine several complexity metrics for a more complete picture (architectural, computational, and deployment complexity).
4. **Comparative Analysis:** Compare your model against others (e.g., GPT, BERT, DALL-E) to contextualize complexity scores.

## **2.10 Tools and Frameworks for Complexity Evaluation**

**Example**: You can use tools like these for computation-heavy components:

* **Weights & Biases (W&B):** For tracking FLOPs, memory use, and other training metrics.
* **Hugging Face Benchmarking Tools:** For evaluating inference performance.
* **Explainability Libraries:** Captum, SHAP, or LIME for interpretability complexity.
* **Energy Usage Estimators:** Like CodeCarbon, to assess power consumption.

By defining and measuring these complexity metrics, you can assess generative AI models more effectively, ensure performance optimization, and improve deployment decisions.

# 3. Resources

## 3.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

No references have been currently identified for this Topic. If you wish to suggest a reference, please leave a comment below.

## 3.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-034 - Acceptance Criteria](/spaces/SWEHBVD/pages/102695413/SWE-034+-+Acceptance+Criteria) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) * [SWE-151 - Cost Estimate Conditions](/spaces/SWEHBVD/pages/102695507/SWE-151+-+Cost+Estimate+Conditions) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-193 - Acceptance Testing for Affected System and Software Behavior](/spaces/SWEHBVD/pages/102695528/SWE-193+-+Acceptance+Testing+for+Affected+System+and+Software+Behavior) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>3</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
|  |

## 3.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
|  |
