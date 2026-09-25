# 7.21 - Multi-condition Software Requirements

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695692. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements

7.21 - Multi-condition Software Requirements

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695692)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695692&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Multi-Logic Testing - Definitions](#tabs-1)
* [2. When Conditions Are Not Discrete](#tabs-2)
* [3. Summary](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Multi-Logic Testing

## 1.1 – Definitions

* **Unit Testing**
  + Testing of individual routines and modules by the developer or an independent tester (ISO/IEC/IEEE 24765).
  + A test of individual programs or modules in order to ensure that there are no analysis or programming errors (ISO/IEC 2382-20).
  + Test of individual hardware or software units or groups of related units. (ISO/IEC/IEEE 24765)
  + MC/DC Testing
* **Software Verification**
  + Confirmation that products properly reflect the requirements specified for them. Verification ensures that “you built it right.” (Source: IEEE 1012)

* **Software Integration Testing -**

+ Integration testing examines if the individual components developed and tested separately, interact as expected when they are combined to form a part of a larger system. (Source: IEEE)

* **Integration Testing -**
  + Integration testing examines if the individual components developed and tested separately, interact as expected when they are combined to form a part of a larger system. (Source: IEEE)

The recommendations in this topic are for unit testing for code coverage in conjunction with correct functional behavior.

See also [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage),

## 1.2 Multi-Logic Condition Requirements

* **Simplified Example of Multi-logic Condition Software Requirement:**
  + “ If mode is STANDBY and status is (ENABLED or ACTIVE), the software shall store the current time.”
* **For software requirements, there should be very few multi-logic condition requirements**
  + Multi-logic condition requirements complicate testing and should be reduced or eliminated, if possible
* **Operators used in textual requirements are typically “and” or “or”**
* **The example above can be restated as: If A and (B or C) then store the current time.**
  + If the result of “A and (B or C)” is TRUE, then the current time will be stored.
  + Operators are “and” and “or”, operands are “A” , “B”, and “C” each with two possible states (i.e. True/False)
  + Three operands yields a possible 2n test combinations, 8 possible test cases

## 1.3 Verifying Multi-logic Condition Requirements

1. If possible, rewrite software requirement to eliminate multi-logic conditions
2. The preferred method of verification should be test. Inspection, Analysis, or Demonstration should only be used if test is not possible
3. For complete condition combination coverage (CCC) also called Multiple Condition Coverage (MCC), a test case for each possible combination may be run.  This covers the full truth table.
4. In many cases, running all 2\*\*N test cases is not practical, in this case MC/DC test coverage is used to perform the minimal set of meaningful test cases  (i.e. tests that use a unique set of inputs to achieve a unique outcome).

Examples below illustrate application of this recommendation.

## 1.4 MC/DC Example

|  |  |
| --- | --- |
| MC/DC (Modified Condition/Decision Coverage) Rules:  1. Each entry and exit point is invoked (lines 1 and 9 are tested) 2. Each decision takes every possible outcome (lines 6 and 8 are tested, abort and null) 3. Each condition in a decision takes every possible outcome (off\_course, abort, and valid are each tested for both TRUE and FALSE) 4. Each condition in a decision is shown to independently affect the outcome - Why? This tests each condition ***only when it matters*** – when it effects outcome | Source Code  **1  function check\_abort()**  **2  {**  **3    if (off\_course OR**  **4       (abort\_commanded AND valid\_abort\_command))**  **5    then**  **6       abort();   // initiate abort sequence**  **7    else**  **8       null;      // do nothing**  **9    return;**  **10  }** |

| Possible Test Cases:  * 4 Green Row Cases (6,4,2,3 in that order) for “unique cause” MC/DC * X’s indicate “don’t care” for “masking” MC/DC * 8 Cases for full Condition Combination Coverage (CCC)   Three (3) types of MCDC3 -- Unique-Cause (N+1 tests), Masking (2\*Sqrt(n) tests), and Unique-Cause+Masking  (NPR7150.2 does not dictate which to use)   * “Unique Cause” MCDC holds all variables constant and changes only one at a time testing for unique outcome   + Example: Only rows 6,2,4,3 in table need be tested (*in that order*) and represent one possible *minimum set of meaningful test cases  (i.e Starting with row 6, changing only “off\_course” in Test 2 results in a different outcome, then test 4 changes only “abort” with a different outcome, then test #3 changes “valid” for a different outcome)* * “Masking” MCDC allows other conditions to change as long as only the condition of interest influences the outcome (See backup for performance)   + Masking MCDC is implemented by “short-circuiting” in computer programs (i.e. stopping as soon as test criteria are met)   + Example: Any 4 tests including one of (5,6,7,8), both (3 and 4), and either (1 or 2) meet the criteria. (i.e. (5,1,3,4), (6,2,3,4), (8,1,3,4), etc…) |  |
| --- | --- |

**Using same methods used to find MCDC minimum set of unit tests: for n logic conditions (operands) n+1 tests will sufficiently verify the requirement.**

# 2. Recommendations for Requirements When Conditions Are Not Discrete

### Simplified Example:

* “ If mode is PROCESSING and TEMPERATURE is greater than 50.0, the software shall set a WARNING.”

### The example above can be restated as: If A and (B>50.0) then set a warning.

* In this case, operand A can have two possible states but B can have many states
* Very difficult to test and analyze all combinations

|  |  |
| --- | --- |
| **Best practice is to run tests with values just below the limit, at the limit, and just above the limit.**   * Note this method is analogous to Parameter Boundary Testing * For each value of A, vary B just below the limit, at limit, and just above the limit |  |
| **Analyzing and testing all combinations becomes even more difficult if both A and B can have many states**    * Simplified Example: If (A < 25.0) and (B > 50.0) then set a warning * Using the same method as the last example, vary both A and B |  |
| **Could break this requirement into two separate requirements, for example:**   * If (A < 25.0) then set LO\_PRESS = TRUE * If (B > 50.0) and LO\_PRESS then set a warning * In this simplified example, the number of test cases is the same (whether there is one requirement or two), but the test cases are easier to understand. |  |
| **In cases where a specific operand can have a range of values best practice is to use Boundary Parameter Testing and also select values in the middle of the range**  Example:   * “ If (PRESURE > 25) and (PRESSURE < 45), the software shall set PRESSURE\_OK.” |  |

# 3. Summary - Verifying Multi-logic Condition Requirements

* **Recommend either running the full set of 2n test cases for Multi-condition requirements, or running the minimal meaningful set using MC/DC criterion**
  + For safety-critical software, MC/DC must be performed with N+1 test cases, or request a waiver (to NPR 7150.2 [083](#_tabs-<p>4</p>) and NASA-STD-8739.8 [278](#_tabs-<p>4</p>))
    - In practicality, all possible MC/DC tests may not be achievable, but in those cases all conditions/decisions not achievable through unit testing should be listed and waived by the appropriate level of technical authority and software assurance.
  + Throughout this unit test process, the developer and/or Subject Matter Experts/Responsible Engineers must ensure not only that the code is exercised, but it functions *correctly* to adequately cover intent or requirement and the expected behavior of the software.
* **If running the full set of test is not practical, run the minimum subset of tests to prove that varying each operand affects the result, independently**
* **For requirements where conditions are not discrete, follow best practice and run tests with values just below the limit, at the limit, and just above the limit.**
  + Recommend thorough requirements analysis to ensure all permutations are represented by selected input values.
* **For requirements where conditions have a range of values, follow best practice and run tests with values just below the limit, at the limit, just above the limit, and at least one value in the middle of the range.**

See [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) for additional guidance. See also [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software), [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software). See also Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis).

## 3.1 Clarifications

**Clarifications**

* Condition - A condition is a leaf-level Boolean expression (it cannot be broken down into simpler Boolean expressions).
* Decision - A Boolean expression composed of conditions and zero or more Boolean operators. A decision without a Boolean operator is a condition.
* Condition coverage - Every condition in the program's decision has taken all possible outcomes at least once.
* Decision coverage - Every entry and exit point in the program has been invoked at least once, and every decision in the program has taken all possible outcomes at least once.
* Condition/decision coverage - Every entry and exit point in the program has been invoked at least once. Every condition in a decision in the program has taken all possible outcomes at least once, and the decision in the program has taken all possible outcomes at least once.
* Modified condition/decision coverage - Every entry and exit point in the program has been invoked at least once. Every condition in a decision in the program has taken all possible outcomes at least once, and each condition has been shown to affect that decision outcome independently. A condition is shown to affect a decision's outcome independently by varying just that condition while holding fixed all other possible conditions. The condition/decision criterion does not guarantee the coverage of all conditions in the module. In many test cases, some conditions of a decision are masked by other conditions. Using the modified condition/decision criterion, each condition must be shown to act on the decision outcome by itself, with everything else being held fixed. The MC/DC criterion is thus much stronger than the condition/decision coverage.

## 3.2 Another Example:

An example

Assume we want to test the following code extract:

Source Code

if ( (A || B) && C )

            {

            /\* instructions \*/

            }

            else

            {

            /\* instructions \*/

            }

A, B, and C represent Boolean expressions (i.e., not divisible in other Boolean sub-expressions).

In order to ensure Condition coverage criteria for this example, A, B and C should be evaluated at least one time "true" and one time "false" during tests, which would be the case with the 2 following tests:

1. A = true / B = true  / C = true
2. A = false / B = false / C = false

In order to ensure Decision coverage criteria, the condition ( (A or B) and C ) should also be evaluated at least one time to "true" and one time to "false". Indeed, in our previous test cases:

1. A = true / B = true  / C = true   --->  decision is evaluated to "true"
2. A = false / B = false / C = false --->  decision is evaluated to "false"

and Decision coverage is also realized.

However, these two tests do not ensure a Modified condition/decision coverage, which implies that each boolean variable should be evaluated one time to "true" and one time to "false," affecting the decision's outcome. It means that changing the value of only one condition will also change the decision's outcome. However, with only the two previous tests, it is impossible to know which condition influences the decision's evaluation.

In practice, for a decision with n boolean conditions, we have to find at least n+1 tests in order to be able to ensure modified condition/decision coverage. As there are 3 boolean conditions (A, B et C) in our example, we can (for instance) choose the following set of tests:

1. A = false / B = false / C = true --->  decision is evaluated to "false"
2. A = false / B = true / C = true   --->  decision is evaluated to "true"
3. A = false / B = true / C = false  --->  decision is evaluated to "false"
4. A = true / B = false / C = true   --->  decision is evaluated to "true"

Indeed, in this case:

* between the 1st and 4th test scenarios, only A changed of value, which also made the decision's outcome change its value ("false" in the 1st case, "true" in the 2nd);
* in the same way, between 1st and 2nd, only B changed of value, which also made the decision's outcome change its value (passing from "false" to "true");
* eventually, between 2nd and 3rd, only C changed value and the decision's outcome's value also changed (passing from "true" to "false").

Besides, Decision and Condition coverage criteria are still respected (each Boolean variable and the decision's outcome itself take at least one time the "true" and "false" values). The modified condition/decision coverage is then ensured.

Additional information can be found in NASA/TM−20205011566, NESC-RP-20-01515, Cyclomatic Complexity, and Basis Path Testing Study  [377](#_tabs-<p>4</p>).

## 3.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-377)

  [Cyclomatic Complexity and Basis Path Testing Study](https://ntrs.nasa.gov/api/citations/20205011566/downloads/20205011566.pdf "Click to open in new window")

  NASA/TM?20205011566, NESC-RP-20-01515
* (SWEREF-384)

  [MCDC Checker](https://gitlab.com/gtd-gmbh/mcdc-checker/mcdc-checker "Click to open in new window")

  MCDC Checker source code implemented by GTD GmbH,  tool to check all conditions in your C/C++ source code if they are in
  the necessary form, so that Gcov can generate modified condition decision coverage.
* (SWEREF-393)

  [Couverture](https://www.open-do.org/projects/couverture/ "Click to open in new window")

  Couverture was an Open Source project financially supported by the French Government, the city of Paris and the Ile-de-France region The original Couverture project had the objectives to produce a Free Software coverage analysis toolset together with the ability to generate artifacts that allow the tools to be used for safety-critical software projects undergoing a DO-178B software audit process for all levels of criticality.
* (SWEREF-394)

  [Formalization and Comparison of MCDC and Object Branch Coverage](https://www.adacore.com/uploads_gems/Couverture_ERTS-2012.pdf "Click to open in new window")

  Cyrille Comar, Jerome Guitton, Olivier Hainque, Thomas Quinot AdaCore, 46 rue d’Amsterdam, F-75009 PARIS (France), comar, guitton, hainque, quinot}@adacore.com, Embedded Real Time Software and Systems Conference, Feb 2012,
* (SWEREF-395)

  [MC/DC for Space: A new Approach to Ensure MC/DC Structural Coverage with Exclusively Open Source Tools](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fgtd-gmbh.gitlab.io%2Fmcdc-checker%2Fmcdc-checker%2FMCDC_for_Space_ESA_Software_PA_Workshop_2021.pdf&data=05%7C01%7Cfred.d.haigh%40nasa.gov%7Cb37530c1af71495be06208db35f0f6ce%7C7005d45845be48ae8140d43da96dd17b%7C0%7C0%7C638163081385218842%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=leZ%2FocVKC3LYdpq65aKY%2B61dgC4O3TQl86XpBDxVOkE%3D&reserved=0 "Click to open in new window")

  Thomas Wucher, Andoni Arregui, ESA Software Product Assurance Workshop 2021,
* (SWEREF-396)

  [An Investigation of Three Forms of the Modified Condition Decision Coverage (MCDC) Criterion](https://www.tc.faa.gov/its/worldpac/techrpt/ar01-18.pdf "Click to open in new window")

  DOT/FAA/AR-01/18, US. Department of Transportation, Federal Aviation Administration, April 2001.
* (SWEREF-397)

  [Object and Source Coverage for Critical Applications with the COUVERTURE Open Analysis Framework](https://www.open-do.org/wp-content/uploads/2010/06/couverture_ertss2010.pdf "Click to open in new window")

  Matteo Bordin, Cyrille Comar, Tristan Gingold, J´erˆome Guitton, Olivier Hainque, Thomas Quinot AdaCore, 46 rue d’Amsterdam, F-75009 PARIS (France) {bordin, comar, gingold, guitton, hainque, quinot}@adacore.com, Embedded Real Time Software and Systems Conference, May 2010

## 4.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

### 4.2.1 gcov

See references 384, 393, 394, 395, 396, and 397 for tools related to MC/DC.

[Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) is one tool that can be used to aid in MC/DC testing, see section XXX for more details. <https://gcc.gnu.org/onlinedocs/gcc/Gcov.html>

## 4.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)        * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 4.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 4.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 5. Lessons Learned

Currently there are no Lessons Learned identified for this topic.
