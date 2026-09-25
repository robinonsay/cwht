# FAQ - Engineering Assurance and Safety

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695765. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695765/FAQ+-+Engineering+Assurance+and+Safety

Frequently Asked Questions and Answers about Engineering, Software Assurance, and Safety topics. You can submit any inputs and suggestions via "Feedback" in the [NASA Technical Standards System (NTSS)](http://standards.nasa.gov/) under Site Menu on left side of the page

Added Software Lessons Learned from Psyche Project Report

**[New in SWEHB](/spaces/SWEHBVD/pages/122388792/New+in+SWEHB)**

FAQ - Engineering, Assurance, and Safety

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695765/FAQ+-+Engineering+Assurance+and+Safety#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695765)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695765&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Engineering Questions](#tabs-1)
* [2. Software Assurance Questions](#tabs-2)
* [3. Safety Questions](#tabs-3)
* [4. Resources](#tabs-4)

# 1. Engineering Questions

# Questions Common to all Areas

### 1. When a NASA directive requirement (e.g., SWE-022 in NPR 7150.2C) levies a NASA technical standard (e.g., NASA-STD-8739.8A), do the requirements in that technical standard become equivalent in priority to those requirements in the directive? Specifically, if NPR 7150.2C [083](#_tabs-<p>4</p>) is in effect, and because NASA-STD-8739.8A [278](#_tabs-<p>4</p>) is levied by virtue of SWE-022 and SWE-023, then are the requirements in NASA-STD-8739.8A equivalent to any SWE requirement in NPR 7150.2C?

Yes, NASA-STD-8739.8 is required by virtue of NPR 7150.2. The requirements in NASA-STD-8739.8A should be equivalent to any SWE in NPR 7150.2.  Both NPR 7150.2 and NASA-STD-8739.8A requirements can be tailored, deleted or changed by agreement of both Center TAs, SMA and Engineering.  There is flexibility if needed with these requirements.

### 2. A related question arising from the NESC IRT study: Have the 2 requirements in NASA-STD-8739.8A on code coverage and cyclomatic complexity been added to NPR 7150.2C?

No, the two requirements have not been added into NPR 7150.2 yet.  I’m not sure what the schedule is for adding the requirements into the NPR.  Both requirements are applicable if you have safety-critical code per NASA-STD-8739.8A.

The NASA Software Assurance and Software Safety Standard, NASA-STD-8739.8, levies additional requirements both on software assurance and on safety-critical software.

### 3. Are some of the non-NASA documents being considered for use with cybersecurity, like those in the automobile industry?

Yes**,** NASA is looking at the documents in other industries and in some cases participates in some of the Standards Groups, such as IEEE. For cybersecurity, NASA has built on the information from NIST (National Institute of Standards and Technology), HSDP (Healthsuite Digital Platform), and FIPS (Federal Information Processing Standard). However, many of the documents from other industries (like automotive) cannot be applied directly, so NASA is developing its own directives and standards.

### 4. What are some of the key activities that improve coding and testing?

The following activities could potentially improve software development:

* Develop better and more explicit requirements
* Use secure coding standards
* Perform bi-directional traces as required in SWE-052 of NPR 7150.2: (For A, B, and C SW classifications)
  + High level requirements to software requirements
  + Software requirements to system hazards
  + Software requirements to software design components
  + Software design components to software code
  + Software requirements to test procedures
  + Software requirements to software non-conformances

For SW Class D Classifications:

* Software requirements to system hazards
* Software requirements to test procedures
* Software requirements to software non-conformances

* Do peer reviews or inspections on complex design and code modules, requirements and test procedures
* Use static analysis tools before testing
* Perform unit testing
* Think about maintenance/future upgrades as the system/software is being designed and coded

Follow good engineering practices

### 5. Is NASA following IEEE 1633 for software reliability practices?

NPR 7150.2 and NASA-STD-8739.8 contain practices that help build more reliable software, but NASA is not specifically following IEEE 1633.

# 2. Software Assurance Questions

### **1. Please explain how the requirements in NASA-STD-8739.8 can be tailored.**

There are three levels of tailoring applicable for the software assurance and safety requirements in NASA-STD-8739.8. They are as follows:

1. The first level of tailoring is the Software Classification Decision, see NPR 7150.2. See Diagram 1 from the NPR.
2. The second level of tailoring is the tailoring in the project’s Software Requirements Mapping Matrix, see NPR 7150.2. See Diagram 2 showing a sample Software Requirements Mapping Matrix.
3. The third level of tailoring is the tailoring by the SA TA of the requirements generated by the corresponding SA requirements to the project’s Software Requirements Mapping Matrix requirements.

**Diagram 1**

**Diagram 2**

### 2. Can programs choose to “opt-out” of this Standard, like engineering may be staying on 7150.2B? That is, are 7150.2C/8739.8A intimately linked so you must move to them together?

It is highly desirable for the programs/projects still using the B version of the NPR to move to the latest version of the Standard, NASA-STD-8739.8A.

[278](#_tabs-<p>4</p>) For those projects still using the B version of the NPR, a mapping from the requirements in NPR 7150.2B to the NASA-STD-8739.8A assurance and safety tasks has been provided in Topic [8.14 - SA Tasking for NPR 7150.2B](/spaces/SWEHBVC/pages/81691461/8.14+SA+Tasking+for+NPR+7150.2B)  in this Handbook. This mapping provides the necessary information for a program/project to use the new Standard with NPR 7150.2B

### 3. Can engineering move to the new revision and SMA keep the old and vice versa?

It is possible for engineering to use NPR 7150.2B [265](#_tabs-<p>4</p>)  with the new NASA-STD-8739.8. As stated in the previous FAQ response, they can use the mapping in this Handbook to align the requirements with the new software assurance and safety tasking in NASA-STD-8739.8A.[278](#_tabs-<p>4</p>)  If engineering is using the NPR7150.2C, Software Assurance should definitely be using the new Standard, NASA-STD-8739.8A.

### 4. In the old standard, sections 5.5.1.4, 6.6.2 and 6.7.1 referenced the building of “lessons learned” throughout a project.   In the new Standard, there is no reference to lessons learned.   What is the reasoning behind this exclusion?

Lessons Learned is really a requirement addressed in Knowledge Policy for Programs and Projects, NPR 7120.6A:

* “5. Responsibility:  
  …..  
  b. The NASA CKO is responsible for policy and integration of knowledge services across programs and projects in the Centers and Mission Directorates and reports to the Office of the Chief Engineer. The NASA CKO shall:  
  (8) Facilitate the dissemination and promote the infusion and utilization of LESSONS LEARNED and best practices, develop and share actionable methodologies, and maintain the NASA LESSONS LEARNED Information System.”

### **5. What value does test witnessing provide?**

The person(s) performing test witnessing should be able to:

1. Confirm that the test environment is set up and configured properly,
2. Confirm that each test case is run correctly, according to the agreed upon test procedures,
3. Confirm that the test produces the expected results, and
4. Confirm that any defects, discrepancies, or problems with the test environment, test configuration, test procedures/cases, test run, or results are documented and addressed before the test is considered complete, either with a “passing result” or in accordance with the acceptance criteria. Ideally:
   1. All tests should result in a “pass”.
   2. If there are defects, discrepancies, or problems preventing a passing result, confirm that they are discussed with or evaluated by the Customer to determine if it must be fixed or if the software can be released with the bug. This will allow the test to be closed out.
   3. Note: If there is a problem with the test environment or test configuration, the test should be cancelled.

### **6. What differences are being introduced with the updated SA Standard (NASA-STD-8739.8)?**

The three main differences are the inclusion of the secure coding practices,  the cybersecurity requirements and revised criteria for determining safety-critical software. This revision of the SA Standard is closely tied to the NPR 7150.2, so it is obvious what assurance and safety practices need to be performed for each NPR requirement. The SW Safety Standard (NASA-STD-8719.13) has also been rolled into the new SA Standard. The new Standard is much more performance based.

# Questions Common to all Areas

### 1. When a NASA directive requirement (e.g., SWE-022 in NPR 7150.2C) levies a NASA technical standard (e.g., NASA-STD-8739.8A), do the requirements in that technical standard become equivalent in priority to those requirements in the directive? Specifically, if NPR 7150.2C [083](#_tabs-<p>4</p>) is in effect, and because NASA-STD-8739.8A [278](#_tabs-<p>4</p>) is levied by virtue of SWE-022 and SWE-023, then are the requirements in NASA-STD-8739.8A equivalent to any SWE requirement in NPR 7150.2C?

Yes, NASA-STD-8739.8 is required by virtue of NPR 7150.2. The requirements in NASA-STD-8739.8A should be equivalent to any SWE in NPR 7150.2.  Both NPR 7150.2 and NASA-STD-8739.8A requirements can be tailored, deleted or changed by agreement of both Center TAs, SMA and Engineering.  There is flexibility if needed with these requirements.

### 2. A related question arising from the NESC IRT study: Have the 2 requirements in NASA-STD-8739.8A on code coverage and cyclomatic complexity been added to NPR 7150.2C?

No, the two requirements have not been added into NPR 7150.2 yet.  I’m not sure what the schedule is for adding the requirements into the NPR.  Both requirements are applicable if you have safety-critical code per NASA-STD-8739.8A.

The NASA Software Assurance and Software Safety Standard, NASA-STD-8739.8, levies additional requirements both on software assurance and on safety-critical software.

### 3. Are some of the non-NASA documents being considered for use with cybersecurity, like those in the automobile industry?

Yes**,** NASA is looking at the documents in other industries and in some cases participates in some of the Standards Groups, such as IEEE. For cybersecurity, NASA has built on the information from NIST (National Institute of Standards and Technology), HSDP (Healthsuite Digital Platform), and FIPS (Federal Information Processing Standard). However, many of the documents from other industries (like automotive) cannot be applied directly, so NASA is developing its own directives and standards.

### 4. What are some of the key activities that improve coding and testing?

The following activities could potentially improve software development:

* Develop better and more explicit requirements
* Use secure coding standards
* Perform bi-directional traces as required in SWE-052 of NPR 7150.2: (For A, B, and C SW classifications)
  + High level requirements to software requirements
  + Software requirements to system hazards
  + Software requirements to software design components
  + Software design components to software code
  + Software requirements to test procedures
  + Software requirements to software non-conformances

For SW Class D Classifications:

* Software requirements to system hazards
* Software requirements to test procedures
* Software requirements to software non-conformances

* Do peer reviews or inspections on complex design and code modules, requirements and test procedures
* Use static analysis tools before testing
* Perform unit testing
* Think about maintenance/future upgrades as the system/software is being designed and coded

Follow good engineering practices

### 5. Is NASA following IEEE 1633 for software reliability practices?

NPR 7150.2 and NASA-STD-8739.8 contain practices that help build more reliable software, but NASA is not specifically following IEEE 1633.

# 3. Safety FAQ

### 1. What should we be doing to identify what software might be safety-critical under the new Standard (NASA-STD-8739.8A [278](#_tabs-<p>4</p>))?

NASA-STD-8739.8A defines a safety criticality software determination process which should be used to identify safety-critical software:

Software is classified as safety-critical, if it meets at least one of the following criteria:

* + Causes or contributes to a system hazardous condition/event,
  + Provides control or mitigation for a system hazardous condition/event,
  + Controls safety-critical functions,
  + Mitigates damage if a hazardous condition/event occurs,
  + Detects, reports, and takes corrective action, if the system reaches a potentially hazardous state.

Look at the systems hazard analysis and see if there is any software that meets any of the above criteria. If so, it is safety-critical

### 2. If the software could affect a command, but there are features built in to ensure the problem will not occur, is it safety-critical?

No.

### 3. What additional requirements or activities are done for safety-critical software?

The majority of the activities for safety-critical software are just good engineering practices. The new Standard only has two new requirements for safety-critical software that were not in the old Standard:

1. Achieve 100% code coverage when testing safety-critical software. (If it can’t be achieved, a rational for why it can’t be reached must be provided)
2. The Cyclomatic Complexity of safety-critical software must be 15 or lower.

Other important activities for safety-critical software include:

* + Perform an assessment of the hazard analysis to identify software components associated with system hazards as per the safety criticality determination listed of Question 1.
  + Develop and maintain a safety analysis throughout the life cycle.
  + Assess that the code meets the requirements in SWE-134.
  + Perform a software assurance design analysis.
  + Confirm that the software test plan addresses the verification of safety-critical software, specifically the off-nominal scenarios.
  + All safety-critical software needs to be verified by test. All critical lines of code must be tested as well as all conditions and end points
  + Confirm that the traceability between software requirements and hazards with software contributions exist.
  + Perform a software assurance analysis on the detailed software requirements to analyze the software requirement sources and identify any incorrect, missing, or incomplete requirements.
  + Confirm that the software design implements all of the required safety-critical functions and requirements.
  + Perform test witnessing for safety-criticality software.
  + Adequate regression testing is performed and includes retesting of all safety-critical code components.

It is important to make sure you have a good hazard analysis. It tells what requirements are safety-critical to indicate which elements of the design, code, and test activities need additional rigor.

### 4. Do we still need to mark the safety-critical code?

Marking (“tagging”) of the software is no longer required.

### 5. Do we still figure out the “levels” of safety-critical software (i.e., use of the levels to scope the work on the safety-critical software) like it is described in the Software Safety Guidebook?

The sub-levels are not needed any more---either the software is safety-critical or it is not.

### 6. The previous method called for a formal preliminary hazard analysis, plus a hazard analysis, now what do we need? Do we need explicit documentation on safety-critical software? When would you see it?

The hardware and software groups should cooperate on developing the hazard analysis reports. You need to have a plan on how you plan to handle the safety-critical software. Now, with the new approach, software by itself must cause a hazard for it to be safety-critical. This may be mitigated with inhibits or just declare it safety-critical. The new approach just requires a few new steps and tracing to hazards.

### 7. What about mission critical software?

Still need to consider [SWE-134](/spaces/SWEHBVC/pages/50888966/SWE-134+-+Safety+Critical+Software+Design+Requirements) for mission critical software.

### 8. Is verification by similarity allowed for safety-critical software?

No, safety-critical software is required to be verified by test. See the requirements below.

#### NPR 7150.2C [083](#_tabs-<p>4</p>)

4.5.12 The project manager [shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique. [SWE-192]](/spaces/SWEHBVC/pages/50889421/SWE-192+-+Software+Hazardous+Requirements)

#### NASA-STD-8739.8A [278](#_tabs-<p>4</p>)

|  |  |  |  |
| --- | --- | --- | --- |
| 4.5.12 | 192 | The project manager shall verify through test the software requirements that trace to a hazardous event, cause, or mitigation technique. | 1. Confirm that the project verifies the software requirements, which trace to a hazardous event, cause, or mitigation techniques, through testing. |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 3.7.3 | 134 | If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software: a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software of functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal | |  | | --- | | 1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l." | | 2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone. | | 3. Confirm 100% code test coverage is addressed for all identified software safety-critical software components or assure that software developers provide a risk assessment explaining why the test coverage is not possible for the safety-critical code component. | |

A project can tailor the requirement if the engineering and SMA TAs agree with the rational and risk.

### **9. In the new NASA-STD-8739.8, safety and software assurance are combined, but they are often performed by different roles. Will the training for each be combined or will there be separate training for each role?**

The SMA Technical Training Program (STEP) program has separate paths of study for the software assurance and software safety roles. However, the training classes for each are available individually. The classes are available in SATERN to anyone who wants to take them, so the individual may select and take a designated class if desired. The STEP program is a tiered, coordinated set of classes and on-the-job-training to prepare participants for certain roles.

# Questions Common to all Areas

### 1. When a NASA directive requirement (e.g., SWE-022 in NPR 7150.2C) levies a NASA technical standard (e.g., NASA-STD-8739.8A), do the requirements in that technical standard become equivalent in priority to those requirements in the directive? Specifically, if NPR 7150.2C [083](#_tabs-<p>4</p>) is in effect, and because NASA-STD-8739.8A [278](#_tabs-<p>4</p>) is levied by virtue of SWE-022 and SWE-023, then are the requirements in NASA-STD-8739.8A equivalent to any SWE requirement in NPR 7150.2C?

Yes, NASA-STD-8739.8 is required by virtue of NPR 7150.2. The requirements in NASA-STD-8739.8A should be equivalent to any SWE in NPR 7150.2.  Both NPR 7150.2 and NASA-STD-8739.8A requirements can be tailored, deleted or changed by agreement of both Center TAs, SMA and Engineering.  There is flexibility if needed with these requirements.

### 2. A related question arising from the NESC IRT study: Have the 2 requirements in NASA-STD-8739.8A on code coverage and cyclomatic complexity been added to NPR 7150.2C?

No, the two requirements have not been added into NPR 7150.2 yet.  I’m not sure what the schedule is for adding the requirements into the NPR.  Both requirements are applicable if you have safety-critical code per NASA-STD-8739.8A.

The NASA Software Assurance and Software Safety Standard, NASA-STD-8739.8, levies additional requirements both on software assurance and on safety-critical software.

### 3. Are some of the non-NASA documents being considered for use with cybersecurity, like those in the automobile industry?

Yes**,** NASA is looking at the documents in other industries and in some cases participates in some of the Standards Groups, such as IEEE. For cybersecurity, NASA has built on the information from NIST (National Institute of Standards and Technology), HSDP (Healthsuite Digital Platform), and FIPS (Federal Information Processing Standard). However, many of the documents from other industries (like automotive) cannot be applied directly, so NASA is developing its own directives and standards.

### 4. What are some of the key activities that improve coding and testing?

The following activities could potentially improve software development:

* Develop better and more explicit requirements
* Use secure coding standards
* Perform bi-directional traces as required in SWE-052 of NPR 7150.2: (For A, B, and C SW classifications)
  + High level requirements to software requirements
  + Software requirements to system hazards
  + Software requirements to software design components
  + Software design components to software code
  + Software requirements to test procedures
  + Software requirements to software non-conformances

For SW Class D Classifications:

* Software requirements to system hazards
* Software requirements to test procedures
* Software requirements to software non-conformances

* Do peer reviews or inspections on complex design and code modules, requirements and test procedures
* Use static analysis tools before testing
* Perform unit testing
* Think about maintenance/future upgrades as the system/software is being designed and coded

Follow good engineering practices

### 5. Is NASA following IEEE 1633 for software reliability practices?

NPR 7150.2 and NASA-STD-8739.8 contain practices that help build more reliable software, but NASA is not specifically following IEEE 1633.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVC/pages/50888842/References+Table)

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
   https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-265)

  [NPR 7150.2B NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450360/N_PR_7150_002B_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2B, Effective Date: November 19, 2014, Expiration Date: November 19, 2019Copy attached to this SWEREF.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
