# 5.3 Product Verification

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 88–98. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §5.3`.

Product Verification The Product Verification Process is the first of the verification and validation processes conducted on an end product. As used in the context of the systems engineering common technical processes, a product is one provided by either the Product Implementation Process or the Product Integration Process in a form suitable for meeting applicable life cycle phase success criteria. Realization is the act of implementing, integrating, verifying, validating, and transitioning the end product for use at the next level up of the system structure or to the customer. At this point, the end product can be referred to as a “realized product” or “realized end product.” Product verification proves that an end product (whether built, coded, bought, or reused) for any element within the system structure conforms to its requirements or specifications. Such specifications and other design description documentation establish the configuration baseline of that product, which may have to be modified at a later time. Without a verified baseline and appropriate configuration controls, such later modifications could be costly or cause major performance problems. From a process perspective, product verification and validation may be similar in nature, but the objectives are fundamentally different. A customer is interested in whether the end product provided will do what the customer intended within the environment of use. Examination of this condition is validation. Simply put, the Product Verification Process answers the critical question, “Was the end product realized right?” The Product Validation Process addresses the equally critical question, “Was the right end product realized?” When cost effective and warranted by analysis, the expense of validation testing alone can be mitigated by combining tests to perform verification and validation simultaneously.

DIFFERENCES BETWEEN VERIFICATION AND VALIDATION TESTING Testing is a detailed evaluation method of both verification and validation Verification Testing: Verification testing relates back to the approved requirements set (such as an SRD) and can be performed at different stages in the product life cycle. Verification tests are the official “for the record” testing performed on a system or element to show that it meets its allocated requirements or specifications including physical and functional interfaces. Verification tests use instrumentation and measurements and are generally accomplished by engineers, technicians, or operator-maintainer test personnel in a controlled environment to facilitate failure analysis. Validation Testing: Validation relates back to the ConOps document. Validation testing is conducted under realistic conditions (or simulated conditions) on any end product to determine the effectiveness and suitability of the product for use in mission operations by typical users and to evaluate the results of such tests. It ensures that the system is operating as expected when placed in a realistic environment.

The outcome of the Product Verification Process is confirmation that the end product, whether achieved by implementation or integration, conforms to its specified requirements, i.e., verification of the end product. This subsection discusses the process activities, inputs, outcomes, and potential product deficiencies.

#### 5.3.1 Process Description

FIGURE 5.3-1, taken from NPR 7123.1, provides a typ-

ical flow diagram for the Product Verification Process and identifies typical inputs, outputs, and activities to consider in addressing product verification.

it was assembled correctly. Any supporting documentation should be supplied with the product.
- Verification plan: This plan will have been developed under the Technical Planning Process and
baselined before entering this verification.
- Specified requirements baseline: These are the
requirements that have been identified to be verified for this product. Acceptance criteria should have been identified for each requirement to be verified.

Key inputs to the process are:

- Enabling products: Any other products needed
to perform the Product Verification Process. This may include test fixtures and support equipment.

- The product to be verified: This product
will have been transitioned from either the Product Implementation Process or the Product Integration Process. The product will likely have been through at least a functional test to ensure

Additional work products such as the ConOps, mission needs and goals, interface control drawings, testing standards and policies, and Agency standards and policies may also be needed to put verification activities into context.

##### 5.3.1.1 Inputs

DIFFERENCES BETWEEN VERIFICATION, QUALIFICATION, ACCEPTANCE AND CERTIFICATION Verification: Verification is a formal process, using the method of test, analysis, inspection or demonstration, to confirm that a system and its associated hardware and software components satisfy all specified requirements. The Verification program is performed once regardless of how many flight units may be generated (as long as the design doesn’t change). Qualification: Qualification activities are performed to ensure that the flight unit design will meet functional and performance requirements in anticipated environmental conditions. A subset of the verification program is performed at the extremes of the environmental envelope and will ensure the design will operate properly with the expected margins. Qualification is performed once regardless of how many flight units may be generated (as long as the design doesn’t change). Acceptance: smaller subset of the verification program is selected as criteria for the acceptance program. The selected Acceptance activities are performed on each of the flight units as they are manufactured and readied for flight/use. An Acceptance Data Package is prepared for each of the flight units and shipped with the unit. The acceptance test/analysis criteria are selected to show that the manufacturing/workmanship of the unit conforms to the design that was previously verified/qualified. Acceptance testing is performed for each flight unit produced. Certification: Certification is the audit process by which the body of evidence that results from the verification activities and other activities are provided to the appropriate certifying authority to indicate the design is certified for flight/use. The Certification activity is performed once regardless of how many flight units may be generated.

##### 5.3.1.2 Process Activities

There are five major activities in the Product Verification Process: (1) prepare to conduct product verification; (2) perform verification; (3) analyze verification results; (4) preparing a product verification report; and (5) capture work products generated during the verification activities. Product Verification is often performed by the developer that produced the end product with participation of the end user and customer. Quality Assurance

(QA) personnel are also critical in the verification planning and execution activities. A verification approach should be adapted (tailored) to the project it supports. The project manager and systems engineer should work with the verification lead engineer to develop a verification approach and plan the activities. Many factors need to be considered in developing this approach and the subsequent verification program. These factors include:

From Product Implementation or Product Integration Process End Product to Be Verified

To Product Validation Process

Prepare to conduct product verification

Verified End Product

Perform the product verification

To Technical Assessment Process

From Configuration Management Process Specified Requirements Baseline

Analyze the outcomes of the product verification Product Verification Plan From existing resources or Product Transition Process Product Verification Enabling Products

Prepare a product verification report

Capture work products from product verification activities

Product Verification Results To Technical Data Management Process Product Verification Report

Product Verification Work Products

FIGURE 5.3-1 Product Verification Process

- Project type, especially for flight projects.
Verification activities and timing depend on the following: The type of flight article involved (e.g., an experiment, payload, or launch vehicle). »» For missions required to follow NPR 7120.5, NASA Space Flight Program and Project Management Requirements, NASA payload classification (NPR 8705.4, Risk Classification for NASA Payloads) guidelines are intended to serve as a starting point for establishing the formality of verification approaches that can be adapted to the needs of a specific project based on the “A–D” payload classification. Further flexibility is imparted to projects following NPR 7120.8, NASA Research and Technology Program and Project Management Requirements. »»

Project cost and schedule implications. Verification activities can be significant drivers of a project’s cost and schedule, and these implications should be considered early in the development of the verification plan. Trade studies should be performed early in the life cycle to support decisions about verification methods and types and the selection of facility capabilities and locations. For example, a trade study might be made to decide between performing a test at a centralized facility or at several decentralized locations. »» Risk management should be considered in the development of the verification approach. Qualitative risk assessments and quantitative risk analyses (e.g., a Failure Mode and Effects Analysis (FMEA)) often identify new concerns that can be mitigated by additional verifications, thus increasing the extent of »»

verification activities. Other risk assessments contribute to trade studies that determine the preferred methods of verification to be used and when those methods should be performed. For example, a trade might be made between performing a model test versus determining model characteristics by a less costly but less revealing analysis. The project manager/systems engineer should determine what risks are acceptable in terms of the project’s cost and schedule.
- Availability of verification facilities/sites and
transportation assets to move an article from one location to another (when needed). This requires coordination with the Integrated Logistics Support (ILS) engineer.
- Availability of appropriately trained users for
interaction with systems having human interfaces.

of the project life cycle and matures as the design is matured. The verification environment is considered as part of procedure development. Operational scenarios are assessed to explore all possible verification activities to be performed. The final element is preparation of the verification environment; e.g., facilities, equipment, tools, measuring devices, and climatic conditions. When operator or other user interaction is involved, it is important to ensure that humans are properly represented in the verification activities. This includes physical size, skills, knowledge, training, clothing, special gear, and tools. Note: Testing that includes representatives of the human in the system is often referred to as “human-in-the-loop” testing.

NOTE: Depending on the nature of the verification effort and the life cycle phase the program is in, some type of review to assess readiness for verification (as well as validation later) is typically held. In

- Acquisition strategy; i.e., in-house development or
system contract. A NASA field Center can often shape a contractor’s verification process through the project’s SOW.

earlier phases of the life cycle, these Test Readiness Reviews (TRRs) may be held informally; in later phases of the life cycle, this review may become a more formal event. TRRs and other technical reviews are an activity of the Technical Assessment Process.

- Degree of design heritage and hardware/software reuse.

On most projects, a number of TRRs with tailored entrance/success criteria are held to assess the

5.3.1.2.1 Product Verification Preparation

readiness and availability of test ranges, test facili-

In preparation for verification, the verification plan and the specified requirements are collected, reviewed, and confirmed. The product to be verified is obtained (output from the Product Implementation Process or the Product Integration Process) along with any enabling products, such as those representing external interfacing products and support resources (including personnel) that are necessary for verification. Procedures capturing detailed step-bystep activities and based on the verification type and methods are finalized and approved. Development of procedures typically begins during the design phase

ties, trained testers, instrumentation, integration labs,

support equipment, and other enabling products. Peer reviews are additional reviews that may be conducted formally or informally to ensure readiness for verification (as well as the results of the verification process). Guidelines for conducting a peer review are discussed in Section 6.7.2.4.5.

TABLE 5.3-1 provides an example of the type of infor-

mation that may be included in a verification procedure and a verification report.

METHODS OF VERIFICATION Analysis: The use of mathematical modeling and analytical techniques to predict the suitability of a design to stakeholder expectations based on calculated data or data derived from lower system structure end product verifications. Analysis is generally used when a prototype; engineering model; or fabricated, assembled, and integrated product is not available. Analysis includes the use of modeling and simulation as analytical tools. A model is a mathematical representation of reality. A simulation is the manipulation of a model. Analysis can include verification by similarity of a heritage product. Demonstration: Showing that the use of an end product achieves the individual specified requirement. It is generally a basic confirmation of performance capability, differentiated from testing by the lack of detailed data gathering. Demonstrations can involve the use of physical models or mock-ups; for example, a requirement that all controls shall be reachable by the pilot could be verified by having a pilot perform flight-related tasks in a cockpit mock-up or simulator. A demonstration could also be the actual operation of the end product by highly qualified personnel, such as test pilots, who perform a one-time event that demonstrates a capability to operate at extreme limits of system performance, an operation not normally expected from a representative operational pilot. Inspection: The visual examination of a realized end product. Inspection is generally used to verify physical design features or specific manufacturer identification. For example, if there is a requirement that the safety arming pin has a red flag with the words “Remove Before Flight” stenciled on the flag in black letters, a visual inspection of the arming pin flag can be used to determine if this requirement was met. Inspection can include inspection of drawings, documents, or other records. Test: The use of an end product to obtain detailed data needed to verify performance or provide sufficient information to verify performance through further analysis. Testing can be conducted on final end products, breadboards, brassboards, or prototypes. Testing produces data at discrete points for each specified requirement under controlled conditions and is the most resource-intensive verification technique. As the saying goes, “Test as you fly, and fly as you test.” (See Section 5.3.2.5 in the NASA Expanded Guidance for Systems Engineering at https://nen.nasa.gov/web/se/doc-repository)

Outcomes of verification preparation include the following:
- The verification plan, approved procedures, and
an appropriate baseline set of specified requirements and supporting configuration documentation is available and on hand;

- Articles/models to be verified and verification-enabling products are on hand, assembled, and
integrated with the verification environment according to verification plans and schedules;
- The resources (funding, facilities, and people
including appropriately skilled operators) needed

TABLE 5.3-1 Example information in Verification Procedures and Reports

Verification Procedure

Verification Report

Nomenclature and identification of the test article or material;

Verification objectives and the degree to which they were met;

Identification of test configuration and any differences from flight operational configuration;

Description of verification activity including deviations from nominal results (discrepancies);

Identification of objectives and criteria established for the verification by the applicable requirements specification;

Test configuration and differences from the flight operational configuration;

Characteristics and design criteria to be inspected, demonstrated, or tested, including values with tolerances for acceptance or rejection;

Specific result of each activity and each procedure, including the location or link to verification data/artifacts;

Description, in sequence, of steps, operations, and observations to be taken;

Specific result of each analysis including those associated with test-data analysis;

Identification of computer software required;

Test performance data tables, graphs, illustrations, and pictures;

Identification of measuring, test, and recording equipment to be used, specifying range, accuracy, and type;

Summary of nonconformance/discrepancy reports, including dispositions with approved corrective actions and planned retest activity if available;

Provision for recording equipment calibration or software version data;

Conclusions and recommendations relative to the success of verification activity;

Credentials showing that required computer test programs/support equipment and software have been verified prior to use with flight operational hardware;

Status of Government-Supplied Equipment (GSE) and other enabling support equipment as affected by test;

Any special instructions for operating data recording equipment or other automated test equipment as applicable;

Copy of the as-run procedure (may include redlines); and

Layouts, schematics, or diagrams showing identification, location, and interconnection of test equipment, test articles, and measuring points and any other associated design or configuration work products;

Authentication of test results and authorization of acceptability.

Identification of hazardous situations or operations; Precautions and safety instructions to ensure safety of personnel and prevent degradation of test articles and measuring equipment; Environmental and/or other conditions to be maintained with tolerances; Constraints on inspection or testing; Provision or instructions for the recording of verification results and other artifacts; Special instructions for instances of nonconformance and anomalous occurrences or results; and Specifications for facility, equipment maintenance, housekeeping, quality inspection, and safety and handling requirements before, during, and after the total verification activity.

to conduct the verification are available according to the verification plans and schedules; and
- The verification environment is evaluated for adequacy, completeness, readiness, and integration.

are some of the most important tests for the systems engineers to participate in or to lead. They review the overall compatibility of the various systems and demonstrate compliance with system-level requirements and whether the system behaves as expected by the stakeholders.

5.3.1.2.2 Perform Product Verification

The actual act of verifying the end product is performed as spelled out in the plans and procedures, and conformance is established with each specified product requirement. The verification lead should ensure that the procedures were followed and performed as planned, the verification-enabling products and instrumentation were calibrated correctly, and the data were collected and recorded for required verification measures. A verification program may include verifications at several layers in the product hierarchy. Some verifications need to be performed at the lowest component level if the ability to verify a requirement at a higher assembly is not possible. Likewise, there may be verifications at assemblies, sub-systems and system levels. If practicable, a final set of testing with as much of the end-to-end configuration as possible is important. The purpose of end-to-end testing is to demonstrate interface compatibility and desired total functionality among different elements of a mission system, between systems (the system of interest and external enabling systems), and within a system as a whole. It can involve real or representative input and operational scenarios. End-to-end tests performed on the integrated ground and flight assets include all elements of the flight article (payload or vehicle), its control, stimulation, communications, and data processing to demonstrate that the entire integrated mission system is operating in a manner to fulfill all mission requirements and objectives. End-to-end tests may be performed as part of investigative engineering tests, verification testing, or validation testing. These

End-to-end testing includes executing complete threads or operational scenarios across multiple configuration items, ensuring that all mission requirements are verified and validated. Operational scenarios are used extensively to ensure that the mission system (or collections of systems) will successfully execute mission requirements. Operational scenarios are a step-by-step description of how the system should operate and interact with its users and its external interfaces (e.g., other systems). Scenarios should be described in a manner that allows engineers to walk through them and gain an understanding of how all the various parts of the system should function and interact as well as verify that the system will satisfy the user’s goals and expectations (MOEs). Operational scenarios should be described for all operational modes, mission phases (e.g., installation, startup, typical examples of normal and contingency operations, shutdown, and maintenance), and critical sequences of activities for all classes of users identified. Each scenario should include events, actions, stimuli, information, and interactions as appropriate to provide a comprehensive understanding of the operational aspects of the system. FIGURE 5.3-2 presents an example of an end-to-end

data flow for a scientific satellite mission. Each arrow in the diagram represents one or more data or control flows between two hardware, software, subsystem, or system configuration items. End-to-end testing verifies that the data flows throughout the multisystem environment are correct, that the system provides the required functionality, and that the outputs at the eventual end points correspond to expected results.

EXTERNAL SYSTEMS

GROUND SYSTEM

FLIGHT SYSTEM

Uplink Process

Mission Planning

Planning

Command Generation

X-rays Instrument Set A Transmission

Software Loads

Community

Archival

Analysis

EXTERNAL STIMULI

Visible

Spacecraft Execution

Data Capture

Ultraviolet

Infrared Instrument Set B Microwave

Downlink Process

FIGURE 5.3-2 Example of End-to-End Data Flow for a Scientific Satellite Mission

Since the test environment is as close an approximation as possible to the operational environment, system performance requirements testing is also included. This figure is not intended to show the full extent of end-to-end testing. Each system shown would need to be broken down into a further level of granularity for completeness. End-to-end testing is an integral part of the verification and validation of the total (mission) system. It is a set of activities that can be employed during selected hardware, software, and system phases throughout the life cycle using developmental forms and external simulators. However, final end-to-end testing should be done on the flight articles in the flight configuration if possible and prior to deployment and launch. In comparison with configuration item testing, end-to-end testing addresses each configuration item (end product) only down to the level designated by the verification plan (generally, the segment r element) and focuses on external interfaces, which can be either hardware, software, or

human-based. Internal interfaces (e.g., software subroutine calls, analog-to-digital conversion) of a designated configuration item are not within the scope of end-to-end testing. When a “discrepancy” is observed (i.e., any variance, lack of agreement, or contradiction with the required or expected outcome, configuration, or result), verification activities should stop and a discrepancy report should be generated. The activities and events leading up to the discrepancy should be analyzed to determine if a nonconforming product exists or there is an issue with the verification procedure or conduct. The Decision Analysis Process should be used to make decisions with respect to needed changes in the verification plans, environment, and/or procedures. Outcomes of performing product verification include the following:
- A verified product is established with supporting
confirmation that the product (in the appropriate

form for the life cycle phase) complies with its specified requirements, and if it does not, a nonconformance report delineating the variance is available.

NOTE: Nonconformance and discrepancy reports may be directly linked with the Technical Risk Management Process. Depending on the nature of the nonconformance, approval through such bodies as a Material Review Board or

- A determination is made as to whether the appropriate results were collected and evaluated to show
completion of verification objectives throughout their performance envelope.

Configuration Control Board (which typically

- A determination is made that the verification
product was appropriately integrated with the enabling products and verification environment.

System design and product realization process activities may be required to resolve product nonconformance. If the mitigation of the nonconformance results in a change to the product, the verification may need to be planned and performed again.

5.3.1.2.3  Analyze Product Verification Results and

Report As the verification activities are completed, the results are collected and analyzed. The data are analyzed for quality, integrity, correctness, consistency, and validity. Any verification discrepancies (anomalies, variations, and out-of-compliance conditions) are identified and reviewed to determine if there is a nonconforming product not resulting from poor verification conduct, procedure, or conditions. If possible, this analysis is performed while the test/analysis configuration is still intact. This allows a quick turnaround in case the data indicates that a correction to the test or analysis run needs to be performed again.

Discrepancies and nonconforming products should be recorded and reported for follow-up action and closure. Verification results should be recorded in a requirements compliance or verification matrix or other method developed during the Technical Requirements Definition Process to trace compliance for each product requirement. Waivers needed as a result of verification to request relief from or modify a requirement are identified.

includes risk management participation) may be required.

Outcomes of analyzing the verification results include the following:
- Product nonconformance (not compliant with
product requirement) is identified.
- Appropriate replanning, redefinition of requirements, redesign, implementation/integration, modification, and reverification have been accomplished
for resolution of the nonconforming product.
- Appropriate facility modifications, procedure
corrections, enabling product modification, and reverification have been performed for non-product-related discrepancies.
- Waivers for nonconforming products are accepted.
- Discrepancy and nonconformance reports including
corrective actions have been generated as needed.
- The verification report is completed.

Re-engineering

Based on analysis of verification results, it could be necessary to re-realize the end product used for verification or to re-engineer the end products assembled and integrated into the product being verified, based on where and what type of nonconformance was found. Re-engineering could require the reapplication of the system design processes (Stakeholder Expectations Definition Process, Technical Requirements Definition Process, Logical Decomposition Process, and Design Solution Definition Process).

- Proof that the realized end product did or did not
satisfy the specified requirements is documented.
- The verification report is developed, including:
»» »» »» »» »» »»

recorded test/verification results/data; version of the set of specified requirements used; version of the product verified; version or standard for tools, data, and equipment used; results of each verification including pass or fail declarations; and discrepancies.

5.3.1.2.4 Capture Product Verification Work Products

Verification work products (inputs to the Technical Data Management Process) take many forms and involve many sources of information. The capture and recording of verification results and related data is a very important, but often underemphasized, step in the Product Verification Process.

##### 5.3.1.3 Outputs

Verification results, peer review reports, anomalies, and any corrective action(s) taken should be captured, as should all relevant results from the application of the Product Verification Process (related decisions, rationale for the decisions made, assumptions, and lessons learned).

- Product verification results: Results from executed
procedures are passed to technical assessment.

Outcomes of capturing verification work products include the following:
- Verification of work products is recorded, e.g.,
method of verification, procedures, environments, outcomes, decisions, assumptions, corrective actions, and lessons learned.
- Variations, anomalies, and out-of-compliance
conditions have been identified and documented, including the actions taken to resolve them.

Key outputs from the process are:
- Verified product ready for validation: After the
product is verified, it will next pass through the Product Validation Process.

- Product verification report(s): A report shows the
results of the verification activities. It includes the requirement that was to be verified and its bidirectional traceability, the verification method used, and reference to any special equipment, conditions, or procedures used. It also includes the results of the verification, any anomalies, variations or out-of-compliance results noted and associated corrective actions taken.
- Product verification work products: These
include discrepancy and nonconformance reports with identified correction actions; updates to requirements compliance documentation; changes needed to the procedures, equipment or
