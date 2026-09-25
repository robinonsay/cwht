# SWE-219 - Code Coverage for Safety Critical Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 105709626. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software

SWE-219 - Code Coverage for Safety Critical Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=105709626)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=105709626&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

3.7.4 If a project has safety-critical software, the project manager shall ensure that there is 100 percent code test coverage using the Modified Condition/Decision Coverage (MC/DC) criterion for all identified safety-critical software components.

## 1.1 Notes

Updated from the Note in NPR

In MC/DC coverage, each entry and exit point is invoked, each decision takes every possible outcome (branch coverage), each condition in a decision takes every possible outcome (i.e. each condition tested for both “true” and “false”), and every condition in a decision is shown to independently effect the outcome. Any deviations from 100 percent should be reviewed and waived with rationale by the TAs approval.

## 1.2 History

Click here to view the history of this requirement: SWE-219 History

SWE-219 - Used first in NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | N/A |
| C |  |
| Difference between C and D | First use of this SWE |
| D | 3.7.4 If a project has safety-critical software, the project manager shall ensure that there is 100 percent code test coverage using the Modified Condition/Decision Coverage (MC/DC) criterion for all identified safety-critical software components. |

## 1.3 Applicability Across Classes

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Class | A | B | C | D | E | F |
| Applicable? |  |  |  |  |  |  |

**Key:**     - Applicable |  - Not Applicable

## 1.4 Related Activities

This requirement is related to the following Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |

# 2. Rationale

All Safety-critical software decisions must be tested to protect against loss of crew or vehicle.  MCDC testing represents the minimal set of tests necessary to achieve test coverage over decisions that change the behavior/outcome/output of a computer program.   Anything less than MCDC exposes a risk of a safety-critical decision based on a set of conditions not being tested. Aerospace and space guidance prioritizes safety above all else in the software development life cycle. MC/DC represents a compromise that finds a balance between rigor and effort, positioning itself between decision coverage (DC) and multiple condition coverage (MCC). MC/DC requires a much smaller number of test cases than multiple condition coverage (MCC) while retaining a high error-detection probability.

Requiring 100% MC/DC test coverage for safety-critical software is a clear and necessary step to achieve the highest level of confidence in software reliability and consistency. It ensures errors in decision-making logic are caught and resolved, safeguards against system failures, aligns with industry safety standards, and facilitates certification processes. In systems where lives, missions, and assets are at stake, this requirement demonstrates a commitment to safety, quality, and risk reduction.

* Similar Standards requiring MC/DC testing for Safety-Critical code
  + Aircraft - DO-178B (Safety-critical Level A or B)
  + Automotive - ISO-26262 (ASIL D)
  + Nuclear - IEC-61508-3 (SIL 1-3)
  + Spacecraft - NASA NPR-7150.2 (Class A Safety-critical)

Modified Condition/Decision Coverage (MC/DC) is a rigorous software testing criterion that ensures every decision point in the code, along with its individual conditions, is thoroughly tested. It is widely regarded as a best practice for safety-critical software, as it ensures high confidence in the correctness, reliability, and robustness of the code.

Below is a clear and direct rationale for this requirement:

## 2.1 Why 100 Percent Code Test Coverage Using MC/DC Is Required:

1. **Maximizes Functional Reliability of Safety-Critical Software:**

   * Safety-critical software often controls systems or operations where failure can lead to catastrophic consequences, including loss of life, mission failure, damage to equipment, or environmental harm. Achieving 100% MC/DC test coverage ensures thorough testing of all execution paths, reducing the risk of undetected logic errors or defects.
2. **Detects and Eliminates Logical and Decision Errors:**

   * MC/DC explicitly tests combinations of individual conditions within decision points, ensuring that all possible outcomes of logical operations are validated. This makes it particularly effective in detecting subtle decision errors and incorrect condition combinations that can lead to unsafe or unintended behaviors.
3. **Ensures Comprehensive Coverage of Safety-Critical Code:**

   * By requiring 100% test coverage for safety-critical components, this requirement ensures that no part of the software controlling hazardous operations remains untested. This thorough level of validation is necessary to mitigate risks stemming from untested logic paths.
4. **Mitigates Risks Arising from Complex Decision Logic:**

   * Safety-critical software often involves complex decision-making logic, where interactions among multiple conditions can lead to challenging edge cases. MC/DC ensures that even intricate, condition-dependent behaviors are thoroughly exercised and verified, minimizing risks of unexpected outcomes in real-world scenarios.
5. **Supports Compliance with Industry Safety Standards:**

   * MC/DC is referenced in many safety standards (e.g., DO-178C for aviation software) as a stringent but achievable testing criterion. Ensuring MC/DC compliance for safety-critical components demonstrates adherence to well-established industry practices and builds confidence in the overall system safety.
6. **Improves System Resilience to Edge Cases:**

   * Safety-critical systems must work as intended not only under normal conditions but also during off-nominal conditions (e.g., hardware faults, environmental challenges). MC/DC's exhaustive testing ensures the code responds predictably in edge cases and abnormal scenarios.
7. **Prepares Software for Certification:**

   * In many sectors (e.g., aerospace, medical devices, automotive), stringent testing requirements such as MC/DC are required for regulatory certification of safety-critical systems. Using MC/DC ensures the project is better positioned to achieve regulatory approval and avoid costly rework.
8. **Addresses the "Cannot Fail" Nature of Safety-Critical Software:**

   * Safety-critical software is characterized by its high stakes—failure is simply not an option. The rigorous testing provided by MC/DC offers the highest level of assurance for software correctness, reducing uncertainty and limiting risk to operators, the system, and the environment.

## 2.2 Key Benefits of MC/DC Testing Criterion:

1. **Positive Identification of Defects:** Forces testing of edge cases that might otherwise go unaddressed using less rigorous test coverage methods (e.g., statement or branch coverage).
2. **Precision in Understanding Code Behavior:** Ensures all condition-dependent logic is clearly understood and works as intended in every decision path.
3. **Early Detection of Risks:** Identifies potential issues in the design or code early in the software development lifecycle, minimizing downstream costs of addressing defects.
4. **Increased Operator and Stakeholder Confidence:** Bolsters system reliability and safety assurance, demonstrating that the software has been thoroughly analyzed and tested through best practices.

## 2.3 Why "100 Percent" Test Coverage Is Specified:

* **Eliminates Untested Code in Safety-Critical Components:** Every uncovered line or decision logic presents an unknown risk. This requirement ensures there are no "blind spots" in critical software.
* **Addresses the Worst-Case Scenarios:** Untested code paths can produce unpredictable behavior during rare or exceptional conditions (e.g., emergency responses). Full coverage ensures all conditions are accounted for.
* **Provides a Standard Benchmark:** Setting 100% MC/DC coverage as the benchmark ensures all teams consistently evaluate code quality using the same metric, reducing ambiguity.

# 3. Guidance

## 3.1 Guidance for MC/DC Testing and Reused Computing System Safety Items

This improved guidance clarifies the key aspects of implementing **Modified Condition/Decision Coverage (MC/DC)** testing and managing reused software or third-party computing system components for safety-critical systems. It emphasizes practicality, risk reduction, and actionable steps to ensure compliance with safety requirements.

## 3.2 MC/DC Testing Guidance

**Definition of MC/DC Coverage:** MC/DC ensures thorough verification of decision-making logic in safety-critical software. This involves:

1. **Entry and Exit Points:** Ensuring every entry and exit point in the code is invoked during testing.
2. **Branch Coverage:** Testing every possible outcome of decisions (e.g., every "if" and "else" branch).
3. **Condition Coverage:** Verifying that each condition within a decision is tested for both “true” and “false” outcomes.
4. **Independent Effect:** Demonstrating that each condition within a decision independently affects the decision outcome (e.g., testing combinations of conditions to validate correct decision logic).

For a detailed example, see **Section 7.21: Multi-condition Software Requirements** in the documentation.

## 3.3 Implementation of MC/DC Testing:

1. **Phase of Testing:**

   * MC/DC testing should primarily be conducted during the **unit test phase**. At this phase, software units are isolated and tested to validate their behavior, as well as to exercise all meaningful conditional paths defined by decision points in the code.
2. **Objective:**

   * The goal is to verify that **all decision logic and conditional paths** in the code behave as expected, aligning with requirements and eliminating ambiguity or defects.
3. **Cyclomatic Complexity:**

   * While a specific type of cyclomatic complexity (strict, normal, or modified) is not mandated, projects should select an approach tailored to their specific needs, such as stricter testing for highly critical code modules and less strict testing for less impactful components.
4. **Use of Tools:**

   * Leverage **unit test tools** to automate the identification of untested decision paths and to generate test cases that adhere to MC/DC criteria. Tools can streamline testing efforts, ensuring comprehensive coverage.
   * Example tools: Use coverage analysis tools such as **gcov** or other commercial offerings to validate that all conditions, branches, and effects have been exercised.
5. **Developer Accountability:**

   * Developers must ensure:
     + Proper MC/DC adherence during testing (e.g., all meaningful execution paths exercised).
     + The software unit is functioning exactly as intended under all tested conditions.
     + Results are documented, including evidence of compliance for future project reviews and audits.

**Supporting Resources:**  
Refer to **Section 7.21: Multi-condition Software Requirements** for additional examples and tools (e.g., how to implement MC/DC testing using "gcov").

## 3.4 Commercial of the shelf real time operating system guidance

Reliance is often placed on the vendor’s certification, pedigree, and existing testing processes.

While 8739.8 (Software Independent Verification and Validation) and 7150.2 (NASA Software Engineering Requirements) both emphasize software assurance, their direct application to object code—especially for an off-the-shelf operating system like VxWorks—can depend on the scope of the project and its specific risk posture.

Typically, object code coverage isn't explicitly required *unless* there are strong mission-specific factors that demand it, such as critical safety functions or specific requirements for verifying low-level code functionality. For non-critical portions, abstracting your verification to the source code level and using established and verified operating systems, like VxWorks, is often deemed satisfactory.

Regarding their inability to achieve 100% MC/DC coverage for VxWorks, this is not uncommon for COTS (Commercial Off-The-Shelf) systems. Achieving full MC/DC coverage can be extremely challenging, particularly for complex systems that weren’t designed with this level of testing in mind. Instead, reliance is often placed on the vendor’s certification, pedigree, and existing testing processes. However, it’s important to ensure that critical functionalities are thoroughly tested—even if 100% MC/DC isn’t met—to minimize risks.

Ultimately, the decision comes down to the mission’s requirements and risk tolerance. If this system interacts with mission-critical elements, it may be worth digging deeper into how they validated the portions of code relevant to operations.

It’s common to rely on the vendor’s certification, pedigree, and existing testing processes when dealing with an RTOS like VxWorks. NASA NPR 8739.8 and 7150.2 don’t explicitly require object code coverage, particularly for low-level, off-the-shelf systems, unless mission-specific requirements dictate otherwise. Validating critical functionalities and relying on vendor assurance, historical use and prior certifications can be an acceptable approach, depending on the mission’s risk tolerance.

## 3.5 Reused and Third-Party Computing System Safety Items Guidance

**The Importance of Validation and Verification for Previously Developed Software:**  
While previously developed computing system safety items (e.g., Commercial Off-The-Shelf [COTS], Government Off-The-Shelf [GOTS], or reused software) can reduce development time and costs, they also introduce risks, especially in new system contexts. Analysis of past software-related accidents has demonstrated that reusing computing system safety items without proper validation can lead to failures. Therefore, projects must thoroughly validate and verify safety requirements when incorporating reused or third-party software.

## 3.6 Steps for Risk Mitigation:

1. **Analysis of Role Differences:**

   * Assess the differences between the software's role in the **new system** versus its role in the **previous system**:
     + How does the software support hazardous operations or safety-critical functionality in the new system?
     + Analysis should include evaluating whether new dependencies, interfaces, or operational conditions could expose weaknesses or flaws.
2. **Identification and Resolution of Previous Issues:**

   * Review the historical use of the reused computing system safety item to identify:
     + Known issues, bugs, or vulnerabilities encountered during its previous use.
     + Ensure any preconditions for safe usage (e.g., specific configurations or known limitations) are well-documented and properly implemented in the new system.
3. **Verification of Compliance:**

   * Validate that the reused safety-critical software complies with:
     + **Developer-specified usage requirements:** Ensure the software is used in accordance with the original vendor's guidelines for safety-critical scenarios.
     + **Safety requirements applicable to the new system:** Perform additional verification and testing (as necessary) to confirm the software meets safety requirements specific to the new system.
4. **Third-Party Software Efforts:**

   * For third-party software or computing system safety items:
     + Evaluate risks associated with external components based on their use and role in the system.
     + Perform system-specific testing to verify successful integration and compliance with all safety-related requirements.

## 3.7 Benefits of Following These Guidelines:

* **Reduction of Development Risks:** Allows projects to leverage existing components while systematically addressing integration risks.
* **Improved System Safety:** Provides confidence that reused or third-party items will not introduce unexpected hazards due to improper implementation.
* **Efficient Reuse:** Enables safe and cost-effective reuse of well-tested software while remaining compliant with program safety requirements.

## 3.8 Important Note on Responsibility:

While a component may have been previously developed by another vendor, the **responsibility for reducing risks** remains with the project integrating the component. It is the project’s duty to:

1. Evaluate the safety-critical role of the component in the current context.
2. Implement additional risk-reduction measures as needed.

## 3.9 Key Types of Reused Software:

1. **COTS Software (Commercial Off-The-Shelf):** Proprietary software purchased from third-party providers.
2. **GOTS Software (Government Off-The-Shelf):** Software developed by government agencies and available for reuse.
3. **Reused Software:** Software developed in-house or externally for prior projects that is now being reincorporated into a new system.

## 3.10 Early Integration of Safety Requirements:

* Incorporating safety requirements for reused computing system items early in the development process is critical. It avoids:
  + Late identification of safety issues that could disrupt the project schedule.
  + Increased costs for rework due to unaddressed risks.
  + Potential hazards stemming from misaligned safety designs.

## 3.11 Supporting Resources:

* See **SWE-147 (Specify Reusability Requirements)** for detailed guidance on implementing safety requirements for reusable software components.

## 3.12 Conclusion

This guidance ensures the thorough testing of **safety-critical software** using MC/DC coverage while addressing risks associated with the reuse of previously developed or third-party computing system components. By following this plan, projects ensure that reused software meets safety requirements, minimizes risks, and supports safe and reliable operations within the new system context.

See also Topic [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations), [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance), 

See also [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis), [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage), 

Confirm that 100% code test coverage is addressed for all identified software safety-critical software components or ensure that software developers provide a risk assessment explaining why the test coverage is impossible for the safety-critical code component: [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

## 3.13 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 3.14 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Safety](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Safety) |

# 4. Small Projects

This requirement applies to all Class A, B, C, and D projects that have safety-critical software regardless of size.

## 4.1 Requirement Recap:

For safety-critical software, projects must ensure **100% code test coverage** using the **Modified Condition/Decision Coverage (MC/DC)** criterion for all identified safety-critical software components.

This guidance provides practical, simplified steps to help small projects achieve compliance while remaining efficient and mindful of resource limits.

## 4.2 Practical Steps for MC/DC Implementation in Small Projects

### 4.2.1. Understand What MC/DC Means (Simplified Explanation)

MC/DC ensures thorough testing of decision-making logic in your software. Specifically:

* Each **condition** inside a decision is tested for **true** and **false** values.
* Each condition’s effect on the final **decision outcome** is tested independently.
* Every entry, exit point, and decision branch in the code is executed during testing.

This ensures your safety-critical software behaves correctly under all scenarios.

### 4.2.2. Focus Resources on Safety-Critical Components

* **Identify safety-critical software components early.**  
  These are the parts of your software that directly impact **hazard control, mitigation, or execution of hazardous operations.**
* **Limit the scope of MC/DC testing to just these components.**  
  Don’t try to apply MC/DC to non-critical code—focus your resources where failure has the highest risk of harm.

### 4.2.3. Use Automated Tools for Testing and Coverage Analysis

Manual MC/DC testing can be resource-intensive for small projects. Use automated tools to streamline the process:

* **Unit Testing Tools:** Tools like **gcov**, **VectorCAST**, or other open-source/commercial tools can help analyze test coverage and identify gaps.
* **MC/DC Test Generation Tools:** Many tools generate missing test cases based on MC/DC requirements, saving time and effort. For example, these tools can generate variations of conditions not yet covered.

**Tip:** Choose affordable or open-source tools that work for your software development environment.

### 4.2.4. Plan MC/DC Testing in the Unit Test Phase

* Perform MC/DC early, during **unit testing.** Testing each software module in isolation helps identify issues before components are integrated into the larger system.
* Focus unit tests on exercising **every meaningful conditional path** within the code.
* Validate that all **decisions and conditions** in safety-critical components behave as expected under normal and abnormal (off-nominal) scenarios.

### 4.2.5. Keep It Simple: Only Test What Matters

* Avoid overcomplicating MC/DC testing. For example, unnecessary testing of straightforward, non-branching code wastes limited resources.
* Instead, prioritize testing where **decisions/conditions impact safety**, such as:
  + Sensor inputs (e.g., "If temperature > threshold, shut down system")
  + Actuator outputs (e.g., "If door is open, motor cannot engage")
  + Error-handling logic ("If condition X fails, transition to Safe State Y")

### 4.2.6. Document Your Coverage

Small projects must clearly demonstrate compliance with 100% MC/DC for safety-critical components. To do this:

* Keep simple coverage reports from tools showing all decision points, tested paths, and uncovered conditions.
* Document how missing test coverage was addressed (e.g., adding test cases).

**Tip:** Even a one-page summary of your tool-generated MC/DC results can suffice for small projects.

### 4.2.7 Tips for Managing Limited Resources

1. **Leverage Team Collaboration:**  
   Assign testing responsibilities to the developers most familiar with the safety-critical code. Peer reviews can help identify missed conditions.
2. **Test Incrementally:**  
   Don’t wait to test everything at the end. Break the software into manageable chunks and test modules (or components) as they are developed. This avoids last-minute time crunches.
3. **Reuse Tests:**  
   If some tests cover specific conditions or decisions, reuse those tests across similar modules instead of rewriting new ones for each case.
4. **Apply Judgment for Simpler Logic:**

   * Not every piece of safety-critical code will have complex decision logic. For example, a straight "if-else" block may already be adequately covered with fewer test cases.
   * Focus rigorous MC/DC efforts on **complex decision points.**

### 4.2.8 Quick MC/DC Sample Process for Small Projects

1. **Example Safety-Critical Code:**

```
if ((sensorReading > threshold) && (overrideSwitch == false)) {
    activateEmergencyBrake();
}
```

1. **What Do You Test for MC/DC?**  
   Test each **condition** and demonstrate its **independent effect**:

   * Test `sensorReading > threshold` as both `true` and `false`.
   * Test `overrideSwitch == false` as both `true` and `false`.
   * Show that changing each condition **independently** changes whether `activateEmergencyBrake()` is triggered.
2. **Result:**

   * 100% MC/DC coverage for this decision logic, with minimal effort.

### 4.2.9 Key Takeaways for Small Projects

* **Focus on Safety-Critical Components:** Limit MC/DC testing to code directly tied to hazardous operations.
* **Automate Whenever Possible:** Use tools to generate and validate test cases.
* **Start Early and Keep it Incremental:** Test as you develop, especially during unit testing.
* **Document and Track Progress:** Keep simple but clear records of your testing to show compliance with 100% MC/DC coverage.

By focusing resources strategically and keeping processes simple, small projects can achieve compliance with MC/DC requirements without unnecessary overhead.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
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
* (SWEREF-434)

  [MC/DC for Space - A new Approach to Ensure MC/DC Structural Coverage with Exclusively
  Open Source Tools](https://swehb.nasa.gov/download/attachments/16449661/MCDC_for_Space_DASIA_2021.pdf?api=v2 "Click to open in new window")

  Thomas Wucher, Andoni Arregui, 2021-10-07, ESA Software Product Assurance Workshop 2021, GTD GmbH
* (SWEREF-486)

  [10 gcov—a Test Coverage Program]( https://gcc.gnu.org/onlinedocs/gcc/Gcov.html "Click to open in new window")

  Offline Gcda Profile Processing Tool,  gcov is a tool you can use in conjunction with GCC to test code coverage in your programs.
* (SWEREF-603)

  [MCDC Coverage Video example.](https://www.youtube.com/watch?v=Cg1J-_ReKmM "Click to open in new window")

  Carnegie Mellon University course 18-642 updated Fall 2020, Koopman, Phil
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

See references 384, 393, 394, 395, 396, and 397 for tools related to MC/DC.

**Gcov [486](#_tabs-<p></p>)**is one tool that can be used to aid in MC/DC testing.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

NASA lessons learned highlight the importance of thorough testing practices, including **100 percent code test coverage**, using methodologies like **Modified Condition/Decision Coverage (MC/DC)** for safety-critical software. These lessons often stem from issues resulting from insufficient testing, untested code paths, or gaps in validation during critical missions. Below is a compilation of relevant NASA lessons learned associated with testing safety-critical software using rigorous methodologies such as the MC/DC criterion, particularly for **Requirement 3.7.4**:

### **Relevant NASA Lessons Learned**

#### **1. Lesson ID: 1281 – OrbView-3 Satellite Power System Failure**

**Summary:**  
The OrbView-3 satellite failure was partly attributed to the inadequate testing of all decision paths in software interfaces for power subsystems. Unanticipated scenarios and interactions revealed gaps in the code validation during dynamic testing.

**Relevance to 3.7.4:**

* **Lesson:** Ensuring **100 percent code test coverage** using **MC/DC** criterion would require testing all independent paths and decision conditions, enabling detection of issues in safety-critical components before deployment.
* **Impact:** Lack of coverage in critical systems significantly increases the chance of unvalidated conditions leading to mission failure.

#### **2. Lesson ID: 0839 – Mars Polar Lander Loss**

**Summary:**  
The Mars Polar Lander failed due to premature shutdown of the descent engines triggered by an untested software condition. Analysis showed that integrated testing failed to cover all decision paths or conditions related to software handling sensor inputs.

**Relevance to 3.7.4:**

* **Lesson:** Testing with **MC/DC** would have ensured every condition impacting the decision logic (sensor input states) was exercised and validated, preventing undetected errors.
* **Impact:** For safety-critical software, every decision condition must be tested to avoid unvalidated paths leading to catastrophic outcomes.

#### **3. Lesson ID: 2451 – Fault Management and Detection Software Challenges**

**Summary:**  
On multiple spacecraft, fault management systems encountered operational anomalies due to software decision logic failing in rare but critical run-time conditions that had not been covered by tests.

**Relevance to 3.7.4:**

* **Lesson:** **MC/DC** ensures that all conditions influencing a decision point are independently tested, reducing the likelihood that rare or edge-case faults in safety-critical software escape detection during testing.
* **Impact:** For safety-critical components, missing coverage on certain conditions can leave faults undetected, posing risks to the mission.

#### **4. Lesson ID: 2197 – Juno Spacecraft Software Challenges**

**Summary:**  
Juno faced post-launch issues in software related to spacecraft orientation and communications. Investigation revealed inadequate testing coverage of certain decision paths in the software logic responsible for handling unexpected operational states.

**Relevance to 3.7.4:**

* **Lesson:** Testing with **MC/DC** improves validation of software handling for unexpected states, ensuring all decision outcomes and conditions are exercised.
* **Impact:** For spacecraft operational software, missed coverage in complex decision trees can lead to incorrect handling of unanticipated states.

#### **5. Lesson ID: 0732 – Galileo Spacecraft Antenna Deployment Failure**

**Summary:**  
The Galileo spacecraft was unable to fully deploy its high-gain antenna, partially due to unexpected conditions in deployment logic that were not adequately tested during software validation. Some critical paths determining antenna feedback and control were missed.

**Relevance to 3.7.4:**

* **Lesson:** Using **MC/DC** testing would have ensured all logical conditions affecting deployment controls and feedback responses were thoroughly validated, improving reliability.
* **Impact:** For highly critical systems such as deployment controls, omitting condition coverage in testing leaves high-risk gaps in the reliability of the software.

#### **6. General Observation: Untested Code Paths in Safety-Critical Software**

**Summary:**  
NASA has identified multiple instances over decades where untested or insufficiently validated safety-critical software caused unexpected mission risks or failures. Common contributing factors include missed edge conditions or incomplete branching logic testing.

**Relevance to 3.7.4:**

* **Lesson:** **MC/DC** testing achieves **100 percent decision path validation**, ensuring that conditions influencing decisions are tested independently and comprehensively.
* **Impact:** This methodology strengthens confidence in the reliability of safety-critical software by exposing hidden defects and unvalidated logic paths.

### **Why NASA Emphasizes MC/DC in Safety-Critical Software**

**Modified Condition/Decision Coverage (MC/DC)** is a rigorous code coverage criterion required for software that controls and monitors high-consequence systems. NASA's requirement for 100 percent coverage using MC/DC for safety-critical software aligns with the following benefits derived from lessons learned:

1. **Identifying Hidden Software Defects**:

   * Ensures that every condition influencing a decision point is tested independently, uncovering defects that might remain hidden with less rigorous methods.
2. **Exercising All Logic Branches**:

   * Prevents defects from untested decision paths or conditions from propagating into operational settings where they could cause hazardous consequences.
3. **Compliance with Industry Standards**:

   * MC/DC is mandated by international safety-critical software standards such as **DO-178C (Software Considerations in Airborne Systems)**. NASA's adoption reflects its alignment with widely recognized best practices.

### **Impact of Lessons Learned on Software Testing**

From the lessons learned, it becomes evident that failing to achieve **100 percent test coverage using MC/DC** can leave critical decision paths unvalidated, increasing risks during real-world operations. Projects that successfully implement MC/DC testing achieve better reliability for software governance over safety-critical systems.

### **Key Takeaways**

From NASA lessons learned, the following practices are reinforced for **Requirement 3.7.4**:

1. **Enforce 100 Percent MC/DC Testing**:  
   Ensure that every condition and decision influencing safety-critical software components is tested to avoid gaps in coverage that can lead to catastrophic mission failures.
2. **Focus on Edge Conditions**:  
   Use MC/DC testing to validate software behavior in rare or edge-case scenarios, which might otherwise remain uncovered in functional testing.
3. **Early Integration of Rigorous Testing**:  
   Incorporate MC/DC into development and unit testing stages to reduce the cost and schedule pressures of debugging and retesting safety-critical software during later stages.

### **References**

* NASA Lessons Learned Database (<https://llis.nasa.gov/>).
* DO-178C (Software Considerations in Airborne Systems).
* NPR 7150.2 and NASA-STD-8739.8 Standards for Software Testing & Validation.
* NASA/TM−20205011566: Testing and Complexity Studies in Safety-Critical Systems.

These lessons reinforce the importance of **MC/DC** in fulfilling NASA’s mandatory requirements for safety-critical software and provide insights into the operational and testing challenges that can arise without proper test coverage.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Going Beyond the Formal Qualification Test (FQT) Scripts: Data Reduction/Automation](https://software.gsfc.nasa.gov/lesson-details/295/). **Lesson Number 295**: The recommendation states: "As early as feasible in the program (pre-FQT time frame), ascertain whether automated testing is planned for Software FQT and ensure that the vendor will provide all relevant test articles well in advance of test run-for-record (will likely require NASA Program Management buy in and support as well). Identify any calls to open up additional views to EGSE, Simulators, raw hex dumps, etc., that may be used to assist with data analysis/processing/reduction in the scripts. Request clarification on how data captured in those views will be used and have snapshots provided (or travel to vendor site) to fully understand verification extent. For automated testing, the Software Systems Engineer should evaluate whether the provider has allocated sufficient time and training to fully understand how the automated testing program will exercise and verify all required functions and behaviors. This lesson can also be applicable for Instrument Software, Simulator Software, and Ground System Software."
* [Remove Debug Settings and Code Prior to Benchmarking](https://software.gsfc.nasa.gov/lesson-details/338/). **Lesson Number 338**: The recommendation states: "Remove or disable debug code and settings before benchmarking to ensure that timing numbers are accurate."

# 7. Software Assurance

3.7.4 If a project has safety-critical software, the project manager shall ensure that there is 100 percent code test coverage using the Modified Condition/Decision Coverage (MC/DC) criterion for all identified safety-critical software components.Software assurance plays a critical role in confirming safety-critical software behavior. The structured approach outlined above ensures comprehensive test coverage, rigorous validation, and a strong alignment to safety standards. Incorporating MC/DC testing methodologies and tracking test metrics in a timely manner helps small and large projects alike meet their safety goals while controlling costs and risks. By addressing gaps proactively and ensuring risk assessments are in place, projects can minimize safety liabilities and demonstrate strict compliance with NASA and industry standards.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that 100% code test coverage is addressed for all identified safety-critical software components or that software developers provide a technically acceptable rationale or a risk assessment explaining why the test coverage is not possible or why the risk does not justify the cost of increasing coverage for the safety-critical code component.

## 7.2 Software Assurance Products.

#### **Core Requirements**

Software assurance (SA) provides independent analysis, oversight, and support to ensure that safety-critical software components meet the required safety, quality, and reliability standards. For this requirement, Software Assurance deliverables should include the following key products:

1. **Software Assurance or Software Engineering Status Reports:**

   * Regular status updates documenting the progress and compliance of safety-critical software with NASA standards.
   * Reports should include any deviations, open risks, and mitigation plans associated with identified software requirements.
2. **Software Design Analysis:**

   * Independent analysis of the software design to confirm adherence to safety requirements, including:
     + Logical integrity of safety-critical functions.
     + Proper isolation and partitioning of safety-critical and non-safety-critical elements.
     + Evaluation of design trade-offs based on the failure philosophy applied (e.g., fault tolerance, control path separation).
   * Ensure traceability between design elements and requirements.
3. **Software Test Analysis:**

   * Analyze test results to confirm that safety-critical software meets specified safety, performance, and reliability standards.
   * Verify that all test cases, including edge cases and off-nominal conditions, exercise the code to the required criteria, such as Modified Condition/Decision Coverage (MC/DC).
4. **Source Code Quality Analysis:**

   * Confirm adherence to coding standards, clarity, and proper implementation of safety-critical software.
   * Ensure code is free of defects (e.g., memory leaks, uninitialized variables) that could lead to unsafe behaviors.
   * Use automated tools to verify maintainability, readability, and compliance with industry standards.
5. **Evidence of Test Coverage, Complexity, and Safety Testing:**

   * Confirm that test code coverage meets the required 100% for safety-critical software components, as mandated by the Modified Condition/Decision Coverage (MC/DC) criterion.
   * Include validation results for complexity levels and the testing of support files that impact hazardous systems.
6. **Risk Assessment for Gaps:**

   * Perform a risk assessment for any untested safety-critical code, components, or requirements not met as part of the development process.
   * Document any software developer rationale for deviations or constraints (e.g., why 100% coverage could not be achieved) and provide an associated SA risk assessment.
7. **Validation of Hazardous Data, Rules, and Scripts:**

   * Confirm that **safety-critical loaded data, uplinked data, rules, and scripts** affecting hazardous system behavior are thoroughly tested.

## 7.3 Metrics

To maintain consistent oversight and ensure overall project quality, incorporate the following metrics for monitoring safety-critical software assurance activities:

1. **100% Code/Test Coverage Metrics:**

   * **Examples:**
     + Safety-critical software code/test coverage percentages (e.g., # of paths tested vs. total # of paths).
     + Test coverage data for specific safety-critical components.
     + Source Lines of Code (SLOC) tested vs. total SLOC written for safety-critical software.
2. **Test Coverage of Safety-Critical Components:**

   * **Focus:** Explicitly track testing progress and compliance for safety-critical elements to validate that no paths are left untested.
3. **Risk Trends:**

   * Track unresolved non-conformances over the life cycle and assess their implications for project safety.

**Note:** Metrics in **bold** are required for all projects, regardless of scope or size.

For additional insights, refer to **Topic 8.18 - SA Suggested Metrics.**

## 7.4 Guidance for Test Coverage and MC/DC

### 7.4.1 Test Coverage Analysis Process

Test coverage analysis requires two complementary steps to ensure requirements are fully met:

1. **Requirements-Based Test Analysis:**

   * Evaluate test cases to confirm that they satisfy all software requirements, especially safety-related requirements.
   * Ensure that test cases align with the specified criteria for safety-critical software.
2. **Structural Coverage Analysis:**

   * Confirm that all code structure (pathways, conditions, decisions) is exercised as required by the appropriate coverage standard, such as MC/DC.
   * Integrate structural analysis findings into iterative design and testing cycles to address gaps early in development.

### 7.4.2 Modified Condition/Decision Coverage (MC/DC)

* MC/DC is the **most stringent and appropriate level of testing for safety-critical software** and is preferred due to its balance between effectiveness and test-case generation effort. It ensures that each condition in a decision independently affects the outcome of the decision.

##### **7.4.3 Key Testing Requirements for MC/DC:**

1. **Invoke All Entry and Exit Points:** All paths leading into and out of logic blocks must be exercised.
2. **Test Every Decision Outcome:** Ensure all decisions (e.g., IF, CASE statements) take both true and false outcomes.
3. **Test Every Condition Outcome:** Validate that every condition within a decision is tested for true and false outcomes.
4. **Independent Condition Impact:** Demonstrate that each condition impacts the decision outcome independently under varied permutations.

---

##### **7.4.4 Why MC/DC Is Important:**

1. **Focus on Critical Software Logic:** It prioritizes testing complex conditional logic where most bugs/errors occur.
2. **Error Detection Efficiency:** Ensures a high probability of detecting subtle defects without requiring exhaustive test-case combinations.
3. **High Safety and Industry Acceptance:** MC/DC is widely adopted in domains requiring extreme reliability (e.g., DO-178C for avionics, ISO 26262 for automotive safety).

---

#### **7.4.5 Untested Code Considerations**

* **Complete test coverage** is non-negotiable for safety-critical code. Untested code introduces unacceptable risk in hazardous operational conditions.
* If achieving 100% coverage is deemed impossible, developers must:
  + Clearly document the gap and provide a compelling justification.
  + Conduct and submit an SA risk assessment to evaluate the impact, mitigation options, and hazard acceptance.
  + Open discussions to determine how safety can be assured via alternative methods (e.g., defensive design or fault tolerance).

---

### **7.4.6 Additional Guidance for Small Projects**

* **Early Planning:** Small projects should integrate testing (including MC/DC) early to avoid rework and missed milestones. Iterative testing at the unit level avoids last-minute, resource-intensive efforts.
* **Automated Testing Tools:** Use affordable or open-source automation tools like **gcov** for MC/DC analysis to reduce costs.
* **Focus on Simplicity:** Small projects should focus MC/DC testing on the most critical logic paths and decision points directly tied to hazardous operations.

## 7.5 Additional Guidance

See also Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis), 

Additional information can be found in NASA/TM−20205011566, NESC-RP-20-01515, Cyclomatic Complexity, and Basis Path Testing Study [377](#_tabs-<p></p>)

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [7.21 - Multi-condition Software Requirements](/spaces/SWEHBVD/pages/102695692/7.21+-+Multi-condition+Software+Requirements) * [7.23 - Software Fault Prevention and Tolerance](/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance) * [8.08 - COTS Software Safety Considerations](/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

# 8. Objective Evidence

To meet this requirement, the project must verify that all safety-critical software components have been tested with 100% code coverage, or provide justified documentation explaining why full coverage was not achieved and whether the identified risk is acceptable in the context of cost versus benefit analysis.

Definition of objective evidence

Objective evidence is an unbiased, documented fact showing that an activity was confirmed or performed by the software assurance/safety person(s). The evidence for confirmation of the activity can take any number of different forms, depending on the activity in the task. Examples are:

* Observations, findings, issues, risks found by the SA/safety person and may be expressed in an audit or checklist record, email, memo or entry into a tracking system (e.g. Risk Log).
* Meeting minutes with attendance lists or SA meeting notes or assessments of the activities and recorded in the project repository.
* Status report, email or memo containing statements that confirmation has been performed with date (a checklist of confirmations could be used to record when each confirmation has been done!).
* Signatures on SA reviewed or witnessed products or activities, or
* Status report, email or memo containing a short summary of information gained by performing the activity. Some examples of using a “short summary” as objective evidence of a confirmation are:
  + To confirm that: “IV&V Program Execution exists”, the summary might be: IV&V Plan is in draft state. It is expected to be complete by (some date).
  + To confirm that: “Traceability between software requirements and hazards with SW contributions exists”, the summary might be x% of the hazards with software contributions are traced to the requirements.
* The specific products listed in the Introduction of 8.16 are also objective evidence as well as the examples listed above.

By providing the outlined objective evidence, the project demonstrates compliance with the requirement to achieve 100% test coverage for safety-critical software components or provide a justified risk-based rationale for coverage gaps. These records offer a clear and defensible trail of testing practices, decision-making, and oversight necessary for safety-critical software assurance.

Below is a comprehensive list of possible objective evidence:

## 8.1 Categories of Objective Evidence

### 8.1.1 Code Coverage Analysis Report

* A complete report showing achieved code coverage results (e.g., via tools such as GCov, Bullseye, JaCoCo, VectorCAST). These reports confirm which portions of the code have been executed under test.

##### **Must Include**:

* Documentation of **code coverage level (%)** attained for each safety-critical software component.
* Detailed breakdown of:
  + Function coverage: Percent of functions exercised during testing (e.g., 100% = all functions tested).
  + Statement (line) coverage: Percent of individual statements exercised during testing.
  + Condition coverage (branch or decision coverage): Percent of decision outcomes (e.g., `if` or `for` branches) executed.
* Total summary showing whether **100% coverage** was achieved.

##### **Examples of Evidence**:

* **Code Coverage Reports**:
  + Example excerpt: "Safety-critical module `navigation.cpp` achieved 100% line coverage, branch coverage, and function coverage using test suite SC-Tests v1.3."
  + Tool-generated coverage maps highlighting tested and untested lines/branches.
  + Coverage metrics tied directly to software requirements.

### 8.1.2 Traceability Matrix of Coverage to Requirements

* A Requirements Traceability Matrix (RTM) ensures that all safety-critical software requirements have corresponding test cases and have been fully executed. The matrix provides proof of test coverage in the context of functional, structural, and safety-critical requirements.

##### **Must Include**:

* Traceability from:
  + Safety-critical software requirements → Code → Test cases.
* Evidence that all lines of code contributing to specific safety-critical requirements are exercised by test cases.
* Mapping of untested code snippets with justifications/risk assessments where applicable.

##### **Examples of Evidence**:

* **RTM Example Excerpt**:

  | **Requirement ID** | **Code Component** | **Test Case ID** | **Coverage** | **Result** |
  | --- | --- | --- | --- | --- |
  | SC-REQ-005 | Safety\_Init.cpp | TC-Init-001 | 100% | Passed |
  | SC-REQ-012 | FaultRecovery.cpp | TC-FR-101 | 95% | See RA-003 |

### 8.1.3 Test Plans and Test Case Execution Logs

* Test plans and execution logs demonstrate that a comprehensive set of test cases has been executed to verify and validate the software's functionality in both nominal and off-nominal conditions.

##### **Must Include**:

* **Test Plan**:
  + Description of all tests performed, including unit, integration, system, and regression tests.
  + Identification of test cases specific to safety-critical components.
  + Inclusion of structural code coverage testing tools and methodologies.
* **Execution Logs**:
  + Evidence that test cases were executed and criteria were met.
  + Proof that test conditions exercised all anticipated use cases and failure scenarios.

##### **Examples of Evidence**:

* **Test Execution Log Snapshot**:
  + Test Case: TC-MotionInit-001
  + Code coverage post-test: 100% line, 100% branch.
  + Status: Passed.
  + Notes: Code for exception handling tested by fault injection.

### 8.1.4 Coverage Gap Analysis and Risk Assessment Reports (if test coverage < 100%)

* If 100% code coverage is not achieved, a clear explanation and risk justification for untested code areas must be provided. This explanation may argue technical infeasibility, low-risk impact, or cost-prohibitive conditions that outweigh the risk.

##### **Must Include**:

* Documentation explaining why certain lines, branches, or functions cannot be tested.
  + Example: “This section of code cannot be tested due to hardware simulation limitations.”
* A **Formal Risk Assessment** that evaluates:
  + **Likelihood of failure** in the untested code.
  + Consequences of a failure in mission/safety-critical scenarios.
  + Mitigation measures undertaken to reduce the associated risks (e.g., redundancy, alternative validation techniques).
* Report signed off by Software Safety and Assurance (SMA) authorities approving the rationale.

##### **Examples of Evidence**:

* **Coverage Gap & Risk Report Example**:
  + "Rationale: Line 245-255 of `Navigation.cpp` is unreachable under standard test environments. Risk is mitigated by redundant checks in FlightControl.cpp. Assessment indicates negligible risk to mission performance. SMA concurrence logged under CR-20-115."

### 8.1.5 Independent Verification and Validation (IV&V) Reports

* Independent verification and validation reports provide an objective third-party review assessing test coverage levels and ensuring that justifications for partial coverage are technically sound and acceptable.

##### **Must Include**:

* Independent evaluation of code coverage results, test cases, and testing methods.
* Evidence of fault injection testing to complement standard testing for hard-to-reach code.
* Acceptance/concurrence by the safety board for deviations from 100% coverage.

##### **Examples of Evidence**:

* **IV&V Approval Letters**:
  + Example: "IV&V assessment confirms 96.5% coverage achieved for safety-critical component FaultHandler.cpp. Remaining gaps are explained and mitigated as per Gap Report GR-25. Approval granted for code deployment."

### 8.1.6 Fault Injection and Stress Testing Evidence for Untested Code Functionality

* Evidence of alternative testing methods, such as fault injection or stress testing, used in cases where 100% coverage could not be achieved. These techniques increase confidence in untested code.

##### **Must Include**:

* Records of fault injection and related alternative validation approaches.
* Analysis showing that untested parts of the code would not result in undetected hazards during off-nominal operations.

##### **Examples of Evidence**:

* **Fault Injection Test Report Example**:
  + "Memory corruption tests in untested code segment of FaultHandler.cpp showed no propagation under fault conditions. Mitigation plan verified through redundant integrity checks."

### 8.1.7 SMA Concurrence or Waiver for Unachieved Coverage

* Formal record of SMA’s involvement in the decision-making process for allowing deviations from 100% coverage.

##### **Must Include**:

* Approved waiver or concurrence letter with signatures from appropriate technical authorities or SMA leads.

##### **Examples of Evidence**:

* **SMA Concurrence**:
  + "SMA has reviewed the rationale for untested portions of software SafetyMonitor.cpp and concludes that the residual risk is acceptable. Approved under waiver WVR-10-208."

### 8.1.8 Summary of Objective Evidence

| **Type of Evidence** | **Examples of Objective Evidence** |
| --- | --- |
| **Code Coverage Reports** | Tool-generated reports demonstrating % coverage for all safety-critical components. |
| **Traceability Matrix** | RTM mapping software requirements to test coverage and explaining coverage gaps. |
| **Test Plans and Execution Logs** | Logs detailing executed test cases and resulting coverage percentages. |
| **Coverage Gap and Risk Justifications** | Rationale and formal risk assessments for untested code sections. |
| **IV&V Reports** | Third-party verification approval of code coverage results or acceptable coverage gaps. |
| **Fault Injection Test Results** | Validation of untested code paths through fault injection and robustness testing. |
| **SMA Concurrence or Waivers** | Signed approval from SMA and other technical authorities for deviations from 100% coverage. |
