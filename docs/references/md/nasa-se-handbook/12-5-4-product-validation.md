# 5.4 Product Validation

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 99–105. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §5.4`.

Product Validation.

• • • • • • •

FIGURE 5.4-1, taken from NPR 7123.1, provides a typical flow diagram for the Product Validation Process and identifies typical inputs, outputs, and activities to consider in addressing product validation.

the verification approach, verification in the life cycle, verification procedures, verification reports end-to-end testing, use of modeling and simulations, and hardware-in-the-loop testing.

The Product Validation Process is the second of the verification and validation processes conducted on an implemented or integrated end product. While verification proves whether “the product was done right,” validation proves whether “the right product was done.” In other words, verification provides objective evidence that every “shall” statement in the requirements document or specification was met, whereas validation is performed for the benefit of the customers and users to ensure that the system functions in the expected manner when placed in the intended environment. This is achieved by examining the products of the system at every level of the product structure and comparing them to the stakeholder expectations for that level. A well-structured validation process can save cost and schedule while meeting the stakeholder expectations.

#### 5.4.1 Process Description

##### 5.4.1.1 Inputs

Key inputs to the process are:
- End product to be validated: This is the end product that is to be validated and which has successfully passed through the verification process.
- Validation plan: This plan would have been developed under the Technical Planning Process and
baselined prior to entering this process. This plan may be a separate document or a section within the Verification and Validation Plan.
- Baselined stakeholder expectations: These would
have been developed for the product at this level during the Stakeholder Expectations Definition Process. It includes the needs, goals, and objectives as well as the baselined and updated concept of operations and MOEs.
- Any enabling products: These are any special
equipment, facilities, test fixtures, applications,

or other items needed to perform the Product Validation Process.

The objectives of the Product Validation Process are:
- To confirm that the end product fulfills its intended
use when operated in its intended environment:

##### 5.4.1.2 Process Activities

The Product Validation Process demonstrates that the end product satisfies its stakeholder (customer and other interested party) expectations (MOEs) within the intended operational environments, with validation performed by anticipated operators and/or users whenever possible. The method of validation is a function of the life cycle phase and the position of the end product within the system structure. There are five major steps in the validation process: (1) preparing to conduct validation, (2) conduct planned validation (perform validation), (3) analyze validation results, (4) prepare a validation report, and (5) capture the validation work products.

Validation is performed for each implemented or integrated and verified end product from the lowest end product in a system structure branch up to the top level end product (the system). »» Evidence is generated as necessary to confirm that products at each layer of the system structure meet the capability and other operational expectations of the customer/ user/operator and other interested parties for that product. »»

From Product Verification Process End Product to Be Validated From Configuration Management Process Stakeholder Expectation Baseline From Design Solution and Technical Planning Processes Product Validation Plan From existing resources or Product Transition Process Product Validation– Enabling Products

To Product Transition Process Prepare to conduct product validation

Perform the product validation

Validated End Product

To Technical Assessment Process Product Validation Results

Analyze the outcomes of the product validation

Prepare a product validation report

Capture the work products from product validation activities

To Technical Data Management Process Product Validation Report

Product Validation Work Products

FIGURE 5.4-1 Product Validation Process

- To ensure the human has been properly integrated
into the system: The user interface meets human engineering criteria. »» Operators and maintainers have the required skills and abilities. »» Instructions are provided and training programs are in place. »» The working environment supports crew health and safety. »»

- To ensure that any problems discovered are
appropriately resolved prior to delivery of the end product (if validation is done by the supplier of the product) or prior to integration with other products into a higher level assembled product (if validation is done by the receiver of the product). 5.4.1.2.1 Product Validation Preparation

To prepare for performing product validation, the appropriate set of expectations, including MOEs and MOPs, against which the validation is to be made

METHODS OF VALIDATION Analysis: The use of mathematical modeling and analytical techniques to predict the suitability of a design to stakeholder expectations based on calculated data or data derived from lower system structure end product verifications. Analysis is generally used when a prototype; engineering model; or fabricated, assembled, and integrated product is not available. Analysis includes the use of modeling and simulation as analytical tools. A model is a mathematical representation of reality. A simulation is the manipulation of a model. Demonstration: Showing that the use of an end product achieves the stakeholder expectations as defined in the NGOs and the ConOps. It is generally a basic confirmation of behavioral capability, differentiated from testing by the lack of detailed data gathering. Demonstrations can involve the use of physical models or mock-ups; for example, an expectation that controls are readable by the pilot in low light conditions could be validated by having a pilot perform flight-related tasks in a cockpit mock-up or simulator under those conditions. Inspection: The visual examination of a realized end product. Inspection is generally used to validate the presence of a physical design features or specific manufacturer identification. For example, if there is an expectation that the safety arming pin has a red flag with the words “Remove Before Flight” stenciled on the flag in black letters, a visual inspection of the arming pin flag can be used to determine if this expectation has been met. Test: The use of an end product to obtain detailed data needed to determine a behavior, or provide sufficient information to determine a behavior through further analysis. Testing can be conducted on final end products, breadboards, brassboards, or prototypes. Testing produces information at discrete points for each specified expectation under controlled conditions and is the most resource-intensive validation technique.

should be obtained. In addition to the V&V Plan, other documentation such as the ConOps and HSI Plan may be useful. The product to be validated (output from implementation, or integration and verification), as well as the appropriate enabling products and support resources (requirements identified and acquisition initiated by design solution activities) with which validation will be conducted should be collected. Enabling products includes those representing external interfacing products and special test equipment. Support resources include personnel necessary to support validation and operators. Procedures, capturing detailed step-by-step activities and based on the validation type and methods are finalized and approved. Development of procedures typically begins during the design phase of the project life cycle and matures as the design is matured. The validation environment is considered as part of procedure development. Operational scenarios are assessed to explore all possible validation activities to be performed. The final element is preparation of the validation environment; e.g., facilities, equipment, software, and climatic conditions. When operator or other user interaction is involved, it is important to ensure that humans are properly represented in the validation activities. This includes physical size, skills, knowledge, training, clothing, special gear, and tools. When possible, actual end users/operators should be used and other stakeholders should participate or observe activities as appropriate and practical. Outcomes of validation preparation include the following:
- The validation plan, approved procedures, supporting configuration documentation, and an
appropriate baseline set of stakeholder expectations are available and on hand;

- Enabling products are integrated within the validation environment according to plans and schedules;
- Users/operators and other resources are available
according to validation plans and schedules; and
- The validation environment is evaluated for adequacy, completeness, readiness, and integration.
5.4.1.2.2 Perform Product Validation

The act of validating the end product is performed as spelled out in the validation plans and procedures, and the conformance established to each specified stakeholder expectation (MOEs and ConOps) shows that the validation objectives were met. Validation differs from qualification testing. Validation testing is focused on the expected environments and operations of the system where as qualification testing includes the worst case loads and environmental requirements within which the system is expected to perform or survive. The verification lead should ensure that the procedures were followed and performed as planned, the validation-enabling products and instrumentation were calibrated correctly, and the data were collected and recorded for required validation measures. When a discrepancy is observed, the validation should be stopped and a discrepancy report generated. The activities and events leading up to the discrepancy should be analyzed to determine if a nonconforming product exists or there is an issue with the verification procedure, conduct, or conditions. If there are no product issues, the validation is replanned as necessary, the environment preparation anomalies are corrected, and the validation is conducted again with improved or correct procedures and resources. The Decision Analysis Process should be used to make decisions with respect to needed changes to the validation plans, environment, and/or conduct.

Outcomes of performing validation include the following:
- A validated product is established with supporting confirmation that the appropriate results were
collected and evaluated to show completion of validation objectives.
- A determination is made as to whether the fabricated/manufactured or assembled and integrated
products (including software or firmware builds and human element allocations) comply with their respective stakeholder expectations.
- A determination is made that the validated product was appropriately integrated with the validation environment and the selected stakeholder
expectations set was properly validated.
- A determination is made that the product being
validated functions together with interfacing products throughout their operational envelopes.

the end product. If it is found to be a result of the test configuration, the configuration should be corrected and the validation repeated. If it is found to be a result of the end product being validated, discussions with the customer should be held and any required system design and product realization process activities should be conducted to resolve deficiencies. The deficiencies along with recommended corrective actions and resolution results should be recorded, and validation should be repeated, as required. Outcomes of analyzing validation results include the following:
- Product anomalies, variations, deficiencies, nonconformance and/or issues are identified.
- Assurances that appropriate replanning, redefinition of requirements, design, and revalidation
have been accomplished for resolution of anomalies, variations, deficiencies or out-of-compliance conditions (for problems not caused by poor validation conduct).

5.4.1.2.3 Analyze Product Validation Results

Once the validation activities have been completed, the results are collected and the data are analyzed to confirm that the end product provided will supply the customer’s needed capabilities within the intended environments of use, validation procedures were followed, and enabling products and supporting resources functioned correctly. The data are also analyzed for quality, integrity, correctness, consistency, and validity, and any unsuitable products or product attributes are identified and reported. It is important to compare the actual validation results to the expected results. If discrepancies are found, it needs to be determined if they are a result of the test configuration or analysis assumptions or whether they are a true characteristic or behavior of

- Discrepancy and corrective action reports are generated as needed.
- The validation report is completed.
Re-engineering

Based on the results of the Product Validation Process, it could become necessary to re-engineer a deficient end product. Care should be taken that correcting a deficiency or set of deficiencies does not generate a new issue with a part or performance that had previously operated satisfactorily. Regression testing, a formal process of rerunning previously used acceptance tests (primarily used for software), is one method to ensure a change does not affect function or performance that was previously accepted.

Validation Deficiencies

Validation outcomes can be unsatisfactory for several reasons. One reason is poor conduct of the validation (e.g., enabling products and supporting resources missing or not functioning correctly, untrained operators, procedures not followed, equipment not calibrated, or improper validation environmental conditions) and failure to control other variables not involved in validating a set of stakeholder expectations. A second reason could be a shortfall in the verification process of the end product. This could create the need for:
- Re-engineering end products lower in the system
structure that make up the end product that was found to be deficient (i.e., that failed to satisfy validation requirements); and/or
- Re-performing any needed verification and validation processes.
Other reasons for validation deficiencies (particularly when M&S are involved) may be incorrect and/or inappropriate initial or boundary conditions; poor formulation of the modeled equations or behaviors; the impact of approximations within the modeled equations or behaviors; failure to provide the required geometric and physics fidelities needed for credible simulations for the intended purpose; and/or poor spatial, temporal, and perhaps, statistical resolution of physical phenomena used in M&S.

NOTE: Care should be exercised to ensure that the corrective actions identified to remove validation deficiencies do not conflict with the baselined stakeholder expectations without first coordinating such changes with the appropriate stakeholders.

Of course, the ultimate reason for performing validation is to determine if the design itself is the right design for meeting stakeholder expectations. After any and all validation test deficiencies are ruled out, the true value of validation is to identify design changes needed to ensure the program/product’s mission. Validation should be performed as early and as iteratively as possible in the SE process since the earlier re-engineering needs are discovered, the less expensive they are to resolve. Pass Verification but Fail Validation?

Sometimes systems successfully complete verification but then are unsuccessful in some critical phase of the validation process, delaying development and causing extensive rework and possible compromises with the stakeholder. Developing a solid ConOps in early phases of the project (and refining it through the requirements development and design phases) is critical to preventing unsuccessful validation. Similarly, developing clear expectations for user community involvement in the HSI Plan is critical to successful validation. Frequent and iterative communications with stakeholders helps to identify operational scenarios and key needs that should be understood when designing and implementing the end product. Should the product fail validation, redesign may be a necessary reality. Review of the understood requirements set, the existing design, operational scenarios, user population numbers and skills, training, and support material may be necessary, as well as negotiations and compromises with the customer, other stakeholders, and/or end users to determine what, if anything, can be done to correct or resolve the situation. This can add time and cost to the overall project or, in some cases, cause the project to fail or be canceled. However, recall from FIGURE 2.5-1 that the earlier design issues are discovered, the less costly the corrective action.

5.4.1.2.4  Prepare Report and Capture Product

Validation Work Products Validation work products (inputs to the Technical Data Management Process) take many forms and involve many sources of information. The capture and recording of validation-related data is a very important, but often underemphasized, step in the Product Validation Process.

Validation results, deficiencies identified, and corrective actions taken should be captured, as should all relevant results from the application of the Product Validation Process (related decisions, rationale for decisions made, assumptions, and lessons learned).

Version or standard for tools and equipment used, together with applicable calibration data; »» Outcome of each validation including pass or fail declarations; and »» Discrepancy between expected and actual results. »»

NOTE: For systems where only a single deliverable item is developed, the Product Validation Process normally completes acceptance testing of the system. However, for systems with several production units, it is important to understand that continuing verification and validation is not an

Outcomes of capturing validation work products include the following:

appropriate approach to use for the items following the first deliverable. Instead, acceptance testing is the preferred means to ensure that subsequent

- Work products and related information generated
while doing Product Validation Process activities and tasks are recorded; i.e., method of validation conducted, the form of the end product used for validation, validation procedures used, validation environments, outcomes, decisions, assumptions, corrective actions, lessons learned, etc. (often captured in a matrix or other tool—see Appendix E).
- Deficiencies (e.g., variations and anomalies and
out-of-compliance conditions) are identified and documented, including the actions taken to resolve.
- Proof is provided that the end product is in conformance with the stakeholder expectation set
used in the validation.
- Validation report including:
»» Recorded validation results/data; »» Version of the set of stakeholder expectations used; »» Version and form of the end product validated;

deliverables meet stakeholder expectations.

##### 5.4.1.3 Outputs

Key outputs of validation are:
- Validated end product: This is the end product
that has successfully passed validation and is ready to be transitioned to the next product layer or to the customer.
- Product validation results: These are the raw
results of performing the validations.
- Product validation report: This report provides
the evidence of product conformance with the stakeholder expectations that were identified as being validated for the product at this layer. It includes any nonconformance, anomalies, or other corrective actions that were taken.
- Work products: These include procedures,
required personnel training, certifications,
