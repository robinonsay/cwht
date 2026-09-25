# 7.10 - Peer Review and Inspections Including Checklists

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695640. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists

7.10 - Peer Review and Inspections Including Checklists

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695640)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695640&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose and Roles](#tabs-1)
* [2. Process Overview](#tabs-2)
* [3. Barriers and Enablers](#tabs-3)
* [4. Checklists](#tabs-4)
* [5. Resources](#tabs-5)
* [6. Lessons Learned](#tabs-6)

# 1. Purpose and Roles

## 1.1 Introduction

Peer reviews and inspections use a straight-forward, organized approach for conducting an evaluation of a work product. The approach is designed to detect potential defects in a product and to methodically evaluate each defect to identify solutions and track the incorporation of these solutions into the product. A product could be almost anything that is being produced, including documentation, designs, manufactured goods, or, in the case of software, the code. The value of this approach is that it is simple to understand and, when adhered to, can result in a very efficient method of identifying defects early in a product's life cycle.

## 1.2 Purpose

This topic provides guidance for projects implementing peer reviews and formal inspections, in accordance with the existing best practices, standards, and guidance at NASA. This topic also provides a procedural overview that cross-references to other resources for more information.

## 1.3 What Software Products Are Peer-Reviewed

The project manager shall perform and report the results of software peer reviews or software inspections for [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures).

1. 1. Software requirements.
   2. Software plans.
   3. Any design items that the project identified for software peer review or software inspections according to the software development plans.
   4. Software code as defined in the software and or project plans.
   5. Software test procedures.

*Note: Software peer reviews or software inspections are recommended best practices for all safety and mission-success related software components. Recommended best practices and guidelines for software formal inspections are contained in NASA-STD-8739.9.*

See also SWE and Topics

* [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis)
* [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis)
* [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis)
* [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation)

## 1.4 Roles

|  |  |
| --- | --- |
| **Role** | **Responsibility** |
| Author | The author:   * Prepares the work product to address applicable standards and to meet the inspection entrance criteria. * Works with the moderator to plan the inspection, providing input on key decisions, such as the most important parts of the document on which to focus, needed expertise on the inspection team, etc. * Responds to questions about the work product at the inspection meeting. * Performs rework, correcting defects identified by the inspection team. * Verify with the moderator that all corrections are made. |
| Moderator | The moderator is the single person responsible for overseeing the inspection process and obtaining a good inspection. The moderator does this by:   * Determining if the work product is ready to inspect. * Organizing the participants and materials, including determining if training and additional informational briefing are needed. * Assigning roles and actions. * Conducting the inspection meeting. * Verifying that rework is accurately completed. * Ensuring that all open issues are dispositioned. * Collecting and recording inspection metrics. * Fulfilling normal inspector responsibilities. |
| Inspectors | Inspectors:   * Allocate time for performing inspection activities. * Attend the overview (if held) and inspection meetings. * Review the materials thoroughly. * Perform any assigned role (reader or recorder). * Support the moderator and author to complete action items outside the inspection itself. * Maintain a professional attitude that focuses on constructively improving the work product under inspection. * Focus on finding defects. * Are you open to learning from the other inspectors and possibly expanding their expertise? * Review the product to determine if the product meets the requirements * Review the product (requirements, design, code) to determine if the product provided is testable. |
| Managers | Managers are essential to the success of an inspection. :   * Demonstrate to the inspection team members the importance of the activity and its contributions to the quality of the software product. * Establish schedules that allow adequate time for all stages of the inspection process. * Ensure that all team members are trained in the inspection process. Managers, however, should not be chosen as part of the inspection team unless they are the authors of the inspected work products or if their expertise is essential to the inspection. If managers participate in an inspection, e.g., on very small teams, both managers and the other inspectors should be aware that defects found during inspections are never used to evaluate authors. |
| Software Assurance (SA)  Representatives | SA Representatives:   * Verify compliance of a team's inspection practice with the process requirements of the software inspection standard by working with the project in defining the inspection procedures and records. * Verify the collection of all required data. * Selectively review inspection packages for required inspection materials. * Participate in inspection meetings, fulfilling any applicable inspection roles, except for those of the author. * Provide an independent evaluation of the effectiveness of the inspection process and product quality. * Assure that reports of inspection process evaluation and analysis are defined, scheduled, provided to appropriate stakeholders, and considered as part of inspection process improvement. |
| Hardware Engineer(s) | * Review the products (requirements, design, code, test procedures). * Look for defects in the product under inspection, ensure software control of hardware is correct * Review the product to determine if the product meets the requirements * Focus on finding defects with how the software controls the hardware. * Review the product (requirements, design, code) to determine if the product provided is testable. |
| System Engineer(s) | * Review the products (requirements, design, code, test procedures). * Look for defects in the product under inspection, ensure software control of the system is correct, including any fault detection, fault isolation, and fault recoveries are correct. * Review the product to determine if the product meets the requirements. * Focus on finding system defects. * Review the product (requirements, design, code) to determine if the product provided is testable. |

## 1.5 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 2. Process Overview

Figure 1, Inspection Process Activity Diagram, illustrates an activity diagram for the inspection process. Activities to be performed in each phase are discussed in detail in the following sections.

Note: Clear diamonds represent optional paths; see descriptions below.

**Figure 1 - Inspection Process Activity Diagram**

## 2.1 Planning

The purpose of this phase is to:

* Organize the inspection, in terms of making key decisions about:
  + The participants to be involved (how many and which areas of expertise should be represented).
  + Exactly which materials are to be inspected (making sure that critical areas of the system are covered, that the materials make sense as a coherent piece, and that the amount of material is appropriate for the time available).
  + Facilities (whether meeting rooms are available for the team on the appropriate dates).
* Ensure that the work product is ready to inspect and that the team's time will be well spent on understanding and assessing the quality of the document.

Activities to be completed during this phase are performed by the moderator and include:

1. Determining whether inspection entry criteria have been met.
2. Determining whether an overview meeting is needed.

   If an overview meeting is needed, make sure to schedule it at this point.
3. Selecting the inspection team, based on an understanding of the key stakeholders in the work product, and ensuring that their perspectives are represented on the team. The moderator assigns to appropriate team members key roles to be filled during the inspection:   
        (a) Reader.  
       ( b) Recorder.
4. Calculating the time required for inspection, based on the amount of material that needs to be reviewed, and assuming each inspection meeting will last no more than 2 hours in duration.  
   See also Topic [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections).

   To understand how much material the team can review per unit of time, use metrics from your own organization (if available) or general recommendations, such as the ones included in NASA-STD-2202.93, Software Formal Inspections Standard. You may need to iteratively replan which material will be reviewed, based on the amount of time that is available.
5. Determining the quality focus of the inspection (what properties of the system are of most concern to the inspection team) and ensuring that checklists and other work aides are available to support that focus.
6. Scheduling the inspection meeting time and place.
7. Making sure that the team has access to the inspection materials – mailing a package of materials, emailing links to where the materials can be found, etc.
8. Recording the amount of time spent to date to allow for later analysis of the effort and cost of the inspection.
9. Recording other identifying information for this inspection, such as the names of the project and the moderator, the sections of the work product under inspection, and the participants and their areas of expertise.

### 2.1.1 Defining the Review Perspectives, Quality Focus, and Checklists

It is important to remember that, while the inspection process itself should not change, the details of how it is applied in different contexts should change. The greatest benefit can be received from an inspection by using the process appropriately and by understanding how to focus it on the specific areas of concern for the various work products being inspected.

To ensure the right quality focus during the planning phase, the moderator:

* Identifies the key stakeholders in the work product, i.e., those persons who use helped to produce, or interface with the technical aspects of the system described in that work product.
* Selects team members so that the expertise of each stakeholder is present on the team.
* Reflects on the high-level quality goals of the team – which characteristics are of the highest priority, e.g., reliability, robustness, performance, maintainability, cost.
* Ensures that items on the checklist(s) for use by the team remind the inspectors to focus on indicators of those quality goals.

More detail about which aspects of the inspection can be adapted (to reflect the quality focus) and which cannot (to avoid omitting important and proven best practices) is provided in NASA-STD-2202.93, which is currently under review.

See also [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking),

## 2.2 Overview

The purpose of this phase is to provide inspectors with the background information needed to properly inspect the technical work product, which may include:

* An overview of the work product itself.
* Special considerations of which the review team should be aware of.
* How the work product fits into the overall system/mission being developed.
* New or unique development techniques that have been or will be used in its construction.

Activities to be completed during this phase include:

1. Conduct of the overview meeting (moderator).
2. Presentation of background information (author or other knowledgeable subject matter expert, as appropriate).
3. Assignment of roles to inspectors, if not already done (moderator).
4. Recording of the total time spent in the overview meeting to allow for later analysis of the effort and cost of the inspection (moderator).

## 2.3 Preparation

The purpose of this phase is to give inspectors time to:

* Learn and understand the work product.
* Identify potential defects.
* Prepare to fulfill their assigned roles.
* Prepare for the meeting by logging or otherwise marking potential defects and other issues that should be discussed by the inspection team.

Activities to be completed during this phase include:

(1) Each inspector should:

      (a) Review the assigned checklist to refresh the memory of the issues that should be focused on during the review.  
      (b) Examine the materials for understanding and possible defects.  
      (c) Prepare for the assigned role (reader, recorder, moderator), if applicable.  
      (d) Record the total time spent in preparation and communicate that to the moderator.  
      (e) Provide an indication to the moderator that individual preparation work has been completed and that the individual is ready for the team meeting.

(2) The moderator reviews the degree of preparation work done by inspectors and:

      (a) Organizes the inspection meeting by making note of where the problem areas seem to be (and where there is sure to be some discussion during the meeting).  
      (b) Makes the "GO" or "NO GO" decision on the inspection meeting, i.e., determines whether the team can proceed and is likely to have an effective discussion or whether the meeting and discussion should be postponed until additional preparation work can be done.  
      (c) Records the total time spent on preparation by the team to allow for later analysis of the effort and cost of the inspection.

See also [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking)

## 2.4 Inspection Meeting

The purpose of this phase is to:

* Find, classify, and record defects.
* Record and assign open issues.

Activities to be completed during this phase include:

1. Introduction of people and identification of roles (if inspection-specific roles, such as reader or recorder, and the technical perspective being contributed) in the inspection meeting (moderator).
2. Iteratively,   
     
         (a) The reader presents an appropriate amount of the work product to the inspection team in a logical and orderly manner. The amount should be selected so as to be large enough to have a meaningful discussion over quality issues but not so large that it does not have a logical cohesion. In other words, the reader should not cover the document line by line, yet should not present huge sections either.  
         (b) The inspectors discuss potential issues, determine if there is really a defect there to be fixed, and classify the resulting defects found.  
         (c) The recorder maintains a list of the defects found, along with classifications and dispositions.  
         (d) Issues that require some additional information to resolve are also recorded as action items and assigned to a member of the inspection team to be resolved outside of the inspection meeting.
3. At the end of the meeting, the recorder summarizes the defects recorded and their classifications to make sure that there is a team consensus on the defects to be fixed.
4. The moderator determines if a re-inspection is required, i.e., if reworking the defects will cause the work product to be so different from the inspected version that no assessment of the resulting quality can be safely made, or if a third-hour meeting is needed.
5. The author provides an estimate of how long it will take to rework the defects recorded by the team, so that followup and closeout of the inspection process are possible.
6. If issues were found in documents outside the one under inspection, action items are generated, and team members are assigned to write the appropriate change requests/problem reports.
7. The moderator records the total time spent by the team to allow for later analysis of the effort and cost of the inspection.
8. The moderator reports information about the defects found during the inspection, including the number of defects by severity (major, minor, or clerical) and the number of defects by type.

## 2.5 Third Hour

If a third-hour activity is needed, make sure to schedule it at this point.

The third hour is an optional phase – an unstructured stage in an otherwise highly structured process. There are two possible forms for the third hour:

* Individual work is done by inspectors to resolve discrepancies and open issues.
* Meeting held at the author's request to discuss solutions or improvements.

Activities to be completed during this phase include:

* Resolution of open issues:
  + Complete assigned action item(s) on a timely basis.
  + Provide information to the author.
  + Provide time spent in the third hour to the moderator.
* Discussion of solutions or improvements:
  + Attend the third-hour meeting.
  + Provide time spent in the third hour to the moderator.
* Informing moderator of time spent.

## 2.6 Rework

The purpose of this phase is to remove known defects from the work product.

* Major defects are required to be removed.
* Minor and trivial defects are removed at the author's discretion, as cost and time allow.

Activities to be completed during this phase include:

1. Resolution of all major defects found during the inspection meeting by the author.
2. Resolution of minor and trivial defects at the author's discretion, as time and cost allow.
3. Recording of time spent for rework.

## 2.7 Follow-up

The purpose of this phase is to:

* Assure that all major defects detected during the inspection have been corrected.
* Check for the possible introduction of new defects during the correction process.
* Assure that all open issues are resolved in one of the following ways:
  + Decided to be a non-issue, with no action required.
  + Communicated to the author as a defect.
  + Recorded as a problem report or change request.

Activities to be completed during this phase include:

1. Verifying that all major defects have been corrected and checking for the introduction of possible new defects during the correction process (moderator and author).
2. Ensuring that all open issues are resolved and that problem reports and change requests are filed (moderator).
3. Verifying that all exit criteria for inspection are met;  if issues remain open or defects are not corrected, the work product is returned to rework (moderator).
4. Recording of time spent on rework and follow-up (moderator).
5. Communication with the inspection team and cognizant manager the outcome of the inspection (moderator).

See also [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements),

## 2.8 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 3. Barriers and Enablers

There is a need for local champions and management support.

Development teams who implement inspections need trained moderators and support materials. Providing explicit training helps improve effectiveness.

Inspections work best if management is not present at inspections, removing the threat that defect information could be used to evaluate workers.

The primary inhibitors to inspection use seem to be in the realm of developer motivation: inspections can be perceived as being labor-intensive in nature, although the return on investment, when done correctly, rewards the effort spent.

# 4. Checklists

This will contain the phase related checklists from the Formal Inspection Standard.

The checklists shown below are good general checklists that cover many areas to be considered in your analysis. Click in the thumbnail to view it. From the viewer, you may download a copy for your use. Each checklist can be used as a starting point and the project can add addition questions that may be relevant to the project, such as safety and security concerns that the project will need.

### 4.1 Software Requirements Checklist  [PAT-013](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-013 - Software Requirements Checklist**

### 4.2 Functional Requirements Checklist [PAT-003](#_tabs-<p>5</p>)

**PAT-003 - Functional Requirements Checklist**

Click on image below to preview all pages and/or download a copy of the asset.

### 4.3 Sample Architectural Checklist [PAT-014](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-014 - Architecture Design Checklist**

### 4.4 Detailed Design Checklist  [PAT-015](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-015 - Detailed Design Checklist**

### 4.5 Functional Design Checklist  [PAT-016](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-016 - Functional Design Checklist**

### 4.6 Sample C Programming Checklist  [PAT-017](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-017 - C Code Inspection Checklist**

### 4.7 Test Plan Checklist  [PAT-018](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-018 - Test Plan Checklist**

### 4.8 Test Procedure Checklist  [PAT-019](#_tabs-<p>5</p>)

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy. 

**PAT-019 - Test Procedure Checklist**

## 4.9 Other Related Checklists

Here are some other checklists related to coding that may be helpful.

* [6.5 - Checklist for C Programming Practices](/spaces/SWEHBVD/pages/102695570/6.5+-+Checklist+for+C+Programming+Practices)
* [6.6 - Checklist for C++ Programming Practices](/spaces/SWEHBVD/pages/102695576/6.6+-+Checklist+for+C+Programming+Practices)
* [6.7 - Checklist for Ada Programming Practices](/spaces/SWEHBVD/pages/102695582/6.7+-+Checklist+for+Ada+Programming+Practices)
* [6.8 - Checklist for Fortran Programming Practices](/spaces/SWEHBVD/pages/102695586/6.8+-+Checklist+for+Fortran+Programming+Practices)
* [6.9 - Checklist for Generic (Non-Language-Specific) Programming Practices](/spaces/SWEHBVD/pages/102695593/6.9+-+Checklist+for+Generic+Non-Language-Specific+Programming+Practices)
* [6.10 - Checklist for General Good Programming Practices](/spaces/SWEHBVD/pages/102695600/6.10+-+Checklist+for+General+Good+Programming+Practices)
* [6.11 - Examples of Programming Practices for Exception Handling](/spaces/SWEHBVD/pages/102695607/6.11+-+Examples+of+Programming+Practices+for+Exception+Handling)

## 4.10Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 5. Resources

## 5.1 Resources

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-521)

  [Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999)](https://llis.nasa.gov/lesson/740 "Click to open in new window")

  Public Lessons Learned Entry: 740.

  

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-015 - Cost Estimation](/spaces/SWEHBVD/pages/102695400/SWE-015+-+Cost+Estimation) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [6.5 - Checklist for C Programming Practices](/spaces/SWEHBVD/pages/102695570/6.5+-+Checklist+for+C+Programming+Practices) * [6.6 - Checklist for C++ Programming Practices](/spaces/SWEHBVD/pages/102695576/6.6+-+Checklist+for+C+Programming+Practices) * [6.7 - Checklist for Ada Programming Practices](/spaces/SWEHBVD/pages/102695582/6.7+-+Checklist+for+Ada+Programming+Practices) * [6.8 - Checklist for Fortran Programming Practices](/spaces/SWEHBVD/pages/102695586/6.8+-+Checklist+for+Fortran+Programming+Practices) * [6.9 - Checklist for Generic (Non-Language-Specific) Programming Practices](/spaces/SWEHBVD/pages/102695593/6.9+-+Checklist+for+Generic+Non-Language-Specific+Programming+Practices) * [6.10 - Checklist for General Good Programming Practices](/spaces/SWEHBVD/pages/102695600/6.10+-+Checklist+for+General+Good+Programming+Practices) * [6.11 - Examples of Programming Practices for Exception Handling](/spaces/SWEHBVD/pages/102695607/6.11+-+Examples+of+Programming+Practices+for+Exception+Handling) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) * [8.56 - Source Code Quality Analysis](/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis) * [PAT-013 - Software Requirements Checklist](/spaces/SITE/pages/114328303/PAT-013+-+Software+Requirements+Checklist) * [PAT-003 - Functional Requirements Checklist](/spaces/SITE/pages/112656804/PAT-003+-+Functional+Requirements+Checklist) * [PAT-014 - Architecture Design Checklist](/spaces/SITE/pages/114328318/PAT-014+-+Architecture+Design+Checklist) * [PAT-015 - Detailed Design Checklist](/spaces/SITE/pages/114328341/PAT-015+-+Detailed+Design+Checklist) * [PAT-016 - Functional Design Checklist](/spaces/SITE/pages/114328352/PAT-016+-+Functional+Design+Checklist) * [PAT-017 - C Code Inspection Checklist](/spaces/SITE/pages/114328366/PAT-017+-+C+Code+Inspection+Checklist) * [PAT-018 - Test Plan Checklist](/spaces/SITE/pages/114328369/PAT-018+-+Test+Plan+Checklist) * [PAT-019 - Test Procedure Checklist](/spaces/SITE/pages/114328380/PAT-019+-+Test+Procedure+Checklist) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Peer Review](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Peer+Review) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.10 Software Peer Reviews and Inspections](/spaces/SWEHBVD/pages/133235386/A.10+Software+Peer+Reviews+and+Inspections) * Peer Reviews may be used in the following activities:    + [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) - reviews of plans, etc.   + [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) - reviews of plans, etc.   + [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) - reviews of requirements, etc.   + [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) - review of architecture and designs   + [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) - review of code   + [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) - review of test plans and procedures   + [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) - review of release documents, operations documents, etc.   + [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) - review of CM plan and audits   + [A.09 Software Risk Management](/spaces/SWEHBVD/pages/133235385/A.09+Software+Risk+Management) - review of risks and related documents |

## 5.6 Process Asset Templates

Click on a link to download a usable copy of the template.

* (PAT-003 - )

  [PAT-003 - Functional Requirements Checklist,](https://swehb.nasa.gov/download/attachments/112656804/PAT-003%20-%20Functional%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, Tab 4,
* (PAT-013 - )

  [PAT-013 - Software Requirements Checklist,](https://swehb.nasa.gov/download/attachments/114328303/PAT-013%20-%20Software%20Requirements%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.1, Also in Peer Review and Requirements Analysis categories.
* (PAT-014 - )

  [PAT-014 - Architecture Design Checklist](https://swehb.nasa.gov/download/attachments/114328318/Architecture%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.3, Also found in Peer Review and Design Analysis categories
* (PAT-015 - )

  [PAT-015 - Detailed Design Checklist](https://swehb.nasa.gov/download/attachments/114328341/Detailed%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.4, Also found in Peer Review and Design Analysis categories.
* (PAT-016 - )

  [PAT-016 - Functional Design Checklist](https://swehb.nasa.gov/download/attachments/114328352/Functional%20Design%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.5, Also found in Peer Review and Design Analysis categories.
* (PAT-017 - )

  [PAT-017 - C Code Inspection Checklist](https://swehb.nasa.gov/download/attachments/114328366/C%20Code%20Inspection%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.6, Also found in Peer Review category.
* (PAT-018 - )

  [PAT-018 - Test Plan Checklist](https://swehb.nasa.gov/download/attachments/114328369/Test%20Plan%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.7, Also found in Peer Review, Test Analysis, and Test Documentation categories.
* (PAT-019 - )

  [PAT-019 - Test Procedure Checklist](https://swehb.nasa.gov/download/attachments/114328380/Test%20Procedure%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 7.10, tab 4.8, Also found in Peer Review, Test Analysis, and Test Documentation categories.

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following:

1. **Deficiencies in Mission Critical Software Development for Mars Climate Orbiter (1999) (Software Reviews can Result in Loss of Spacecraft), Lesson Number 0740[521](#_tabs-<p>5</p>):**  Experience at NASA has also shown that a lack of software reviews can result in loss of spacecraft: "1. Non-compliance with preferred software review practices may lead to mission loss. 2. To identify mission-critical software, require concurrent engineering and thorough review by a team of systems engineers, developers, and end-users... 3) For all mission-critical software (or software interfaces between two systems or two major organizations), systems engineers, developers, and end-users should participate in ... walkthroughs of requirements, design, and acceptance plans."

### 6.2 Other Lessons Learned

* A substantial body of data and experience justifies the use of inspections on requirements. Finding and fixing requirements problems during requirements analysis is more cost-effective than doing so later in the life cycle and is substantially cheaper than finding and fixing the same defects after delivery of the software. Data from NASA, as well as from numerous other organizations, such as IBM, Toshiba, the Defense Analysis Center for Software, all confirm this effect. [277](#_tabs-<p>5</p>)
* The effectiveness of inspections for defect detection and removal in any artifact has also been amply demonstrated. Data from numerous organizations have shown a reasonable rule of thumb to be that a well-performed inspection typically removes between 60  and 90 percent of the existing defects, regardless of the artifact type.[277](#_tabs-<p>5</p>)
