# 5.03 - Inspect - Software Inspection Peer Reviews Inspections

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695657. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections

5.03 - Inspect - Software Inspection, Peer Reviews, Inspections

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695657)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695657&showCommentArea=true&showComments=true#addcomment)

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

Minimum recommended content for the Software Inspections and Peer Reviews. 

1. 1. Identification information (including item being reviewed/inspected, review/inspection type (e.g., requirements inspection, code inspection, etc.) and review/inspection time and date).
   2. Summary on total time expended on each software peer review/inspection (including total hour summary and time participants spent reviewing/inspecting the product individually).
   3. Participant information (including total number of participants and participant's area of expertise).
   4. Total number of defects found (including the total number of major defects, total number of minor defects, and the number of defects in each type such as accuracy, consistency, completeness).
   5. Peer review/inspection results summary (i.e., pass, re-inspection required).
   6. Listing of all review/inspection defects.

# 2. Rationale

The recommended metrics and data are ones that allow monitoring of the effectiveness of peer reviews/inspections and that develop an understanding of how to plan and perform an inspection leading to optimal effectiveness.

**a. Identification information:** At the most basic level, a peer review's/inspection's results need to be traceable to the document inspected, so that the team can make sure problems get fixed and so that a quality history of key system components can be developed. It is also important to be able to trace results to the type of document inspected. Research and experience have shown that many key inspection parameters will vary greatly from one type of document to another, even though the same basic inspection procedure applies. For example, teams are often larger for reviews of requirements documents since more stakeholders may need to have their concerns incorporated. The review time and date can be used to detect whether inspection planning or results have varied over time, e.g., over different phases of the project.

**b. Total time expended:** When done correctly, peer reviews/inspections require a non-trivial amount of effort. This metric can help build baselines of how much time is required to perform an inspection, so that future project plans can be constructed realistically, allocating appropriate time for the inspections needed. The effort expended on an inspection also allows an analysis of the return on investment. Moderators pay attention to the person-hours expended on a peer review/inspection and the benefit received (e.g., the number of defects found) to make sure that the time is well spent and to find opportunities for improving the process next time.

* It is worth noting that the time spent on individual review needs to be reported separately. This information can help the inspection moderator assess whether to reschedule the meeting. If participants spend too little time preparing, inspection meetings tend to be inefficient; because reviewers are looking at the material for the first time, it is typically hard to really get into a discussion of key technical details. Inspections with too little individual preparation time may find *some* defects but are not likely to find a majority of defects.

**c. Participant info:** The number and perspectives of participants are factors greatly correlated with inspection success and are aspects over which the moderator has direct control. A good rule of thumb is that the number of participants involved in the inspection should be between four and six people, regardless of the type of document being inspected. These values reflect the fact that teams of less than four people are likely to lack important perspectives, while larger teams are more likely to experience dynamics that limit full participation.

* It is important to note that the areas of participants' expertise also is reported. This reflects the idea that the best review process in the world cannot find defects if the required human expertise is missing. Reporting the expertise or job categories that participated allows an analysis of whether the right judgments have been brought to bear for the type of system and the type of document.

**d. Defect found:** A key indicator of peer review/inspection benefit is the number of defects found, i.e., how many defects can be removed from the system early, rather than waiting until later when more work has been done based on these defects and the corrections required are more expensive.

* Teams report the number of major and minor defects separately. Looking for trends in these measures can provide important indications to a team, such as whether the documents being inspected are of very low quality (high number of major defects being found, consistently) or whether the inspection process may not be focused on the most important issues (the vast majority of defects being found are minor defects).

* Teams report the number of defects according to some categorization scheme. This information allows teams to look for trends over time for which they should be aware. For example, if defects of "completeness" are routinely found to be the majority of defects found in inspections, the team should consider whether corrective actions could be taken to help developers understand the components or aspects that need to be included.

**e. Results summary:** Teams indicate whether the document under peer review/inspection passes (i.e., once the corrections are made, it will be of sufficient quality for the development process to proceed) or whether it should be sent for a re-inspection. Re-review/inspection should be chosen when a large number of defects has been found or when the corrections to the defects found would result in major and substantial changes to the work product.

**f. Listing of all defects:** The defects found in an inspection are recorded so that they can be tracked until they are resolved.

See also [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

# 3. Guidance

The recommended metrics are all intrinsic to a well-run peer review/inspection. If the inspection process is being followed adequately, these metrics are already collected along the way to support key stakeholders and their decisions. For example, the names of participants and their areas of expertise are used to support the moderator during planning to compose a team capable of covering the important quality aspects of the document under review. Likewise, defects are recorded and counted to ensure that they are tracked until actually fixed or otherwise dispositioned.

NASA-STD-8739.9 [277](#_tabs-<p></p>), NASA Software Formal Inspection Standard includes lessons that have been learned by practitioners over the last decade. This Standard provides a more detailed list of the inspection data and metrics to be collected.

The creators of NASA-STD-8739.9, NASA Software Formal Inspection Standard, suggest additional best practices related to the collection and content of inspection data and metrics. They recommend that:

* To the extent possible, metrics are collected as they become available during the inspection process, rather than being compiled after the entire inspection is over.
* Teams maintain the data records across the inspections that they perform, so that they can look for trends between the parameters they control and the number and types of defects detected. Parameters that are under an inspection moderator's control include:

* The number and expertise of inspectors.
* The size of the document inspected.
* The amount of effort spent by the inspection team.

Best practices related to the various activities that employ the information recorded in the Software Peer Review/Inspection Report include:

* The moderator reviews the individual inspectors' preparation efforts to decide whether sufficient preparation has been done to proceed with the inspection meeting.
* The moderator ensures that all major defects have been resolved.
* A set of analyses are performed periodically on the recorded data to monitor progress (i.e., the number of inspections planned vs. completed, and to understand the effort and benefits of inspection.
* The outcomes of the analyses are leveraged to support the continuous improvement of the inspection process.

See also [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking), Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).

In creating baselines of inspection performance, it is important to ensure that:

* The units of measure are recorded consistently, e.g., one inspection does not record effort in person-hours and another in calendar-days.
* The definition of measures is consistent, e.g., things like prep time and other activities are counted consistently across all inspections.
* Zeroes and missing values are handled consistently, e.g., if a value is blank, is it clear whether the data could be missing or 0 hours were spent on the given activity?

The following defect severity classification taxonomy is typically used for classifying anomalies or defects identified in inspection meetings:

1. **Major Defect:** A defect in the product under inspection, which, if not corrected, would either cause a malfunction or prevent the attainment of a required result and would result in a Discrepancy Report.
2. **Minor Defect:** A defect in the product under inspection, which, if not fixed, would not cause a malfunction, would not prevent the attainment of a required result, and would not result in a Discrepancy Report but which could result in difficulties in terms of operations, maintenance, and future development.
3. **Clerical Defect:** A defect in the product under inspection at the level of editorial errors, such as spelling, punctuation, and grammar.

The types of identified defects are further classified according to a pre-defined defect taxonomy. The following defect taxonomy has been frequently used to classify code-related anomalies or defects:

1. **Algorithm/method:** An error in the sequence or set of steps used to solve a particular problem or computation, including mistakes in computations, incorrect implementation of algorithms, or calls to an inappropriate function for the algorithm being implemented.
2. **Assignment/initialization:** A variable or data item that is assigned a value incorrectly or that is not initialized properly or where the initialization scenario is mishandled, e.g., incorrect publish or subscribe, incorrect opening of file.
3. **Checking:** Inadequate checking for potential error conditions or an inappropriate response is specified for error conditions.
4. **Data:** Error in specifying or manipulating data items, incorrectly defined data structures, pointer or memory allocation errors, or incorrect type conversions.
5. **External interface:** Errors in the user interface, including usability problems, or in the interfaces with other systems.
6. **Internal interface:** Errors in the interfaces between system components, including mismatched calling sequences and incorrect opening, reading, writing, or closing of files and databases.
7. **Logic:** Incorrect logical conditions on if, case, or loop blocks, including incorrect boundary conditions (e.g., "off by one" errors) being applied, or incorrect expression (e.g., incorrect use of parentheses in a mathematical expression).
8. **Non-functional defects:** Includes non-compliance with standards, failure to meet non-functional requirements, such as portability and performance constraints, and lack of clarity of the design or code to the reader (both in the comments and in the code itself).
9. **Timing/optimization:** Errors that will cause timing (e.g., potential race conditions) or performance problems (e.g., unnecessarily slow implementation of an algorithm).
10. **Other:** Anything that does not fit any of the above categories that is logged during an inspection of a design artifact or source code.

Both experience and research have shown that the parameters under control of the moderator have significant effect on the results of an inspection. Where teams do not have their own baselines of data, Agency-wide heuristics have been developed to assist in planning.

For example, analyzing a database of over 2,400 inspections across the Agency, researchers have found that inspections with team sizes of 4 to 6 inspectors find 12 defects on average, while teams outside this range find on average only 7. [320](#_tabs-<p></p>)

Heuristics for how many pages can be reviewed by a team during a single inspection vary greatly according to the type of the document, which is to be expected since the density of information varies greatly between a page of requirements, a page of a design diagram, and a page of code. Similar to the heuristics for team size, inspection teams that follow the heuristics for document size also find on average significantly more defects than those which do not. [320](#_tabs-<p></p>) The recommended heuristics for document size are listed below. All of these values assume that inspection meetings will be limited to 2 hours. See also [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) for items to be peer reviewed.

|  |  |  |
| --- | --- | --- |
| **Inspection Type** | **Target** | **Range** |
| Functional Design | 20 Pages | 10 to 30 Pages |
| Software Req. | 20 Pages | 10 to 30 Pages |
| Arch. Design | 30 Pages | 20 to 40 Pages |
| Detailed Design | 35 Pages | 25 to 45 Pages |
| Source Code | 500 LOC | 400 to 600 LOC |
| Test Plans | 30 Pages | 20 to 40 Pages |
| Test Procedures | 35 Pages | 25 to 45 Pages |

Teams have consistently found that inspection meetings should last at most 2 hours at a time. Beyond that, it is hard, if not impossible, for teams to retain the required level of intensity and freshness to grapple effectively with technical issues found. This heuristic is a common rule of thumb found across the inspection literature.

Over the course of hundreds of inspections and analysis of their results, NASA's Jet Propulsion Laboratory (JPL) has identified key lessons learned, which lead to more effective inspections, including:

* Inspection meetings are limited to 2 hours.
* Material is covered during the inspection meeting within an optimal page rate range that has been found to give maximum error finding ability.
* Statistics on the number of defects, the types of defects, and the time expended by engineers on the inspections are kept.

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

No additional guidance is available for small projects. The community of practice is encouraged to submit guidance candidates for this paragraph.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-235)

  [An analysis of defect densities found during software inspections](https://ntrs.nasa.gov/search.jsp?R=19920010193 "Click to open in new window")

  John C. Kelly, Joseph S. Sherif, Jonathan Hops, NASA. Goddard Space Flight Center, Proceedings of the 15th Annual Software Engineering Workshop; 35 p
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-320)

  [Fully Employing Software Inspections Data,](http://dx.doi.org/10.1007/s11334-010-0132-1 "Click to open in new window")

  Shull., F., Feldmann, R., Seaman, C., Regardie, M., and Godfrey, S.,Innovations in Systems and Software Engineering - a NASA Journal, 2010.  Available at: http://dx.doi.org/10.1007/s11334-010-0132-1.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-088 - Software Peer Reviews and Inspections - Checklist Criteria and Tracking](/spaces/SWEHBVD/pages/102695473/SWE-088+-+Software+Peer+Reviews+and+Inspections+-+Checklist+Criteria+and+Tracking) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements)        * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Peer Review](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Peer+Review) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.10 Software Peer Reviews and Inspections](/spaces/SWEHBVD/pages/133235386/A.10+Software+Peer+Reviews+and+Inspections) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

No Lessons Learned have currently been identified for this requirement.

### 6.2 Other Lessons Learned

* “Both experience and research have shown that the parameters under control of the moderator have significant effect on the results of an inspection. Where teams do not have their own baselines of data, Agency-wide heuristics have been developed to assist in planning.

For example, analyzing a database of over 2,400 inspections across the Agency, researchers have found that inspections with team sizes of 4 to 6 inspectors find 12 defects on average, while teams outside this range find on average only 7. [320](#_tabs-<p></p>)

Heuristics for how many pages can be reviewed by a team during a single inspection vary greatly according to the type of the document, which is to be expected since the density of information varies greatly between a page of requirements, a page of a design diagram, and a page of code. Similar to the heuristics for team size, inspection teams that follow the heuristics for document size also find on average significantly more defects than those which do not. [320](#_tabs-<p></p>) The recommended heuristics for document size are listed below. All of these values assume that inspection meetings will be limited to 2 hours.

|  |  |  |
| --- | --- | --- |
| **Inspection Type** | **Target** | **Range** |
| Functional Design | 20 Pages | 10 to 30 Pages |
| Software Req. | 20 Pages | 10 to 30 Pages |
| Arch. Design | 30 Pages | 20 to 40 Pages |
| Detailed Design | 35 Pages | 25 to 45 Pages |
| Source Code | 500 LOC | 400 to 600 LOC |
| Test Plans | 30 Pages | 20 to 40 Pages |
| Test Procedures | 35 Pages | 25 to 45 Pages |

Teams have consistently found that inspection meetings should last at most 2 hours at a time. Beyond that, it is hard, if not impossible, for teams to retain the required level of intensity and freshness to grapple effectively with technical issues found. This heuristic is a common rule of thumb found across the inspection literature.

Over the course of hundreds of inspections and analysis of their results, NASA's Jet Propulsion Laboratory (JPL) has identified key lessons learned, which lead to more effective inspections, including:

* + - Inspection meetings are limited to 2 hours.
    - Material is covered during the inspection meeting within an optimal page rate range that has been found to give maximum error finding ability.
    - Statistics on the number of defects, the types of defects, and the time expended by engineers on the inspections are kept.”
