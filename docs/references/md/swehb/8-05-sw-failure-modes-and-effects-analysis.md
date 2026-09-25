# 8.05 - SW Failure Modes and Effects Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695706. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis

8.05 - SW Failure Modes and Effects Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695706/8.05+-+SW+Failure+Modes+and+Effects+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695706)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695706&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Purpose & Issues](#tabs-2)
* [3. Process Introduction](#tabs-3)
* [4. Identify Components](#tabs-4)
* [5. Identify Failures](#tabs-5)
* [6. Identify Consequences](#tabs-6)
* [7. Detection & Compensation](#tabs-7)
* [8. Design Changes](#tabs-8)
* [9. Impact of Changes](#tabs-9)
* [10. Forms](#tabs-10)
* [11. Resources](#tabs-11)

# 1. Introduction

The Failure Modes and Effects Analysis (FMEA) is a “bottom-up” analysis technique that looks at how each component could fail, how the failure propagates through the system and whether it can lead to a hazard. This technique requires a fairly detailed design of the system. In the Architectural Design phase, only a preliminary Software FMEA can be completed. See also [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture), [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design), [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations). See also Topic [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description).

A widely used FMEA procedure for hardware is MIL-STD-1629 [092](#_tabs-<p>11</p>), which is based on the following steps:

1. Define the system to be analyzed
2. Construct functional block diagrams
3. Identify all potential item and interface failure modes
4. Evaluate each failure mode in terms of the worst potential consequences
5. Identify failure detection methods and compensating provisions
6. Identify corrective design or other actions to eliminate/control failure
7. Identify impacts of corrective change
8. Document the analysis and summarize the problems which could not be corrected

A Software FMEA (SFMEA) uses the methods of a standard (hardware) FMEA, substituting software components for hardware components in each case. This topic is provided to assist systems safety engineers and software developers with an introductory explanation of the Software Failure Modes and Effects Analysis technique. The information presented here has typically been part of the NASA Safety-Critical Software Analysis course. See also Topic [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists)

Failure Modes and Effects Analysis (FMEA) begins looking for potential system problems while the project is still in the design phase.  Each component in the system is examined, and all the ways it can fail are listed.  Each possible failure is traced through the system to see what effects it will have and whether it can result in a hazardous state.  The likelihood of the failure is considered, as well as the severity of the system failure.

See also [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements),

## 1.1 Terminology:

* **Failure** is the inability of a system or component to perform its required functions within specified performance requirements. An event that makes the equipment deviate from the specified limits of usefulness or performance is also a failure. Failures can be complete, gradual, or intermittent.
  + C**omplete** system failure is manifested as a system crash or lockup.  At this juncture, the system is usually unusable in part, or in whole, and may need to be restarted as a minimum. - What precautions are needed to guard against this, if it is inevitable, then what can be done to ensure the system is safe and can recover safely.
  + **Gradual** system failure may be manifested by decreasing system functionality. Functions may start to disappear and others follow or, the system may start to degrade (as in the speed with which functions are executed may decrease). Often resource management is a fault here, the CPU may be running out of memory or time slice availability.
  + **Intermittent** failures are some of the most frustrating and difficult to solve. Some of these may be cyclical or event-driven or where some condition periodically occurs which is unexpected and/or non-predictive. Usually, an unrealized path through the software takes place under unknown conditions.
* These types of failures should be kept in mind when considering failure modes (described below).  Unlike most hardware failures, software faults don’t usually manifest as “hard” (complete lockup of the system) type system failures. The software doesn’t wear out and break. It is either functional or already broken (but no one knows it)!
* **Failure Mode** is defined as the type of defect contributing to failure; the physical or functional manifestation of a failure (IEEE Std 610.12-1990 [222](#_tabs-<p>11</p>)).  The Failure Mode is generally the manner in which a failure occurs and the degree of the failure’s impact on normal required system operation.  Examples of failure modes are fracture (hardware), the value of data out of limits (software), and garbled data (software).
* **Failure Effect** is the consequence(s) a failure mode has on the operation, function, or status of an item or system.  Failure effects are classified as local effects (at the component), next higher level effects (the portion of the system that the component resides in), and end effect (system level).

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 2. Purposes and Issues

## 2.1 Why do an SFMEA?

SFMEA’s identify key software fault modes for data and software actions. They analyze the effects of abnormalities on other components in the system, and on the system as a whole. This technique is used to uncover system failures from the perspective of the lowest level components.  It is a “bottom-up” (or “forward”) analysis, propagating problems from the lowest levels, up to a failure within the broader system.

Software Fault Tree Analysis (SFTA, See [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis)) is a “top-down” (or “backward”) approach. It identifies possible system failures and asks what could have caused them.  SFTA looks backward from the failure to the component(s) whose defects could cause or contribute to the failure.

The SFMEA asks “What is the effect of this component operates incorrectly?” Failures for the component are postulated and then traced through the system to see what the final result will be. Not all component failures will lead to system problems.  In a good defensive design, many errors will already be managed by the error-handling part of the design.

A Software FMEA takes a systems approach, analyzing the software’s response to hardware failures and the effects on the hardware of anomalous software actions. Doing an FMEA on software can identify:

* Hidden failure modes, system interactions, and dependencies
* Unanticipated failure modes
* Unstated assumptions
* Inconsistencies between the requirements and the design

SFMEA’s are not a panacea.  They will not solve all of your problems!  You will probably not get all of the above results, but you should be a lot closer to a clean system than if you had not done the analysis.

It’s important to interact with other members of the team as you perform an SFMEA.  No one person understands all components, software or hardware.  Have hardware and software designers/engineers review your analysis as you are performing it.  Their point of view will help uncover the hidden assumptions or clarify the thought process that led to a requirement or design element.  SFMEA is not a silver bullet, but a tool to hedge your bets (reduce your risk).

## 2.2 Issues with SFMEA:

If SFMEA’s are so wonderful, why isn’t everyone doing them?  Some of the problems in using the technique are:

* Time-consuming
* Tedious
* Manual method (for now)
* Dependent on the knowledge of the analyst
* Dependent on the accuracy of the documentation
* The questionable benefit of the incomplete failure modes list

The place to reap the greatest advantages of this technique is in requirements and design analysis.  This may take some time, but it is well worth the effort in terms of the different perspectives with which you’ll be able to view the project (hardware, software, operations, etc.).

The technique is considered tedious by some.  However, the end result is a greater and more detailed project and/or system knowledge.  This is most true when used earlier (requirements and design) in the life cycle.  It is easier to use SFMEA later in the project, since components and their logical relationships are known, but at this point (i.e. detailed design and implementation) it is often too late (and expensive) to affect the requirements or design.  Early in the project, lower-level components are conjecture and may be wrong, but this conjecture can be used to drive out issues early.  There must be a balance in the approach.  There is no value in trying to perform analysis on products that are not ready for examination.

The technique is dependent on how much the analyst knows and understands the system. However, as mentioned earlier, the technique should be helpful in bringing out more information as it is being used.  Include more reviewers who have a diverse knowledge of the systems involved.  In addition to looking at the project from different angles, the diversity of background will result in a keener awareness of the impact of changes to all organizations.

Documentation is also very important to use this analysis technique. So, when reviewing documents, use many and different types of resources (systems and software engineers, hardware engineers, system operations personnel, etc.), so that different perspectives have been utilized in the review process.  The obvious benefit is a better product as a result of critique from numerous angles.

See also [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures).

Again, don’t work in a vacuum!  Communication is paramount to success.

Where should you use the SFMEA technique? SFMEA's should be used in all of the following areas, though you should focus on the safety-critical aspects.

* Single Failure Analysis
* Multiple Failure Analysis
* Hardware/Software Interfaces
* Requirements
* Design
* Detailed Design

## 2.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 3. Process Introduction

Figure 1

FMEA analysis begins at the bottom (the “end” items).  Figure 1 shows a subsystem, indicating how each piece interacts with the others.  Logic (and and ors) is not included in this introductory diagram.  The end items are the pressure sensor and temperature sensor. The diagram shows how the failures propagate up through the system, leading to a hazardous event.

Software FMEA’s follow the same procedure used for hardware FMEA’s, substituting software components for the hardware.  Alternately, the software could be included in the system FMEA, if the systems/reliability engineer is familiar with software or if a software engineer is included in the FMEA team.  MIL-STD-1629 [092](#_tabs-<p>11</p>) is a widely used FMEA procedure, and this topic is based on it.

To perform a Software Failure Modes and Effects Analysis (SFMEA), you identify:

* Project/system components
* Ground rules, guidelines, and assumptions
* Potential functional and interface failure modes
* Each failure mode in terms of potential consequences
* Failure/fault detection methods and compensating provisions
* Corrective design or actions to eliminate or mitigate failure/fault
* Impacts of corrective changes

## 3.1 Ground Rules

Before you begin the SFMEA, you need to decide what the ground rules are. There are no right or wrong rules, but you need to know ahead of time what will be considered a failure, what kinds of failures will be included levels of fault-tolerance, and other information.  Some sample ground rules are: (Some words bold for emphasis)

1. All failure modes are to be identified at the appropriate level of detail: component, subsystem, and system.
2. Each experiment's mission shall be evaluated to determine the appropriate level of analysis required.
3. The propagation of failure modes across interfaces will be considered to the extent possible based on available documentation.
4. Failures or faults resulting from defective software (code) shall be analyzed to the function & object-level during detailed design.
5. Failure modes induced by human error shall not be included in this FMEA.
6. The criticality categorization of a hardware item failure mode shall be made on the basis of the worst-case potential failure effect.
7. Identical Items that perform the same function, in the same environment (where the only difference is location) will be documented on a worksheet only once provided that the failure mode effects are identical.
8. Containment structures such as combustion chambers and gas cylinders will be analyzed.
9. For catastrophic hazards, **dual**component failures (items which are one-fault tolerant) are credible.
10. For **catastrophic**hazards, triple component failures (items with two-fault tolerance) are not credible.
11. For critical hazards, single component failures are credible.
12. For critical hazards, **dual**component failures are not credible
13. The release of the contents in a single containment gas bottle does not constitute a hazard of any kind provided that the gases released are pre-combustion gases. (e.g., flammability, toxicity, 02 depletion)
14. Items exempt from failure modes and effects analysis are tubing, mounting brackets, secondary structures, electrical wiring, and electronic enclosures.

Besides the ground rules, you need to identify and document the assumptions you’ve made.  You may not have sufficient information in some areas, such as the speed at which data is expected at an interface port of the system. If the assumption is incorrect, when it is examined it will be found to be false and the correct information will be supplied (sometimes loudly).  This examination will occur when you describe what you believe to be the normal operation of the system or how the system handles faults to the other project members.

Don’t let assumptions go unwritten.  Each one is important.  In other words, “ASSUME NOTHING” unless you write it down. Once written, it serves as a focus to be further explored and exploded.

Try to think “outside the box” – beyond the obvious.  Look at the project as a whole, and then at the pieces/parts.  Look at the interactions between components, look for assumptions, limitations, and inconsistencies.

Figure 2 shows the process of recognizing your assumptions, documenting them, finding out what the reality is, and clarifying them for future reference.

Figure 2

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-11) in the Resources tab.

# 4. Identify Project/System Components

Engineers must know the project, system, and purpose and keep the “big picture” in mind as they perform the analysis.  A narrow perspective can prevent you from seeing interactions between components, particularly between software and hardware.  Communicate with those of differing backgrounds and expertise.

In performing an FMEA, defining whatever is being worked on is the first order of business.  The “whatever” can be a project, system, subsystem, “unit”, or some other piece of the puzzle.  Depending on where the project is in the development life cycle (requirements, design, implementation), documents will exist as resources for performing the SFMEA.  If the documentation is lacking, you will have to do some detective work.  Often there is a collection of semi-formal paperwork on the requirements or design produced by the software team but not written into a formal requirement or design document.  Look for a “Software Development Folder”, talk with the developers, and accumulate whatever information you can. If little is on paper, you will have to interview the developers (and project management, hardware engineers, systems people, etc.) to create your own documentation.

Once you know what the system is and what it is supposed to do, it’s time to start breaking down the system into bite-size chunks.  Break a project down into its subsystems.  Break a subsystem down into its components.  This process begins with a high-level project diagram which consists of blocks of systems, functions, or objects.  Each block in the system will then have its own diagram, showing the components that make up the block (subsystem).  This is a lot of work, but you don’t usually have to do the whole project!  Not every subsystem will need to be detailed to its lowest level.  Deciding what subsystems need further breakdown comes with experience. If in doubt, speak with the project members most familiar with the subsystem or component.

During the requirements phase, the lowest-level components may be functions or problem domains.  At the preliminary (architectural) design phase, functions, Computer Software Configuration Items (CSCIs), or objects/classes may be the components. CSCIs, units, objects, instances, etc. may be used for the detailed design phase.

Take the “blocks” you’ve created and put them together in a diagram, using logic symbols to show interactions and relationships between components.  You need to understand the system, how it works, and how the pieces relate to each other. It’s important to lay out how one component may affect others, rippling up through the system to the highest level. Producing this diagram helps you, the analyst, put the information together. It also provides a “common ground” when you are discussing the system with other members of the team. They can provide feedback on the validity of your understanding of the system.

# 5. Identify Failures

Once you understand the system, have broken it into components, created ground rules, and documented your assumptions, it’s time to get to the fun part: identifying the possible failures.  Failures can be functional (it doesn’t do what it was supposed to do), undesirable responses to bad data or failed hardware, or interface related.

Functional failures will be derived from the Preliminary Hazard Analysis (PHA) and subsequent Hazard Analyses, including subsystem, HAs.  There will probably be hardware items on this list.  This analysis looks at the software’s relationship to hardware. See also Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis),

It is important to identify functions that need protection.  These functions are “must work functions” and “must not work functions”.  A failure may be the compromise of one of these functions by a lower-level software unit.

There are also interfaces to be dealt with.  There are more problems identified with interfaces, according to some researchers than any other aspect of software development. Interfaces are software-to-software (function calls, interprocess communication, etc.), software-to-hardware (e.g. setting a Digital-to-Analog port to a specified voltage), hardware-to-software (e.g. software reads a temperature sensor), or hardware-to-hardware. SFMEA’s deal with all of these except the hardware-to-hardware interfaced.  These are included in the system FMEA.  Interfaces also (loosely) include transitions between states or modes of operation.

As you look at the system, you will find that you need to make more assumptions.  Write them down. When all else fails, and there is no place to get useful information, sometimes a guess is in order.  Again, write it down and go discuss it with others.  The “others” should include people outside of your area of expertise. If you are a software person, go talk with safety and systems.  If you are a safety specialist, talk with systems, software, and reliability experts.

See also Topic [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description)

## 5.1 Examination of Normal Operations as Part of the System

The normal operations of the system include it performing as designed, being able to handle known problem areas, and its fault tolerance and failure response (if designed into the system).  Hopefully, the system was designed to correctly and safely handle all anticipated problems.  The SFMEA will find those areas where *unanticipated* problems create failures.

This step identifies how the software responds to the failures.  This step validates the sufficiency, or lack thereof, of the product “to do what it’s supposed to do”.  This has the side effect of confirming the product developers’ understanding of the problem.  In order to understand the operation of a system, it may be necessary to work and communicate with systems engineering if you are a software engineer.  Systems engineering must also communicate with software engineering, and both must talk with safety and Software Assurance (SA). See also Topic [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists). [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review), [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones), [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight).

The normal operation of the software as part of the system or function is described in this part of the SFMEA.

## 5.2 Identify Possible Areas for Faults

Areas to examine for possible faults include:

* **Data Sampling Rate.**Data may be changing more quickly than the sampling rate allows for, or the sampling rate may be too high for the actual rate of change, clogging the system with unneeded data.
* **Data Collisions.** Examples of data collisions are transmission by many processors at the same time across a LAN, modification of a record when it shouldn't be because of similarities, and modification of data in a table by multiple users in an unorganized manner.
* **Command Failure to Occur.**  The command was not issued or not received.
* **Command Out of Sequence.** There may be an order to the way equipment is commanded on (to an operational state).  For instance, it is wise to open dampers to the ductwork going to the floors, as well as the dampers to bring in outside air before turning on the air handling units of a high rise office building.
* **Illegal Command.**Transmission problems or other causes may lead to the reception of an unrecognized command. Also, a command may be received that is illegal for the current program state.
* **Timing.** Dampers take a long time to open (especially the big ones) so, timing is critical.  A time delay would be necessary to keep from imploding (sucking in) the outside air dampers or possibly exploding the supply air dampers, by turning on the air handler prematurely.
* **Safe Modes.** It is sometimes necessary to put a system that may or may not have software in a mode where everything is safe (i.e. nothing melts down or blows up). Or the software maintains itself and other systems in a hazard-free mode.
* **Multiple Events or Data.** What happens when you get the data for the same element twice, within a short period of time?  Do you use the first or second value?
* **The Improbable.** The engineers or software developers will tell you that something “can’t happen”.  Try to distinguish between truly impossible or highly improbable failures and those that are unlikely but possible.  The improbable **will** happen if you don’t plan for it.
* These are all sorts of things that software can do to cause system or subsystem failures.  Not every software fault will lead to a system failure or shutdown, and even those failures that occur may not be safety-critical.  There are lots more types of faults than these, but these are a good start when looking for things that can go wrong.

## 5.3 Possible Failure Modes

Identify the possible failure modes and effects in an Events Table and Data Table, included in the FORMS section of this topic.

Examples of failure modes are:

**Hardware Failures/Design Flaws**

* Broken sensors lead S/W down the wrong path
* No sensors or not enough sensors - don’t know what H/W is doing
* Stuck valves or other actuators

**Software**

* Memory is overwritten (insufficient buffer or processing times).
* Missing input parameters, incorrect command, incorrect outputs, out of range values, etc.
* The unexpected path took under previously unthought-of conditions.

**Operator**

* Accidental input of an unknown command, or proper command at the wrong time.
* Failure to issue a command at the required time.
* Failure to respond to error conditions within a specified time period.

**Environment**

* Gamma Radiation
* EMI
* Cat hair in hard drive
* Power fluctuations

## 5.4 Start at the Bottom

Go back to the block diagrams you created earlier.  Starting at the lowest level, look at a component and determine the effect of that component failing, in one of its failure modes, on the components in the level above it.

You may need to consider the effect of this component and all the affected components at the next higher level as well.  This must be worked all of the ways up the chain.

This is a long process. However, if the safety-critical portions are fairly isolated in a system, then the analyst will be looking at only those parts of the system that can lead to a critical failure.  This is true for the detailed design and implementation phases/versions of this analysis.  For the requirements and preliminary design phases, the system is more abstract (and therefore smaller and more manageable).

# 6. Identify the Consequences of Failures

The next thing to look at is the effect (consequences) of the defined faults/failures.  It is also important to consider the criticality or severity of the failure/fault.

So far in the FMEA process, we’ve concentrated on the safety perspective.  However, it’s time to look at reliability as well. Like safety, reliability looks at:

* **Severity** may be catastrophic, critical, marginal, or negligible.
* **Likelihood of occurrence** may be probable, occasional, remote or improbable.

Risk levels are defined as 1 through 5, with 1 being prohibitive (i.e. not allowed-must make requirements or design change). The critical categories include the added information of whether the component or function has redundancy or would be a single point of failure.

For each project and Center, there may be some variation in the ranking of severity level and risk level.  This is, after all, not an exact science so much as a professional best guess (best engineering judgment).

The relationship between reliability’s criticality categories and the safety risk level is shown in the following table:

| **Criticality Category** | Relative Safety Risk Level |
| --- | --- |
| 1- A single failure point that could result in a hazardous condition, such as the loss of life or vehicle | Levels 1 to 2 |
| 1R- Redundant components/items for which, if all fail, could result in a hazardous condition | Levels 1 to 2 |
| 2- A single failure point that could result in a degree of mission failure (the loss of experimental data) | Levels 2 to 3 |
| 2R- Redundant items, all of which if failed could result in a degree of mission failure (the loss of experimental data) | Levels 2 to 3 |
| 3- All others | Levels 4 and 5 |

See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality),

# 7. Detection and Compensation

At this step, you need to identify the methods used by the system to detect a hazardous condition, and provisions in the system that can compensate for the condition.

For each failure mode, a fault/failure detection method should be identified. A failure detection mechanism is a method by which a failure can be discovered by an operator under normal system operation or by some diagnostic. Failure detection in hardware is via sensing devices or instruments. In software, this could be done by error detection software on transmitted signals, data or messages, memory checks, initial conditions, etc.

For each failure mode, a compensating provision should be identified, or the risk accepted if it is not a hazardous failure. Compensating provisions are either design provisions or operator actions that circumvent or mitigate.  This step is required to record the true behavior of the item in the presence of an internal malfunction of failure. A design provision could be a redundant item or a reduced function that allows continued safe operation. An operator action could be the notification at an operator console to shut down the system in an orderly manner.

An example: The failure is the loss of data because of a power loss (hardware fault), or because other data overwrote it (a software fault).

Detection:  A critical source and CPU may be backed up by a UPS (uninterruptible power supply) or maybe not.  Detect that power was lost and the system is now on this backup source.  Mark data at time x as not reliable.  This would be one detection scheme.

Compensation for the occurrence of this failure: Is there another source for that data? Can it be re-read? Or just marked as suspect or thrown out and wait for next normal data overwrite it? What if having a UPS, battery backup, redundant power supply? Of course, these are all hardware answers. Can software detect if the data is possibly suspect and tag it or toss it, wait for new input, request for new input, get data from alternate sources, calculate from previous data (trend), etc.?

What if input data comes in faster than expected and was overwriting previous data before it was processed.  How would this system know?   What could be done about it?  For example, a software system normally receives data input cyclically from 40 sources, then due to partial failures or maintenance mode, now only 20 sources are in cycles and the token is passed 2 times faster.  Can buffers handle the increased data rate?

# 8. Design Changes

After a critical hazard has been identified, the project needs to

* Identify corrective actions
* Identify changes to the design
* Verify the changes
* Track all changes to closure

After a critical hazard has been identified it is usually eliminated or mitigated.  The result of either of these two actions is a corrective action.  This corrective action may be via documented new requirements, design, process, procedure, etc.  Once implemented, it must be analyzed and verified to correct the failure or hazard.

It is important to look at the new design, once the change is made, to verify that no new hazards have been created.

# 9. Impacts of Corrective Changes

Corrective action will have an impact.  Impacts can be on the schedule, design, functionality, performances, process, etc. If the corrective action results in a change to the design of the software, then some segment of that software will be impacted. Even if the corrective action is to modify the way an operator uses the system, there is an impact.

You need to go back and analyze the impact of the changes to the system or operating procedures to be sure that they (singularly or jointly) don’t have an adverse effect and do not create a new failure mode for a safety-critical function or component.

Often fixes introduce more errors and there must be a set process to ensure this does not occur in safety-critical systems. Ensure that verification procedures cover the affected areas.

# 10. Forms for Use With SFMEA

| Form Description | Form for viewing and download |
| --- | --- |
| 10.1 SFMEA Worksheet The SFMEA worksheet is used to gather relevant information on the system.  It is also a great place to put the data developed during the analysis. The ID number can be a drawing number, work break down structure number, CSCI identification, or other identification value. The format of the worksheet is shown below. Click on the image below to view or download a copy. |  |
| 10.2 SFMEA Components Worksheet Once elements of the system are identified, list them in this worksheet and identify their functions. Click on the image below to view or download a copy. |  |
| 10.3 SFMEA Data Table For a Software FMEA, the **Data Table** is used to list the effects of **bad data** on the performance of the system or process being analyzed.  A **Data Item** can be an input, output, or information stored, acted on, passed, received, or manipulated by the software.  The **Data Fault Type** is the manner in which a flaw is manifested (**bad data**), including data that is out of range, missing, out of sequence, overwritten, or wrong. Click on the image below to view or download a copy. |  |
| 10.4 SFMEA Events Table The **Events Table** is used to list the effects of an event is performed.  The **Event Item** is the occurrence of some action, either within the software or performed on hardware or other software. An event can be an expected and correct, expected but incorrect, unexpected and incorrect, or unexpected but correct action.  **Event Fault Types** can occur locally (with a module) or on the system as a whole.  Types can include halt (abnormal termination), omission (failure of the event to occur), incorrect logic/event, or timing/order (wrong time or out of sequence). Click on the image below to view or download a copy. |  |

# 11 Resources

## 11.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-092)

  [MILITARY STANDARD: PROCEDURES FOR PERFORMING A FAILURE MODE, EFFECTS, AND CRITICALITY ANALYSIS](http://everyspec.com/MIL-STD/MIL-STD-1600-1699/MIL_STD_1629A_1556/ "Click to open in new window")

  MIL-STD-1629A, (24 NOV 1980) This standard establishes requirements and procedures for performing a failure mode, effects, and criticality analysis (FMECA) to systematically evaluate and document, by item failure mode analysis, the potential impact of each functional or hardware failure on mission success, personnel and system safety, system performance, maintainability, and maintenance requirements.
* (SWEREF-222)

  [IEEE Computer Society, "IEEE Standard Glossary of Software Engineering Terminology,"](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=2238 "Click to open in new window")

  IEEE STD 610.12-1990, 1990. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.

## 11.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-018 - Software Activities Review](/spaces/SWEHBVD/pages/102695404/SWE-018+-+Software+Activities+Review) * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones) * [SWE-039 - Software Supplier Insight](/spaces/SWEHBVD/pages/102695416/SWE-039+-+Software+Supplier+Insight) * [SWE-057 - Software Architecture](/spaces/SWEHBVD/pages/102695442/SWE-057+-+Software+Architecture) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-126 - Tailoring Considerations](/spaces/SWEHBVD/pages/102695490/SWE-126+-+Tailoring+Considerations) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements)        * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [7.07 - Software Architecture Description](/spaces/SWEHBVD/pages/102695632/7.07+-+Software+Architecture+Description) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.07 - Software Fault Tree Analysis](/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis) * [8.17 - Software Safety Audit Checklists](/spaces/SWEHBVD/pages/102695755/8.17+-+Software+Safety+Audit+Checklists) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 11.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>11</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 11.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |
