# SWE-194 - Delivery Requirements Verification

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695529. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification

SWE-194 - Delivery Requirements Verification

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695529/SWE-194+-+Delivery+Requirements+Verification#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695529)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695529&showCommentArea=true&showComments=true#addcomment)

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

4.6.4 The project manager shall complete, prior to delivery, verification that all software requirements identified for this delivery have been met or dispositioned, that all approved changes have been implemented, and that all defects designated for resolution prior to delivery have been resolved. 

## 1.1 Notes

NPR 7150.2, NASA Software Engineering Requirements, does not include any notes for this requirement.

## 1.2 History

Click here to view the history of this requirement: SWE-194 History

SWE-194 - Last used in rev NPR 7150.2D

| Rev | SWE Statement |
| --- | --- |
| A |  |
| Difference between A and B | N/A |
| B |  |
| Difference between B and C | NEW |
| C | 4.6.4 The project manager shall complete, prior to delivery, verification that all software requirements identified for this delivery have been met, that all approved changes have been implemented, and that all defects designated for resolution prior to delivery have been resolved. |
| Difference between C and D | Added 'or dispositioned' to this requirement. |
| D | 4.6.4 The project manager shall complete, prior to delivery, verification that all software requirements identified for this delivery have been met or dispositioned, that all approved changes have been implemented, and that all defects designated for resolution prior to delivery have been resolved. |

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
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |

# 2. Rationale

Requirements are the basis for building a product that meets the needs of the project. They define the behavior of the system and the constraints under which the problem is to be solved. The implemented product must be verified against the requirements to show that it meets all of the requirements.

However, requirements change over time and the documentation of the requirements is not always up to date. Also, for Agile approaches, not all of the requirements are necessarily documented upfront. It is critical that the Project Manager uses an appropriate method or tool to keep track of the requirements necessary for each delivery of the software and that these are kept up to date with any changes or defect resolutions.

The verification planning, execution, and results should include all requirements for that delivery. A traceability matrix that shows all of the planned and modified requirements for the test procedures/results is critical for showing compliance with this NPR requirement. Also critical are the test reports that show that each requirement verification passed.

This requirement ensures that before delivery, the software product is thoroughly verified to confirm that it meets specified requirements, incorporates approved changes, and resolves identified defects. These steps are critical to ensuring the delivered product is functionally complete, free of known issues (to the extent possible), and aligned with customer expectations. By mandating verification prior to delivery, the requirement seeks to reduce risks for operations, maintenance, and eventual system deployment, ensuring quality, reliability, and traceability.

---

### **1. Ensuring the Software Meets Operational and Mission Objectives**

Software requirements are the foundation of any project—they represent the customer's operational and performance goals as well as mission-critical constraints. Verifying that all requirements have been met prior to delivery guarantees the following:

* **Operational Readiness**: The software is ready for immediate use upon delivery, supporting intended mission objectives or operational needs.
* **Performance Assurance**: Functionality, reliability, safety, and other performance criteria are confirmed through testing, audits, and verification processes.
* **Risk Reduction**: By confirming requirements are fulfilled or dispositioned (e.g., deferred, removed via change control), risks related to incomplete functionality or ambiguous requirements are mitigated.

---

### **2. Traceability and Accountability for Approved Changes**

Changes to software requirements or design often occur throughout development due to evolving customer needs, technical challenges, or unforeseen circumstances. This requirement ensures:

* **Controlled Evolution**: All changes approved during the lifecycle have been implemented and accounted for, maintaining consistency across requirements, design, and implementation.
* **Customer Satisfaction**: The customer’s requested changes are fulfilled, ensuring alignment between the delivered product and expectations.
* **Preventing Scope Creep**: Verification ensures no unapproved changes or unnecessary features are introduced, which could result in unintended outcomes, delays, or increased costs.

---

### **3. Resolving Defects Before Delivery**

Addressing defects prior to delivery safeguards the software’s integrity, reliability, and usability. Defects designated for resolution are typically those affecting high-priority functionality, safety, security, or mission-critical operations. This requirement ensures:

* **Quality Assurance**: The software delivered to the customer is free from major flaws and meets agreed-upon quality standards.
* **Risk Mitigation**: Known defects that could negatively impact operational readiness are resolved, reducing downtime, safety risks, or mission failure.
* **Customer Trust**: Resolving defects demonstrates NASA’s commitment to delivering a reliable and compliant system.

---

### **4. Justifying Non-Resolved Items (Dispositioning Requirements, Changes, or Defects)**

Not all requirements, changes, or defects may be implemented by the delivery date due to certain constraints (technical feasibility, timeline, funding, etc.). This requirement ensures the following:

* **Formal Dispositioning**: Requirements, changes, or defects that are not included in the delivery are reviewed, justified, and documented with clear rationale.
* **Transparency**: Customers are informed of deferred or removed items, along with their implications, workarounds, or planned resolutions during maintenance phases.
* **Risk Documentation**: Any risks associated with dispositioned items (e.g., deferred requirements) are highlighted, allowing appropriate planning for future resolution.

---

### **5. Supporting Maintenance and Post-Delivery Activities**

Having a fully verified software baseline prior to delivery simplifies future phases, including operations, support, and maintenance. Meeting or dispositioning requirements ensures:

* **Traceability and Historical Record**: Post-delivery teams can understand the full scope of what was implemented and what was deferred via dispositioning.
* **Efficient Maintenance**: Clear defect resolution records avoid confusion when addressing issues in future updates.
* **Minimized Operational Disruption**: By resolving critical defects pre-delivery, operational teams face fewer interruptions during deployment and use.

---

### **6. Compliance with NASA Standards**

NASA’s software engineering standards emphasize quality, reliability, and lifecycle traceability in all software products. This requirement contributes to achieving those goals by ensuring the delivered product complies with requirements, aligns with approved changes, and has undergone rigorous defect resolution processes. It helps ensure adherence to:

* **Safety-Critical Requirements**: Ensures safety-critical functionality is delivered and verified, reducing hazards to personnel or equipment.
* **Mission-Critical Reliability**: Reduces the risk of software failure during mission-critical operations.
* **Regulatory and Contractual Obligations**: Provides evidence that deliverables meet the agreed-upon requirements for delivery, changes, and defect resolution.

---

### **Key Benefits of Requirement 4.6.4**

1. **Customer Confidence**: Verifiable fulfillment or disposition of requirements, implementation of changes, and resolution of defects reassures customers about the delivered software's quality and readiness for operations.
2. **Minimized Costs and Delays**: By identifying and resolving issues pre-delivery, this requirement reduces costs associated with post-deployment fixes, downtime, or rework.
3. **Improved Software Integrity**: Rigorous verification ensures the delivered system functions as intended, minimizing the risks of failures during operations.
4. **Maintainability and Documentation**: Dispositioning ensures that deferred or removed items are properly tracked for future consideration, making maintenance and updates more efficient.

---

### **Conclusion**

Requirement 4.6.4 ensures the integrity, reliability, and mission readiness of delivered software systems by mandating the verification of software requirements, implementation of approved changes, and resolution of designated defects before delivery. By taking a systematic approach and providing rationale for dispositioned items, NASA can deliver a product that satisfies customer expectations, minimizes risks, and supports sustainable operations and maintenance. This upfront rigor strengthens confidence in the delivered system and lays the foundation for long-term mission success.

# 3. Guidance

This requirement applies to **all NASA centers** and software classified as **Class A, B, C, D, and F**. It emphasizes the thorough verification of software requirements, changes, and defect resolutions before delivery, ensuring alignment between the delivered software and its intended operational objectives.

---

### **General Guidance**

Effective management and verification of requirements, changes, and defect resolutions are critical to the delivered software's success. Whether the project follows a **non-Agile** (traditional) or **Agile** development lifecycle, the following principles apply universally:

1. **Requirements Verification and Traceability**:  
   Verification must provide assurance that all performance, functional, and safety-critical requirements identified for the delivery are fulfilled, or any deviations are dispositioned and documented with clear rationale.

   * Maintain full **bidirectional traceability** between requirements, design, code, testing, and verification results. Reference **SWE-052 - Bidirectional Traceability** for additional guidance.
   * Use automated tools, where feasible, to streamline traceability and minimize errors in requirements tracking.
2. **Defect and Change Request Analysis**:

   * Perform detailed **impact analysis** for all change requests and defect resolutions to ensure proper verification coverage.
   * Verify that any safety-critical defect resolutions are fully tested under nominal and off-nominal conditions. Reference **HR-33 - Inadvertent Operator Action** for specific hazards related to operator actions.
3. **Test Plan Adequacy**:

   * Ensure that software test plans and procedures align with project requirements and test objectives. The plans should adequately verify functionality under normal, boundary, and failure conditions, with appropriate testing of hazard controls.

---

### **Specific Guidance for Non-Agile Life Cycles**

For projects using a traditional non-Agile development approach, the scope of verification typically spans the entire set of baseline software requirements:

1. **Comprehensive Requirement Analysis**:

   * Review the project’s baseline requirements. These should include functional, performance, safety, interface, and regulatory requirements.
   * Account for all approved **change requests** and incorporate them into the verification process.
   * Ensure requirements traceability records are up-to-date.
2. **Verification Plan Alignment**:

   * Cross-check the baseline set of requirements and all approved changes against the **verification plans** to ensure all requirements are covered.
   * Validate that the corresponding **test procedures** and **results** confirm that every requirement has been successfully verified.
3. **Verification Deliverables for Non-Agile Life Cycles**:

   * Ensure that the following deliverables are completed and traceable to the requirements:
     + Test Plans and Procedures (**SWE-065 Test Plan Development**)
     + Test Reports and Test Results (**SWE-066 Perform Testing**, **SWE-068 Evaluate Test Results**)
     + Regression Testing Results (**SWE-191 Software Regression Testing**)
     + Updated Verification Plans and Procedures (**SWE-071 Update Test Plans and Procedures**).
4. **Dispositioning of Deviations/Deferrals**:

   * Document any requirements that are deferred, removed, or changed as part of the delivery process. Dispositions should be approved, justified, and shared with the customer as part of the delivery records.

---

### **Specific Guidance for Agile Life Cycles**

For Agile development processes, where work is delivered incrementally via planned releases, the process needs to focus on the verification of requirements, changes, and defect resolutions relevant to each specific release:

1. **Incremental Requirement Verification**:

   * At the end of each sprint or iteration, verify that the implemented requirements for the planned release have been met. This includes both completed backlog items and approved changes associated with those items.
2. **Change Request Impact Analysis**:

   * For every planned release, analyze all approved change requests associated with specific requirements. Ensure these changes are tested, verified, and traceable to corresponding verification results.
3. **Defect Resolution Verification**:

   * Analyze all defect resolutions scheduled for inclusion in the release. Reference corresponding test cases to confirm the defects are resolved without negatively impacting existing functionality.
   * Perform **regression testing** to verify that defect fixes do not unintentionally alter unrelated system behavior.
4. **Agile Verification Deliverables**:

   * Agile development should maintain the following verification artifacts:
     + Iteration Test Results.
     + Updated Traceability Matrices mapping backlog items and approved changes to completed tests.
     + Regression Test Results for each defect resolution.
5. **Continuous Retrospection and Updates**:

   * Continuously review and refine test and verification procedures throughout Agile iterations to ensure they remain aligned with evolving requirements and changes.

---

### **Tracking Requirements and Changes**

Maintaining control over requirements and changes is critically important for successful verification. Use tools and processes to track and manage:

* Requirements changes (**SWE-053 - Manage Requirements Changes**).
* Software Change Requests (CRs) and Problem Reports (PRs) (**Topic 5.01 - CR-PR**).

For Agile projects, these tracking efforts typically integrate with product backlog management tools to provide real-time traceability. For non-Agile projects, formal change control boards (CCBs) document and approve changes.

---

### **Verification Processes and Methods**

Verification involves a mix of techniques to ensure requirements are satisfied:

1. **Inspections and Reviews**:

   * Leverage walkthroughs, peer reviews, and inspections of design, code, and test results during development phases. For detailed guidance, see **Section 5.3 of NPR 7150.2**.
2. **Testing**:  
   Testing is the cornerstone of verification. Comprehensive test strategies should account for:

   * Functional and performance tests under both nominal and off-nominal conditions (**SWE-066 - Perform Testing**).
   * Boundary and edge case testing to identify potential vulnerabilities.
   * Regression testing to ensure changes and defect fixes do not introduce new issues within the system.
   * Safety-critical testing, including hazard mitigation scenarios (**HR-33 - Inadvertent Operator Action**).
3. **Requirements Traceability Testing**:  
   Utilize bidirectional traceability to connect test cases and results back to individual requirements to ensure full coverage (**SWE-052 - Bidirectional Traceability**).

---

### **Mitigating Undetected Issues**

Although the goal is to deliver a fully verified system, situations may arise where issues or risks are identified late in the process:

* For safety-critical software, ensure comprehensive testing and validation of hazard controls are performed.
* In situations where known defects or risks remain unresolved upon delivery, ensure they are documented and dispositioned appropriately, with justifications for acceptance (e.g., low severity, workarounds available). Communicate these risks to the customer and update maintenance plans accordingly.

---

### **Integration with Operations and Maintenance Planning**

Verification activities should align with post-delivery needs. Ensure:

* All test artifacts (e.g., test cases, scripts, results) are delivered to support maintenance teams.
* Off-nominal and regression test cases are flagged as high-priority for periodic execution during routine maintenance.
* Operations, maintenance, and retirement plans fully account for any changes resulting from verified change requests or defect resolutions (**SWE-075 - Plan Operations, Maintenance, and Retirement**).

---

### **Conclusion**

Requirement 4.6.4 defines a critical phase in the software delivery lifecycle to ensure that completed software fulfills all baseline and incremental requirements, incorporates approved changes, and resolves designated defects. Whether employing non-Agile or Agile methodologies, careful tracking, analysis, and verification of requirements will result in a quality product that is reliable, safe, and aligned with customer expectations. By ensuring end-to-end traceability and focusing on defect-free delivery, NASA reduces operational risks and ensures mission success.

Keeping track of requirements changes can be done by several methods as described in [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes). See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report)

Verification is done by several methods. For guidance on inspections, see section 5.3 in the NPR. For guidance on testing, see section 4.5 in the NPR, specifically [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), and [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing).

For this effort, having a complete bi-directionality between requirements, design, and verification is significant and will make the analysis easier. See [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability).

See also [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement),

Analyze that the software test plans and software test procedures cover the software requirements and provide adequate verification of hazard controls, specifically the off-nominal commanding scenarios to mitigate the impact of inadvertent operator actions. See [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action), 

## 3.1 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

## 3.2 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

# 4. Small Projects

Small projects typically have limited scope, resources, and timeline constraints, requiring streamlined yet effective processes to meet this requirement without compromising quality or reliability. The guidance below helps small projects efficiently verify requirements, implement changes, and resolve defects while maintaining traceability and meeting delivery standards.

---

### **Principles for Small Projects**

1. **Focus on Simplicity:** Reduce overhead by using lightweight, straightforward processes while ensuring compliance with the requirement.
2. **Leverage Automation:** Use simple tools to manage requirements, testing, and defect resolution.
3. **Prioritize High-Risk Areas:** Allocate resources and testing efforts toward safety-critical, mission-critical, or high-risk software components.
4. **Emphasize Communication:** Foster clear and concise communication with stakeholders about requirements, changes, and known limitations.
5. **Utilize Templates and Checklists:** Standardized templates and checklists help ensure coverage with minimal customizations.

---

### **1. Streamlined Requirement Verification Process**

For small projects, verifying requirements can be simplified with the following approach:

#### **a. Use a Simple Requirements Management Tool:**

* Tools such as spreadsheets, lightweight databases, or open-source requirement management platforms (e.g., Trello, Jira) can be used to track requirements and their verification status.
* Ensure each requirement has a unique identifier for traceability.

#### **b. Traceability Without Overhead:**

* Create a **lightweight traceability matrix** linking requirements to their corresponding test cases and results.
* Use manual or semi-automated methods to maintain traceability (e.g., Excel or Google Sheets templates).

#### **c. Verification Scope:**

* List all requirements applicable for the delivery (functional, performance, and safety-related) and track their verification status:
  + Verified: Requirements met and tested successfully.
  + Dispositioned: Requirements deferred or removed, with rationale documented.
* Simplify verification by combining related requirements into **test scenarios** instead of verifying each independently.

#### **d. Review Relevant Change Requests:**

* Track changes to requirements using a change request log or an issue tracker.
* Review each change to confirm:
  + It addresses the original issue or enhancement.
  + It has been verified against the revised requirements.

---

### **2. Lightweight Change Evaluation and Implementation**

Small projects often deal with fewer change requests, making it easier to evaluate, implement, and verify changes using the following practices:

#### **a. Use a Compact Change Request Process:**

* Implement a simple, centralized tracking system for all software changes. For example:
  + Log change requests in a spreadsheet or a lightweight issue tracker (e.g., GitHub Issues, Jira).
  + Categorize changes as "critical," "enhancement," or "cosmetic" to prioritize efforts.

#### **b. Verify Change Implementation:**

* For every approved change request:
  + Confirm that the change has been implemented as specified.
  + Verify that corresponding test cases address the change.
  + Perform small-scale regression testing to assess impacts on related functionality.

#### **c. Keep Stakeholders Informed:**

* Document the list of approved changes in **delivery notes or release documentation**.
* Highlight any rejected or deferred changes with clear rationale.

---

### **3. Simplified Defect Management Process**

Resolving critical defects before delivery is essential for a successful software release. For small projects, a lightweight defect management approach is recommended:

#### **a. Tracking Defects:**

* Use a spreadsheet or lightweight tracking tool (e.g., Bugzilla, GitHub Issues).
* Categorize defects based on priority (e.g., critical, major, minor) to focus limited resources on high-impact issues.

#### **b. Establish Resolution Criteria:**

* Define simple criteria for defect resolution:
  + A defect is resolved when the functionality works as intended.
  + Testing confirms that the defect fix does not negatively impact other areas of the software.

#### **c. Regression Testing:**

* For every defect resolved, perform **small-scale regression testing** to ensure fixes do not introduce new issues.
* Focus testing efforts on the software areas most affected by the defect.

#### **d. Communicate Known or Deferred Defects:**

* Document unresolved defects with clear rationale in the delivery notes, along with any workarounds or acceptable risks.
* Confirm customer acceptance of deferred defects before delivery.

---

### **4. Testing and Verification Guidance**

Testing for small projects should be focused and efficient, ensuring adequate verification without unnecessary complexity:

#### **a. Focused Test Coverage:**

* Create a simple test plan covering these key areas:
  + Functional tests for implemented requirements.
  + Boundary and edge-case tests for critical software components.
  + Safety or hazard tests for off-nominal scenarios (if applicable).
* Use reusable test cases to minimize preparation efforts.

#### **b. Combine Tests Where Possible:**

* Group related requirements into a small number of combined test scenarios to reduce the total number of test cases.

#### **c. Tools for Automating Testing:**

* Use lightweight test automation frameworks (e.g., Selenium for UI testing, pytest for Python applications) to save time on repetitive test execution.

#### **d. Verification Artifacts:**

* Collect basic evidence for each requirement and defect:
  + Test logs showing pass/fail results.
  + Screenshots for UI verification.
  + Summary tables showing requirements coverage.

---

### **5. Clear Delivery Documentation**

Delivery documentation provides the customer with essential insight into the verification process and the state of the software:

#### **a. Use Templates for Documentation:**

Small teams can speed up documentation by using pre-made templates. Delivery documents should include:

* **Verification Report:** Summarizing all verified requirements, implemented changes, and resolved defects.
* **Change Log:** Listing all approved and implemented changes.
* **Defect Summary:** Listing all fixed, deferred, or known defects, including rationale and risk assessments.
* **Traceability Matrix:** Mapping requirements to their corresponding verification activities (optional but recommended).

#### **b. Customer Agreement for Deferred Items:**

* Ensure the customer explicitly agrees to the disposition of deferred requirements or defects. Highlight any risks associated with these deferred items.

#### **c. Customer-Friendly Delivery Notes:**

* Provide short, easy-to-understand summaries of delivery items for the customer, including known limitations or outstanding defects.

---

### **6. Streamlined Audits**

For small projects, formal audits can be simplified, allowing for efficient verification of deliverables:

#### **a. Functional Configuration Audit (FCA):**

* Review requirements traceability matrix and test results to verify that planned functionality was implemented and tested successfully.
* Use a checklist to ensure every requirement has been verified or dispositioned.

#### **b. Physical Configuration Audit (PCA):**

* Review the delivery package to confirm all required artifacts (e.g., software binaries, user manuals, test reports) are included and correctly versioned.
* RCA (Rapid Configuration Audit) methods using automation tools like Git can streamline this process.

---

### **Summary of Steps for Small Projects**

To simplify the implementation of Requirement 4.6.4 for small projects, follow these streamlined steps:

1. Use simple tools (spreadsheets, lightweight trackers) for requirements tracking and traceability.
2. Implement and verify each requirement and change via combined testing efforts.
3. Focus defect resolution efforts on safety-critical or high-priority issues.
4. Use reusable templates for delivery documentation (verification reports, change logs, defect summaries).
5. Perform checklist-driven FCA and PCA prior to delivery.
6. Ensure stakeholders have visibility into any deferred items or defects, obtaining customer agreement where necessary.

By tailoring processes to fit the scope, complexity, and resources of the project, small teams can efficiently meet requirement 4.6.4 while maintaining high-quality deliverables and reliability.

# 5. Resources

### 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-197)

  [Software Processes Across NASA (SPAN)](https://nen.nasa.gov/web/software/wiki "Click to open in new window")

  Software Processes Across NASA (SPAN) web site in NEN SPAN is a compendium of Processes, Procedures, Job Aids, Examples and other recommended best practices.

### 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

Lessons learned provide valuable insights from previous NASA projects to help prevent common issues and improve the likelihood of success in meeting this requirement. Below are relevant lessons captured from NASA's **Lessons Learned Information System (LLIS)**, historical project reviews, and mission debriefs that align with this requirement.

---

### **Key Lessons Learned Relevant to Requirement 4.6.4**

#### **1. Ensure Complete Requirements Verification Before Delivery**

* **Lesson ID:** 3870
* **Title:** Incomplete Verification of Software Requirements Led to Post-Delivery Issues
* **Occurrence:** In prior projects, some requirements were not fully tested or dispositioned before delivery, which led to software failures during operational use. In particular, missing verification for safety-critical and high-risk requirements caused significant rework and mission delays.
* **Recommendation:**
  + *Verify All Requirements*: Perform a comprehensive review of the requirements traceability matrix to confirm that all requirements are verified by corresponding test cases.
  + *Disposition Any Exceptions*: Clearly document rationale for deferred requirements and ensure risk acceptance is signed off by stakeholders prior to delivery.
  + *Reassess Safety-Critical Requirements*: Double-check high-risk requirements (e.g., related to interface management, hazard control, performance, and reliability) to avoid late-stage gaps.

---

#### **2. Prioritize Regression Testing of Changes and Fixes**

* **Lesson ID:** 2206
* **Title:** Insufficient Regression Testing After Implementing Changes and Fixes
* **Occurrence:** Projects that rapidly resolved defects or implemented last-minute changes often failed to perform adequate regression testing, leading to unintended and undetected disruptions to existing functionality.
* **Recommendation:**
  + *Regression Testing is Critical*: Always execute regression test cases after integrating changes or resolving defects to validate their impact on the entire system.
  + *Automated Regression Tools*: For small or large projects, leverage tools like JUnit, Selenium, or Python test frameworks to automate regression testing and reduce the likelihood of human error.
  + *Focus on High-Risk Areas*: Prioritize testing for software functions tied to human safety, mission-critical operations, and external system interfaces.

---

#### **3. Maintain Traceability (Requirements ↔ Test Results ↔ Changes)**

* **Lesson ID:** 5702
* **Title:** Gaps in Requirements Traceability Delayed Issue Resolution and Delivery
* **Occurrence:** A lack of bidirectional traceability between requirements, design, test cases, and test results led to missing or duplicated work during verification. Projects struggled to determine whether certain requirements were fully met.
* **Recommendation:**
  + *Bidirectional Traceability*: Maintain and regularly update the requirements traceability matrix to map each requirement to its corresponding test cases, verification results, and associated changes. Reference **SWE-052** for traceability best practices.
  + *Simplify Documentation*: Especially for small projects, use lightweight tools such as spreadsheets or simpler traceability systems for managing all verification and defect resolution efforts.

---

#### **4. Coordinate Verification of External Interfaces**

* **Lesson ID:** 0960
* **Title:** Defects in Verified Software Were Caused by Unverified Interface Issues
* **Occurrence:** A NASA project delivered software that passed its internal verification process, but subsequent integration testing identified critical issues stemming from unverified external interfaces. The project faced additional costs and delays to resolve these late-discovered issues.
* **Recommendation:**
  + *Interface Verification*: Include interface requirements in the verification process and ensure relevant test cases validate proper interactions with external subsystems, APIs, or hardware.
  + *Collaborate with Partners*: For projects involving third-party systems or components, coordinate early and regularly with external teams to prevent interface mismatches.

---

#### **5. Validate Off-Nominal Scenarios and Hazard Controls**

* **Lesson ID:** 1261
* **Title:** Limited Testing of Off-Nominal Scenarios Increased Operator Error Risk
* **Occurrence:** A mission-critical project faced complications during operations because off-nominal scenarios (e.g., unexpected commands, incorrect operator inputs) were not adequately tested. A hazard introduced by this gap caused a brief system outage.
* **Recommendation:**
  + *Test Off-Nominal Scenarios*: While verifying requirements, always include hazard controls and boundary conditions for potential operator errors and unexpected conditions. Reference **HR-33** for scenarios related to inadvertent operator actions.
  + *Ensure Coverage*: Verify that all critical and hazardous use cases are explicitly mapped to test scenarios and are adequately exercised before delivery.

---

#### **6. Communicate Known Risks and Deferred Requirements to Stakeholders**

* **Lesson ID:** 2213
* **Title:** Failure to Document and Communicate Dispositioned Defects/Requirements
* **Occurrence:** Customers encountered unexpected operational limitations because the project team failed to document deferred requirements or unresolved defects in delivery notes. The absence of this information led to misunderstandings and post-delivery problems.
* **Recommendation:**
  + *Transparent Communication*: Clearly document and communicate:
    - Dispositioned (deferred or eliminated) requirements and the rationale behind those decisions.
    - Known risks or unresolved defects, especially their safety and operational impacts.
  + *Obtain Customer Signoff*: Secure agreement from the customer for all deviations or exceptions before delivery to avoid confusion or disputes post-delivery. Include this information in the formal delivery letter.

---

#### **7. Define and Enforce Criteria for "Ready for Delivery"**

* **Lesson ID:** 2321
* **Title:** Premature Delivery Created Significant Rework
* **Occurrence:** In a previous project, delivery occurred before software verification and defect resolution were fully completed, leading to operational interruptions, cost overruns, and penalties for late fixes. The delivery was rushed due to unclear criteria for measuring delivery readiness.
* **Recommendation:**
  + *Delivery Readiness Checklist*: Develop a checklist to confirm:
    - All critical and high-priority requirements are verified successfully.
    - Designated defect resolutions have been tested and validated.
    - Regression tests for the entire system have been executed.
    - All deviations and risks have been approved by customers.
  + *Do Not Rush*: Resist the pressure to deliver software prematurely—ensure that readiness metrics defined in the project scope are fully achieved before delivery.

---

#### **8. Integrate CM Audits With Verification Efforts**

* **Lesson ID:** 1745
* **Title:** Configuration Management (CM) Issues Introduced Delivery Errors
* **Occurrence:** Software was delivered with mismatched versions between the source code, test results, and documentation due to inadequate configuration management auditing during verification.
* **Recommendation:**
  + *Perform Physical Configuration Audits (PCA)*: Before delivery, audit configuration records to ensure that:
    - The source code matches the implemented and verified requirements.
    - Artifacts like executable files, test reports, and user documentation reflect the latest changes.
  + *Involve Software Assurance in Verification*: Leverage software assurance personnel to help audit CM practices and ensure delivery consistency.

---

### **Summary of Key Recommendations**

1. Use a requirements traceability matrix to ensure full bidirectional traceability.
2. Verify all requirements (baseline and changes) and regression test fixes before delivery.
3. Include off-nominal scenarios and external interfaces in the verification plan.
4. Clearly communicate dispositioned requirements, deferred defects, and their risks.
5. Define specific "ready for delivery" criteria and enforce them prior to release.

By applying these lessons, NASA projects can strengthen their verification processes, improve delivery quality, and reduce post-delivery risks while efficiently meeting **Requirement 4.6.4**.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.

# 7. Software Assurance

**SWE-194 - Delivery Requirements Verification**

4.6.4 The project manager shall complete, prior to delivery, verification that all software requirements identified for this delivery have been met or dispositioned, that all approved changes have been implemented, and that all defects designated for resolution prior to delivery have been resolved.

## 7.1 Tasking for Software Assurance

**From NASA-STD-8739.8B**

1. Confirm that the project has identified the software requirements to be met, the approved changes to be implemented, and defects to be resolved for each delivery. 

2. Confirm that the project has met all software requirements identified for delivery. 

3. Confirm requirements once planned for delivery but no longer appearing in delivery documentation have been dispositioned. 

4. Confirm that approved changes have been implemented and tested.

5. Confirm that the approved changes to be implemented and the defects to be resolved have been resolved.

6. Approve or sign off on the projects delivered products.

## 7.2 Software Assurance Products

As part of the software assurance process, the following inputs and outputs (artifacts) must be reviewed, developed, and signed off to ensure accurate and verified deliveries. These products help demonstrate that all requirements, changes, and defect resolutions for the delivery have been addressed.

#### **Key Products Include**:

1. **Approvals and Sign-offs on Deliverables:**

   * Ensure that every delivery has formal sign-off from software assurance personnel indicating that the delivery is complete, correct, and meets the requirements agreed upon.
   * Verify that all open issues, risks, and accepted deviations are acknowledged and documented as part of the delivery sign-off.
2. **List of Risks and Issues Found with the Delivery:**

   * Develop a summary document that highlights significant risks or unresolved issues identified during the delivery process, including their potential impact, mitigation plans, and customer agreement (if applicable).
3. **Verification and Validation Documentation:**

   * **Software Test Reports:**
     + Review reports covering all tests executed for the delivery, including functional, performance, boundary, off-nominal, and regression tests.
     + Confirm that test results meet acceptance criteria for all requirements and defect fixes.
   * **Traceability Data:**
     + Review the bidirectional traceability matrix to ensure all requirements for this delivery are implemented and verified by test cases.
     + Ensure changes, defects, and their tests are traceable to the requirements and their associated results.
   * **Configuration Management Data:**
     + Verify that all changes and delivered artifacts are included in the project's configuration management system and match version baselines referenced within the delivery.
4. **Change and Defect Assurance Audit Results:**

   * Conduct audits of the change management process to ensure defect fixes and changes were implemented as documented.
   * Check for alignment between approved changes, planned deliveries, and implemented software configurations.
5. **Software Milestone Results:**

   * Verify results from critical milestones (e.g., Functional Configuration Audit (FCA), Physical Configuration Audit (PCA)) to validate deliverable readiness.

---

## 7.3 Key Metrics

Metrics help track and monitor the progress and quality of software development, verification, and delivery. They provide insights into how well the project's software assurance goals are being met.

**Recommended Metrics**:

1. **Planned vs. Delivered**:

   * Number of software components (e.g., modules, functions) planned versus released in each build.
   * Number of software units planned versus successfully built and verified by delivery.
2. **Requirements Verification**:

   * Total number of requirements (detailed, high-level, system, etc.) tested to date vs. total requirements applicable to the delivery.
   * Number of planned software requirements implemented in each build vs. actual software requirements implemented.
3. **Defect Tracking**:

   * Number of defects (non-conformances) identified at each phase (e.g., design, testing, integration).
   * Number of resolved defects vs. unresolved defects, with priority/severity breakdowns.
4. **Testing Effectiveness**:

   * Number of tests completed vs. total planned tests (by lifecycle phase or build).
   * Number of successful tests vs. failed tests.
   * Regression test coverage of critical functionality.
5. **Lifecycle Trends**:

   * Non-conformance trends (quantity and severity) by phase over time to assess process improvements.
   * Track rework time and costs associated with defects identified during verification.

**See also:** **SWE Topic 8.18 - Suggested Metrics** for additional metrics that may apply to your project.

---

## 7.4 Detailed Guidance

The software assurance personnel play a pivotal role in validating the completeness and correctness of the software delivery. The following activities must be performed as part of the assurance process:

#### **Delivery Documentation Reviews**

Review the delivery package and documentation, ensuring that the following items are explicitly addressed:

1. **Requirements Fulfillment:**

   * Confirm that delivery documentation (e.g., version description document, delivery letter) includes a list of requirements verified for the delivery and their associated test results.
   * Ensure requirements that are deferred or dispositioned are explicitly identified, justified, and agreed upon with stakeholders.
2. **Change Implementation:**

   * Review the configuration management records and change logs to validate that all approved changes were included in this delivery.
   * Check that the changes have been implemented correctly and any test results associated with these changes confirm their effectiveness.
   * Verify that changes align with their authorized baselines.
3. **Defect Resolution:**

   * Review the list of defects targeted for the delivery. Validate that:
     + Fixed defects have been tested to ensure proper functionality.
     + Any workarounds for unresolved defects are documented and included in user manuals or operational procedures.
     + Deferred defect resolutions have been approved by customers, including acknowledgment of associated risks.

---

#### **Testing Assurance**

Testing is a key component of the verification process. Software assurance personnel must:

1. **Review Test Coverage:**

   * Ensure that all requirements associated with the delivery are verified by test cases that cover normal, boundary, and off-nominal conditions.
   * Specifically ensure hazard controls (e.g., inadvertent operator actions, HR-33) are adequately tested.
2. **Regression Testing:**

   * Confirm that a full set of regression tests has been performed for critical software components.
   * Ensure that defect fixes and changes pass regression testing without introducing new issues in the existing functionality.
3. **Results Verification:**

   * Analyze test results to confirm that all planned tests were completed, and verify discrepancies between planned and completed tests.

---

#### **Change and Defect Management Audits**

Audit the change and defect management process for the following:

* Changes have been tested with results demonstrating they meet their objectives (e.g., defect is fixed, new capability works as intended).
* Verify test coverage specifically for similar defects or related areas of the system to avoid compounding errors ("sibling defects").
* Ensure that all changes and fixes are tested under integrated and anticipated operational conditions.

---

#### **Customer Communication and Risks**

1. **Deferred Requirements and Defects:**

   * Confirm that deferred requirements or defects are documented with clear rationale, stakeholder approval, and plans for resolution in future releases or maintenance. Highlight any critical risks associated with deferrals.
2. **Delivery Risks:**

   * Identify all unresolved risks associated with the delivery, including potential impacts on safety, functionality, and operations.

---

#### **Software Assurance Sign-Off**

Software assurance personnel must review the final delivery package against the criteria outlined above and provide formal sign-off. This indicates that:

* The delivery is complete and correct.
* Risks and discrepancies are documented and accepted.
* Verification and assurance activities meet required standards.

Sign-off should include the following statement or equivalent:

* "Software assurance has reviewed the delivery and determined it meets the requirements for completeness, correctness, and compliance with planned changes and defect resolutions."

---

### **Conclusion**

This revised software assurance guidance ensures focused, efficient, and effective verification of requirements, changes, and defect resolutions prior to delivery. By incorporating clear metrics, thorough reviews, robust traceability, and active risk management, software assurance personnel can confidently endorse a software delivery that is aligned with NASA’s high standards of quality and mission success.

For guidance on testing, see section 4.5 in the NPR, specifically [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures), and [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing). For more guidance on managing changes and release management, see [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes), [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes), and [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management).

## 7.5 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-053 - Manage Requirements Changes](/spaces/SWEHBVD/pages/102695435/SWE-053+-+Manage+Requirements+Changes) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-071 - Update Test Plans and Procedures](/spaces/SWEHBVD/pages/102695453/SWE-071+-+Update+Test+Plans+and+Procedures) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-080 - Track and Evaluate Changes](/spaces/SWEHBVD/pages/102695459/SWE-080+-+Track+and+Evaluate+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-191 - Software Regression Testing](/spaces/SWEHBVD/pages/102695526/SWE-191+-+Software+Regression+Testing) * [HR-33 - Inadvertent Operator Action](/spaces/SWEHBVD/pages/167805149/HR-33+-+Inadvertent+Operator+Action)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [8.18 - SA Suggested Metrics](/spaces/SWEHBVD/pages/102695756/8.18+-+SA+Suggested+Metrics) |

# 8. Objective Evidence

Objective Evidence

Objective evidence is critical for demonstrating compliance with this requirement. The evidence should clearly document the processes and outcomes related to requirements verification, approved changes, and defect resolution. Below is a detailed list of potential **objective evidence** for Requirement 4.6.4, grouped by relevant areas.

---

### **Categories of Objective Evidence**

#### **1. Requirements Verification**

Objective evidence related to the verification of software requirements involves showing that the project's requirements were fully tested, met, or dispositioned.

* **Requirements Traceability Matrix (RTM):**

  + A bidirectional traceability matrix that maps each software requirement to its test procedures and results. This provides a clear audit trail from requirements to their corresponding verification efforts.
  + For each requirement, the RTM should show:
    - Verification method (e.g., test, analysis, inspection, demonstration).
    - Test case IDs and corresponding results.
    - Status of the requirement (e.g., “verified,” “deferred,” “not applicable”).
* **Verification Plan and Procedures:**

  + Evidence from the **Verification and Validation (V&V) Plan** showing the approach for verifying specific baseline requirements and changes within the delivery.
  + Test procedures for each requirement, detailing setup steps, execution conditions, and expected results.
* **Test Results and Reports:**

  + Evidence that planned verification activities were conducted, typically including:
    - Pass/fail status of tests for all requirements.
    - Logs of functional testing, performance testing, boundary testing, and off-nominal testing.
    - Regression testing results to validate that changes and fixes have not negatively impacted previously verified requirements.
* **Requirement Disposition Records:**

  + Documentation of how each requirement was addressed if it was not verified. Disposition records should include:
    - Rationale for deferring or changing a requirement.
    - Customer-approved documentation indicating agreement on deferred requirements.

---

#### **2. Approved Changes**

For software changes implemented during the lifecycle, the objective evidence must demonstrate that all approved changes have been properly applied and verified:

* **Change Request Log:**

  + A consolidated log or database listing all submitted change requests (e.g., enhancements, corrections). Each record should include:
    - Status (approved/implemented/deferred/rejected).
    - Unique identifier.
    - Priority and impact evaluation.
* **Configuration Management Records (SWE-109):**

  + Evidence that all approved changes have been tracked, authorized, and implemented in the correct version of the software.
  + A version control log showing when specific changes were integrated into the software baseline.
* **Test Evidence for Approved Changes:**

  + Test reports confirming that each implemented change has been independently verified. These should demonstrate:
    - Correct functionality of the implemented change.
    - Validation against requirements or user stories.
    - Regression and integration test results ensuring no unintended side effects.

---

#### **3. Defect Resolution**

Objective evidence should demonstrate that all identified defects designated for resolution have been fixed, deferred, or dispositioned.

* **Defect Log (Non-Conformance Report):**

  + A central record of all defects identified during the project, typically including:
    - Defect ID, description, severity (critical, major, minor), and priority.
    - Status (open, resolved, tested, deferred, etc.).
    - Resolution (e.g., fixed, workaround, deferred).
  + Evidence includes a clean mapping of resolved defects to test cases or resolution notes.
* **Root Cause Analysis Reports (If Applicable):**

  + For significant or recurring defects, provide evidence of root cause analysis with findings and corrective actions.
* **Defect Test Reports:**

  + Testing results showing that resolved defects have been corrected and validated against expected behavior.
  + Evidence of regression testing performed to confirm that defect fixes did not introduce new issues.
* **Unresolved Defects Approval Documents:**

  + Records of agreements with stakeholders/customers for deferred defects or defects to be left as-is. These documents should:
    - Explain the rationale for deferral.
    - Include risk assessments and any workarounds.

---

#### **4. Regression and Integration Testing**

Objective evidence should confirm that no unintended functionality was impacted during defect fixes or changes:

* **Regression Test Plan and Results:**

  + A documented summary of all regression tests executed, including:
    - Scope and focus of the regression tests.
    - Test results with pass/fail status.
* **Integration Test Results:**

  + Evidence that integrated components, subsystems, and interfaces were tested to validate proper operation in the system context.
  + Includes boundary conditions, interface tests, and multi-subsystem compatibility checks.

---

#### **5. Delivery Documentation**

Delivery packages and artifacts must explicitly highlight the state of requirements, changes, defects, and risks in the software being delivered.

* **Version Description Document (VDD):**

  + Outlines the release scope and summarizes:
    - Requirements implemented and tested in this release.
    - Approved changes included in the delivery.
    - Defects resolved and deferred.
    - New capabilities and any limitations.
* **Delivery Letter:**

  + A formal document addressed to the customer that:
    - Summarizes what is included in the delivery.
    - Lists unresolved issues or risks with agreed disposition.
    - Confirms satisfaction of requirements verification.
* **Customer Acceptance Letter:**

  + Objective evidence showing formal customer/external stakeholder acceptance of the delivered software, including acknowledgment of unresolved or deferred defects/issues.

---

#### **6. Milestone and Audit Records**

Software approval milestones and audits provide critical evidence for project compliance:

* **Functional Configuration Audit (FCA):**

  + Records from the FCA demonstrate that all baseline requirements are met, and testing is complete.
* **Physical Configuration Audit (PCA):**

  + Records from the PCA indicate that all items delivered match the approved configuration baseline.
* **Software Assurance Audit Reports:**

  + Results of software assurance reviews of the delivery package (e.g., completeness, traceability, defect status, and risk assessments).
* **Software Configuration Management Records:**

  + Logs of software builds/releases, their associated configurations, and approvals.
* **Peer or Independent Reviews:**

  + Records of reviews (e.g., design review, test readiness review, delivery reviews) where the state of requirements, defects, and customer priorities were presented and agreed upon.

---

### **Summary: Evidence Checklist for Requirement 4.6.4**

1. **Requirements Verification:**

   * **Traceability Matrix** showing test coverage for all requirements.
   * **Test Plans and Results** for normal, boundary, and off-nominal scenarios.
   * Documentation of any deferred or unverified requirements with customer approval.
2. **Approved Changes:**

   * **Change Request Records** with status, implementation, and test results.
   * **Configuration Management Data** to cross-check implemented changes.
3. **Defects:**

   * **Defect Log** with resolution or disposition status for all defects.
   * **Defect Test Results** and regression reports.
   * Stakeholder/customer sign-off for deferred defects.
4. **Testing and Regression:**

   * **Regression and Integration Testing Results.**
   * Confirmed successful execution for existing operational functionality.
5. **Delivery Package:**

   * **Version Description Document (VDD).**
   * Formal **Delivery Letter** with summarized verification results.
   * Customer acceptance letter or approval records.
6. **Milestone and Audit Records:**

   * **FCA and PCA audit results.**
   * Software assurance review reports.

---

By providing this objective evidence, the project team and software assurance personnel can demonstrate compliance with Requirement 4.6.4, ensuring that the software meets NASA’s high standards and is ready for delivery and operation with minimal risk.

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
