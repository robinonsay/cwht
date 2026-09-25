# 7.25 - Artificial Intelligence And Software Engineering

> NASA Software Engineering Handbook (SWEHB Ver D), page id 184320054. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering

7.25 - Artificial Intelligence And Software Engineering

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/184320054/7.25+-+Artificial+Intelligence+And+Software+Engineering#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=184320054)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=184320054&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Background](#tabs-1)
* [2. NASA Authorities](#tabs-2)
* [3. AI/ML in a Project](#tabs-3)
* [4. Guidance on Data](#tabs-4)
* [5. Criticality](#tabs-5)
* [6. Code Generation](#tabs-6)
* [7. Considerations for SWEs](#tabs-7)
* [8. Resources](#tabs-8)

# 1. Background

Artificial Intelligence (AI) is a computer’s capability to emulate a human’s ability to think.  One example of AI is autonomy/automation, which NASA has been using since inception.  AI is implemented in software and governed by software development processes.  Machine Learning (ML), a subfield of AI, presents training data to a computer program to generate an algorithm without being explicitly programmed.  This can be referred to as generative AI which includes general adversarial networks (GANs), recurrent neural networks (RNNs), transformers, reinforcement learning, and so on.  People use the term AI/ML frequently with regard to general AI; however, engineering teams should be clear to specify the type of AI being discussed and to be consistent when referring to AI. This is critical when working with vendors.

AI/ML uses statistical modelling to determine weights (the coefficients) for a set of equations.  AI/ML models often include randomization functions on the outputs to avoid producing the same information each time, but this can be omitted or disabled.  The underlying statistical nature of AI/ML algorithms make predicted behavior complex or indeterministic in many cases.  AI/ML model responses are usually coupled with training data and dependent on modeling assumptions and systems design/architecture.

## 1.1 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 2. NASA Authorities and Usage

NASA’s roles and responsibilities regarding implementation of AI systems are listed below and follow similarly to other software systems.

* **Office of the Chief Engineer** (OCE)
  + Technical authority for the engineering usage of AI on mission systems.
  + OCE will assess the technical capabilities and provide the software policies and requirements for the use of AI on missions.
* **Office of Safety and Mission Assurance** (OSMA)
  + Technical authority for the safety and providing independent assessments and verifications on missions.
  + OSMA will provide the hazard analysis, safety determinations, and independent verification and validation (V&V) of the AI system.
* **Office of the Chief Health and Medical Officer** (OCHMO)
  + Technical authority for the health and wellness of the entire NASA workforce including crew and ground personnel.
  + OCHMO will provide the impacts and guidance, if the AI system presents any medical impacts to personnel.
* **Office of the Chief Information Officer** (OCIO)
  + Responsible for the tools and security posture of the AI systems deployed at NASA.
  + OCIO will authorize the ability to use the AI systems, this can be for day-to-day work, generation of reports, summarization, generation of images, and so on.
* **Office of the General Counsel** (OGC)
  + Responsible for the full spectrum of legal disciplines related to AI.
  + OGC will provide guidance and support related to legal usage, intellectual property rights, ethics, and related topics.

# 3. Guidance on when to use AI/ML for a Project

AI/ML is a tool or strategy for development within the suite of software tools.  While AI/ML can solve multiple problems, it is not a solution for every type of problem.  Below is general guidance on when to use, and  not use, AI/ML algorithms. This is not intended to be a complete list and include exceptions.

## 3.1 If rules, computations, or predetermined steps can be explicitly programmed, it is not necessary to use AI/ML.

V&V of software is simplified for explicitly programmed or deterministic systems and has a well-established set of standard tools and techniques that have been used for decades.  During testing, inspection of algorithms and specific test cases can be created.  Generally, though not always, explicit programming techniques can more easily predict and determine the behavior of the software.  Computers are fundamentally deterministic but can also be used to perform probabilistically through varying techniques, including random number generation.  Architecture of the code can introduce inconsistencies; interaction among multiple tasks adds complexities.  AI/ML algorithms add another layer of complexity to the software.  Engineers and scientists may need to know if the approximation of a computation is of a certain magnitude or if the algorithm needs to model nonlinear effects.  Analysts and testers can calculate linear, polynomial, or similar methods using explicitly programmed software.

## 3.2 A good candidate for AI/ML: if rules cannot be coded explicitly or if the problem is statistical in nature.

The complexity of the software rules that would be created if the code is written out may exceed cyclomatic complexity or create code with simplifying assumptions of the system.  As stated previously, an AI/ML system uses the data presented to generate a statistical approximation of the system.  Underlying patterns in this data may not easily be identified by a human.  These underlying effects may or may not need to be modeled, and through the choice of the software developer, those effects need to be considered.  A tradeoff between computation (calculating the equations directly) versus utilizing a neural network algorithm, which may be memory intensive, should be conducted during design.  Overlapping rules or finely tuning code based on gathered data lends itself to utilizing AI/ML algorithms due to the direct usage of the data.  The parameters used for creation of the AI/ML algorithm will drive how well the model matches the data.  The possibility for overfitting the model to the data makes the model produce a result specific to that dataset.

## 3.3 Information or processes cannot be scaled manually.

Scaling applies in general to automation and computing, by having a machine do repetitive, controlled tasks faster than humans. The developed software can retain the input information and can repeat the same steps with high precision and speed.  AI/ML provides a method for the software to emulate a human at a larger and faster scale.  Software developers can directly utilize the data and scale processing on new data quicker rather than having an algorithm be developed.  The AI/ML model will only examine the correlation between the input data, humans will need to use their knowledge to filter the inputs.  AI/ML models can reduce the amount of data to analyze manually by providing a threshold or confidence level for a filter.

## 3.4 Having large data sets of useable information.

For specialized AI applications (NASA has developed or customized the AI with discipline specific data) as opposed to general AI, there must exist enough truth data to both train the model and test it.   The amount of data containing the effects to be captured by an AI/ML model must be statistically significant.  NASA develops software for many applications, but each application is often specialized.  When utilizing AI/ML algorithms, no new information is calculated; the system is interpolating or extrapolating from the data set on which it was trained.  That is, if the data being used does not include the effect, an answer will still be generated but it may be erroneous.  Using data to train and test the model indicates that if the representative data for the effects is not large enough to have a statistically significant effect on the model coefficients, this can impact results.  An extreme example is, if the data representing the specific phenomenon is included only in the training set, then the testing data will not properly test the created model, deceiving the developer into thinking the model has higher accuracy.  The opposite is true if all the data for a specific phenomenon is included only in the test set but not the training.  When the developer tests the model with the data on which it was not trained, the model will present lower accuracy.  These are both examples where the result is known.

An operational mission problem where the software is used but the answer is unknown or unchecked, may produce unintended results.  Keep in mind, the amount and quality of data drive the AI/ML model:  if the data is labeled, that means that a solution or conclusion has been provided for the system to utilize; if the data is unlabeled, this means that the data is not marked and therefore has no reinforcement of the correctness.  For example, if humans have labeled a requirement as verifiable or not verifiable, the AI/ML can utilize that for calculations and output.

## 3.5 If the computation results are acceptable within a tolerance or confidence level – if errors can be tolerated.

Many AI/ML systems provide results along with a confidence level or degree of certainty.  For systems which require 100% deterministic confidence, an AI/ML system may not be recommended.  When defining requirements, the expected correctness or reliability of a system must be quantified.  The reliability will drive system architecture and put performance parameters on expected performance of the chosen design solution.

# 4. Guidance on Data

Data is the most critical part of an AI/ML system.  The input data carries with it all of the information that the AI/ML algorithm will use to determine the probabilities for outcomes.

## 4.1 Fully data-driven systems are a paradigm shift for software systems.

Traditional software systems use written code with predetermined rules that execute on input data.  Fully data-driven systems do not have the same suite of tools to test the data as code.  Examples are code coverage and Modified Condition/Decision Coverage (MC/DC).  In traditional code, the code can be executed and analyzed to ensure that all lines are executed, all branches are executed, and each conditional of the branch is shown to affect the branch selection.  In a fully data-driven system, these tools do not currently exist to ensure that all of the data is influential (affecting the decisions) and a complete data set.  Users must test the datafiles to ensure all data is shown to affect the execution of the code.  Users must test that all the data is used to affect the response of the software.  Data-driven systems limit logical errors that static and/or dynamic analysis tools identify in traditional code.  Users must test the combinations of the input data executing with the code to identify and eliminate logical errors in both the data and the configured code.

## 4.2 The data must be fair and encapsulate all of the intended outcomes.

AI/ML models do not calculate the underlying equations represented in the data; the models approximate the data by statistical means.  This has multiple effects on the resulting code.  The most obvious effect is when a situation is presented to the AI/ML code that was not in the data; nothing anchors the execution of the code, which elevates the probability of an erroneous output from the code.  Due to the weights (or coefficients) being generated by the input data, if the input data does not fairly represent the problem, the resulting code will not be correct for the intended purpose, thus leading to an erroneous output.  Off-nominal events may present lower probabilities of occurring, and statistically may be eliminated, when compared to nominal runs or even no data collected.

## 4.3 Model data being used as input data for AI/ML.

For NASA’s specialized applications, engineers often do not have enough experimental or measured data from a real system (e.g., landing on Earth’s Moon with a newly developed lander).  Simulations for these situations are developed, which contain approximations of the reality (simplifications, correct/incorrect assumptions).  If simulation results are used to create an AI/ML model, this leads to a model of a model.  Models of models can contain a buildup of approximation error and implicit filters of effects through these approximations.  Regularly, when using the data from a simulation, the assumptions from the creation of that data can be lost.  The generated data must encapsulate all of the intended outcomes.

## 4.4 The data and the AI/ML model need to be explainable and transparent on how results were determined.

The software needs to be verifiable and validated, as well as explainable, so that as the mission is being operated, engineers can reconstruct events to mitigate anomalies or failures, and to maintain safety, security, and scientific accuracy.  Implementations in software can influence how scientific data is interpreted or collected.  This could be through calculations for turning on systems to modifying control surfaces.  Software developers must document the algorithms and all decision paths that the software can take.  The code must protect against unintended paths and be able to trace which paths were taken.

## 4.5 The data and the AI/ML model need to be secure and safe for use.

Utilizing data sets that may or may not have been examined potentially leads to multiple attack vectors from a security perspective.  If data sets have been corrupted or contain hidden malicious information, this may be concealed from users and developers until deployment, or an incident occurs.  The AI libraries may have security vulnerabilities or exploits that are unknown.  OSMA still has authority on the definition and declaration of safety critical code, but Engineering needs to include the data files as part of the safety criticality, applying the same level of rigor and requirements to the data files as the safety critical code.  Due to most AI/ML packages featuring off-the-shelf code, software developers need to understand and test the limits of the code as required by [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) and [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks).  If the AI/ML system is used to generate code, [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code), applies as well.

## 4.6 The data and the AI/ML models need to be scientifically and technically robust.

While software is an important part of the system, the software is created to control systems or do calculations for scientific and engineering work.  To that end, both the AI/ML model and data need to adhere to NASA-STD-7009 [248](#_tabs-<p>8</p>) and provide methodologies to test the software.  Software requirements for the system must be created and include considerations for failures.  If the AI/ML system is learning during deployment, the data needs to be controlled in order to maintain traceability and configuration control.  The software system requires unit testing beyond the testing/training data sets used to create the model.  While AI/ML models can be created from limited data, a data-driven system differs from traditional software methods because of the ability to run a larger code path than restricted known paths which are explicitly coded by developers.

## 4.7 The data split for training and testing should typically be around 70% - 80% for training, and the remaining 20-30% for testing.

The split between training and testing is a decision for the project and its technical authorities and should be captured within the software design documentation.  Academic papers are supporting and the AI/ML community has converged on this split.  Multiple techniques can determine how to split the data and what methodology to use.  The training and testing data sets must be representative of the scenario, and example of how to do this can be found in "**AI Testing: Ensuring a good data split between data sets (Training and Test) using K-means clustering and decision tree analysis**" [307](#_tabs-<p>8</p>).

# 5. Criticality Considerations

While AI/ML is not a new field — the theories have been around since the 1950s — the computing power that is available to apply the algorithms has evolved to where usage is more common.  In deep space applications, the processing power is still limited by the size, weight, and power (SWaP) considerations in addition to the radiation hardening of the processor and supporting systems.  During training of an AI/ML algorithm, the computational load is the highest and graphics processing units (GPUs) are used to accelerate the computations due to the massively parallel computations.  Space systems orders feature less computational ability than ground systems.

If hardware challenges are overcome, software AI/ML algorithm challenges are still present.  There is a distinction between the algorithm and the software code.  Software code focuses more on the implementation of the algorithm and does not directly consider if the algorithm is correct or accurate. An example of this could be using the ideal gas law for calculation instead of the real gas law.  This does not mean that software developers have no responsibility for the correctness of accuracy of the software.  Software developers are still required to apply the software engineering requirements such as testing against the requirements ([SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing)), using validated and accredited software models … ([SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools)).

As required by [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software), the safety-criticality of the software shall be determined with OSMA.  In addition to the safety criticality, the software developers must understand the mission criticality of the AI/ML algorithm.  Safety of human lives and infrastructure must be at the top of the list for any developer.  AI/ML enables new applications for software, but this application must be balanced with the criticality of the system.  The most significant problem being faced is the confidence that for any safety-critical applications, there is not a provable means to evaluate the AI/ML system and show that they meet the safety requirements.

## 5.1 AI/ML for safety-critical or other high criticality application is not recommended.

**GenAI tools may be used on safety critical software projects; however, at this time we do not recommend using AI/ML or GenAI tools to generate, modify, or be safety critical code.** These tools may be used only to support evaluation activities—such as analyzing existing code, reviewing soft-ware artifacts, or assisting with documentation assessment—where all results can be inde-pendently verified through established methods.  
In the future, direct use of AI/ML in safety critical functions may become feasible once proven, certifiable methods exist to evaluate AI/ML systems against safety requirements. Until such methods are in place, AI/ML should operate strictly in an advisory capacity, with all outputs confirmed using non AI means.  
Examples include:  
• Using an AI/ML system to provide advisory recommendations to a controller or pilot, with all suggestions independently validated before action is taken.  
• Using AI/ML algorithms in manufacturing processes, provided all resulting materials or com-ponents undergo complete destructive and non destructive evaluation to verify safety and per-formance.

# 6. Guidelines for using AI for Code Generation

Leveraging AI technology for code generation offers significant productivity gains for software engineers developing systems.  Developers should be cognizant of the code generation tool(s) used and the data being generated in accordance with Agency policy and approved tools.  For general software that is not mission specific or sensitive, obtaining AI-generated code should be treated similarly to obtaining other open-source code, freely available on the internet.  The code can be incorporated as re-use.  Agency-provided secure AI code generation tools should be used for code specific to missions.  More information on this guideline should be found in OCIO guidance **"Updated Guidance on the Use of Generative AI Capabilities"** [440](#_tabs-<p>8</p>) (Internal NASA-only). 

If code is generated by AI, the developer is still responsible for the code and must review before submitting.  No markings that an AI generated the code is necessary.

# 7. AI/ML Considerations for Specific SWEs

#### All NPR 7150.2 SWEs are applicable to AI/ML software.

## 7.1 NPR 7150.2 SWEs apply to AI/ML software the same as all other software.

Developers and users of AI/ML software will need to apply special attention to several of the SWEs, but they do not have any additional guidance.  The [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) must contain documentation regarding the AI/ML system, including management of the data, models, and associated AI/ML information.  The software requirements must contain specific ones for the AI/ML system, such as performance, uncertainty, accuracy, and redundancies.  Developers, scientists, and engineers need to ensure that the AI/ML system is well documented, planned, and features developed architecture, design, code, data sets, testing,  and V&V. The test, and V&V planning and execution portions of the software lifecycle will have a new set of challenges because of the AI/ML data, hybrid of model and data driven system, and the statistical nature of the system.  The software cybersecurity requirements are more complex with the additional attack vectors of the data.

## 7.2 Specific considerations for AI systems in SWEs

Specific considerations for AI systems in relation to the NPR 7150.2 SWEs are listed below. Updated formal guidance for AI will be included in the NPR in subsequent revisions.

**SWE-033 - Acquisition vs. Development Assessment**

3.1.2 The project manager shall assess options for software acquisition versus development.

* This includes if using AI/ML and if using an open source or off-the-shelf model or building the model.

**SWE-042 - Source Code Electronic Access**

3.1.10 The project manager shall require the software developer(s) to provide NASA with electronic access to the source code developed for the project in a modifiable format.

* Input data used to train and test the models must be provided. The resulting model, including weights and biases, should also be provided.

**SWE-219 - Code Coverage for Safety Critical Software**

3.7.4 If a project has safety-critical software, the project manager shall ensure that there is 100 percent code test coverage using the Modified Condition/Decision Coverage (MC/DC) criterion for all identified safety-critical software components.

* For MC/DC and AI/ML, each node in a neural network must be shown to affect the solution and all paths evaluated.

**SWE-146 - Auto-generated Source Code**

3.8.1 The project manager shall define the approach to the automatic generation of software source code including:

a. Validation and verification of auto-generation tools.  
b. Configuration management of the auto-generation tools and associated data.  
c. Description of the limits and the allowable scope for the use of the auto-generated software.  
d. Verification and validation of auto-generated source code using the same software standards and processes as hand-generated code.  
e. Monitoring the actual use of auto-generated source code compared to the planned use.  
f. Policies and procedures for making manual changes to auto-generated source code.  
g. Configuration management of the input to the auto-generation tool, the output of the auto-generation tool, and modifications made to the output of the auto-generation tools.

* AI/ML falls under this requirement since it is a means of auto-generation of source code. AI/ML algorithms including data, data files, model files, and AI-generated source code are all subject to this SWE.

**SWE-206 - Auto-Generation Software Inputs**

3.8.2 The project manager shall require the software developers and custom software suppliers to provide NASA with electronic access to the models, simulations, and associated data used as inputs for auto-generation of software.

* This SWE is emphasized for AI/ML and the data files.

**SWE-055 - Requirements Validation**

4.1.7 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment.

* AI/ML implementations must assure that validation of the system is done with data beyond the training and test data set used to develop and verify the AI/ML model.

**SWE-196 - Software Retirement Archival**

4.6.6 The project manager shall identify the records and software tools to be archived, the location of the archive, and procedures for access to the products for software retirement or disposal.

* Any data files used to train, test, or modify the AI/ML model must be maintained and archived along with the model itself.

**SWE-057 - Software Architecture**

4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture.

* The software architecture must contain a representation of the neural-net model and where the data is routed through the system. The architecture description of the AI/ML system should be clearly described.

**SWE-058 - Detailed Design**

4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested.

* The software design must clearly depict the number of nodes, any feedback loops for reinforcement learning, and where each set of data is input and output. The design must show any bias information, weights (or coefficients) of the nodes, and any other design considerations.

# 8. Resources

### 8.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-248)

  [NASA HANDBOOK FOR MODELS AND SIMULATIONS: AN IMPLEMENTATION GUIDE FOR NASA-STD-7009](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009 "Click to open in new window")

  NASA-HDBK-7009 Revision: A, Document Date: 2019-05-08,
  Next 5-Year Review Date: 2024-05-08
* (SWEREF-307)

  [AI Testing: Ensuring a good data split between data sets (Training and Test) using K-means clustering and decision tree analysis](https://www.enrichedpublications.com/ep_admin/jounral/pdf/1709635755.pdf#page=41 "Click to open in new window")

  Sugali, K., Sprunger, C. and Inukollu V., International Journal on Soft Computing (IJSC) Volume 15, Issue 01, January-April 2024, pp. 34-45.
* (SWEREF-440)

  [Updated Guidance on the Use of Generative AI Capabilities](https://nasa.sharepoint.com/sites/AIML/SitePages/Generative-AI-guidance.aspx "Click to open in new window")

  NASA AIML Team,  NASA can empower its workforce to use GenAI capabilities to develop next-generation technology and discover new data-driven insights.

### 8.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

### 8.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-033 - Acquisition vs. Development Assessment](/spaces/SWEHBVD/pages/102695412/SWE-033+-+Acquisition+vs.+Development+Assessment) * [SWE-042 - Source Code Electronic Access](/spaces/SWEHBVD/pages/102695418/SWE-042+-+Source+Code+Electronic+Access) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-196 - Software Retirement Archival](/spaces/SWEHBVD/pages/102695531/SWE-196+-+Software+Retirement+Archival) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |

### 8.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>8</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| To be developed later. |
