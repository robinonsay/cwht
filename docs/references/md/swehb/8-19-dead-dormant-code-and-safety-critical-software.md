# 8.19 - Dead Dormant Code and Safety-Critical Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695759. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software

8.19 - Dead / Dormant Code and Safety-Critical Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695759)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695759&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Introduction

This topic discusses the issues of having dead or dormant code in software that is safety-critical. 

## 1.1 What is Dead Code or Dormant Code?

**Definitions:**

* Code, definition, function or configuration that is never used during runtime.
* Section of source code that is executed, but the result is never used.
* Logic branch that is unreachable or can never be executed under current configuration
* Configuration items that are no longer called or utilized.
* **Summation:** Dead/Dormant code is:
  + Code that is not executed.
  + Function that is not used.
  + Configuration that is not used.
  + A result of a function that is never used.

**Note:** Dead and Dormant code are, in this respect, considered fundamentally the same thing.   
**For the remainder of this topic, “Dead” code will be used to refer to both “Dead” and “Dormant” code.**

## 1.2 Why are Dead Code and Dormant Code problems?

**Potential problems with Dead/Dormant Code:**

* Makes the Code Base harder to understand and maintain (Increases cost and time)
* Increases inefficiency of the system.
* Increases potential instability and thus increases risk.
* Results in a greater chance for unexpected or undesired result.

## 1.3 What are the best practices to use with Dead/Dormant Code?

## 1.3.1 What should be done to minimize Dead Code?

* Dead code should be identified. Comment statements might be one way to identify the Dead code.
* Dead code should be removed if possible.
* Avoid duplication of code or functions. This leads to Dead code as well as increased difficulties in maintaining the Code Base. If portions of the code will be used multiple times, put them in a function that can be called.
* If available, use analysis tools for identifying Dead code. These tools are separate from compilers. Some compilers identify the Dead code and don’t put it into the executable, but that still leaves the Dead code in the Code Base that is being maintained.
* Ensure 100% code coverage for unit testing. This will help to determine if any Dead code exists. If 100% coverage cannot be achieved, determine and document why and determine the potential risk.

## 1.3.2 General Guidelines and best practices to manage Dead Code.

* Avoid duplication of code or functions. This often leads to Dead code during future code modifications.
* When using a compiled language, do not depend on the compiler to remove any Dead code. Any identified Dead code should be actively removed before the compilation.
* Use a Code Analysis tool to identify Dead code.
* Avoid using test or temporary code inside the Code Base. This includes all code that is not directly needed for operation in a live environment. If using test code within the code base is required for testing purposes, it must be removed before the code base is released.
* Verify configuration items are documented and utilized. If not utilized, they should be removed.
* Each development team should have established procedures for identifying, handling and removing Dead code. These procedures should be tailored to the needs of each team to facilitate requirements and ensuring stable and reliable code.
* Before removing Dead code, ensure it is not being utilized by other processes. This is especially important in software that is used between multiple projects and purposes.

For more discussion and some examples, see  the [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion) in the Software Design Principles tab.

See related topics involving "dead code": [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class), [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis), [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis),

See also [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis), [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements), [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage),

## 1.4 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

No references have been currently identified for this Topic. If you wish to suggest a reference, please leave a comment below.

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage)        * [7.13 - Transitioning to a Higher Class](/spaces/SWEHBVD/pages/102695646/7.13+-+Transitioning+to+a+Higher+Class) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) * [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
