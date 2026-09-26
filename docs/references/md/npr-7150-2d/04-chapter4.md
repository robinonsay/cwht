# NPR 7150.2D — Chapter4

> Source: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4
> Page title: NPR 7150.2D - Chapter4
> Machine conversion; tables may be flattened. SWE-NNN identifiers are authoritative.

# Chapter 4: Software Engineering Life Cycle Requirements

## 4.1 Software Requirements

4.1.1 The requirements phase is one of the most critical phases of software engineering. Studies show that the top problems in the software industry are due to poor requirements elicitation, inadequate requirements specification, and inadequate management of changes to requirements. Requirements provide the foundation for the entire life cycle, as well as for the software product. Requirements also provide a basis for planning, estimating, and monitoring. Requirements are based on customer, user, and other stakeholder needs and design and development constraints. The development of requirements includes elicitation, analysis, documentation, verification, and validation. Ongoing customer validation of the requirements to ensure the end products meet customer needs is an integral part of the life cycle process. Customer validation can be accomplished via rapid prototyping and customer-involved reviews of iterative and final software requirements.

4.1.2 The project manager shall establish, capture, record, approve, and maintain software requirements, including requirements for COTS, GOTS, MOTS, OSS, or reused software components, as part of the technical specification. [SWE-050]

Note: The software technical requirements definition process is used to transform the baselined stakeholder expectations into unique, quantitative, and measurable technical software requirements that can be used for defining a design solution for the software end products and related enabling products. This process also includes validation of the requirements to ensure that the requirements are well-formed (clear and unambiguous), complete (agrees with customer and stakeholder needs and expectations), consistent (conflict free), and individually verifiable and traceable to a higher level requirement. Recommended content for a software specification can be found in NASA-HDBK-2203.

4.1.3 The project manager shall perform software requirements analysis based on flowed-down and derived requirements from the top-level systems engineering requirements, safety and reliability analyses, and the hardware specifications and design. [SWE-051]

4.1.4 The project manager shall include software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software in the software requirements documentation. [SWE-184]

4.1.5 The project manager shall track and manage changes to the software requirements. [SWE-053]

4.1.6 The project manager shall identify, initiate corrective actions, and track until closure inconsistencies among requirements, project plans, and software products. [SWE-054]

4.1.7 The project manager shall perform requirements validation to ensure that the software will perform as intended in the customer environment. [SWE-055]

## 4.2 Software Architecture

4.2.1 Experience confirms that the quality and longevity of a software-reliant system is primarily determined by its architecture. The software architecture underpins a system’s software design and code; it represents the earliest design decisions, ones that are difficult and costly to change later. The transformation of the derived and allocated requirements into the software architecture results in the basis for all software development work.

4.2.2 A software architecture:

a. Formalizes precise subsystem decompositions.

b. Defines and formalizes the dependencies among software work products within the integrated system.

c. Serves as the basis for evaluating the impacts of proposed changes.

d. Maintains rules for use by subsequent software engineers that ensure a consistent software system as the work products evolve.

e. Provides a stable structure for use by future groups through the documentation of the architecture, its views and patterns, and its rules.

f. Follows guidelines created by the NASA Space Asset and the Enterprise Protection Program to protect mission architectures.

g. Documents the valid and invalid modes or states of operation within the software requirements.

4.2.3 The project manager shall transform the requirements for the software into a recorded software architecture. [SWE-057]

Note: A documented software architecture that describes: the software’s structure; identifies the software qualities (i.e., performance, modifiability, and security); identifies the known interfaces between the software components and the components external to the software (both software and hardware); identifies the interfaces between the software components and identifies the software components. Reference NASA’s Software Architecture Review Board (SARB) paper NTRS ID 20160005787, “Quality Attributes for Mission Flight Software: A Reference for Architects.”

4.2.4 The project manager shall perform a software architecture review on the following categories of projects: [SWE-143]

a. Category 1 Projects as defined in NPR 7120.5.

b. Category 2 Projects as defined in NPR 7120.5, that have Class A or Class B payload risk classification per NPR 8705.4.

## 4.3 Software Design

4.3.1 Software design is the process of defining the software architecture, components, modules, interfaces, and data for a software system to satisfy specified requirements. The software architecture is the fundamental organization of a system embodied in its components, their relationships to each other and the environment, and the principles guiding its design and evolution. The software architectural design is concerned with creating a strong overall structure for software entities that fulfill the allocated system and software-level requirements. Typical views captured in an architectural design include the decomposition of the software subsystem into design entities, computer software configuration items, definitions of external and internal interfaces, dependency relationships among entities and system resources, and finite state machines. The design should be further refined into lower-level entities that permit the implementation by coding in a programming language. Typical attributes that are documented for lower-level entities include the identifier, type, purpose, function, constraints, subordinates, dependencies, interface, resources, processing, and data. Rigorous specification languages, graphical representations, and related tools have been developed to support the evaluation of critical properties at the design level. Projects are encouraged to take advantage of these improved design techniques to prevent and eliminate errors as early in the life cycle as possible. Software, developed or purchased, has additional requirements to comply with from Section 508 of the Rehabilitation Act, as defined inNPR 2800.2.

4.3.2 The project manager shall develop, record, and maintain a software design based on the software architectural design that describes the lower-level units so that they can be coded, compiled, and tested. [SWE-058]

## 4.4 Software Implementation

4.4.1 Software implementation consists of implementing the requirements and design into code, data, and records. Software implementation also consists of following coding methods and standards. Unit testing is also usually a part of software implementation (unit testing can also be conducted during the testing phase).

4.4.2 The project manager shall implement the software design into software code. [SWE-060]

4.4.3 The project manager shall select, define, and adhere to software coding methods, standards, and criteria. [SWE-061]

4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity. [SWE-135]

Note: Although no maximum cyclomatic complexity score is required for non-safety critical software, all software projects should regularly collect and maintain complexity metrics and use them to manage risk, either when high-complexity code must be modified, or proactively to improve the overall quality and maintenance of the code base. For safety critical software, the analysis should take into account the requirements for cyclomatic complexity and code coverage as defined in 3.7.5 and 3.7.4 respectively.

4.4.5 The project manager shall unit test the software code. [SWE-062]

Note: For safety critical software, the unit testing should follow the requirement established in 3.7.4 of this document.

4.4.6 The project manager shall assure that the unit test results are repeatable. [SWE-186]

4.4.7 The project manager shall provide a software version description for each software release. [SWE-063]

4.4.8 The project manager shall validate and accredit the software tool(s) required to develop or maintain software. [SWE-136]

Note: All software development tools contain some number of software defects. Validation and accreditation of the critical software development and maintenance tools ensure that the tools being used during the software development life cycle do not generate or insert errors in the software executable components. Software tool accreditation is the certification that a software tool is acceptable for use for a specific purpose. Accreditation is conferred by the organization best positioned to make the judgment that the software tool in question is acceptable. The likelihood that work products will function properly is enhanced, and the risk of error is reduced if the tools used in the development and maintenance processes have been validated and accredited themselves.

## 4.5 Software Testing

4.5.1 The purpose of testing is to verify the software functionality and remove defects. Testing verifies the code against the requirements and the design to ensure that the requirements are implemented. Testing also identifies problems and defects that are corrected and tracked to closure before product delivery. Testing also validates that the software operates appropriately in the intended environment. Please note for Class A software there are additional software test requirements and software integration requirements as defined in NPR 8705.2.

4.5.2 The project manager shall establish and maintain: [SWE-065]

a. Software test plan(s).

b. Software test procedure(s).

c. Software test(s), including any code specifically written to perform test procedures.

d. Software test report(s).

4.5.3 The project manager shall test the software against its requirements. [SWE-066]

Note: A best practice for Class A, B, and C software projects is to have formal software testing planned, conducted, witnessed, and approved by an independent organization outside of the development team.

4.5.4 The project manager shall place software items under configuration management prior to testing. [SWE-187]

Note: This includes the software components being tested and the software components being used to test the software, including components such as support software, models, simulations, ground support software, COTS, GOTS, MOTS, OSS, or reused software components.

4.5.5 The project manager shall evaluate test results and record the evaluation. [SWE-068]

4.5.6 The project manager shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment. [SWE-070]

Note: Information regarding specific V&V techniques and the analysis of models and simulations can be found in NASA-STD-7009, Standard for Models and Simulations, NASA-HDBK-7009, Handbook for Models and Simulations, or discipline-specific recommended practice guides.

4.5.7 The project manager shall update the software test and verification plan(s) and procedure(s) to be consistent with software requirements. [SWE-071]

4.5.8 The project manager shall validate the software system on the targeted platform or high-fidelity simulation. [SWE-073]

Note: Typically, a high-fidelity simulation has the exact processor, processor performance, timing, memory size, and interfaces as the target system.

4.5.9 The project manager shall ensure that the code coverage measurements for the software are selected, implemented, tracked, recorded, and reported. [SWE-189]

Note: This requirement can be met by running unit, integration, and validation tests; measuring the code coverage; and achieving the code coverage by additional (requirement based) tests, inspection, or analysis.

If the project does not get 100 percent structural coverage, it means one of four things and each requires action on the project manager’s part:

• Requirement missing - the code that hasn’t been covered is performing an essential activity, but no requirement indicates that this should be done;

• Test missing - the code that hasn’t been covered relates to an existing requirement, but no test was implemented for it;

• Extraneous/dead code – the code that hasn’t been covered is not traceable to any requirement and isn’t needed by the software;

• Deactivated code - the code that hasn’t been covered isn’t traceable to any requirements for the current system, but is intended to be executed in specific configurations.

The code coverage data and any rationale for uncovered code should be presented and reviewed at major project milestones.

4.5.10 The project manager shall verify code coverage is measured by analysis of the results of the execution of tests. [SWE-190]

Note: If it can be justified that the required percentage cannot be achieved by test execution, the analysis, inspection, or review of design can be applied to the non-covered code. The goal of the complementary analysis is to assess that the non-covered code behavior is as expected.

4.5.11 The project manager shall plan and conduct software regression testing to demonstrate that defects have not been introduced into previously integrated or tested software and have not produced a security vulnerability. [SWE-191]

4.5.12 The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique. [SWE-192]

4.5.13 The project manager shall develop acceptance tests for loaded or uplinked data, rules, and code that affects software and software system behavior. [SWE-193]

Note: These acceptance tests should validate and verify the data, rules, and code for nominal and off-nominal scenarios.

4.5.14 The project manager shall test embedded COTS, GOTS, MOTS, OSS, or reused software components to the same level required to accept a custom developed software component for its intended use. [SWE-211]

## 4.6 Software Operations, Maintenance, and Retirement

4.6.1 Planning for operations, maintenance, and retirement are typically considered throughout the software life cycle. Operational concepts and scenarios are derived from customer requirements and validated in the operational or simulated environment. Software maintenance activities sustain the software product after the product is delivered to the customer until retirement.

4.6.2 The project manager shall plan and implement software operations, maintenance, and retirement activities. [SWE-075]

4.6.3 The project manager shall complete and deliver the software product to the customer with appropriate records, including as-built records, to support the operations and maintenance phase of the software’s life cycle. [SWE-077]

4.6.4 The project manager shall complete, prior to delivery, verification that all software requirements identified for this delivery have been met or dispositioned, that all approved changes have been implemented, and that all defects designated for resolution prior to delivery have been resolved. [SWE-194]

4.6.5 The project manager shall maintain the software using standards and processes per the applicable software classification throughout the maintenance phase. [SWE-195]

4.6.6 The project manager shall identify the records and software tools to be archived, the location of the archive, and procedures for access to the products for software retirement or disposal. [SWE-196]

  

|  |
| --- |
| | [TOC](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=main) | [Preface](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Preface) | [Chapter1](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter1) | [Chapter2](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter2) | [Chapter3](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter3) | [Chapter4](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter4) | [Chapter5](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter5) | [Chapter6](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=Chapter6) | [AppendixA](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixA) | [AppendixB](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixB) | [AppendixC](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixC) | [AppendixD](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixD) | [AppendixE](displayDir.cfm?Internal_ID=N_PR_7150_002D_&page_name=AppendixE) | [ALL](displayAll.cfm?Internal_ID=N_PR_7150_002D_&page_name=ALL) | |
|  |
| | [NODIS Library](main_lib.html) | [Program Formulation(7000s)](lib_docs.cfm?range=7) | [Search](adv_search.cfm) | |
