# 8.07 - Software Fault Tree Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695720. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis

8.07 - Software Fault Tree Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695720/8.07+-+Software+Fault+Tree+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695720)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695720&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Description](#tabs-2)
* [3. Goal](#tabs-3)
* [4. Use](#tabs-4)
* [5. Benefits](#tabs-5)
* [6. Resources](#tabs-6)

# 1. Introduction

This topic is provided to assist systems safety engineers and software developers with an introductory explanation of the Software Fault Tree Analysis technique. Most of the information presented in this entry is extracted from Leveson et al. [615](#_tabs-<p>6</p>), [618](#_tabs-<p>6</p>)

It is possible for a system to meet requirements for a correct state and to also be unsafe.  It is unlikely that developers will be able to identify, prior to the fielding of the system, all correct but unsafe states which could occur within a complex system. In systems where the cost of failure is high, special techniques or tools such as Fault Tree Analysis (FTA) need to be used to ensure safe operation. Fault Tree Analysis (FTA) is one method that focuses on how errors, or even normal functioning of the system, can lead to hazards. FTA can provide insight into identifying unsafe states when developing safety-critical systems. Fault trees have advantages over standard verification procedures. Fault trees provide the focus needed to give priority to catastrophic events, and they assist in determining environmental conditions under which a correct or incorrect state becomes unsafe.

The requirements phase is the time to perform a preliminary software fault tree analysis (SFTA). This is a “top-down” analysis, looking for the causes of presupposed hazards. The top of the “tree” (the hazards) must be known before this analysis is applied.  The Preliminary Hazard Analysis (PHA) is the primary source for hazards, along with the Requirements Criticality Analysis and other analyses described in the Software Safety Guidebook, NASA-GB-1740.13.

The result of a fault tree analysis is a list of failures or a combination of failures, that can lead to a hazard.  Some of those failures will be in software.  At this top level, the failures will be very general (e.g., “computer fails to raise alarm”).  When this analysis is updated in later phases, the failures can be assigned to specific functions or modules.

FTA was originally developed in the 1960s for safety analysis of the Minuteman missile system. It has become one of the most widely used hazard analysis techniques.  In some cases, FTA techniques may be mandated by civil or military authorities.

Most of the information presented in this section is extracted from Leveson et al. [616](#_tabs-<p>6</p>), [617](#_tabs-<p>6</p>)

See also Topic [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis).

# 2. Description

The Fault Tree Handbook [619](#_tabs-<p>6</p>) from the U.S. Nuclear Regulatory Commission gives the following description of the technique :

"Fault tree analysis can be simply described as an analytical technique, whereby an undesired state of the system is specified (usually a state that is critical from a safety standpoint), and the system is then analyzed in the context of its environment and operation to find all credible ways in which an undesired event can occur. The fault tree is a graphic model of the various parallel and sequential combinations of faults (or system states) that will result in the predefined undesired event. A fault tree thus depicts the logical relationships of basic events that lead to the undesired event - which is the top event of the fault tree".

A sample showing graphical representation symbols for a fault tree is shown in Figure 1 below:

Figure 1: SFTA Graphical Representation Symbols.

# 3. Goal

SFTA is a technique to analyze the safety of software design. The goal of SFTA is to show that the logic in software design or in an implementation (actual code) will not produce a hazard. The design or code is modified to compensate for those failure conditions deemed to be hazardous threats to the system. In this manner, a system with safer operational characteristics is produced. SFTAs is most practical to use when we know that the system has relatively few states that are hazardous

Developers typically use forward inference to design a system. That is, their analysis focuses on generating the next state from a previously safe state. The software is developed with key assumptions about the state of the system prior to entering the next state. In complex systems that rely on redundancy, parallelism, or fault tolerance, it may not be feasible to go exhaustively through the assumptions for all cases.

The SFTA technique provides an alternative perspective that uses backward inference. The experience from projects that have employed SFTA shows that this change of perspective is crucial to the issue of finding safety errors. The analyst is forced to view the system from a different perspective, one that makes finding errors more apparent.

SFTA is very useful for determining the conditions under which fault tolerance and fail-safe procedures should be initiated. The analysis can help guide safety engineers in the development of safety-critical test cases by identifying those areas most likely to cause a hazard. On larger systems, this type of analysis can be used to identify safety-critical software modules, if they have not already been identified.

SFTA is language independent and can be applied to any programming language (high level or low level) as long as the semantics are well defined. The SFTA is an axiomatic verification where the postconditions describe the hazard rather than the correctness condition. This analysis shows that, if the weakest precondition is false, the hazard or postcondition can never occur and conversely, if the precondition is true, then the program is inherently unsafe and needs to be changed.

Software fault trees should not be reviewed in isolation from the underlying hardware, because to do so would deny a whole class of interface and interaction problems. Simulation of human failure such as operator mistakes can also be analyzed using the SFTA technique.

The symbols used for the graphical representation of the SFTA, to a large extent, have been borrowed from the hardware fault tree set (see Figure 1: SFTA Graphical Representation Symbols) [620](#_tabs-<p>6</p>) . This facilitates the linking of hardware and software fault trees at their interfaces to allow the entire system to be analyzed.

The SFTA makes no claim as to the reliability of the software. When reusing older modules, a new safety analysis is necessary because the fundamental safety assumptions used in the original design must be validated in the new environment. The assertion that highly reliable software is safe is not necessarily true. In fact, safety and reliability at times run counter to each other. An example of this conflict can be found in the actual experience of air traffic controllers from the U.S. who attempted to port an air traffic control software application from the U.S. to Britain. The U.S. software had proved to be very reliable but certain assumptions had been made about longitude (i.e., no provision for both east and west coordinates) that caused the map of Britain to fold in half at the Greenwich meridian [621](#_tabs-<p>6</p>). See also Topic [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality), [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis).

SFTA is not a substitute for the integration and test procedures that verify functional system requirements. The traditional methods that certify that requirements are correct and complete will still need to be used. The SFTA helps provide the extra assurance that is required of systems that are either safety-critical or very costly by verifying that safety axioms have been implemented through a rigorous analysis of those software modules that are responsible for the safety controls of the system.

Two examples of the application of the SFTA technique illustrate that it is cost-effective and helps improve the robustness of a design. SFTA techniques have been applied with success on the Canadian Nuclear Power Plant shutdown software. The software consisted of approximately 6000 lines of Pascal and Fortran code[621](#_tabs-<p>6</p>). Although no errors were detected in SFTA's, the changes implemented improved the robustness of the system. The increased robustness was achieved by inserting run-time assertions to verify safe operating conditions.

Another example of an application of SFTA was on the spacecraft called FIREWHEEL (NASA/ESA). This spacecraft had an Intel 8080 assembly language program of approximately 1200 lines of code that controlled flight and telemetry. The code had already been extensively tested when the SFTA techniques were applied. This analysis discovered that an unanticipated environment hazard could have resulted in the loss of the craft [620](#_tabs-<p>6</p>).

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-6) in the Resources tab.

# 4. Use

Any SFTA must be preceded by a hazard analysis of the entire system. The information in the hazard analysis identifies those undesired events in the system that can cause serious consequences. It should be noted that in complex systems not all hazards can be predetermined. In this respect, the technique does not claim to produce consistent results irrespective of the analyst. It is dependent on the judgment of the individual as to when to stop the process and which hazards to analyze.

The SFTA can be used at different stages of the software life cycle. The earliest stage where the technique should be used is Preliminary Design (if at this point, the design still has excessive TBDs, then the technique is ineffective). In practice, it will be used most frequently at the code level, preferably prior to integration and test.

The basic procedure in an SFTA is to assume that the hazard has occurred and then to determine its set of possible causes. The technique is useless if one starts with the overly generalized hazard "system fails". A more specific failure, such as those identified from the earlier hazard analysis, has to be the starting point for the analysis. The hazard is the root of the fault tree and its leaves are the necessary preconditions for the hazard to occur. These preconditions are listed in the fault tree and connected to the root of the tree via a logical AND or logical OR of the preconditions (see Figure 2: Example of High-Level Fault Tree).

Figure 2: Example of High-Level Fault Tree

In turn, each one of the preconditions is expanded in the same fashion as the root fault (we identify the causes of each precondition). The expansion continues until all leaves describe events of computable probability or the event cannot be analyzed further. The analysis also stops when the precondition is a hardware malfunction that has no dependency on software.

The fault tree is expanded from the specified system-level failure to the software interface level where we have identified the software outputs or lack of them that can adversely affect system operation. At this stage, the analysis begins to take into account the behavior specific to the language. The language constructs can be transformed into templates using preconditions, postconditions, and logical connectives. (For templates of Ada constructs, see Leveson et al.[621](#_tabs-<p>6</p>)) All the critical code must be traced until all conditions are identified as true or false or an input statement is reached.

The technique will be illustrated with an example using a Pascal-like language [620](#_tabs-<p>6</p>). The code will be analyzed for the occurrence of the variable Z being output with a value greater than 100. We should assume B, X, Z are integers.

While B>Xdo

 begin B :=B? 1;

Z := Z + 10;

end

if Z ~ 100 then output Z;

In this piece of code there are assignment statements, an "if" and a "while" construct. The templates for these statements will be applied, starting from the occurrence of the event we are searching for "output Z with Z > 100". Refer to Figure 3: Example Code Fault Tree for the discussion that follows.

Figure 3: Example Code Fault Tree

The templates for the constructs will be drawn showing all the considerations that are required for the analysis to be complete. Some leaves of the tree are not expanded further because they are not relevant to the event or postcondition that we are analyzing. The "if" template shows that the event is triggered by the "then" clause. This follows from the condition in the "if" statement. At this point, we need to determine the preconditions necessary for Z > 100 prior to the entry into the while construct.

In this example, we have only two simple assignments within the "while" construct but they could be replaced by more complex expressions. The analysis would still be similar to that shown here in the example. The "while" construct would be analyzed as a unit and the expressions within the "while" would generate a more complex tree structure as previously described using the language templates to determine the preconditions. By analysis of the transformations in the "while" loop, we arrive at the conclusion that for the Z > 100 to be output, the weakest precondition at the beginning of the code was that for B > X, Z + 1 OB? 10X > 100. At this point, we have identified the weakest condition necessary for this code to output Z with Z > 100. More detailed examples are provided in references and [620](#_tabs-<p>6</p>). Anyone interested in applying the technique should study the examples in the two references or other articles where the technique is illustrated.

The analysis that was shown in the section above determined the preconditions for the event to occur. One way to preclude a hazard from happening is to place an assertion in the code that verifies that the precondition for the hazard, as determined in the analysis, does not occur.  SFTAs point out where to place assertions and the precondition to assert. If the preconditions do occur, some corrective action needs to take place to remedy the problem or, if a remedy is not possible, to mitigate the consequences.

Typically, a small percentage of the total software effort on projects will be spent on safety-critical code. The Canadian Nuclear Power Plant safety-critical shutdown software was reviewed via the SFTA technique in three work months. The cost of this technique is insignificant considering the total amount spent on testing and verification. Full functional verification of the same software took 30 work years [621](#_tabs-<p>6</p>). In cases where no problems are found, the benefits can still justify the investment. The resulting code is made more robust by the inclusion of the safety assertions and the analysis verifies that major hazardous states identified have been avoided.

Due to complexity, the figures from the example cited above (3 work months for 6K lines of code) will probably not scale up. The technique can be selectively applied to address only certain classes of faults in the case where a large body of safety-critical code requires a safety verification.

# 5. Benefits

Overall, the benefits of carrying out an SFTA are well worth the small investment that is made at either the design or code stage, or at both stages. SFTAs can provide the extra assurance required of safety-critical projects. When used in conjunction with the traditional functional verification techniques, the end product is a system with safer operational characteristics than prior to the application of the SFTA technique.

# 6. Resources

## 6.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-615)

  [The space shuttle primary computer system](https://pdfs.semanticscholar.org/d065/4a9cea75ad4e34eed797003e02d854624c7e.pdf "Click to open in new window")

  Alfred Spector, David Gifford Alternate source for article in ACM: https://dl.acm.org/citation.cfm?id=358246
  Communications of the ACM 27 (1984): 874-900
* (SWEREF-616)

  [AN EXPERIMENTAL EVALUATION OF THE ASSUMPTION OF INDEPENDENCE IN MULTI-VERSION PROGRAMMING](http://sunnyday.mit.edu/papers/nver-tse.pdf "Click to open in new window")

  Knight , John C. ; Leveson, Nancy G.,  Also available from IEEE: https://ieeexplore.ieee.org/document/6312924
* (SWEREF-617)

  [Analysis of Faults in an N-Version Software Experiment](http://sunnyday.mit.edu/papers/nver2.pdf "Click to open in new window")

  Brilliant, Susan S. , Virginia Commonwealth Univ., Richmond, Knight, John C. ,Univ. of Virginia, Charlottesville, Leveson, Nancy G. ,Univ. of California, Irvine, IEEE Transactions on Software Engineering archive, Volume 16 Issue 2, February 1990, Page 238-247 Also available: https://dl.acm.org/citation.cfm?id=78716
* (SWEREF-618)

  [NASA Langley Research and Technology-Transfer Program in Formal Methods](https://ntrs.nasa.gov/search.jsp?R=20040111237 "Click to open in new window")

  Butler, Ricky W., Caldwell, James L. , Carreno, Victor A., Holloway, C. Michael,
  Miner, Paul S. (NASA Langley Research Center, Hampton, VA, United States);
  DiVito, Ben L., (Vigyan Research Associates, Inc., Hampton, VA, United States)
* (SWEREF-619)

  [Fault Tree Handbook (NUREG-0492)](https://www.nrc.gov/reading-rm/doc-collections/nuregs/staff/sr0492/ "Click to open in new window")

  NUREG-0492,
* (SWEREF-620)

  [Defense Systems Software Development](https://www.product-lifecycle-management.com/download/DOD-STD-2167A.pdf "Click to open in new window")

  DOD-STD-2167A Military Standard,   (this document has been replaced by DOD-STD-498, which was cancelled in 1998 when IEEE 12207 was released) https://standards.ieee.org/standard/12207-2017.html
* (SWEREF-621) JPL Software Systems Safety Handbook SSSHB 3.2/Draft JPL Software Systems Safety Handbook

## 6.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 6.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-037 - Software Milestones](/spaces/SWEHBVD/pages/102695415/SWE-037+-+Software+Milestones)        * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.09 - Software Safety Analysis](/spaces/SWEHBVD/pages/102695725/8.09+-+Software+Safety+Analysis) * [8.58 - Software Safety and Hazard Analysis](/spaces/SWEHBVD/pages/102695750/8.58+-+Software+Safety+and+Hazard+Analysis) |

## 6.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>6</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 6.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |
