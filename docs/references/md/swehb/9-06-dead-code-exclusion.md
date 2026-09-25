# 9.06 Dead Code Exclusion

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695797. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion

9.06 Dead Code Exclusion

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695797)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695797&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Principle and Rational](#tabs-1)
* [2. Examples](#tabs-2)
* [3. Inputs](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Principle

[9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles)

* [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards)
* [9.04 Command Receipt Acknowledgement](/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement)
* [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity)
* [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion)
* [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response)
* [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification)
* [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access)
* [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode)
* [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling)
* [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins)
* [9.13 Resource Oversubscription](/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription)
* [9.14 Resource Usage Measurement](/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement)
* [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions)
* [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety)
* [9.17 Toggle Commands](/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands)

Establish a policy for eliminating unreachable code or mitigating the risk of any unreachable code.

## 1.1 Rationale

Code that is believed to be unreachable poses a residual risk to the system in the event that it is executed inadvertently.

## 2. Examples and Discussion

One approach to implementing this design principle is to perform an analysis of unnecessary and/or unreachable code early in the life cycle. Although it is possible to identify unused code through manual code reviews, many commercial static analysis tools can be configured to identify unreachable code in an automated fashion. Run-time coverage analysis tools can also be used to identify unused sections of the code, although this technique may only be available later in the life cycle once an executable is available.  Regardless of the means of identifying unused or unreachable code, an engineering analysis would be performed to describe the functionality associated with the code, and the relative cost/benefit of leaving it in place versus removing it. If the recommendation is to leave the code in place, the analysis would provide the rationale for doing so, and the justification (e.g., mitigating action) that explains why the included code does not provide a risk to the mission. The focus is on technical risk to the long term mission, not cost. See also Topic [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software)**.**

.

There are significant benefits to re-using software from past missions but each mission has different requirements and re-using heritage software often carries forward software not required by the current mission. Unnecessary and unreachable software can also occur within a mission’s life cycle as system and software requirements change during the software development process. Unnecessary and unreachable software is typically not verified or validated as part of the current mission test programs, as a mission is only required to verify its mission requirements. This creates the potential for negative side-effects, costs and risks during the current mission’s on-orbit life. Table 1 provides sample types of unnecessary or unreachable code.

**Table 1 Sample Types of Unnecessary and Unreachable Software**

| **Sample Types** | **Definition** |
| --- | --- |
| Parameter Checking | A section of software that can never be executed because pre-conditions should never be met.  For example, a properly developed function will validate all parameters to ensure the function doesn’t perform any illegal actions based upon the input parameters.  However, it is possible to write the software system such that it never calls the function with invalid input parameters.  In such a case, the error condition checks within the function should never execute. |
| Unused Design Capability | Application Program Interfaces (API) are developed to promote software reuse.  For example, an Operating System (OS) API will have interface calls for dealing with semaphores (e.g., *create, give, take*, etc.).  If a new mission does not require the use of semaphores; then these OS API functions will never be executed. |
| Unused Reuse Capabilities | A reused software component/library or set of reused software components/libraries will typically contain capabilities and features not required by a mission. |
| Debug/Test Features | Debug and test features, which are not a required part of the operational system, are often required to test the software system.  For example, debug software is often used in conjunction with testing Error Detecting And Correcting (EDAC) memory.  It is extremely difficult to inject correctable and uncorrectable errors into EDAC memory, whereas a test command can easily inject these erroneous conditions to verify that the application software handles and reports the EDAC errors correctly. |

While it is desirable to completely eliminate dead code (or unreachable code), it is sometimes not practical or cost effective. However, the existence of dead code must be known and analyzed. The following table describes one way to identify and manage dead and unreachable code during the development life cycle.

**Table 2. Example Life Cycle Based Implementation of Dead Code Exclusion**

| **Phase** | **A** | **B** | **C** | **D** |
| --- | --- | --- | --- | --- |
| **Activities:** | 1.  Document that a flight software (FSW) Reuse Plan and risk assessment of unnecessary and/or unreachable code will be developed. | 1.  Document the FSW Reuse Approach and the plan for managing unnecessary and/or unreachable code in the FSW Mgmt./ Development Plan(s).   2.  Identify and document code capabilities/ requirements that are not required for the current mission but are intended to be included in the FSW product(s).   3.  Provide initial risk Identification, assessment & anticipated mitigation technique for each known type of unnecessary/ unreachable code.      4.  Present analysis at FSW Reviews | 1.  Analyze the potential risk of leaving the code in the flight product rather than removing it.   2.  Remove unnecessary and unreachable software that creates risk.   3.  Update software verification plans if justified to reduce risk.   4.  Present analysis and risk mitigations at FSW Reviews   5.  Update the documentation of unnecessary and unreachable code associated with  the intended flight products | 1.  Update and analyze the documentation of unnecessary and unreachable code from heritage and newly developed flight products.   2.  Remove unnecessary and unreachable software that creates risk.   3.  Update software verification plans if justified to reduce risk.   4.  Present analysis at FSW reviews. |
| **Verification:** | Verify at Mission Definition Review (MDR). | 1.  Verify at FSW Software Requirements Review (SRR) & FSW Preliminary Design Review (PDR)    2.  Verify at SDR & PDR | 1.  Verify at Critical Design Review (CDR)    2.  Verify at FSW CDR | 1.  Verify at FSW Acceptance Test Review   2.  Verify at Pre-Ship Review (PSR) and Flight Readiness Review (FRR). |

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

None

### 3.2 GSFC

None

### 3.3 JPL

None

### 3.4 MSFC

None

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) |

## 4.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 4.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

## 5. Lessons Learned

No lessons learned [439](#tabs-4)  have currently been identified for this principle .
