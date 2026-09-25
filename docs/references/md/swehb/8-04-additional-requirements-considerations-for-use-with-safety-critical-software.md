# 8.04 - Additional Requirements Considerations for Use with Safety-Critical Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695705. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software

8.04 - Additional Requirements Considerations for Use with Safety-Critical Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695705/8.04+-+Additional+Requirements+Considerations+for+Use+with+Safety-Critical+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695705)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695705&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Introduction

Below are additional detailed technical software safety requirements to be considered when you have safety-critical software on a program/project/facility. These requirements were derived from both the Constellation and International Space Station Software Safety Requirements, NPR 7150.2 (requirement [SWE-134](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) in Revision C) and Software Assurance and Software Safety Standard, NASA-STD-8739.8. More information on the International Space Station Software Safety Requirements is in NASA-SSP-50038, Computer-Based System Safety Requirements [014](#_tabs-<p>2</p>).

## 1.1 General Software Safety Requirements- Approach for handling Software Safety-Critical components contained in NPR 7150.2 and in NASA-STD-8739.8.

**Step 1.** Implement the requirements in [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements)

**SWE-134 - Safety-Critical Software Design Requirements**

3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:

a. The software is initialized, at first start and restarts, to a known safe state.  
b. The software safely transitions between all predefined known states.  
c. Termination performed by software functions is performed to a known safe state.  
d. Operator overrides of software functions require at least two independent actions by an operator.  
e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard.  
f. The software detects inadvertent memory modification and recovers to a known safe state.  
g. The software performs integrity checks on inputs and outputs to/from the software system.  
h. The software performs prerequisite checks prior to the execution of safety-critical software commands.  
i. No single software event or action is allowed to initiate an identified hazard.  
j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event.  
k. The software provides error handling.  
l. The software can place the system into a safe state.

**Step 2.** Assess and determine if security measures are in place to prevent viruses and other unwanted attacks that could contribute to a hazard

See the following requirements from NPR 7150.2, section 3.11:

**3.11 Software Cybersecurity**

* 3.11.1 Software defects are a central and critical aspect of computer security vulnerabilities. Software defects with cybersecurity ramifications include implementation bugs such as buffer overflows and design flaws such as inconsistent error handling.
* [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks)  

  **SWE-156 - Evaluate Systems for Security Risks**

  3.11.2 The project manager shall perform a software cybersecurity assessment on the software components per the Agency security policies and the project requirements, including risks posed by the use of COTS, GOTS, MOTS, OSS, or reused software components.

* [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks)  

  **SWE-154 - Identify Security Risks**

  3.11.3 The project manager shall identify cybersecurity risks, along with their mitigations, in flight and ground software systems and plan the mitigations for these systems.
* [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access)  

  **SWE-157 - Protect Against Unauthorized Access**

  3.11.4 The project manager shall implement protections for software systems with communications capabilities against unauthorized access per the requirements contained in the NASA-STD-1006, Space System Protection Standard.
* [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations)  

  **SWE-159 - Verify and Validate Risk Mitigations**

  3.11.5 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis.
* [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)  

  **SWE-207 - Secure Coding Practices**

  3.11.6 The project manager shall identify, record, and implement secure coding practices.
* [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification)  

  **SWE-185 - Secure Coding Standards Verification**

  3.11.7 The project manager shall verify that the software code meets the project’s secure coding standard by using the results from static analysis tool(s).
* [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions)  

  **SWE-210 - Detection of Adversarial Actions**

  3.11.8 The project manager shall identify software requirements for the collection, reporting, and storage of data relating to the detection of adversarial actions.

**Step 3.** Implement the Software Safety-Critical Requirements and activities is contained in NASA-STD-8739.8:

1. Confirm that the identified safety-critical software components have implemented the safety-critical software assurance requirements listed in this standard.
2. Analyze the software design to ensure that partitioning or isolation methods used in the design to logically isolate the safety-critical design elements from those that are non-safety-critical.
3. Analyze the design and work with the project to implement NPR 7150.2 requirement items "a" through "l."
4. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical software at each code inspection, test review, safety review, and project review milestone.
5. Confirm 100% code test coverage has been achieved or addressed for all identified software safety-critical components or provide a risk assessment explaining why the test coverage is not possible for the safety-critical code component.
6. Assess each safety-critical software component to determine the software component’s cyclomatic complexity value.
7. Confirm that all identified software safety-critical components have a cyclomatic complexity value of 20 or lower. If not, provide a risk assessment showing why the cyclomatic complexity value needs to be higher than ten and why the software component cannot be structured to be lower than 20.
8. Develop a Software Assurance Plan. The plan should address the content defined in NASA-HDBK-2203 for a software assurance plan, including software safety if required.
9. The defined software assurance, software safety, and IV&V processes for the activities on the project per the requirements in the Software Assurance and Software Safety Standard.
10. Develop a tailoring matrix of the software assurance and software safety requirements as needed and document the software assurance, software safety, and IV&V approach in the SA plan and schedule.
11. Develop a software assurance cost estimation for the project, including cost estimation associated with handling safety-critical software.
12. Confirm that the hazard reports contain (or safety data packages) all known software contributions or events where software; either by its action, inaction or incorrect action, lead to a hazard.
13. Analyze the updated hazard reports and design at review points to determine if any newly identified software components are safety-critical.
14. Develop and maintain a list of all software safety-critical components that have been identified by the system hazard analysis.
15. Develop and maintain a software safety analysis throughout the software development lifecycle.
16. Analyze that the software related safety constraints, controls, mitigations, and assumptions between the hardware, operator, and software are in the software requirements documentation. The analysis must ensure the software does not violate the independence of hazard inhibits and hardware redundancy.
17. Analyze the software architecture features to determine if any software architecture features impact safety and mission assurance.
18. Develop a list of software architecture features that impact safety and mission assurance.
19. Confirm that the software design implements all of the required safety-critical functions and requirements.
20. Confirm that the project successfully executes the required unit tests, particularly those testing safety-critical functions.
21. Perform additional rigor (e.g., test witnessing, results in review) if applicable based on software classification and safety-criticality.
22. Confirm the software regression testing includes retesting of all safety-critical code components.
23. Analyze proposed changes to software products for impacts, particularly to safety, and security.
24. Assess that the software safety-critical items are configuration managed, including hazard reports and safety analysis.
25. Assess the impact of non-conformances on the safety, quality, and reliability of the project software.

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality), [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis), [8.21 - Software Hazard Causes](/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes),

**Step 4.** Additional considerations to be accessed when you have safety-critical software components:

The provider should include the following general software safety requirements in the project software requirements:

1. The software recovers to a known safe state when an anomaly is detected.
2. The software properly handles missing and spurious data.
3. The software checks the quality of loaded configuration data (such as day of launch guidance parameters) used by the software.
4. The software provides at least one independent command for each operator initiated action used to shutdown a function leading to or reducing the control of a hazard.
5. The software provides independent safety-critical threads.
6. The software commands are required to be diverse from other commands so that a single bit flip could not transform a benign command into an inhibit.
7. The software provides a unique command message to remove or change an inhibit that controls a hazard.
8. The software provides the status of the inhibits controlling hazards to the operator.
9. The software rejects input and output data determined to be invalid by the integrity checks.
10. The software provides and checks a functionally independent parameter before issuance of any sequence that could remove an inhibit or perform a hazardous action.
11. The software uses separate control paths with different functionality for each inhibit to control a hazard.

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

### 2.1 Resources

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-014)

  [Computer-Based Control System Safety Requirements](https://swehb.nasa.gov/download/attachments/16450414/SSP%2050038-Rev%20C.docx?api=v2 "Click to open in new window")

  SSP 50038, Revision C, NASA International Space Station Program, 1995.

## 2.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-154 - Identify Security Risks](/spaces/SWEHBVD/pages/102695510/SWE-154+-+Identify+Security+Risks) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-159 - Verify and Validate Risk Mitigations](/spaces/SWEHBVD/pages/102695515/SWE-159+-+Verify+and+Validate+Risk+Mitigations) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices) * [SWE-210 - Detection of Adversarial Actions](/spaces/SWEHBVD/pages/102695330/SWE-210+-+Detection+of+Adversarial+Actions)        * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.21 - Software Hazard Causes](/spaces/SWEHBVD/pages/109969546/8.21+-+Software+Hazard+Causes) * [PAT-012 - Detection of Adversarial Actions - Retired](/spaces/SITE/pages/114328278/PAT-012+-+Detection+of+Adversarial+Actions+-+Retired) |

## 2.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 2.4 Associated Activities

This topic is associated with the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |
