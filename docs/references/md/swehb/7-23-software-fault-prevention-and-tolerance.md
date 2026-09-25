# 7.23 - Software Fault Prevention and Tolerance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 166592616. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance

7.23 - Software Fault Prevention and Tolerance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/166592616/7.23+-+Software+Fault+Prevention+and+Tolerance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=166592616)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=166592616&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Software Fault Prevention and Tolerance

Mission or safety-critical spaceflight systems should be developed to both reduce the likelihood of software faults pre-flight and to detect/mitigate the effects of software errors should they occur in-flight. New data is available that categorizes software errors from significant historic spaceflight software incidents with implications and considerations to better develop and design software to both minimize and tolerate these most likely software failures. [436](#_tabs-<p>2</p>)

## 1.1 New Historical Data Compilation Summary

Previously unquantified in this manner, this data characterizes a set of 55 high-impact historic aerospace "software failure" incidents. [437](#_tabs-<p>2</p>)  Key findings are that software is much more likely to fail by producing erroneous output rather than failing silent, and that rebooting is ineffective to clear these erroneous situations.

|  | Erroneous | Fail-Silent |
| --- | --- | --- |
| Error Manifestations | 85% | 15% |
| Reboot Effectiveness | 2% | 38% |

The origin of each error is categorized to focus specific development, test, and validation techniques for error prevention in each category. This new data focuses on manifestations of unexpected flight software behavior independent of ultimate root cause. It is provided for considerations to improve software design, test, and operations for resilience to the most common software errors and to augment established processes for NASA software development.

| Error Origin | % of Total |
| --- | --- |
| Code / Logic | 58% |
| Configurable Data | 16% |
| Unexpected Sensor Input | 15% |
| Command/Operator Input | 11% |

Forty percent (40%) of software errors were due to absence of code, which includes missing requirements or capabilities, and inability to handle unanticipated situations. Only 18% of these incidents fall within the software discipline itself, with no incidents related to choice of platform or toolset.

| Other Categories | Individually % of Total |
| --- | --- |
| Absence of Code | 40% |
| Unknown-unknowns | 16% |
| Computer Science Discipline | 18% |

## 1.2 Implications and Considerations

These findings indicate that for software fault tolerance, primary consideration should be given to software behaving erroneously rather than going silent, especially at critical moments, and that reboot recoverability can be unreliable. Special care should be taken to validate configurable data and commands prior to each use.

“Test-like-you-fly”, including sensor hardware-in-the-loop, combined with robust off-nominal testing should be used to uncover missing logic arising from unanticipated situations. Some best practice strategies to emphasize pre-flight and during operations based on this data are shown below.

| Software Error Prevention Strategies |
| --- |
| * Utilize a disciplined software engineering and assurance approach with  applicable standards   + NPR 7150.2 NASA Software Engineering Requirements  [083](#_tabs-<p>2</p>)   + SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD  [278](#_tabs-<p>2</p>) |
| * Perform off-nominal scenario, fault, and input testing to expose missing code not covered by requirements alone, with multidisciplinary involvement |
| * Employ logic for handling off-nominal sensor and data input, handling  exceptions, and performing check-point restart |
| * Validate mission data prior to each use |
| * **“**Test like you Fly” with hardware-in-the-loop, especially sensors, over  expected mission durations if possible |
| * Employ two-stage commanding with operator implication acknowledgement for critical commands |

## 1.3 Best Practices for Safety-Critical Software Design

Although best efforts can be made prior to flight, software behavior reflects a model of real-world events that cannot be fully proven or predicted, and traditional system design usually employs only one primary flight software load, even if replicated on multiple strings. Like designing avionic systems to protect for radiation and mistrusted communication ("Byzantine"-faults), safety-critical systems must be designed for resilience to erroneous software behavior. NASA Human-Rating requirements  [024](#_tabs-<p>2</p>) call for in-flight mitigation to hazardous erroneous software behavior, detection and annunciation of critical software faults, manual override of automation, and at least single fault tolerance to software errors without use of emergency systems. Each project/designer must evaluate these requirements against safety hazards and time-to-effect and then invoke appropriate automation fail-down strategies. Common mitigation techniques during flight are shown below.

| In-Flight Software Error Detection and Mitigation Strategies |
| --- |
| * Provide crew/ground insight, control, and override |
| * Employ independent monitoring of critical vehicle automation   + Manual or automated detection, followed by response |
| * Employ software backups (targeted to full) which are:   + Simple (compared to primary flight software)   + Dissimilar (especially in requirements and test) |
| * Enter safe mode (reduced capability primary software subset)   + Examples: restore power/communication, conserve fuel |
| * Uplink new software and/or data (time permitting) |
| * Design system to reduce/eliminate dependency on software |
| * Reboot (often ineffective for logic/data errors) |

See also [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements), [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements), [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software),

## 1.4 Summary

Significant software failures have occurred steadily since first use in space. New data has characterized the behavior of these failures to better understand manifestation patterns and origin. The strategies outlined here should be considered during vehicle design, and throughout the software development and operations lifecycle to minimize the occurrence and impact of errant software behavior.

## 1.5 Terminology

* Software Failure – Software behaving in an unexpected manner causing loss of life, injury, loss/end of mission, or significant close-call
* Byzantine – Active, but possibly corrupted/untrusted communication

## 1.6 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-024)

  [Human-Rating Requirements for Space Systems (Updated w/Change 2)](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8705&s=2C "Click to open in new window")

  NPR 8705.2C, NASA Office of Safety and Mission Assurance, 2008.,
  Effective Date: July 10, 2017, Expiration Date: July 10, 2025
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-435)

  [Considerations for Software Fault Prevention and Tolerance](https://ntrs.nasa.gov/api/citations/20230013383/downloads/TB23%2006%20Software%20Errors%20FINAL%20091923.pdf "Click to open in new window")

  NASA Engineering and Safety Center Technical Bulletin No. 23-06, Prokop, Lorraine,  Mission or safety-critical spaceflight systems should be developed to both reduce the likelihood of software faults pre-flight and to detect/mitigate the effects of software errors should they occur in-flight.
* (SWEREF-436)

  [Software Error Incident Categorizations in Aerospace](https://ntrs.nasa.gov/api/citations/20230012154/downloads/8-17-23%2020230012154.pdf "Click to open in new window")

  NASA/TP−20230012154, NESC-NPP-22-01775, Prokop, Lorraine, Langley Research Center,
* (SWEREF-437)

  [Historical Aerospace Software Errors
  Categorized to Influence Fault Tolerance](https://ntrs.nasa.gov/api/citations/20230012909/downloads/Historical%20Aerospace%20Software%20Errors.pdf "Click to open in new window")

  IEEE Aerospace Conference, Prokop, Lorraine, Johnson Space Center, September 5, 2023 This paper categorizes a set of 55 historic aerospace software error incidents from 1962 to 2023 to determine trends of how and where automation is most likely to fail, behaving unexpectedly.

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-023 - Software Safety-Critical Requirements](/spaces/SWEHBVD/pages/102695408/SWE-023+-+Software+Safety-Critical+Requirements) * [SWE-134 - Safety-Critical Software Design Requirements](/spaces/SWEHBVD/pages/102695493/SWE-134+-+Safety-Critical+Software+Design+Requirements) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Center Libraries](https://nen.nasa.gov/web/software/wiki) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) |
