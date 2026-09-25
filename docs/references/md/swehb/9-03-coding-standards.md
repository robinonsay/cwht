# 9.03 Coding Standards

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695794. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards

9.03 Coding Standards

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695794)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695794&showCommentArea=true&showComments=true#addcomment)

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

Implement a "secure" coding standard on all mission-critical software.

## 1.1 Rationale

Consistent use of approved coding standards reduces the frequency of common run-time errors and promotes maintainability and re-usability.

## 2. Examples and Discussion

Coding standards promote readability and maintainability---important features for code that is likely to be used over a period of years or reused on other projects and [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) in NPR 7150.2 [083](#_tabs-<p>4</p>) calls for the use of secure coding standards. A quality set of coding standards can improve the quality of code in many other ways as well. The list below specifies a minimal set of standards commonly found in standards for high-reliability software. These rules have been found to reduce the likelihood of run time errors.

1. Restrict the use of dynamic memory allocation to one-time events at system initialization.
2. Use the simplest flow control constructs possible, and avoid the use of “go to”, *setjump/longjump*.
3. Ensure that all loop constructs have a fixed upper bound, and avoid the use of recursion.
4. Declare data objects at the lowest scope possible.
5. Verify the validity of input parameters at the start of each function, and take appropriate action when inputs are off-nominal. (see also [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) and [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) design principles) See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) .
6. Implement logic to check, and possibly act, on the return value of non-void functions.

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).

A complete set of coding standards typically includes best practices, such as strict language adherence and the use of automated tools to identify problems either at compile time or run time. Language-specific guidance, domain-specific guidance, local standards for code organization and commenting, and standard file header format are often specified as well.

Good coding standards have two things in common: (1) they are concise and relevant enough to be easily used by programmers and quality assurance professionals in their daily activities; and (2) they enable the use of automated code checking. The first is important for obvious reasons. A standard that is too cumbersome will quickly fall into disuse. The second is important because it reduces cost and increases the likelihood that violations that would lead to program errors will be caught before deployment.

A draft version of design principles produced by the Marshall Space Flight Center (MSFC) includes guidance on the use and development of coding standards. In keeping with a “keep it simple” approach, the standard had only six mandatory practices applicable across all programming languages and allows the inclusion of language-specific and project-specific aspects. The mandatory practices strongly overlapped with the minimal set above, and the standard made it clear that the fundamental practices were not to be overridden by language-specific standards, which in turn were not to be overridden by project-specific standards. This tiered approach makes it easier for an organization to implement a basic set of standards that may be tailored on a per-project basis. This approach supports a Capability Maturity Model Integration (CMMI) Level 3 and above organization.

JPL has taken a somewhat different approach. All projects are required to identify the coding standards used in the development, but no specific standard is imposed. An institutionally supported C coding standard is available. This standard is broken down into six levels of compliance, each more rigorous than the next. Projects that use the institutional standard must determine the level of compliance appropriate for their project. Projects are allowed to produce their own standard, use an alternative standard, or tailor the institutional standard. Except for a general provision concerning safety-critical software, there are no restrictions on the standards that may be used. This approach also supports a CMMI Level 3 certification.

Specific coding standards in use include JPL's C Coding Standard [331](#_tabs-<p>4</p>) , GSFC's C Coding Standard for Flight Software [333](#_tabs-<p>4</p>), and GSFC's C++ Coding Standard for Flight Software [338](#_tabs-<p>4</p>), which is all available in the Software Processes Across NASA (SPAN)  library. Another resource for coding standards is Gerard Holzmann's "Power of Ten" [417](#_tabs-<p>4</p>) paper. There are a number of static analysis tools that can help verify adherence to coding standards, including VectorCast, Polyspace, and Klocwork.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

## 3.1 NESC inputs

**6.3.1.4.1 Coding and Implementation Issues Related to Reliability** [669](#_tabs-<p>4</p>)  
  
Definition of suitable coding standards and conventions: Coding standards and conventions can enhance reliability by considering such issues as:

* Policies on dynamic memory allocation in safety-critical systems (generally, it should not be allowed)
* “Defensive” coding practices for out of range inputs and response times
* Exception handler implementation
* Coding to enhance testability and readability
* Documentation to support verification
* Interrupt versus deterministic timing loop processing for safety-critical software
* Policies on allowable interprocess communications mechanisms (e.g., point to point versus publish and subscribe)
* Permitted use of dynamic binding (an alternative is static "case statements")
* Policies on initialization of variables (some standards prohibit the assignment of dummy values to variables upon initialization in order to enable detection of assignment errors in subsequent execution)
* Use of “friend” (C++) or “child” (Ada) declarations to enable testing and evaluation of encapsulated data code during development without requiring the subsequent removal of “scaffold code”.
* For object-oriented languages, limitations on levels of inheritance in order to prevent “accidental inheritance” due to the introduction of variables with the same name or variable misspelling.

See also [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification), [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices), Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality).

### 3.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-331) JPL Institutional Coding Standard for the C Programming Language Version: 1.0, Date: March 3, 2009, JPL DOCID D-60411 This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-333) C CODING STANDARD
   GFSC - Flight Software Branch - Code 582, Version 1.1 - 11/29/05, 582-2000-005, This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-338) C++ CODING STANDARD GSFC, Flight Software Branch - Code 582, Version 1.0 - 12/11/03, 582-2003-004 This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-417)

  ["The Power of 10: Rules for Developing Safety-Critical Code"](http://spinroot.com/gerard/pdf/Power_of_Ten.pdf "Click to open in new window")

  Holzmann, G.J., NASA Jet Propulsion Laboratory (JPL), 2006.
* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.
* (SWEREF-669)

  [Design Development Test and Evaluation (DDT&E) Considerations for Safe and Reliable Human Rated Spacecraft Systems](http://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20080019636.pdf "Click to open in new window")

  NASA/TM-2008- 215126/Vol II, NESC-RP-06-108/05-173-E/Part 2, April, 2008,  See report section: 6.3.1.4.1 Coding and Implementation Issues Related to Reliability
* (SWEREF-684)

  [Flight Software Deadly Embrace](http://llis.nasa.gov/lesson/369 "Click to open in new window")

  Public Lessons Learned Entry: 0369, Date: 1995-01-24, Submitting Organization: JPL, Submitted by: B. Larman

## 4.2  Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices)       * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity) * [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling) |

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

### 5.1 NASA Lessons Learned

Lessons that appear in the NASA LLIS or Center Lessons Learned Databases. [439](#_tabs-<p>4</p>)

* **Flight Software Deadly Embrace**. **Lesson Learned 0369: **[684](#_tabs-<p>4</p>)**** "During a walk-through of the Galileo Spacecraft System fault protection implementation a possible "deadly embrace" in the flight software was uncovered. A deadly embrace is a continuous software looping operation that may preclude the achievement of an acceptable spacecraft state."
