# 8.08 - COTS Software Safety Considerations

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695724. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations

8.08 - COTS Software Safety Considerations

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695724/8.08+-+COTS+Software+Safety+Considerations#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695724)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695724&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. COTS SW Safety Considerations](#tabs-1)
* [2. Resources](#tabs-2)

# 1. COTS SW Safety Considerations

The decision to create, operate and maintain a system or system of systems needs to consider many aspects besides the technical requirements that are needed to bring about the functions needed to accomplish the mission. The development, operational, and maintenance infrastructure must also be considered. While the actual product is naturally the main focus of the development activity, there is also a need to assure the tools and processes that support development, test, certification, operations, and maintenance. COTS software can play a significant role in all aspects of both the final products and the support framework.

First, there are the “embedded” COTS which are an integral part of a system and are not really noticed as a separate entity once integrated into with the rest of the system. Some COTS are fairly straight forward: bus controllers and other standard communication packages, perhaps a GPS system or gyroscope system needs to be incorporated, digital camera remote operations, telescope pointing and tracking, user interfaces, graphical output packages, etc. Then there is the main embedded COTS in use, Operating Systems. Even compilers and their library programs used for developed code can be considered a form of embedded COTS. These COTS can be commercial, open-source, and/or a combination (e.g., Linux).

The other types of software COTS are either standalone or separate packages that are perhaps then networked together with either other COTS or developed code or a combination. But it is clear, for the most part, that they are their own program or system. These would be things like a commercial configuration management system, problem reporting and corrective action system built on a commercial database, internet/web-access packages, telecommunications packages, MATLAB, etc. These COTS usually have user-created applications programmed on to them for the specific needs of each user or, in the case of a database package, must be loaded with user-specific data and possibly also programmed to appear and create reports and other outputs as desired for the particular user. On the other hand, they may be tools such as debuggers and code checkers (e.g., Coverity, SPIN), development environments, translators, VDHL Compilers, PROM/E-PROM programmers, etc. When used on or for safety-critical software or to transmit, manipulate, and store safety-critical data, then those also need to be assessed for hazard contributions.

## 1.1 Safety Critical

NASA uses a simple initial test defined in the definition of "safety-critical software" in NASA-STD-8739.8 [278](#_tabs-<p>2</p>) to determine what software is "safety-critical". This is the first step in determining if software plays a role in the safety of the system. This can and should be applied to COTS software as well. Once the software is determined to be safety-critical, the level and extent of criticality must be determined and from there, the software safety and assurance efforts are scoped and tailored to match the criticality, likelihood of failure, complexity, time to criticality, autonomy and software effort. How COTS software fits into the overall systems safety process of hazard analyses, reports and certification should be the same as developed software, with some modifications. A good initial trade study comparing the COTS software’s functional capabilities, performance measures, known limitations, interface specifications, etc. should provide the assurance and safety community with a significant head start. The first step is either involving the SW Assurance and system safety personnel in on the trade study or at least requiring that a copy of the trade study results be sent to Software Assurance.

Starting with the initial NASA Software Safety-Critical Test from NASA-STD-8739.8, if a preliminary systems hazard analyses determines that the system in which COTS software is resident is safety-critical or if the system for which COTS is used as a tool to test or validate software or hardware is safety-critical, then the COTS is safety-critical.

## 1.2 COTS as Safety Critical

It is also possible to apply this safety-critical test directly to the COTS software.  If the requirements COTS is to perform are known and its activities in relation to a system deemed safety-critical are known, then application of the Software Safety-Critical Test to the COTS software should be straight forward. If the COTS software is identified as safety-critical, then the real work begins. Assuming for now that the source code is not available, the main requirements for performing software safety processes, including hazard analyses, need only minor modifications. For instance, the requirement to uniquely identify safety-critical requirements and trace them into the design, code, and tests allows for quickly determining where to look for safety impacts when software changes. When the requirements that a COTS software product fulfills are determined to be safety-critical, then a safety operation (command, calculation, data transfer, etc.), mitigation, or control is documented and traced into associated interfaces, wrappers and glueware as well as hazard reports and verification efforts. Changes to safety-critical COTS software either by application changes, upgrades, problem fixes, etc. would need to undergo hazard analyses once designated as safety-critical. Resulting requirements must be documented, appropriately identified as safety criticality, whether performed by the COTS software or developed software or a combination.

For some reason, there is often a general misguided thought process that if the code is not available, safety and reliability analyses cannot be performed. But when the processes for either safety or reliability analyses of developed software are appropriately performed, most of the analyses which contribute to better designs take place based on detailed requirements and functionality. Of course, hazards that are identified within COTS software can not usually impact the design that led to the development of that COTS package, however, the design of the wrappers can and will be impacted and perhaps the operating and uses limited. Tests and verification that must prove that the COTS software is controlled, and mitigated properly as identified in one or more hazard reports which have to look at whether or not the COTS performs any safety functions, could its performance or failure to perform impact a system that is safety-critical. 

Of course, many of NASA’s operating systems will fall under the Software Safety-Critical Test criteria and when used in a safety-critical system must be analyzed for hazard contributions and even potential hazard mitigations. To date, most of the analyses of the COTS operating systems is done upfront during the selection process and seldom thought of again. Those who design the applications that run on those COTS OS are not always those who selected the OS and thus, though given the specifications and parameters, maybe even the limitations of a “safety certified” OS, there is little further thought given to including the OS in the hazard analyses. The work on COTS OS in safety-related systems discusses the main aspects of safety to be considered for a COTS OS and should be incorporated into NASA’s generic software safety hazard analyses with specific instances of when these safety COTS OS potential failure areas might contribute to specific hazards. For the NASA Constellation Program, the new space launch and transportation systems program, an approach of presenting a set of “generic” software hazard contributors in one hazard report where the common methods for controls, mitigations, and verifications can be expounded upon once has been adopted. Then, when specific hazard reports listing one or more of those “generic” SW hazards as a cause or contributor, the generic hazard report is referenced rather than repeating a common failure mode, mitigation, and verification method in each. This approach would allow for the inclusion of COTS OS potential failures as well as other possible identified COTS common failure modes and keep them in the thoughts of the developers throughout the development and hazard analysis process.

\*Adapted from: Wetherholt, Martha, “The Software Assurance of COTS Software Products,” [171](#_tabs-<p>2</p>)

See also [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements), [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels),

## 1.3 Additional Guidance

There are links in many SWEs and Topics referencing this topic. Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-171)

  [The Software Assurance of COTS Software Products](https://arc.aiaa.org/doi/abs/10.2514/6.2009-1920 "Click to open in new window")

  Wetherholt, Martha, Session: I@A-33: Software Assurance, AIAA Infotech@Aerospace Conference, 06 April 2009 - 09 April 2009, Seattle, Washington,
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
| * [SWE-020 - Software Classification](/spaces/SWEHBVD/pages/102695405/SWE-020+-+Software+Classification) * [SWE-027 - Use of Commercial, Government, and Legacy Software](/spaces/SWEHBVD/pages/102695410/SWE-027+-+Use+of+Commercial+Government+and+Legacy+Software) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-156 - Evaluate Systems for Security Risks](/spaces/SWEHBVD/pages/102695512/SWE-156+-+Evaluate+Systems+for+Security+Risks) * [SWE-192 - Software Hazardous Requirements](/spaces/SWEHBVD/pages/102695527/SWE-192+-+Software+Hazardous+Requirements) * [SWE-201 - Software Non-Conformances](/spaces/SWEHBVD/pages/102695535/SWE-201+-+Software+Non-Conformances) * [SWE-202 - Software Severity Levels](/spaces/SWEHBVD/pages/102695536/SWE-202+-+Software+Severity+Levels) * [SWE-203 - Mandatory Assessments for Non-Conformances](/spaces/SWEHBVD/pages/102695537/SWE-203+-+Mandatory+Assessments+for+Non-Conformances) * [SWE-205 - Determination of Safety-Critical Software](/spaces/SWEHBVD/pages/102695539/SWE-205+-+Determination+of+Safety-Critical+Software) * [SWE-211 - Test Levels of Non-Custom Developed Software](/spaces/SWEHBVD/pages/102695542/SWE-211+-+Test+Levels+of+Non-Custom+Developed+Software) * [SWE-219 - Code Coverage for Safety Critical Software](/spaces/SWEHBVD/pages/105709626/SWE-219+-+Code+Coverage+for+Safety+Critical+Software)        * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [6.4 - Checklist for Choosing Off-The Shelf Software (OTS)](/spaces/SWEHBVD/pages/102695563/6.4+-+Checklist+for+Choosing+Off-The+Shelf+Software+OTS) * [7.19 - Software Risk Management Checklists](/spaces/SWEHBVD/pages/102695678/7.19+-+Software+Risk+Management+Checklists) * [7.20 - Assessing - Meets the Intent](/spaces/SWEHBVD/pages/102695679/7.20+-+Assessing+-+Meets+the+Intent) * [8.02 - Software Quality](/spaces/SWEHBVD/pages/102695703/8.02+-+Software+Quality) * [8.20 - Safety Specific Activities in Each Phase](/spaces/SWEHBVD/pages/102695762/8.20+-+Safety+Specific+Activities+in+Each+Phase) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

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
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |
