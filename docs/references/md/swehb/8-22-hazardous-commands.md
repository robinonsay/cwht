# 8.22 - Hazardous Commands

> NASA Software Engineering Handbook (SWEHB Ver D), page id 109969544. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/109969544/8.22+-+Hazardous+Commands

8.22 - Hazardous Commands

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/109969544/8.22+-+Hazardous+Commands#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=109969544)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=109969544&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Introduction

## 1.1 Software Hazard Causes

The identification of hazardous commands is required for implementation of the Computing System Requirements in both the current Standard, NASA-STD-8739.8 [278](#_tabs-<p>2</p>), and in the previous version, NASA-STD-8719.13 [271](#_tabs-<p>2</p>).  A hazardous command is defined as:

* A command whose execution could lead to a critical or catastrophic hazard as identified in the Hazard Analysis. This includes but not limited to:
  + inadvertent execution
  + out-of-sequence execution or
  + incorrect execution
* A command whose execution can lead to a reduction in the control of a hazard identified in the Hazard Analysis reports. This includes but not limited to:
  + reduction in failure tolerance against a hazard or
  + the elimination of an inhibit a hazard).

Commands can be internal to a software set (e.g., from one component to another) or external (e.g., crossing an interface to/from hardware or a human operator or any other external source).

Longer command paths increase the probability of an undesired or incorrect command response due to:

* noise on the communications channel,
* link outages,
* equipment malfunctions, or
* human error.

## 1.2 Hazard Considerations

**When there is a hazardous command, the following should be considered:**

* All defined prerequisite conditions for the safe execution of an identified hazardous command should be met prior to executing the command. Examples of prerequisite conditions include:
  + correct mode,
  + correct parameters
  + correct configuration,
  + component availability,
  + proper sequence,
  + parameters in range, and
  + input verification.

If prerequisite conditions have not been met, the software should reject the command and alert the crew, ground operators, or controlling executive.

* Software that executes hazardous commands should notify the initiating crew, ground operator, or controlling executive upon execution or provide the reason for failure or response of completion to execute a hazardous command.
* The software interface should have the ability to identify and display the status of each software inhibit.
* Software should make available the current status of software inhibits associated with hazardous commands to the crew, ground operators, or controlling executive.
* All software inhibits associated with a hazardous command should have a unique identifier.
* If an automated sequence is already running when a software inhibit associated with a hazardous command is executed, the sequence should complete before the software inhibit is started unless automated sequence contributes to the hazard.
* Software should have the ability to resume control of an inhibited operation after deactivation of a software inhibit associated with a hazardous command and after all prerequisite checks have been verified.

## 1.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
|  |

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
