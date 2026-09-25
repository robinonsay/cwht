# 7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695649. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009

7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695649)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695649&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose and Overview](#tabs-1)
* [2. Resources](#tabs-2)
* [3. Lessons Learned](#tabs-3)

# 1. Purpose

This topic discusses the relationship between the requirements and associated processes for NPR 7150.2, NASA Software Engineering Requirements [083](#_tabs-<p>2</p>), and the content of NASA-STD-7009, Standard for Models and Simulation. Because NASA-STD-7009 is generally applicable to all types of models and simulations (which are most commonly embodied in software), it is important to understand its relevance to NPR 7150.2 and the precedence to be maintained between the two documents. Software developers can use this topic to understand the relevance and applicability of NASA-STD-7009 when developing software under NPR 7150.2.

## 1.1 Introduction

### 1.1.1 Relevant Guidance in NPR 7150.2

As discussed elsewhere, the NPR 7150.2 requirements applicability to the software being developed is determined by the contents of its Appendix C, Requirements Mapping Matrix. Requirement [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements) implements the contents of Appendix C. NPR 7150.2 applies to the development of software models and simulations. The NASA-STD-7009, in turn, describes how models and simulations are to be verified within the bounds of the governing SWE requirements of the NPR 7150.2.

NPR 7150.2 references the content of NASA-STD-7009 via requirement [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) in the presentation of the requirement in its section 4.5.6 and the accompanying Note:

**SWE-070 - Models, Simulations, Tools**

4.5.6 The project manager shall use validated and accredited software models, simulations, and analysis tools required to perform qualification of flight software or flight equipment.

Information regarding specific V&V techniques and the analysis of models and simulations can be found in NASA-STD-7009, Standard for Models and Simulations, NASA-HDBK-7009, Handbook for Models and Simulations, or discipline-specific recommended practice guides

See also Topic [7.20 - Assessing - Meets the Intent](/spaces/SWEHBVD/pages/102695679/7.20+-+Assessing+-+Meets+the+Intent), [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code).

See also requirements [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation), [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports), [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing), [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results), [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations), [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items), [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management).

### 1.1.2 Applicability and Scope of NASA-STD-7009

The applicability and scope are stated in section 1.2 of NASA-STD-7009 [248](#_tabs-<p>2</p>), where the acronym "M&S" denotes "models and simulations":

This NASA Technical Standard establishes uniform practices in modeling and simulation to ensure essential requirements are applied to their design, development, and use, while ensuring acceptance criteria are defined by the program/project and approved by the responsible Technical Authority.

This NASA Technical Standard provides an approved set of requirements, recommendations, and criteria with which models and simulations (M&S) may be developed, accepted, and used in support of NASA activities. As the M&S disciplines employed and application areas involved are broad, the common aspects of M&S across all NASA activities are addressed. The discipline-specific details of a given M&S should be obtained from relevant recommended practices.

### 1.1.3 Implications for Other Models and Simulations

For all other models and simulations that are deemed by the M&S Risk Assessment to be in the scope of NASA-STD-7009, there is the need to ensure that the requirements of both documents are satisfied. From the perspective of NASA-STD-7009, some of the requirements in NPR-7150.2 are not related to M&S, some are supplemental to requirements in NASA-STD-7009, and others are subsets of requirements in NASA-STD-7009.

### 1.1.4 Rationale for STD-7009

The NASA Standard for Models and Simulations (NASA-STD-7009) had its genesis in the Space Shuttle Columbia Accident Investigation (2003). Generally, its purpose is to improve the "development, documentation, and operation of models and simulations" (Diaz Report) and per a September 2006 memo from the Office of the Chief Engineer "which include a standard method to assess the credibility of the models and simulations". After an approximately three-year development period, the NASA Standard for Models and Simulations, NASA-STD-7009 was approved by NASA's Engineering Review Board on July 11, 2008, for voluntary use.

NASA-STD-7009 holds a unique place in the world of modeling and simulation in that it is, by direction, generally applicable to all types of models and simulations (M&S) and in all phases of development, though it is primarily focused on the results of an M&S-based analysis. All standards and recommended practices for M&S to date have either been focused on a single type of M&S (e.g., structures, fluids, electrical controls, etc.) or a particular phase of M&S development (e.g., verification, validation, etc.). NASA management is confronted with numerous types of analyses that may be involved in making critical decisions. Depending on the situation at hand, a common framework for understanding the results and assessing the credibility of that analysis may seem intuitive. However, this is complicated by the vast differences in engineering systems, and, thus, the adoption of a standard like this has been slow.

After formal approval in July 2008, and the update in 2016, the NASA-STD-7009 was largely left to the individual program, project, or M&S practitioner to adopt as they wished. While already existing programs and projects were not required to adopt it, new programs and projects were to adopt it, depending on their needs, desires, and criticality of the M&S-based analysis at hand.

### 1.1.5 Guidance for NASA-STD-7009

Guidance for use and application of NASA-STD-7009 can be found in the NASA-HDBK-7009 Handbook [248](#_tabs-<p>2</p>). This is a comprehensive instruction set on the use and application of NASA-STD-7009 as it relates to the Verification and Validation of Models and Simulations.

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-005)

  [Towards a Credibility Assessment of Models and Simulations, .](https://arc.aiaa.org/doi/abs/10.2514/6.2008-2156 "Click to open in new window")

  AIAA-2008-2156 Blattnig, S.R.; Green, L.L.; Luckring, J.M.; Morrison, J.H.; Tripathi, R.K.; Zang, T.A. (2008).  NASA users can access AIAA documents via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of AIAA documents.
* (SWEREF-009)

  [Agency Risk Management Procedural Requirements,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8000&s=4B "Click to open in new window")

  NPR 8000.4C, NASA Office of Safety and Mission Assurance, 2022. Effective Date: April 19, 2022 Expiration Date: April 19, 2027
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-124)

  [V&V 10 Guide for Verification and Validation in Computational Solid Mechanics.](http://cstools.asme.org/csconnect/CommitteePages.cfm?Committee=100012534 "Click to open in new window")

  ASME (2006). New York, NY Available to members
* (SWEREF-126)

  [Quality Assessment, Verification, and Validation of Modeling and Simulation Applications.](http://www.informs-sim.org/wsc04papers/015.pdf "Click to open in new window")

  Balci, O. (2004). Proceedings of the 2004 Winter Simulation Conference. R.G. Ingalls; M.D. Rossetti; J.S. Smith; B.A. Peters, eds. Dec. 5-8. Piscataway, NJ: IEEE. pp. 122-129.
* (SWEREF-128)

  [Handbook of Simulation: Principles, Methodology, Advances, Applications, and Practice](https://books.google.com/books/about/Handbook_of_Simulation.html?id=dMZ1Zj3TBgAC "Click to open in new window")

  Banks, J., ed. (1998). New York: John Wiley & Sons, Sep 14, 1998,
* (SWEREF-144)

  [A Renewed Commitment to Excellence: An Assessment of the NASA Agency-wide Applicability of the Columbia Accident Investigation Board Report.](http://www.nasa.gov/pdf/55691main_Diaz_020204.pdf "Click to open in new window")

   Diaz, Al,NASA Goddard Space Flight Center (Jan, 2004). CAIB Columbia Accident Investigation Board Report. (August 2003). Vol. 1. PB2005-100968
* (SWEREF-155)

  [Making Hard Decisions; an Introduction to Decision Analysis,](https://epdf.pub/queue/making-hard-decisions-an-introduction-to-decision-analysis-business-statistics.html "Click to open in new window")

  Clemen, R.T. (1996). Second Edition. Pacific Grove, CA: Brooks/Cole. download available from link.
* (SWEREF-164)

  [Experts in Uncertainty: Opinion and Subjective Probability in Science.](https://scholar.google.com/scholar?q=Cooke,+R.M.+%281991%29.+Experts+in+Uncertainty:+Opinion+and+Subjective+Probability+in+Science.&hl=en&as_sdt=0&as_vis=1&oi=scholart&sa=X&ved=0ahUKEwiHq8O2zdLXAhVPkeAKHWYWAsoQgQMIJDAA "Click to open in new window")

  Cooke, R.M. (1991). New York: Oxford University Press.
* (SWEREF-187)

  [Report from the Fidelity Implementation Study Group (ISG). Fidelity ISG Glossary.](https://www.sisostds.org/AboutSISO/Overview.aspx "Click to open in new window")

  Fidelity ISG Glossary Simulation Interoperability Standards Organization (SISO). (Dec. 1998). Vol. 3.0.  Site still exists at https://www.sisostds.org/. Unable to locate the Fidelity ISG Glossary.
* (SWEREF-198)

  [Guide for Verification and Validation of Computational Fluid Dynamics Simulation,](http://standards.globalspec.com/std/924557/aiaa-g-077 "Click to open in new window")

  AIAA G-077. Reston, VA: AIAA. 1998. This document is avaible from AIAA; NASA has access to the AIAA website via the NASA START (AGCY NTSS) system (https://standards.nasa.gov ).
* (SWEREF-200)

  [A Common M&S Credibility Criteria-set Supports Multiple Problem Domains.](http://www.aegistg.com/Technical_Papers/A%20common%20MS%20credibility%20criteria-set%20supports%20multiple%20problem%20domains%20v3%201.pdf "Click to open in new window")

  Hale, J.P.; Hartway, B.L.; Thomas, D.A. (2007). The 5th Joint Army-Navy-NASA-Air Force (JANNAF) Modeling and Simulation Subcommittee Meeting, May, CDJSC 49. Columbia, MD: Johns Hopkins University.
* (SWEREF-202)

  [A Proposed Model for Simulation Validation Process Maturity,](https://www.researchgate.net/publication/273204187_A_Proposed_Model_for_Simulation_Validation_Process_Maturity "Click to open in new window")

  Harmon, S.Y.; Youngblood, S.M. (2005). Vol. 2, No. 4, pp. 179-190. Conference: Spring 2003 SISO Simulation Interoperability Workshop, At Kissimmee, FL
* (SWEREF-222)

  [IEEE Computer Society, "IEEE Standard Glossary of Software Engineering Terminology,"](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=2238 "Click to open in new window")

  IEEE STD 610.12-1990, 1990. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-240)

  [CFD Code Validation of Wall Heat Fluxes for a GO2/GH2 Single Element Combustor,](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20050203996.pdf "Click to open in new window")

  Lin, J.; West, J.S.; Williams, R.W.; Tucker, P.K. (2005). AIAA-2005-4524 .
* (SWEREF-248)

  [NASA HANDBOOK FOR MODELS AND SIMULATIONS: AN IMPLEMENTATION GUIDE FOR NASA-STD-7009](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009 "Click to open in new window")

  NASA-HDBK-7009 Revision: A, Document Date: 2019-05-08,
  Next 5-Year Review Date: 2024-05-08
* (SWEREF-251)

  [Simulation Credibility Scale and Credibility Assessment Scale,](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20120006603.pdf "Click to open in new window")

  Mehta, U.B. (2007). The 5th Joint Army-Navy-NASA-Air Force (JANNAF) Modeling and Simulation Subcommittee Meeting, CDJSC 49, May, CPIAC. Columbia, MD: Johns Hopkins University.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-272)

  [NASA Standard for Models and Simulations,](https://standards.nasa.gov/standard/nasa/nasa-std-7009 "Click to open in new window")

  NASA-STD-7009A w/ CHANGE 1: ADMINISTRATIVE/ EDITORIAL CHANGES 2016-12-07
* (SWEREF-286)

  [NASA General Safety Program Requirements,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=8715&s=3D "Click to open in new window")

  NPR 8715.3D, Effective Date: December 16, 2021, Expiration Date: December 21, 2026
* (SWEREF-288)

  [Predictive Capability Maturity Model for Computational Modeling and Simulation,](https://cfwebprod.sandia.gov/cfdocs/CompResearch/docs/Oberkampf-Pilch-Trucano-SAND2007-5948.pdf "Click to open in new window")

  Oberkampf, W.L.; Pilch, M.; Trucano, T.G. (October 2007), SAND2007-5948. Sandia National Laboratories: Albuquerque, New Mexico 87185 and Livermore, California 94550.
* (SWEREF-311)

  [VV&A Recommended Practices Guide,](https://vva.msco.mil/ "Click to open in new window")

  Defense Modeling and Simulation Office. http://vva.dmso.mil/.
* (SWEREF-312)

  [Sensitivity Analysis: Gauging the Worth of Scientific Models.](http://www.wiley.com/WileyCDA/WileyTitle/productCd-0471998923.html "Click to open in new window")

  Saltelli, A.; Chan, K.; Scott, E.M., eds. (2000). Chichester, England: John Wiley & Sons. Available via http://www.wiley.com/WileyCDA/WileyTitle/productCd-0471998923.html.
* (SWEREF-414)

  [NASA Standard for Models and Simulations: Credibility Assessment Scale,](https://arc.aiaa.org/doi/abs/10.2514/6.2009-1011 "Click to open in new window")

  Babula, M. et al. (2008). Published Online:15 Jun 2012 https://doi.org/10.2514/6.2009-1011
* (SWEREF-460) NPR 7150 traced to NASA-STD-8739 8 and NASA-STD-8719 13B\_20100924 This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-582)

  [Performance Decrease due to Propulsion Thruster Plume Impingement on the Voyager Spacecraft](https://llis.nasa.gov/lesson/377 "Click to open in new window")

  Public Lessons Learned Entry: 377.

  

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-055 - Requirements Validation](/spaces/SWEHBVD/pages/102695440/SWE-055+-+Requirements+Validation) * [SWE-065 - Test Plan, Procedures, Reports](/spaces/SWEHBVD/pages/102695448/SWE-065+-+Test+Plan+Procedures+Reports) * [SWE-066 - Perform Testing](/spaces/SWEHBVD/pages/102695449/SWE-066+-+Perform+Testing) * [SWE-068 - Evaluate Test Results](/spaces/SWEHBVD/pages/102695451/SWE-068+-+Evaluate+Test+Results) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-073 - Platform or Hi-Fidelity Simulations](/spaces/SWEHBVD/pages/102695454/SWE-073+-+Platform+or+Hi-Fidelity+Simulations) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-139 - Shall Statements](/spaces/SWEHBVD/pages/102695497/SWE-139+-+Shall+Statements)        * [7.20 - Assessing - Meets the Intent](/spaces/SWEHBVD/pages/102695679/7.20+-+Assessing+-+Meets+the+Intent) * [8.11 - Auto-Generated Code](/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Verification and Validation](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Verification+and+Validation) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) |

# 3. Lessons Learned

### 3.1 NASA Lessons Learned

A documented lesson from the NASA Lessons Learned database notes the following:

* **Performance Decrease due to Propulsion Thruster Plume Impingement on the Voyager Spacecraft, Lesson Number: 0377[582](#_tabs-<p>2</p>):** "A 21% shortfall in Voyager's velocity change was suspected to be due to exhaust plume impingement. Due to the complexity of spacecraft/thruster configurations, additional care must be taken in the development and utilization of spacecraft and plume models. Analysis should be conducted on early and final designs.".

### 3.2 Other Lessons Learned

The requirements for a NASA Standard have matured from the Columbia Accident Investigation Board (CAIB) Report.  The CAIB report found problems pertaining to "ineffective and inconsistent application of M&S tools, along with cases of misuse."  It called on NASA to "develop, validate, and maintain physics-based computer models to evaluate Thermal Protection System damage from debris impacts. These tools should provide realistic and timely estimates of any impact damage from possible debris from any source that may ultimately impact the Orbiter." NASA was to establish impact damage thresholds that trigger responsive corrective action, such as on-orbit inspection and repair, when indicated.

Lessons Learned and their applicability to the need to perform verification and validation are well documented in the above identified resources.  These should be reviewed and retained by any program or project utilizing Modeling and Simulation products throughout the Software development life cycle.
