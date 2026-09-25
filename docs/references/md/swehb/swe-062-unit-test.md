# SWE-062 - Unit Test

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695446. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test

SWE-062 - Unit Test

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695446)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695446&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. The Requirement](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)
* [7. Software Assurance](#tabs-7)
* [8. Objective Evidence](#tabs-8)

# 1. Requirements

4.4.5 The project manager shall unit test the software code.

## 1.1 Notes

For safety-critical software, the unit testing should follow the requirement established in 3.7.4 of this document.

## 1.2 History

Click here to view the history of this requirement: SWE-062 History

SWE-062 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A | 3.3.4 The project shall ensure that the software code is unit tested per the plans for software testing. |
| Difference between A and B | No change |
| B | 4.4.5 The project manager shall unit test the software code per the plans for software testing. |
| Difference between B and C | Removed "per the plans for software testing". |
| C | 4.4.5 The project manager shall unit test the software code. |
| Difference between C and D | No change |
| D | 4.4.5 The project manager shall unit test the software code. |

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
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |

# 2. Rationale

Unit testing is the process of testing the range of inputs to a unit to ensure that only the intended outputs are produced. By doing this at the lowest level, fewer issues will be discovered when the components are later integrated and tested as a whole. Therefore, during unit testing, it is important to check the maximum and minimum values, invalid values, empty and corrupt data, etc. for each input and output to ensure the unit properly handles the data (processes or rejects it).

Unit testing can be described as the confirmation that the unit performs the capability assigned to it, correctly interfaces with other units and data, and represents a faithful implementation of the unit design.

Ensuring that developers perform unit testing following written test plans helps build quality into the software from the beginning and allows bugs to be corrected early in the project life cycle when such corrections cost the least to the project.

1. **Accountability for Quality**  
   Unit testing by the project manager ensures that there is an added layer of accountability for code quality. The project manager, being deeply familiar with the project's requirements and goals, has greater insight into how the software needs to function. This direct involvement helps ensure that the code aligns with the overall project vision and meets quality standards.
2. **Early Defect Detection**  
   Unit testing is a critical step in identifying and addressing defects early in the development lifecycle. By conducting unit tests, the project manager can catch errors before they propagate to later stages, thus avoiding costly rework and ensuring smoother integration and final testing phases.
3. **Deep Understanding of Code Functionality**  
   Involving the project manager in unit testing provides them with a deeper understanding of how the software functions at the technical level. This knowledge enables them to make better decisions regarding project planning, risk assessment, and resource allocation, as they have firsthand information about the code performance and its limitations.
4. **Ensuring Adherence to Requirements**  
   Unit testing by the project manager helps verify that the implemented code properly aligns with the specified requirements. As the project manager generally oversees the requirements definition process, their involvement in unit testing provides continuity and helps ensure that the implementation delivers the intended functionality without deviation.
5. **Promoting Team Collaboration**  
   When the project manager is actively involved in technical processes like unit testing, it fosters collaborative teamwork by bridging the gap between management and development. This involvement demonstrates leadership by example, encouraging developers to prioritize quality assurance and take ownership of their work.
6. **Enhanced Risk Management**  
   The project manager’s engagement in unit testing allows them to identify technical risks early. By understanding potential vulnerabilities or bottlenecks in the code, they can proactively mitigate risks, ensuring the project stays on schedule and avoiding surprises during later stages of development.
7. **Improved Communication Between Stakeholders**  
   Since the project manager connects developers, business stakeholders, and clients, their firsthand experience with the code through unit testing allows them to communicate technical details more effectively. This enhances transparency in progress tracking and fosters trust among all stakeholders.
8. **Validation of Developer Work**  
   Unit testing by the project manager ensures developers are held to a high standard of quality. It also acts as an independent check on the accuracy and reliability of the code, ensuring that the software meets the project's success criteria without relying solely on developer assessments.
9. **Supporting Agile Development Processes**  
   In agile frameworks, iterative cycles require continuous testing and validation. By participating in unit testing, the project manager contributes to this agile practice, ensuring quick feedback on code quality and functional alignment during each iteration.
10. **Cross-Skilling and Role Versatility**  
    Encouraging project managers to unit test software code develops their technical skillset, enhancing their domain knowledge and versatility. This can prove valuable, especially in smaller teams or organizations where roles and responsibilities need to be fluid.

### Caveat: Role Appropriateness

While there is merit to this requirement, it assumes the software development team possesses the necessary technical competence to unit test software code. If this skillset is not part of their expertise, the requirement may need revision to ensure alignment with both capability and role appropriateness.

# 3. Guidance

## 3.1 Unit Test

Unit testing is a fundamental step in ensuring the quality, reliability, and correctness of individual software components. To accomplish this, the following enhanced guidance is provided:

1. **Repeatability of Unit Test Results**  
   The project manager shall ensure that unit test results are **repeatable**. Repeatability means that the same test conditions produce identical results upon re-execution, ensuring consistency and confidence in the reliability of the test process. See [SWE-186 - Unit Test Repeatability](https://chat.nasa.gov/chats).
2. **Safety-Critical Code Coverage Requirements**  
   For safety-critical software, unit tests must include **Modified Condition/Decision Coverage (MC/DC)**. This ensures high coverage of decision-making logic in the code, which is critical for verifying the correctness of safety features. See [SWE-219 - Code Coverage for Safety-Critical Software](https://chat.nasa.gov/chats).
3. **Definition of a "Unit"**  
   According to IEEE Std 610.12-1990, IEEE Standard Glossary of Software Engineering Terminology, a "unit" is defined as:

   * **A separately testable element** specified in the design of a computer software component.
   * **A logically separable part** of a computer program.
   * **A software component** that is not subdivided into other components.
4. **Developer-Driven Insight for Unit Testing**  
   Given the low-level nature of a unit, **the developer who created it is the best suited to fully test it**. Developers have full insight into the code under test, allowing them to anticipate edge cases, errors, and off-nominal behaviors that the unit may encounter in production. Unit tests should include:

   * **Off-nominal conditions** (unexpected or erroneous inputs).
   * **Error handling and robustness tests.**
   * Tests that verify behavior **beyond basic requirements** to ensure comprehensive validation of code.  
     See [Topic 8.01 - Off-Nominal Testing](https://chat.nasa.gov/chats) and [Topic 7.06 - Software Test Estimation and Testing Levels](https://chat.nasa.gov/chats).

---

## 3.2 Prepare for Unit Testing

Before executing unit tests, projects must ensure proper preparation, including environmental setup, resource availability, and personnel training. The following are key steps:

1. **Test Environment and Materials**  
   Ensure the unit test environment accurately replicates the expected operational inputs, outputs, and stimuli the code will experience. Note known differences between the unit test environment and the actual target environment, as these may impact results and need to be factored into assessments.
2. **Test Planning and Execution**  
   Unit tests should be executed according to an approved schedule ([SWE-016 - Software Schedule](https://chat.nasa.gov/chats)) and documented test plans ([5.10 - STP - Software Test Plan](https://chat.nasa.gov/chats)). Monitoring must occur in line with the project’s software assurance plan. Key practices include:

   * **Predefined Criteria:** Success criteria must be established prior to executing tests.
   * **Weakness Identification:** Capture gaps between test and operational environments to ensure validity of results.
3. **Unit Test Result Management**  
   The following activities are critical for managing test results:

   * Capturing unit test results systematically.
   * Documenting issues discovered during testing. Minor issues (e.g., typos) may be corrected without documentation if approved project protocols allow.
   * Correcting identified issues, including:
     + **Faults in code.**
     + **Errors in test instruments** (e.g., scripts, data, procedures).
     + **Defects in testing tools** (e.g., configuration or setup).
   * Recording corrections to support root cause analysis and improve test processes.
4. **Independent Evaluation**  
   Where feasible, results should be reviewed by personnel other than the tester to validate outcomes. Document evaluations as evidence of test confirmation.
5. **Assets for Regression Testing**  
   Capture all unit test artifacts for reuse in regression testing, including:

   * Test cases, procedures, scripts, data, test stubs, and test drivers.
   * Developer notes or observations during testing.
6. **Objective Evidence and Documentation**  
   Document test pass evidence and ensure objective proof of testing activities is included in the Software Development Folders (SDFs) or equivalent repositories. Relevant documentation includes:

   * Tester notes.
   * Test result evaluations.
   * Problem reports and resolutions.
   * Comparison of test outcomes with documented plans.  
     Documented evidence ensures compliance with project standards (e.g., [5.08 - SDP-SMP - Software Development-Management Plan](https://chat.nasa.gov/chats), [5.06 - SCMP - Software Configuration Management Plan](https://chat.nasa.gov/chats)).
7. **Metrics Collection**  
   Define and collect appropriate metrics (e.g., coverage statistics, defect rates) that provide insights into unit test effectiveness and quality, and align metrics with project goals.

---

#### **Unit Test Verification**

Verification of unit testing is vital to ensure completeness. Software assurance or Independent Verification and Validation (IV&V) personnel must verify that unit tests adequately test the software and are properly executed. For less formal verification needs, a designated project member (e.g., team lead) may verify completeness by:

* Comparing test results against the Software Test Plan.
* Confirming metrics such as logic path coverage and test accuracy.

---

#### **Unit Testing Types: Automated vs Manual**

1. **Automated Unit Tests**  
   Automated unit tests are preferred as they can be integrated into a regression suite for continuous testing. These tests ensure scalability and repeatability, which are especially useful for large or frequently changing projects.
2. **Manual Unit Tests**  
   Manual unit testing may sometimes be necessary for scenarios where automation tools cannot completely exercise specific code behaviors. These tests require developers to write and execute test cases manually, emphasizing edge cases or areas requiring deeper scrutiny.

---

#### **Integration with Continuous Integration/Deployment (CI/CD)**

In projects employing CI/CD pipelines, all unit tests must be rerun each time code is updated. This ensures that only fully functional code is integrated, maintaining project stability. See [SWE-066 - Perform Testing](https://chat.nasa.gov/chats).

---

#### **Supporting Safety-Critical Software Reviews**

Per NASA-GB-8719.13, NASA Software Safety Guidebook, unit test documentation provides critical evidence for reviews of safety-critical software. Adequate safety testing must be demonstrated through thorough documentation of the testing process, results, metrics, and corrections. Unit test results play a pivotal role in maintaining compliance and supporting project safety objectives.

---

#### **Key References**

* [NASA-GB-8719.13 - NASA Software Safety Guidebook](https://chat.nasa.gov/chats).
* [SWE-191 - Software Regression Testing](https://chat.nasa.gov/chats).
* Proper documentation ensures traceability and continuity, supporting long-term project goals and compliance.

Per IEEE Std 610.12-1990 [222](#_tabs-<p></p>), IEEE Standard Glossary of Software Engineering Terminology, a "unit" is defined as:

1. A separately testable element specified in the design of a computer software component.
2. A logically separable part of a computer program.
3. A software component that is not subdivided into other components.

Given the low-level nature of a unit of code, the person most able to fully test that unit is the developer who created it. Unit tests should be accomplished with full insight into the code under test and include off-nominal and error tests.  Unit tests should test more than just the requirements of the unit of code. See also Topic [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing), [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels).

Make sure evidence of all test passes is captured.

See also [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing),

See also [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software), [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access), [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage)

Consult Center PALs for Center-specific guidance and resources related to unit testing.

## 3.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)       * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

# 4. Small Projects

For small projects with limited budgets, resources, or personnel, unit testing can be approached in a more streamlined and less formal manner while still ensuring quality and compliance with project objectives. The following refined guidance outlines how smaller projects can adapt unit testing processes effectively and efficiently.

---

#### **1. Simplified Unit Testing Approach**

Small projects may opt for leaner processes to conduct unit testing that align with available resources. However, it is critical to maintain the core principles of unit testing, including repeatability, coverage, and documentation. Key steps include:

1. **Automation Where Possible**: Use lightweight automation tools that are affordable or open-source to reduce manual testing efforts and improve test repeatability.
2. **Scope Tests Strategically**: Concentrate on testing critical and high-risk portions of the code to make the best use of limited resources. Identify areas where failure would have the greatest impact, such as safety-critical functions, major algorithms, or key interfaces.

---

#### **2. Test Plans with Essential Details**

Even in a resource-limited environment, software test plans for unit testing must include the following essential elements:

1. **Test Environment and Setup**: Clearly describe the environment used for testing (e.g., platforms, tools, configurations). If the environment is limited, document any gaps between the test setup and the actual operational environment.
2. **Captured Results**: Record the following information at a minimum:
   * Test case inputs.
   * Expected vs. actual outputs.
   * Observations on pass/fail status.
3. **Streamlined Documentation Procedures**: Adopt simple formats for documentation, such as checklists, spreadsheets, or templated logs, to document test cases, results, and issues. Avoid unnecessary complexity.
4. **Compliance Checks**: Ensure test activities adhere to the documented test plan. Conduct a basic compliance check by comparing executed procedures against the planned approach.

---

#### **3. Tailored Procedures and Tools**

Some NASA Centers or organizations may provide tailored "lean" unit test procedures and lightweight tools designed for small projects. These can simplify the testing process and align with resource constraints. If available, small projects are encouraged to use these resources. Examples include:

1. **Minimalist Testing Frameworks**: Open-source or in-house frameworks that require minimal setup and knowledge to execute tests.
2. **Predefined Scripts**: Simplified, reusable scripts for common types of unit tests that can be customized to fit project needs.
3. **Lightweight Test Tracking Tools**: Simple tools or spreadsheets designed for smaller projects to track testing artifacts and results without complex software.

---

#### **4. Small Project Considerations**

When tailoring unit testing for small projects, ensure efforts focus on delivering reliable and functional software while minimizing overhead. Practical considerations include:

1. **Risk-Based Testing**: For smaller projects, prioritize unit tests based on risk, ensuring the most critical code areas receive the necessary test coverage.
2. **Leverage Developer Knowledge**: Developers can often wear multiple hats in small projects. Allow developers to perform both code implementation and unit testing, while implementing peer reviews or lightweight verification by another team member to ensure impartiality.
3. **Automated Regression Tests**: Use automation for unit tests whenever possible so tests can be quickly rerun after code changes, avoiding the need for repeated manual effort.

---

#### **5. Documentation and Compliance**

While the documentation requirements for smaller projects can be reduced in scope and complexity, the following must still be captured to ensure compliance with testing standards:

1. **Test Environment**: Document minimal details about the test setup, including platform, configurations, inputs, and outputs.
2. **Captured Results and Defects**: Record all test results (including pass/fail status) and any defects identified during testing.
3. **Test Procedure Compliance**: Verify that all listed test procedures were executed as planned; deviations should be documented for traceability.

---

#### **6. Benefits of Lean Unit Testing for Small Projects**

A resource-sensitive approach to unit testing provides the following advantages to small projects:

* **Cost Efficiency**: Reduces overhead without compromising test quality.
* **Focus on Critical Areas**: Enables prioritization of testing for components with the highest risk or value.
* **Scalability**: Allows small projects to adopt processes that can scale with future resource increases.
* **Flexibility**: Supports iterative or agile methods often used by smaller teams.

---

#### **7. Continuous Improvement**

Even in small projects, it is essential to iterate and improve upon unit testing practices. Collect feedback about the testing process and use lessons learned to streamline further or increase the effectiveness of testing in future iterations.

---

By adopting lean principles and tailoring procedures to fit the constraints of smaller projects, teams can still maintain the integrity, reliability, and safety of the software while optimizing their limited resources. Use provided tools and templates wherever available to streamline documentation, and ensure test plans remain robust yet efficient enough to meet project needs effectively.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-013) "Code and Unit Test,"  HOU-EGP-310, Boeing, 2002. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-031)

  [Manager's Handbook for Software Development,](http://www.everyspec.com/NASA/NASA-General/SEL-84-101_REV-1_1990_30283/ "Click to open in new window")

  SEL-84-101, Revision 1, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1990.
* (SWEREF-047)

  ["Recommended Approach to Software Development,"](http://everyspec.com/NASA/NASA-GSFC/GSFC-General/SEL-81-305_REV-3_2419/ "Click to open in new window")

  SEL-81-305, Revision 3, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1992.
* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.
* (SWEREF-220)

  [IEEE Computer Society, "IEEE Standard for Software Unit Testing", IEEE STD 1008-1987, 1987.](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=27763 "Click to open in new window")

  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-222)

  [IEEE Computer Society, "IEEE Standard Glossary of Software Engineering Terminology,"](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=2238 "Click to open in new window")

  IEEE STD 610.12-1990, 1990. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-452) SED Unit Test Guideline,  580-GL-062-02, Systems Engineering Division, NASA Goddard Space Flight Center (GSFC), 2012.  This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook. Replaces SWEREF-081
* (SWEREF-530)

  [MPL Uplink Loss Timer Software/Test Errors (1998)](https://llis.nasa.gov/lesson/939 "Click to open in new window")

  Public Lessons Learned Entry: 939.
* (SWEREF-533)

  [Computer Software/Configuration Control/Verification and Validation (V&V)](https://llis.nasa.gov/lesson/1023 "Click to open in new window")

  Public Lessons Learned Entry: 1023.
* (SWEREF-695)

  [Goddard Space Flight Center (GSFC) Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned "Click to open in new window")

  The NASA GSFC Lessons Learned system. Lessons submitted to this repository by NASA/GSFC software projects personnel are reviewed by a Software Engineering Division review board. These Lessons are only available to NASA personnel.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

## 6.1 NASA Lessons Learned

The **NASA Lessons Learned database** provides important insights related to this requirement, emphasizing key practices for unit testing based on real-world experiences. Below are the lessons directly linked to the need for thorough and effective unit testing:

---

#### **1. MPL Uplink Loss Timer Software/Test Errors (1998)**

* **Lesson Number**: 0939
* **Summary**: Issues occurred in the Mars Polar Lander mission due to insufficient testing of software parameters. Logic errors went undetected because testing did not cover the full operational range of parameters. This underscores the importance of comprehensive unit and integration testing.
* **Lesson**: Unit and integration testing should, at a **minimum**, test against the full range of operational parameters. Specifically:
  + When database parameters that influence logic decisions are modified, the **logic needs to be retested** to verify correctness.
  + Changes to critical parameters can have cascading effects that may not be apparent without exhaustive testing.
* **Relevance to Unit Testing Requirement**:
  + Comprehensive unit testing, including **off-nominal cases and the entire range** of input parameters, is required to prevent unnoticed logic errors.
  + Retesting after changes ensures that modifications do not introduce unforeseen defects, maintaining system reliability.

---

#### **2. Computer Software/Configuration Control/Verification and Validation (V&V)**

* **Lesson Number**: 1023
* **Summary**: The use of the Matrix X auto-code generator in the development of ISS software revealed significant issues stemming from a lack of unit-level verification and validation (V&V). Problems arose when the auto-generated code and the auto-code generator itself were not subjected to appropriate configuration control or unit-level testing and V&V.
* **Lesson**:
  + **Unit-level V&V is critical even for auto-generated code.** Code generated by auto-code tools (e.g., Matrix X) must be rigorously tested to detect potential defects introduced by the auto-coding process.
  + Effective **configuration control** of both the auto-code generator and its outputs is essential to ensure consistency.
  + Hand-modification of auto-generated code can exacerbate issues if not properly tested and controlled.
* **Relevance to Unit Testing Requirement**:
  + Emphasizes the need for **unit-level testing** as a key part of the V&V process for all code, including auto-generated code.
  + Highlights the importance of testing the integrity of code outputs, particularly when auto-code is modified by hand.
  + Supports the practice of establishing configuration control measures to ensure alignment between the auto-coder, generated code, and any subsequent adjustments.

---

#### **3. Software Validation Practices (General Lessons from NASA Missions)**

* While not explicitly included as a formal lesson in the database, additional well-documented NASA experiences highlight recurring challenges and practices:
  + **Incremental Validation**: Ensure tests are performed incrementally (e.g., unit, integration, and system testing phases) to isolate and resolve defects early.
  + **Regression Testing Discipline**: When code changes are introduced—whether manually or via auto-code generators—unit tests must be rerun to confirm there is no regression in functionality.
  + **Boundary and Edge Cases**: Unit tests must specifically test edge cases and boundary conditions (both nominal and off-nominal), particularly in safety-critical systems.

---

### Key Takeaways for Unit Testing Practices

Based on the lessons learned, the following recommendations emerge for projects implementing unit testing:

1. **Thorough Testing Against Full Input Range**:
   * Include **exhaustive coverage** of all operational parameters, boundary values, and corner cases. Test inputs that fall within expected ranges, along with inputs that aim to stress the limits or break the behavior of the unit's logic.
2. **Retesting After Changes**:
   * Any modifications to code, dependent parameters, or database configurations must trigger **re-execution of unit tests** to validate the impact.
3. **Auto-Code Validation and Control**:
   * Treat **auto-generated code** as carefully as manually written code, ensuring that robust unit testing practices, configuration control, and documentation requirements apply equally.
   * Avoid untested manual modifications of auto-generated code. If modifications are necessary, they must be validated with updated test procedures.
4. **Verification and Validation (V&V)**:
   * Establish clear V&V processes that incorporate **unit testing as a foundational element** to verify functionality, correctness, and reliability at the component level.
5. **Configuration Control**:
   * Maintain **configuration management** practices to track changes in tools, code versions, and test artifacts. Ensure alignment between the **code under test** and the **test environment**.

---

### Applicability of NASA Lessons to This Requirement

The lessons learned from NASA missions reinforce the need for rigorous, repeatable, and well-documented unit testing practices. By implementing these lessons:

* Projects can reduce the risk of software errors propagating to later stages of development or operations.
* Software, particularly safety-critical and auto-generated code, will meet both functional and reliability requirements.
* Testing efforts can focus on preventing historical issues that have led to failures in previous missions, ensuring higher quality and overall mission success.

By applying these lessons, the unit testing process remains aligned with best practices while accounting for operational, environmental, and safety-critical challenges.

## 6.2 Other Lessons Learned

The Goddard Space Flight Center (GSFC) [Lessons Learned online repository](https://software.gsfc.nasa.gov/LessonsLearned) [695](#_tabs-<p></p>) contains the following lessons learned related to software requirements identification, development, documentation, approval, and maintenance based on analysis of customer and other stakeholder requirements and the operational concepts. Select the titled link below to access the specific Lessons Learned:

* [Run static analysis on code developed for unit test](https://software.gsfc.nasa.gov/lesson-details/217/). **Lesson Number 217**: The recommendation states: "Static analysis tools should be run not only on flight code (or production code in non-flight cases), but also on code developed for unit test. The issues identified for all code should be properly dispositioned and resolved."

# 7. Software Assurance

**SWE-062 - Unit Test**

4.4.5 The project manager shall unit test the software code.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project successfully executes the required unit tests, particularly those testing safety-critical functions.

2. Confirm that the project addresses or otherwise tracks to closure errors, defects, or problem reports found during unit testing.

## 7.2 Software Assurance Products

Software assurance (SA) activities help ensure software quality, reliability, and compliance by verifying that unit testing is thorough, repeatable, and aligns with project objectives. The following artifacts are expected as part of the software assurance process:

* **Unit Test Results**: Verified and documented evidence demonstrating that unit tests were successfully executed against the defined criteria and captured any failures or anomalies.
* **Software Problem or Defect Reports**: Details of findings and issues identified during unit testing, including root causes, corresponding corrective actions, and status updates.
* **Test Validation Records**: Records showing that software assurance personnel confirmed the integrity and repeatability of unit tests, particularly for safety-critical components.

While currently no other specific software assurance products are required, projects should consider adapting additional evidence or documentation needs as appropriate for their scope and criticality.

---

## 7.3 Metrics

To monitor the effectiveness and coverage of unit testing, software assurance should track the following metrics. These metrics will provide insights into project progress and quality and identify potential risks or areas requiring additional focus.

**Unit Test Execution and Completeness**

* **# of Planned Unit Test Cases vs. # of Actual Unit Test Cases Completed**: Helps determine whether all planned tests are executed on schedule.
* **# of Tests Completed vs. Total # of Tests**: Provides visibility into the progress of testing activities.
* **# of Tests Executed vs. # of Tests Completed**: Tracks the execution of test cases and identifies unfinished or incomplete tests.

**Defect and Non-Conformance Tracking**

* **# of Software Work Product Non-Conformances Identified by Phase over Time**: Tracks trends in defects across life cycle phases.
* **# of Non-Conformances Identified During Each Testing Phase** (e.g., Open, Closed, Severity): Monitors defect counts and resolution status during testing phases.
* **Total # of Non-Conformances Over Time** (e.g., Open, Closed, # of Days Open, Severity of Open Issues): Tracks the backlog and severity of unresolved defects, showing project health.
* **# of Non-Conformances in the Current Reporting Period** (e.g., Open, Closed, Severity): Provides a snapshot for immediate reporting and decision-making.
* **# of Safety-Related Non-Conformances Identified by Life Cycle Phase Over Time**: Ensures critical safety issues are tracked, resolved, and do not persist across phases.

**Requirements Coverage**

* **# of Requirements Tested vs. Total # of Requirements**: Measures the coverage of requirements by unit testing.
* **# of Safety-Critical Requirement Verifications vs. Total # of Safety-Critical Requirement Verifications Completed**: Tracks verification progress of critical functions for risk management.

**Test Coverage and Safety Focus**

* **# of Safety-Critical Tests Executed vs. # of Safety-Critical Tests Witnessed by SA**: Ensures critical functions receive sufficient oversight by software assurance.
* **# of Detailed Software Requirements Tested to Date vs. Total # of Detailed Software Requirements**: Tracks project progress towards testing detailed requirements.
* **# of Hazards Containing Software Tested vs. Total # of Hazards Containing Software**: Ensures hazard-related functionality is appropriately tested.

**Open and Closed Actions**

* **# of Open Issues vs. # of Closed Over Time**: Monitors resolution progress and backlog trends.
* **# of Closed Action Items vs. # of Open Action Items**: Tracks the completion of defect or issue corrections.

By consistently capturing and analyzing these metrics, SA can evaluate testing completeness, identify bottlenecks, and ensure timely correction of defects.

---

## 7.4 Guidance

Software assurance must take an active role in verifying that unit testing activities align with the project's software test plan, especially for critical and safety-related software components. The following guidance ensures unit testing effectiveness and adherence to project standards:

---

**1. Review and Verify Accuracy of Test Plans**

* Confirm that detailed unit tests are included in the **Software Test Plan (STP)**. Verify that the plan includes:
  + Test objectives and success criteria.
  + Test environment descriptions, setup, and configuration details.
  + A list of tests specific to **safety-critical code** and **off-nominal conditions** (edge cases, invalid or extreme inputs).
  + Repeatability as per [SWE-186 - Unit Test Repeatability](https://chat.nasa.gov/chats).
* Ensure that planned unit tests cover **critical paths**, decision logic, and the full operational range of input parameters, as highlighted in lesson learned [0939 - MPL Software/Test Errors](https://chat.nasa.gov/chats).

---

**2. Oversee Unit Test Execution**

* Verify that developers execute planned unit tests according to the documented schedule and procedures.
* Ensure that unit tests are **repeatable** and produce consistent outcomes. See SWE-186 guidance for repeatability criteria.

---

**3. Monitor Safety-Critical Function Testing**

* Confirm that **safety-critical functions** are adequately tested as part of the unit testing process. These functions may not be as fully exercised during later integration or system testing.
* Any updates or changes in safety-critical code must trigger re-execution of applicable unit tests.

---

**4. Evaluate and Document Test Results**

* Ensure that **unit test results** are documented in detail, including:
  + Test outcomes (success/failure).
  + Test inputs, outputs, and procedures.
  + Observations of behavior under both nominal and off-nominal conditions.
  + Identified defects and their root causes.
* Verify that test data, artifacts, and scripts are captured for use in regression testing and future reviews.

---

**5. Track and Close Issues**

* Confirm that all **defects, errors, or irregularities identified** during unit testing are:
  + Properly documented (e.g., in problem reports or defect trackers).
  + Prioritized based on severity (especially safety-critical and mission-critical issues).
  + Tracked to closure and verified via retesting to confirm the issue has been resolved.

---

**6. Confirm Regression Testing**

* Ensure that unit tests are **rerun** following:
  + Code corrections, updates, or enhancements.
  + Changes in dependent parameters, tools, or environments.
* Regression testing is particularly critical for safety-critical code to avoid introducing unanticipated side effects.

---

**7. Capture Objective Evidence**

* Validate that sufficient **objective evidence** is collected to demonstrate that unit testing is complete and compliant with the **SDP (Software Development Plan)** and other project documents (e.g., [5.06 - Software Configuration Management Plan](https://chat.nasa.gov/chats)).

---

**8. Use Metrics for Continuous Improvement**

* Continuously monitor testing metrics to identify trends, bottlenecks, or gaps in testing coverage.
* Use metrics to improve future iterations of testing activities, particularly for repeatable, safety, or risk-critical tests.

---

By confirming these key aspects of unit testing, software assurance helps ensure that unit tests are rigorous, safety-critical functions are adequately tested, issues are resolved, and test results are well-documented for verification and validation purposes. This oversight minimizes risks and strengthens overall software quality, aligning unit testing activities with project goals and compliance requirements.

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-016 - Software Schedule](/spaces/SWEHBVD/pages/102695402/SWE-016+-+Software+Schedule) * [SWE-017 - Project and Software Training](/spaces/SWEHBVD/pages/102695403/SWE-017+-+Project+and+Software+Training) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)       * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [7.06 - Software Test Estimation and Testing Levels](/spaces/SWEHBVD/pages/102695626/7.06+-+Software+Test+Estimation+and+Testing+Levels) * [8.01 - Off Nominal Testing](/spaces/SWEHBVD/pages/102695701/8.01+-+Off+Nominal+Testing) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical to demonstrating that unit testing has been planned, executed, and completed in accordance with the project's requirements, quality standards, and software assurance practices. This evidence should be collected, organized, and retained in project repositories (e.g., Software Development Folders (SDFs), version control systems, or test result databases). Below is a comprehensive list of objective evidence for this requirement:

---

#### **1. Test Plan and Design Evidence**

* **Approved Software Test Plan (STP):**

  + Documented plans detailing the unit test objectives, strategy, scope, success criteria, tools, and schedule.
  + Inclusion of test approaches for **safety-critical software components** and the **full range of operational parameters**, including nominal, off-nominal, and edge cases.
  + Traceability matrix linking unit tests to software requirements to ensure full coverage (see "Requirements Traceability Matrix" below).
* **Unit Test Case Documents:**

  + Test case descriptions with inputs, expected outputs, test environment details, and success/failure criteria.
  + Identification of all specific cases for testing decision logic, boundary conditions, faulty inputs, and contingencies.

---

#### **2. Test Environment Evidence**

* **Test Environment Configuration Document:**

  + Documentation of the unit test environment, including tools, version numbers, hardware/software setups, simulation/stub functions, scripts, and test drivers used.
  + Any captured differences between the unit test environment and the operational (target) environment.
* **System Configuration Evidence:**

  + Software and system configuration snapshots to demonstrate the version of the software under test (traceability to change requests or configuration-controlled baselines).

---

#### **3. Unit Test Execution Evidence**

* **Unit Test Logs:**

  + Logs documenting each executed test, including:
    - Test case identifier.
    - Date, time, and tester.
    - Inputs provided, outputs observed, and test status (e.g., pass, fail).
    - Descriptions of unexpected behaviors or errors encountered during testing.
  + Logs should demonstrate **repeatability** by showing that the same inputs produce the same outputs on repeated runs (in accordance with [SWE-186 - Unit Test Repeatability](https://chat.nasa.gov/chats)).
* **Automated Test Reports:**

  + Output of automated unit testing tools, including execution records, coverage metrics, and test pass/fail summary.
  + Attach artifacts (e.g., screenshots, logs, code coverage results).
* **Witness Logs (Optional for High-Risk Projects):**

  + Evidence that software assurance personnel or independent reviewers witnessed the execution of critical tests, especially for safety-critical components.

---

#### **4. Code Coverage Evidence**

* **Code Coverage Reports:**

  + Reports documenting code coverage metrics, such as:
    - Statement coverage.
    - Decision/branch coverage.
    - **Modified Condition/Decision Coverage (MC/DC)** for safety-critical software (as per SWE-219).
  + Evidence demonstrating that all logic paths were tested and validated.
* **Traceability Matrix Linking Requirements to Tests:**

  + Mapping of requirements to specific unit tests demonstrates full verification of functionality, including tests for safety-critical requirements or hazard-related functionality.

---

#### **5. Defect Management Evidence**

* **Defect or Problem Reports (PRs):**

  + Documentation of defects found during unit testing, including:
    - Problem description.
    - Severity classification (e.g., critical, major, or minor).
    - Root cause analysis.
    - Actions taken to address the defect.
    - Verification log showing that fixes resolved the issue.
  + Linking defect reports to the specific test case(s) where the defect was identified.
* **Defect Closure Evidence:**

  + Confirmation that all defects or issues raised during unit testing were resolved or mitigated before integration, including re-execution of applicable tests to verify fixes.

---

#### **6. Regression Testing Evidence**

* **Regression Test Results:**
  + Evidence showing that unit tests were successfully rerun after:
    - Code modifications or bug fixes.
    - Parameter or configuration changes.
  + Test logs showing no new defects were introduced by the changes.
  + Evidence that safety-critical functions were re-verified as part of the regression execution.

---

#### **7. Peer Review and Independent Evaluation**

* **Test Results Evaluations:**

  + Documentation of review and evaluation of unit test results by individuals other than the tester, ensuring impartiality.
  + Includes comments, findings, and approval of test results.
* **Peer Review Logs:**

  + Records of peer review meetings or checklists showing that test cases and results met project criteria, and objective reviews were conducted.

---

#### **8. Safety Assurance Evidence**

* **Safety-Critical Unit Test Evidence:**

  + Records that safety-critical functions were fully tested, including specific test cases, results, and comparison to safety requirements.
  + Reports showing that hazards associated with software were addressed and tested.
* **Non-Conformance Scenarios Documented:**

  + Evidence that fault tolerance and mitigation scenarios were tested (e.g., handling of invalid inputs or off-nominal conditions).

---

#### **9. Documentation Evidence**

* **Unit Test Report:**

  + A summary report of all unit testing activities, documenting:
    - Tests executed.
    - Success/failure outcomes.
    - Metrics captured during testing.
    - Summary of defects and resolutions.
    - Lessons learned or recommendations for improvement.
* **Captured Artifacts:**

  + Test data, scripts, stubs, drivers, and procedures used during unit testing.
  + Documentation of any deviations from the planned test process, including rationale and evidence of risk management.
* **Software Engineering Notebooks or SDF Entries:**

  + Notes, diagrams, design insights, and observations made during the unit testing phase.
* **Objective Evidence of Traceability:**

  + Proof that the entire process — from plans to test execution and results — aligns with the Software Development/Management Plan (SDP-SMP) and Software Configuration Management Plan (SCMP).

---

#### **10. Metrics Summary**

* **Captured Metrics Reports:**
  + Reports tracking key unit test metrics (e.g., test coverage, pass/fail rates, number of safety-related defects, etc.).
  + Evidence that metrics are monitored and analyzed, and actions are taken based on trends (e.g., regression test priority or resource allocation).

---

By maintaining and organizing this objective evidence consistently, projects can demonstrate compliance with unit testing requirements, ensure proper verification of functionality, and document traceability for audits, safety reviews, and lessons learned. Objective evidence also supports software assurance in confirming rigorous and completed unit test coverage.

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
