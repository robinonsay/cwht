# 5.06 - SCMP - Software Configuration Management Plan

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695666. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan

5.06 - SCMP - Software Configuration Management Plan

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695666)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695666&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Minimum Recommended Content](#tabs-1)
* [2. Rationale](#tabs-2)
* [3. Guidance](#tabs-3)
* [4. Small Projects](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

Return to [7.18 - Documentation Guidance](/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance)

# 1. Minimum Recommended Content

Minimum recommended content for the Software Configuration Management Plan. 

1. The project organization(s).
2. Responsibilities of the software configuration management organization.
3. References to the software configuration management policies and directives that apply to the project.
4. All functions and tasks required to manage the configuration of the software, including:
   1. Configuration identification,
   2. Configuration control,
   3. Status accounting,
   4. Configuration audits and reviews,
   5. Configuration of auto-generation tools and associated data,
   6. Configuration management of input to auto-generation tools, the output of the auto-generation tools, and modifications made to the output of the auto-generation tools.
5. Schedule information, which establishes the sequence and coordination for the identified activities and for all events affecting the plan's implementation.
6. Resource information, which identifies the software tools, techniques, and equipment necessary for the implementation of the activities.
7. Plan maintenance information, which identifies the activities and responsibilities necessary to ensure continued planning during the life cycle of the project.
8. Release management and delivery.

# 2. Rationale

Configuration management is the "process of identifying and defining the configuration items in a system, controlling the release and change of these items throughout the system life cycle, recording and reporting the status of configuration items and change requests, and verifying the completeness and correctness of configuration items." [276](#_tabs-<p></p>) This work can only be properly accomplished if there exists a plan addressing all of these activities, which has been reviewed by an appropriate set of stakeholders and tailored for a specific project's needs.

# 3. Guidance

The Software Configuration Management (SCM) Plan may be tailored by software classification. Goddard Space Flight Center's (GSFC's) 580-STD-077-01, Requirements for Minimum Contents of Software Documents, provides one suggestion for tailoring an SCM Plan based on the recommended contents and the classification of the software being developed.

When creating an SCM Plan, using a template ensures consistent plans for all projects at a Center. Consider the following guidance, listed by the recommended elements, to ensure that all content is properly addressed and tailored for the project. See also [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan).

## 3.1 Project organization(s)

Consider the following when writing the project organization section of the SCM Plan:

* Describe where SCM fits into the technical and managerial reporting chain of the project.
* Identify by role project personnel responsible for managing the SCM activities for the project.
* Identify by role those persons on the project who will carry out SCM activities for the project.

## 3.2 Responsibilities

The responsibilities of the SCM organization include:

* Responsibilities for each role participating in SCM activities, including team personnel, leads, Change Control Board (CCB), quality assurance, managers, and any other roles relevant for the project.
* Responsibilities for carrying out each of the SCM functions defined in the SCM Plan.
* Responsibilities of each CCB established for the project, including references to their charters or other governing documents (purpose, objectives, scope of authority, duration of existence) and the hierarchy among the CCBs; charts or diagrams may be helpful here.
* CCB participants, either by project name and role or by individual names.
* CCB meeting schedules, if not captured elsewhere.
* Responsibilities for releasing software, if not captured elsewhere.
* Provider roles and integration of provider SCM into overall project SCM.
* Responsibilities for maintaining SCM tools.

## 3.3 References to SCM policies and directives

This section of the SCM Plan needs to list any specific SCM policies and directives that apply to or impact SCM for the project. Those policies and directives may be named in a reference section of the plan, so referring to that section may be appropriate. However, the impact of those policies and directives on SCM for the project is described here.

Consider:

* Existing CCB procedures.
* Existing status accounting procedures.
* Existing configuration identification procedures.
* Existing audit procedures.

See also [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items), [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes),

## 3.4 All functions and tasks required to manage the configuration of the software

This section of the plan describes configuration identification, configuration control, status accounting, configuration audits and reviews, and management of auto-generation tool data. Guidance for each of these topics is found in the related requirements (see table below) in this Handbook.

This section of the SCM Plan describes how each of these SCM functions will be performed. Consider using a separate subsection for each of these functions. As appropriate for the project, the following highlights are to be included but are not to be considered the only items to document:

* List of configuration items (or reference to where this list can be found or how it can be obtained).
* Naming convention for configuration items.
* Activities to define, track, store, and retrieve configuration items.
* Process for capturing a configuration item in the SCM system.
* How to request a change (how to enter a change request and transition it into the review and approval process).
* Levels of control for changes (CCBs).
* Activities for verifying and implementing an approved change.
* Schedule, purpose, responsible party for status accounting forms and reports, including metrics.
* Access to status accounting data.
* List, description, and purpose of planned SCM audits and reviews.
* Activities to define, track, store, and retrieve the configuration of auto-generation tools and associated data.
* Process for performing the configuration management of input to auto-generation tools, the output of the auto-generation tools, and modifications made to the output of the auto-generation tools.

See also Topic [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews),

If the project uses data management in addition to SCM, those activities are described in this section of the SCM Plan, including:

* Receiving data.
* Cataloging data.
* Maintaining status records.
* Establishing and maintaining secure data access and control.
* Providing change control monitoring and review.
* Archiving data.
* Plans for backups and disaster recovery.

## 3.5 Schedule

This section of the plan includes information necessary to describe the sequence and coordination for the identified activities and for all events affecting the plan's implementation (NPR 7150.2). The SCM schedule needs to coordinate with the project schedule, and this part of the SCM Plan shows that coordination. Graphics (timelines) may be useful.

Typically, configuration items are uncontrolled until some gate or milestone is reached, at which time they are required to be placed under configuration control. Each configuration item or group of items may have its own gate. Because those gates can be points in the project timeline, consider describing those gates in this section.

Also consider for the SCM schedule:

* Timeline or phase for creation of planned baselines.
* SCM audit schedule.

See also [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting), [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits).

## 3.6 Resources and Tools

**NASA Software Safety Guidebook - NASA-GB-8719.13**

4.5 Software Configuration Management  
"Software Configuration Management is usually performed using a tool (program). However, a file or folder needs to be maintained, to collect information that is not in electronic form. This information could include the design notes scribbled on a napkin or a fax that only exists in hard-copy. The point is to collect all pertinent information in one place. It is a good idea to catalog all the hardcopy information in the electronic SCM system, so that it can be found again when needed."[276](#_tabs-<p></p>)

The resources section of the SCM Plan describes the software tools, techniques, and equipment that will be used to carry out SCM for the project. References to the relevant documentation for installing and using these tools is included, as well as the configuration controls for each tool.

Typical resources include:

* Personnel (note level of effort and any required training and/or qualifications).
* Tools for managing source code, documents, requirements, design, and any other configuration items.
* Tools for managing change requests if not integrated with the main configuration management tool.
* Tools for managing data not subject to configuration control and CCB change authority, such as meeting minutes, reports, action items, corrective actions.
* Manual procedures.
* Equipment to support or host SCM tools.
* Training for SCM personnel.

See also Topic [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report), [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test), [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability),

## 3.7 Plan maintenance

Paraphrasing from NPR 1441.1E - NASA Records Management Program Requirements,

* Describe how the project will manage information throughout its life cycle, including the development and maintenance of an electronic program library.
* Explain how the project will ensure identification, control, and disposition of project records in accordance with NPD 1440.6, NASA Records Management, and NPR 1441.1, Records Retention Schedules. [037](#_tabs-<p></p>)

The maintenance section provides information such as:

* History of changes.
* Role responsible for monitoring the SCM Plan.
* Frequency of scheduled updates.
* Process for evaluating and approving changes to the SCM Pan.
* Process for implementing and communicating approved changes to the SCM Plan.

See also [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review), [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking), [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination)

## 3.8 Release management and delivery

NASA-GB-8719.13, NASA Software Safety Guidebook, [276](#_tabs-<p></p>)  states: "Configuration Management should act as the sole distributor of media and documentation for all system tests and for delivery to [sub]system integration and testing. Pulling the latest program off the developer's machine is not a good idea. One aspect of system testing is repeatability, which can only be assured if the software under test comes from a known, and fixed, source." [276](#_tabs-<p></p>)

The release management and delivery activity is described in this portion of the SCM Plan (see [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) for release management guidance), including formal control of the build, release, and delivery of software products and documentation.

Additional guidance related to the content of the configuration management plan may be found in the following requirements in this Handbook:

## 3.9 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

Configuration management activities are based on risk, so projects designated small by size of the team or budget need to ensure that their Software Configuration Management (SCM)Plans include all the recommended content, while including only those processes and the associated structure necessary to manage project risk. This might mean planning to use simpler tools or fewer personnel (filling multiple roles) to carry out the SCM processes. It could also mean planning to use a single tool for multiple purposes to reduce tool management and overhead.

Small projects may not require the formality of a separate SCM Plan; instead, SCM planning may be documented as a section of the project's Software Management Plan. Alternatively, one master SCM Plan may document configuration management for multiple small projects.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-037)

  [NASA Records Management Program Requirements (Updated w/Change 3),](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1441&s=1E "Click to open in new window")

  NPR 1441.1E, NASA Office of the Chief Information Officer, Effective Date: January 29, 2015, Expiration Date: January 29, 2024
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-574)

  [Place Flight Scripts Under Configuration Management Prior to ORT](https://llis.nasa.gov/lesson/2476 "Click to open in new window")

  Public Lessons Learned Entry: 2476.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-036 - Software Process Determination](/spaces/SWEHBVD/pages/102695414/SWE-036+-+Software+Process+Determination) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-079 - Develop CM Plan](/spaces/SWEHBVD/pages/102695458/SWE-079+-+Develop+CM+Plan) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-083 - Status Accounting](/spaces/SWEHBVD/pages/102695465/SWE-083+-+Status+Accounting) * [SWE-084 - Configuration Audits](/spaces/SWEHBVD/pages/102695466/SWE-084+-+Configuration+Audits) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) * [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability)        * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Configuration Management](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Configuration+Management) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

* **Place Flight Scripts Under Configuration Management Prior to ORT (Project attention to configuration control). Lesson Number 2476[574](#_tabs-<p></p>):**  "Project attention to the configuration control of flight scripts is likely to prevent the generation of unnecessary software iterations, improve the rigor of mission system engineering processes, and ensure consistency in the test and operations environments."

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
