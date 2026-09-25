# 7.05 - Work Breakdown Structures That Include Software

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695623. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software

7.05 - Work Breakdown Structures That Include Software

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695623/7.05+-+Work+Breakdown+Structures+That+Include+Software#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695623)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695623&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Definition](#tabs-2)
* [3. The Basic WBS](#tabs-3)
* [4. Common Issues](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

# 1. Purpose

Provide guidance on the development of a work breakdown structure (WBS) for software on projects. The WBS provides a common planning framework to use in estimating the scope of a project.

# 2. Definition

Per the NASA Systems Engineering Handbook [273](#_tabs-<p></p>) (Section 6.1.2.1), a work breakdown structure is a hierarchical breakdown of the work necessary to complete a project. The WBS can be product- or process-oriented. A product-oriented WBS has work activities grouped by the product or service they support. A process-oriented WBS includes in the appropriate WBS element the work activities associated with the processes being used. [389](#_tabs-<p></p>) The WBS provides the framework to plan, organize, and control a project. [388](#_tabs-<p></p>)

Excellent information on the development and usage of the WBS can be found in NASA/SP-2010-3404, NASA Work Breakdown Structure (WBS) Handbook. [390](#_tabs-<p></p>) Additionally, both the NASA Systems Engineering Handbook [273](#_tabs-<p></p>) and the "CMMI for Development, Guidelines for Process Integration and Product Improvement"[388](#_tabs-<p></p>) provide further guidance on the development of WBS structures containing software. The NASA Software Engineering curriculum, especially [389](#_tabs-<p></p>), addresses the use of the WBS for software on projects. These resources are cited in the Resources tab.

# 3. The Basic WBS

A good work breakdown structure (WBS) for software projects provides a detailed and hierarchical decomposition of the work required. This decomposition helps manage, organize, and guide the project's planning, execution, and monitoring. Here's an example of a hierarchical WBS for a generic software project:

### 1. Project Management

* 1.1. Project Initiation
  + 1.1.1. Project Charter
  + 1.1.2. Stakeholder Identification
* 1.2. Project Planning
  + 1.2.1. Project Plan Development
  + 1.2.2. Schedule and Budget Planning
  + 1.2.3. Risk Management Plan
  + 1.2.4. Quality Management Plan
* 1.3. Project Execution
  + 1.3.1. Team Management
  + 1.3.2. Communication Plan Execution
* 1.4. Project Monitoring & Control
  + 1.4.1. Progress Tracking
  + 1.4.2. Change Management
  + 1.4.3. Quality Assurance
* 1.5. Project Closure
  + 1.5.1. Final Reports
  + 1.5.2. Post-mortem Analysis

### 2. Requirements Analysis

* 2.1. Requirements Gathering
  + 2.1.1. Stakeholder Interviews
  + 2.1.2. Surveys and Questionnaires
* 2.2. Requirements Documentation
  + 2.2.1. Functional Requirements
  + 2.2.2. Non-functional Requirements
* 2.3. Requirements Review and Validation
  + 2.3.1. Review Meetings
  + 2.3.2. Requirement Sign-off

### 3. Design

* 3.1. Architectural Design
  + 3.1.1. System Architecture
  + 3.1.2. Database Design
* 3.2. Detailed Design
  + 3.2.1. Module Design
  + 3.2.2. Interface Design
* 3.3. Design Reviews
  + 3.3.1. Internal Review
  + 3.3.2. Stakeholder Review

### 4. Development

* 4.1. Development Environment Setup
  + 4.1.1. Infrastructure Setup
  + 4.1.2. Tool Configuration
* 4.2. Coding
  + 4.2.1. Module Development
  + 4.2.2. Integration
* 4.3. Code Reviews and Inspections
  + 4.3.1. Peer Reviews
  + 4.3.2. Static Analysis

### 5. Testing

* 5.1. Test Planning
  + 5.1.1. Test Strategy
  + 5.1.2. Test Cases Development
* 5.2. Unit Testing
* 5.3. Integration Testing
* 5.4. System Testing
* 5.5. User Acceptance Testing (UAT)
* 5.6. Performance Testing

### 6. Deployment

* 6.1. Deployment Planning
  + 6.1.1. Production Environment Setup
  + 6.1.2. Deployment Checklist
* 6.2. Deployment Execution
  + 6.2.1. Pilot Deployment
  + 6.2.2. Full-scale Deployment

### 7. Maintenance and Support

* 7.1. Troubleshooting and Bug Fixing
* 7.2. Performance Monitoring
* 7.3. User Support and Training
* 7.4. Regular Updates

### 8. Documentation

* 8.1. Technical Documentation
  + 8.1.1. API Documentation
  + 8.1.2. System Design Documentation
* 8.2. User Documentation
  + 8.2.1. User Manuals
  + 8.2.2. Training Guides

Each level in this hierarchical structure breaks down the project into finer detail, making it easier to manage, assign responsibilities, estimate costs, timeline, and monitor progress. The WBS should be tailored to the specific requirements and nature of the software project for effectiveness.

A project's software may be a stand-alone system or exist as part of a larger system or project. For example, for a space flight project, the software may be shown under the Avionics subsystem. For both types, the WBS developer needs to be aware of the responsibilities required of his or her project.

As another example consider the following list-oriented approach to a WBS. Again, the use of NASA/SP-2010-3404, NASA Work Breakdown Structure (WBS) Handbook,[390](#_tabs-<p></p>) will help in the development of the lower levels of the WBS elements.

1. SW Management (incl. budget, schedule, contractor mgmt, risk, CM, training, IV&V coordination, lesson learned, etc.)
2. SW Requirements Management
3. SW Testbed Management
4. CSCI Development
5. CSCI Test
6. CSC Test
7. Sustaining Engineering
8. Security (physical and IT)

The project's software may also be developed in the context of a product-driven structure. Lower level development of the WBS will include the approach to software development for the individual component or system to be produced in the sub-element. The following figure suggests several approaches for this type of WBS.

The WBS is updated iteratively over the project life cycle. The initial WBS is used for early estimating of cost and schedule. The detailed WBS helps organize and control the work done by populating the project's cost plans and schedule.

A companion WBS dictionary, which is also developed, fully describes the work being done including the title and objective of the element, expected products/services from each element, and the dependencies between elements.

The Software Development Plan ([5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)) is a place to record the WBS of the life cycle processes and activities.

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Common Issues

There are several work activities that are often forgotten in developing the WBS:

* Process planning and monitoring activities - see [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans), [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking), [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review)
* Requirement engineering activities
* Formal review activities - see [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones)
* Development activities
* Stakeholder activities
* Training activities
* Planning, documenting, and tracking of commitments from other organizations see [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule).

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-153)

  [CMMI © for Development, Guidelines for Process Integration and Product Improvement,](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=31054 "Click to open in new window")

  Chrissis, M.B., Konrad, M., Shrum, S., This book is the definitive reference for CMMI-DEV Version 1.3. It describes best practices for the development and maintenance of products and services across their lifecycle. 3rd Edition, 2010, Addison-Wesley Professional, ISBN: 0-321-71150-5
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-389)

  [APPEL Software Engineering Management 301 (SWE 301).](http://appel.nasa.gov/course-catalog/appel-swem/ "Click to open in new window")

  Course from APPEL: Academy of Program/Project & Engineering Leadership.
* (SWEREF-390)

  [NASA Work Breakdown Structure (WBS) Handbook.](https://ntrs.nasa.gov/search.jsp?R=20110012671&hterms=NASA+SP-2010-3404&qs=N%3D0%26Ntk%3DAll%26Ntt%3DNASA%2520SP-2010-3404%26Ntx%3Dmode%2520matchallpartial%26Nm%3D123%7CCollection%7CNASA%2520STI%7C%7C17%7CCollection%7CNACA "Click to open in new window")

  NASA SP-2010-3404, NASA Headquarters. January 2010.

  

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-013 - Software Plans](/spaces/SWEHBVD/pages/102695397/SWE-013+-+Software+Plans) * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-024 - Plan Tracking](/spaces/SWEHBVD/pages/102695409/SWE-024+-+Plan+Tracking) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule)        * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
