# 7.18 - Documentation Guidance

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695654. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance

7.18 - Documentation Guidance

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695654/7.18+-+Documentation+Guidance#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695654)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695654&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Resources](#tabs-2)
* [3. Lessons Learned](#tabs-3)

# 1. Purpose

Provide a set of minimum content guidance for software project plans, reports, and procedures. This guidance originally appeared in the version of this Handbook associated with NPR 7150.2, which contained requirements for software documentation.  Those requirements have been removed from the NPR and incorporated into the guidance provided in this Handbook topic.

## 1.1 Introduction

Guidance for each document is provided via the linked pages below. Software documentation resources and lessons learned are also reiterated on those respective pages.

The tab labels are abbreviated as follows:

* [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) — Minimum recommended content for the Software Change Request - Problem Report.
* [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) — Minimum recommended content for the Interface Design Description.
* [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) — Minimum recommended content for the Software Inspections and Peer Reviews.
* [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) — Minimum recommended content for the Software Maintenance Plan.
* [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) — Minimum recommended content for the Software Metrics Report.
* [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) — Minimum recommended content for the Software Configuration Management Plan.
* [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) — Minimum recommended content for the Software Data Dictionary.
* [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) — Minimum recommended content for the Software Development - Management Plan.
* [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) — Minimum recommended content for the Software Requirements Specification.
* [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) — Minimum recommended content for the Software Test Plan at a high level,
* [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) — Minimum recommended content for the Software Test Report.
* [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) — Minimum recommended content for the Software User Manual.
* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) — Minimum recommended content for a Software Design Description.
* [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) — Minimum recommended content for the Software Test Procedures Plan.
* [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan) — Minimum recommended content for the Software Training Plan.
* [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) — Minimum recommended content for the Version Description Document.
* [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content) — Minimum Recommended Content for a Software Assurance Plan.
* [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content) — Minimum Recommended Content for a Safety Plan.
* [5.19 - Software Assurance Status Report Minimum Content](/spaces/SWEHBVD/pages/138707621/5.19+-+Software+Assurance+Status+Report+Minimum+Content) — Minimum Recommended Content for Software Assurance Status Reports.
* [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) — Minimum Recommended Content for IV&V Project Execution Plan.
* [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) — Minimum Recommended Content for Software Requirements Analysis Report.
* [5.22 - Software Design Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641618/5.22+-+Software+Design+Analysis+Report+Minimum+Content) — Minimum Recommended Content for Software Design Analysis Report.
* [5.23 - Testing Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641646/5.23+-+Testing+Analysis+Report+Minimum+Content) — Minimum Recommended Content for Testing Analysis Report.
* [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) — Minimum Recommended Content for Hazard Report.
* [5.25 - Audit Report Minimum Content](/spaces/SWEHBVD/pages/140641711/5.25+-+Audit+Report+Minimum+Content) — Minimum Recommended Content for Audit Report.
* [5.26 - Source Code Quality Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641734/5.26+-+Source+Code+Quality+Analysis+Report+Minimum+Content) — Minimum Recommended Content for Source Code Quality Analysis Report.
* [5.27 - Risk Management Plan - Under Contruction](/spaces/SWEHBVD/pages/195560246/5.27+-+Risk+Management+Plan+-+Under+Contruction) — The content of the Risk Management Plan is established by NPR 8000.4C .  Minimum content is:
* [Copy of 5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/215777623/Copy+of+5.09+-+SRS+-+Software+Requirements+Specification) — Minimum recommended content for the Software Requirements Specification.

Guidance on the Minimum Recommended Content for the Requirements Mapping Matrix is provided via the linked pages below:

* Software Engineering Requirements Mapping Matrix in Topic [7.16 - Appendix C. Requirements Mapping and Compliance Matrix](/spaces/SWEHBVD/pages/102695651/7.16+-+Appendix+C.+Requirements+Mapping+and+Compliance+Matrix)
* Software Assurance Requirements Mapping Matrix in tab 4 of  [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan)

Note: Software Assurance items have been moved to the [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products). The following products have been moved and renamed as appropriate:

* SAP - Software Assurance Plan is in tab 2 of [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan).
* SSP - Software Safety Plan is in tab 3 of  [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan)
* SAANALYSIS is now [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis).
* SADESIGN is now [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis).
* SASTATUS - Software Status Report is now in tab 2 of [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports)

## 1.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-001) Software Development Process Description Document,  EI32-OI-001, Revision R, Flight and Ground Software Division, Marshall Space Flight Center (MSFC), 2010. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-025)

  ["IDD-DID SW Interface Design Description,"](http://www.everyspec.com/DATA+ITEM+DESC+%28DIDs%29/DI-IPSC/download.php?spec=DI-IPSC-81436A.003748.pdf "Click to open in new window")

  DI-IPSC-81436A, Department of Defense, 1999.
* (SWEREF-029) JSC Software Engineering Improvement Plan,  JSC 29542,rev A, NASA Lyndon B. Johnson Space Center (JSC), 2003.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-031)

  [Manager's Handbook for Software Development,](http://www.everyspec.com/NASA/NASA-General/SEL-84-101_REV-1_1990_30283/ "Click to open in new window")

  SEL-84-101, Revision 1, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1990.
* (SWEREF-037)

  [NASA Records Management Program Requirements (Updated w/Change 3),](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=1441&s=1E "Click to open in new window")

  NPR 1441.1E, NASA Office of the Chief Information Officer, Effective Date: January 29, 2015, Expiration Date: January 29, 2024
* (SWEREF-038)

  [NASA Software Engineering Initiative Implementation Plan,](http://www.nasa.gov/pdf/417063main_NSII_Plan.pdf "Click to open in new window")

  Release 1.0, NASA Office of the Chief Engineer, 2002.
* (SWEREF-047)

  ["Recommended Approach to Software Development,"](http://everyspec.com/NASA/NASA-GSFC/GSFC-General/SEL-81-305_REV-3_2419/ "Click to open in new window")

  SEL-81-305, Revision 3, Software Engineering Laboratory Series, NASA Goddard Space Flight Center, 1992.
* (SWEREF-051) Software and Systems Engineering Process Implementation (SSEPI) Plan,
   KSC-PLN-2302, Revision A, NASA Kennedy Space Center (KSC).
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-056) Software Engineering Improvement Plan FY12,  NASA Langley Research Center (LaRC), 2012.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-057)

  [Software Management Plan (SMP) Template,](https://nasa.sharepoint.com/:w:/r/teams/grcsepg/_layouts/15/Doc.aspx?sourcedoc=%7BF3CD9E46-25D3-4622-BDF6-FDDDE2EA7D58%7D&file=GRC-SW-TPLT-SMP%20-%20Software%20Management%20Plan%20Template.docx&action=default&mobileredirect=true&DefaultItemOpen=1 "Click to open in new window")

  GRC-SW-TPLT-SMP, NASA Glenn Research Center (GRC), 2009.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-061)

  [Software Requirements Engineering: Practices and Techniques,](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=875d04783add30ea3ed1381f682207a992169ebc "Click to open in new window")

  JPL Document D-24994, NASA Jet Propulsion Laboratory, 2003.
   See Page 20.
  Approved for U.S. and foreign release.
* (SWEREF-063) Software User Manual (SUM) Template,  GRC-SW-TPLT-SUM, NASA Glenn Research Center (GRC), 2011.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-072) Checklist for the Contents of Software Critical Design Review (CDR),
   580-CK-008-02, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2010.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-073) Checklist for the Contents of Software Preliminary Design Review (PDR),  580-CK-007-02, Software Engineering Division, NASA Goddard Space Flight Center (GSFC), 2010.  This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-074)

  ["David Bowman's Information Management Checklist, Software Testing Procedures" (2009).](http://www.information-management-architect.com/software-testing-procedures.html "Click to open in new window")

  At www.information-management-architect.com. Retrieved May 17, 2011, from http://www.information-management-architect.com/software-testing-procedures.html.
* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-096) Software Design Description Template,  GRC-SW-TPLT-SDD, NASA Glenn Research Center (GRC), 2011.
   This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-110)

  ["Test Plan Template (IEEE 829-1998 Format)", Version 7.0, Software Quality Engineering, 2001.](http://www.ecs.csun.edu/~rlingard/comp480/TestPlanTemplate.pdf "Click to open in new window")
* (SWEREF-140)

  [Sample Software Testing Standards and Procedures,](http://it.toolbox.com/blogs/enterprise-solutions/sample-software-testing-standards-and-procedures-12772 "Click to open in new window")

  Borysowich, Craig, 2006. Observations from a Tech Architect: Enterprise Implementation Issus & Solutions,
* (SWEREF-145)

  [Software Quality Assurance Plan Template,](http://users.csc.calpoly.edu/~jdalbey/308/Resources/NASAsqaplan.html "Click to open in new window")

  California Polytechnic University, extracted from Reusable Software Management Plan, NASA Goddard Space Flight Center (GSFC). Accessed January 3, 2012 from http://users.csc.calpoly.edu/~jdalbey/308/Resources/NASAsqaplan.html.
* (SWEREF-151)

  [An Axiomatic Approach of Software Functionality Measure,](http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=243908&userType=inst "Click to open in new window")

  Chen, Yuan-Tsong; Tanik, Murat M.; Southern Methodist University, Dallas, TX IEEE0-8186-3520-7/92, 1992. Published in: 1992 Proceedings - The Third International Workshop on Rapid System Prototyping
* (SWEREF-157)

  [CMMI for Development, Version 1.3: Improving processes for developing better products and services,](http://www.sei.cmu.edu/reports/10tr033.pdf "Click to open in new window")

  CMMI Development Team (2010). CMU/SEI-2010-TR-033, Software Engineering Institute.
* (SWEREF-165)

  [Software Development Management Planning,](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=5010194 "Click to open in new window")

  Cooper, Jack, IEEE Transactions on Software Engineering, January 1984.  Retrieved December 21, 2011 from http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5010194&tag=1.
* (SWEREF-169)

  [Quality Is Free: The Art of Making Quality Certain.](https://www.amazon.com/Quality-Free-Certain-Becomes-Business/dp/0070145121 "Click to open in new window")

  Crosby, P.B. New York, McGraw-Hill, 1979.
* (SWEREF-176)

  [Software Design Document Data Item Description,](https://sce.uhcl.edu/helm/ms_2167/over_2167.html "Click to open in new window")

  Department of Defense, DI-MCCR-80012A, 1988.
* (SWEREF-188)

  [Software Quality Measurement: A Framework for Counting Problems and Defects,](http://www.sei.cmu.edu/reports/92tr022.pdf "Click to open in new window")

  Florac, William; CMU/SEI-92-TR-022, Software Engineering Institute. 1992.
* (SWEREF-203)

  [An Introduction to Function Point Analysis,](http://www.qpmg.com/fp-intro.htm "Click to open in new window")

  Heller, Roger, Q/P Management Group, Inc. 2002,
* (SWEREF-209)

  [IEEE Standard for System, Software, and Hardware Verification, and Validation](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8055462 "Click to open in new window")

  IEEE Computer Society, IEEE Std 1012-2016 (Revision of IEEE Std 1012-2012), Published September 29, 2017,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards. Non-NASA users may purchase the document from: http://standards.ieee.org/findstds/standard/1012-2012.html
* (SWEREF-211)

  [IEEE Guide for Software Verification and Validation Plans,](http://standards.ieee.org/findstds/standard/1059-1993.html "Click to open in new window")

  IEEE Computer Society, IEEE STD 1059-1993, 1993. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-214)

  [IEEE Recommended Practice for Software Requirements Specifications,](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=5841 "Click to open in new window")

  IEEE Computer Society, IEEE STD 830-1998, 1998. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-215)

  [IEEE Standard for Software and System Test Documentation,](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=4578271 "Click to open in new window")

  IEEE Computer Society, IEEE Std 829-2008, 2008.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-216)

  [828-2012 - IEEE Standard for Configuration Management in Systems and Software Engineering](https://ieeexplore.ieee.org/document/6197683 "Click to open in new window")

  IEEE STD IEEE 828-2012, 2012.,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-217)

  [IEEE Computer Society, "IEEE Standard for Software Project Management Plans",](http://standards.ieee.org/findstds/standard/1058-1998.html "Click to open in new window")

  IEEE 1058-1998, 1998.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-218)

  [IEEE Computer Society, "IEEE Standard for Software Quality Assurance Plans", IEEE 730-2002, 2002.](http://standards.ieee.org/findstds/standard/730-2002.html "Click to open in new window")

   IEEE 730-2002, 2002.  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-221)

  [IEEE Computer Society, "IEEE Standard for Software User Documentation,"](http://standards.ieee.org/findstds/standard/1063-2001.html "Click to open in new window")

  IEEE STD 1063-2001, 2001. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-222)

  [IEEE Computer Society, "IEEE Standard Glossary of Software Engineering Terminology,"](http://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=2238 "Click to open in new window")

  IEEE STD 610.12-1990, 1990. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-228)

  [International Standards Organization (ISO), "Software Engineering - Software Life Cycle Processes - Maintenance,"](http://www.iso.org/iso/cataloguedetail.htm?csnumber=39064 "Click to open in new window")

  ISO/IEC 14764:2006, 2006. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-232)

  [Software Quality Metrics,](http://www.developer.com/tech/article.php/3644656/Software-Quality-Metrics.htm "Click to open in new window")

  Jayaswal, Bijay, and Patton, Peter. (2006). Developer.com.
* (SWEREF-235)

  [An analysis of defect densities found during software inspections](https://ntrs.nasa.gov/search.jsp?R=19920010193 "Click to open in new window")

  John C. Kelly, Joseph S. Sherif, Jonathan Hops, NASA. Goddard Space Flight Center, Proceedings of the 15th Annual Software Engineering Workshop; 35 p
* (SWEREF-252)

  [Software Metrics: SEI Curriculum Module SEI-CM-12-1.1.](http://www.sei.cmu.edu/reports/88cm012.pdf "Click to open in new window")

  Mills, Everald E. (1988). Carnegie-Mellon University-Software Engineering Institute.  Retrieved on December 2017 from http://www.sei.cmu.edu/reports/88cm012.pdf.
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-276)

  [NASA Software Safety Guidebook,](https://standards.nasa.gov/standard/nasa/nasa-gb-871913 "Click to open in new window")

  NASA-GB-8719.13, NASA, 2004. Access NASA-GB-8719.13 directly: https://swehb.nasa.gov/download/attachments/16450020/nasa-gb-871913.pdf?api=v2
* (SWEREF-277)

  [Software Formal Inspections Standard,](https://standards.nasa.gov/standard/nasa/nasa-std-87399 "Click to open in new window")

  NASA-STD-8739.9, NASA Office of Safety and Mission Assurance, 2013. Change Date:
  2016-10-07, Change Number: 1
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-282) Software Requirements Specification (SRS) Template, GRC-SW-TPLT-SRS, NASA Glenn Research Center, 2011. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-287)

  [Analysis of Requirements Volatility during Software Development Life Cycle,](https://opus.lib.uts.edu.au/handle/10453/2603 "Click to open in new window")

  Nurmuliani, N; Zowghi, Didar; Fowell, Sue. Proceedings of the 2004 Australian Software Engineering Conference, 2004, pp. 28 - 37, University of technology, Sydney, ASWEC'04, 2004.
* (SWEREF-294)

  [OSMA/NSC's SMA Technical Excellence Program (STEP) program.](https://nsc.nasa.gov/professional-development/safety-and-mission-assurance-technical-excellence-program "Click to open in new window")

  The Safety and Mission Assurance (SMA) Technical Excellence Program (STEP) is a career-oriented, professional development roadmap for SMA professionals.
* (SWEREF-303)

  [What are Interface Requirements Specifications, Interface Design Descriptions, Interface Control Documents, and how do they relate?,](https://www.ppi-int.com/resources/systems-engineering-faq/interface-requirements-specifications-interface-design-descriptions-interface-control-documents-relate/ "Click to open in new window")

  Robert Halligan, Project Performance International. (Expressing and Organizing Interface Information). Accessed November 3, 2014 from http://ppi-int.com/systems-engineering/irs-idd-icd-relationship.php.
* (SWEREF-320)

  [Fully Employing Software Inspections Data,](http://dx.doi.org/10.1007/s11334-010-0132-1 "Click to open in new window")

  Shull., F., Feldmann, R., Seaman, C., Regardie, M., and Godfrey, S.,Innovations in Systems and Software Engineering - a NASA Journal, 2010.  Available at: http://dx.doi.org/10.1007/s11334-010-0132-1.
* (SWEREF-328)

  [Software Engineering Institute. (November, 2010). "CMMI for Acquisition, Version 1.3,"](http://www.sei.cmu.edu/reports/10tr032.pdf "Click to open in new window")

  Software Engineering Institute. (November, 2010). CMU/SEI-2010-TR-032. Carnegie-Mellon University. For SWE-035, see page 351 of this document.
  Retrieved on November 20, 2017 from http://www.sei.cmu.edu/reports/10tr032.pdf.
* (SWEREF-329)

  [Software Measurement Guidebook,](https://ntrs.nasa.gov/search.jsp?R=19980228474 "Click to open in new window")

  Technical Report - NASA-GB-001-94 - Doc ID: 19980228474 (Acquired Nov 14, 1998), Software Engineering Program,
* (SWEREF-336)

  [Software Metrics Capability Evaluation Guide,](http://www.dtic.mil/docs/citations/ADA325385 "Click to open in new window")

  Software Technology Support Center (STSC) (1995), Hill Air Force Base. Accessed 6/25/2019.
* (SWEREF-342)

  [STEP Level 2 Overview of Software Safety course,](https://saterninfo.nasa.gov/ "Click to open in new window")

  SMA-SA-WBT-230 SATERN (need user account to access SATERN courses). This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-343)

  [STEP Level 2 Software Configuration Management and Data Management course, SMA-SA-WBT-204, SATERN (need user account to access SATERN courses).](https://saterninfo.nasa.gov/ "Click to open in new window")

  This NASA-specific information and resource is available in at the System for Administration, Training, and Educational Resources for NASA (SATERN), accessible to NASA-users at https://saterninfo.nasa.gov/.
* (SWEREF-347)

  [Understanding Requirements Volatility in Software Projects,](http://ieeexplore.ieee.org/Xplore/login.jsp?url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5%2F5428222%2F5428274%2F05428606.pdf%3Farnumber%3D5428606&authDecision=-203 "Click to open in new window")

  Thakurta, Rahul; Ahlemann, Frederick, Proceedings of the 43rd Hawaii International Conference on System Sciences, 2010. NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-355)

  [12 Steps to Useful Software Metrics,](http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics_in_12_steps_paper.pdf "Click to open in new window")

  Westfall, Linda, The Westfall Team (2005),   Retrieved November 3, 2014 from http://www.win.tue.nl/~wstomv/edu/2ip30/references/Metrics\_in\_12\_steps\_paper.pdf
* (SWEREF-365)

  [Conceptualizing Measures of Required Software Functionality,](http://www.cc.uah.es/ssalonso/papers/Ontose07.pdf "Click to open in new window")

  Lopez, C., Cuadrado, J.J. and Sánchez-Alonso, S. (2007). In Proceedings of ONTOSE 2007 -Second International Workshop on Ontology, Conceptualizations and Epistemology for Software and Systems Engineering.
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-381) Software Requirements Specification (SRS) Template,  GRC-SW-TPLT-SRS, NASA Glenn Research Center, 2011. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA users from the SPAN tab in this Handbook.
* (SWEREF-401)

  [Software Test Plan (STP),](http://everyspec.com/DATA-ITEM-DESC-DIDs/DI-IPSC/DI-IPSC-81438A_3750/ "Click to open in new window")

  Federal Aviation Administration (FAA), December, 1999. DI-IPSC-81438A,
* (SWEREF-402)

  [NASA Information Security Policy,](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPD&c=2810&s=1E "Click to open in new window")

  NASA Office of the Chief Information Officer, May, 2015. NPD 2810.1E,
* (SWEREF-403)

  [Security of Information and Information Systems](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2810&s=1F "Click to open in new window")

  NPR 2810.1F, Office of the Chief Information Officer, Effective Date: January 03, 2022, Expiration Date: January 03, 2027,
* (SWEREF-433)

  [Lessons Learned in Software Quality Assurance.](https://link.springer.com/chapter/10.1007/978-3-662-05129-0_12 "Click to open in new window")

  Rosenberg, Dr. Linda H. NASA Goddard Space Flight Center (GSFC). In Journal of Software Technology, Vol. 6, Number 2. October, 2003. Lessons Learned Reference.
* (SWEREF-448) Software Process Improvement Plan EI32-SPIP,  Revision F, NASA Marshall Space Flight Center (MSFC) Flight Software Branch, 10-26-2010.  Replaces SWEREF-058
* (SWEREF-452) SED Unit Test Guideline,  580-GL-062-02, Systems Engineering Division, NASA Goddard Space Flight Center (GSFC), 2012.  This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook. Replaces SWEREF-081
* (SWEREF-453) Project Planning Process,  580-PC-004-07, Software Engineering Division (ISD), NASA Goddard Space Flight Center (GSFC), 2020. This NASA-specific information and resource is available in Software Processes Across NASA (SPAN), accessible to NASA-users from the SPAN tab in this Handbook.
* (SWEREF-490)

  [History of NASA’s Academy of Program/Project & Engineering Leadership.](http://appel.nasa.gov/about-us/history/ "Click to open in new window")

  Academy of Program/Project and Engineering Leadership (APPEL). Retrieved on September 14, 2015 from http://appel.nasa.gov/about-us/history/.
* (SWEREF-501)

  [Mars Observer Inertial Reference Loss](https://llis.nasa.gov/lesson/310 "Click to open in new window")

  Public Lessons Learned Entry: 310.
* (SWEREF-502)

  [Quality Assurance Expertise in Special Technical Areas (e.g., optics)](https://llis.nasa.gov/lesson/331 "Click to open in new window")

  Public Lessons Learned Entry: 331.
* (SWEREF-503)

  [Quality Assurance Access to Critical Areas, Management](https://llis.nasa.gov/lesson/332 "Click to open in new window")

  Public Lessons Learned Entry: 332.
* (SWEREF-507)

  [Thrusters Fired on Launch Pad (1975)](https://llis.nasa.gov/lesson/403 "Click to open in new window")

  Public Lessons Learned Entry: 403.
* (SWEREF-508)

  [Interface Control and Verification](https://llis.nasa.gov/lesson/569 "Click to open in new window")

  Public Lessons Learned Entry: 569.
* (SWEREF-511)

  [Consider Language Differences When Conveying Requirements to Foreign Partners (1997)](https://llis.nasa.gov/lesson/608 "Click to open in new window")

  Public Lessons Learned Entry: 608.
* (SWEREF-513)

  [Mars Climate Orbiter Mishap Investigation Board - Phase I Report](https://llis.nasa.gov/lesson/641 "Click to open in new window")

  Public Lessons Learned Entry: 641.
* (SWEREF-514)

  [Preliminary Design Review](https://llis.nasa.gov/lesson/655 "Click to open in new window")

  Public Lessons Learned Entry: 655.
* (SWEREF-515)

  [Critical Design Review for Unmanned Missions](http://llis.nasa.gov/lesson/657 "Click to open in new window")

  Public Lessons Learned Entry 657.
* (SWEREF-517)

  [Fault Tolerant Design](https://llis.nasa.gov/lesson/707 "Click to open in new window")

  Public Lessons Learned Entry: 707.
* (SWEREF-519)

  [Pre-Flight Problem/Failure Reporting Procedures](https://llis.nasa.gov/lesson/733 "Click to open in new window")

  Public Lessons Learned Entry: 733.
* (SWEREF-520)

  [Problem Reporting and Corrective Action System](https://llis.nasa.gov/lesson/738 "Click to open in new window")

  Public Lessons Learned Entry: 738.
* (SWEREF-526)

  [Software Design for Maintainability](https://llis.nasa.gov/lesson/838 "Click to open in new window")

  Public Lessons Learned Entry: 838.
* (SWEREF-529)

  [Probable Scenario for Mars Polar Lander Mission Loss (1998)](https://llis.nasa.gov/lesson/938 "Click to open in new window")

  Public Lessons Learned Entry: 938.
* (SWEREF-530)

  [MPL Uplink Loss Timer Software/Test Errors (1998)](https://llis.nasa.gov/lesson/939 "Click to open in new window")

  Public Lessons Learned Entry: 939.
* (SWEREF-532)

  [Computer Software/Software Safety Policy Requirements/Potential Inadequacies](https://llis.nasa.gov/lesson/1021 "Click to open in new window")

  Public Lessons Learned Entry: 1021.
* (SWEREF-536)

  [International Space Station (ISS) Program/Computer Hardware-Software/Software](https://llis.nasa.gov/lesson/1062 "Click to open in new window")

  Public Lessons Learned Entry: 1062.
* (SWEREF-540)

  [Computer Hardware-Software/Software Development Tools/Maintenance](https://llis.nasa.gov/lesson/1128 "Click to open in new window")

  Public Lessons Learned Entry: 1128.
* (SWEREF-542)

  [Computer Hardware-Software/International Space Station/Software Development](https://llis.nasa.gov/lesson/1132 "Click to open in new window")

  Public Lessons Learned Entry: 1132.
* (SWEREF-543)

  [International Space Station (ISS) Program/Computer Hardware-Software/International Partner Source Code](https://llis.nasa.gov/lesson/1153 "Click to open in new window")

  Public Lessons Learned Entry: 1153.
* (SWEREF-544)

  [Lack of Education and Training in the Use and Processes of Independent Verification & Validation (IV&V) for Software Within NASA](https://llis.nasa.gov/lesson/1173 "Click to open in new window")

  Public Lessons Learned Entry: 1173.
* (SWEREF-545)

  [Deep Space 2 Telecom Hardware-Software Interaction (1999)](https://llis.nasa.gov/lesson/1197 "Click to open in new window")

  Public Lessons Learned Entry: 1197.
* (SWEREF-550)

  [ADEOS-II NASA Ground Network (NGN) Development and Early Operations -- Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned](https://llis.nasa.gov/lesson/1346 "Click to open in new window")

  Public Lessons Learned Entry: 1346.
* (SWEREF-551)

  [Lessons Learned From Flights of ?Off the Shelf? Aviation Navigation Units on the Space Shuttle, GPS](https://llis.nasa.gov/lesson/1370 "Click to open in new window")

  Public Lessons Learned Entry: 1370.
* (SWEREF-552)

  [Kennedy Space Center (KSC) Projects and Resources Online (KPRO) Software Development and Implementation](https://llis.nasa.gov/lesson/1384 "Click to open in new window")

  Public Lessons Learned Entry: 1384.
* (SWEREF-556)

  [Take CM Measures to Control the Renaming and Reuse of Old Command Files (2002)](https://llis.nasa.gov/lesson/1481 "Click to open in new window")

  Public Lessons Learned Entry: 1481.
* (SWEREF-557)

  [MER Spirit Flash Memory Anomaly (2004)](https://llis.nasa.gov/lesson/1483 "Click to open in new window")

  Public Lessons Learned Entry: 1483.
* (SWEREF-565)

  [Develop and Test the Launch Procedure Early (1997)](https://llis.nasa.gov/lesson/609 "Click to open in new window")

  Public Lessons Learned Entry: 609.
* (SWEREF-568)

  [Erroneous Onboard Status Reporting Disabled IMAGE's Radio](https://llis.nasa.gov/lesson/1799 "Click to open in new window")

  Public Lessons Learned Entry: 1799.
* (SWEREF-571)

  [NASA Study of Flight Software Complexity](https://llis.nasa.gov/lesson/2050 "Click to open in new window")

  Public Lessons Learned Entry: 2050.
* (SWEREF-574)

  [Place Flight Scripts Under Configuration Management Prior to ORT](https://llis.nasa.gov/lesson/2476 "Click to open in new window")

  Public Lessons Learned Entry: 2476.

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report) * [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description) * [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections) * [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan) * [5.05 - Metrics - Software Metrics Report](/spaces/SWEHBVD/pages/102695659/5.05+-+Metrics+-+Software+Metrics+Report) * [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan) * [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary) * [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan) * [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification) * [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan) * [5.11 - STR - Software Test Report](/spaces/SWEHBVD/pages/102695672/5.11+-+STR+-+Software+Test+Report) * [5.12 - SUM - Software User Manual](/spaces/SWEHBVD/pages/102695673/5.12+-+SUM+-+Software+User+Manual) * [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description) * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan) * [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document) * [5.17 - Software Assurance Plan Minimum Content](/spaces/SWEHBVD/pages/138707548/5.17+-+Software+Assurance+Plan+Minimum+Content) * [5.18 - Safety Plan Minimum Content](/spaces/SWEHBVD/pages/138707600/5.18+-+Safety+Plan+Minimum+Content) * [5.19 - Software Assurance Status Report Minimum Content](/spaces/SWEHBVD/pages/138707621/5.19+-+Software+Assurance+Status+Report+Minimum+Content) * [5.20 - IV&V Project Execution Plan Minimum Content](/spaces/SWEHBVD/pages/140641556/5.20+-+IV+V+Project+Execution+Plan+Minimum+Content) * [5.21 - Software Requirements Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641581/5.21+-+Software+Requirements+Analysis+Report+Minimum+Content) * [5.22 - Software Design Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641618/5.22+-+Software+Design+Analysis+Report+Minimum+Content) * [5.23 - Testing Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641646/5.23+-+Testing+Analysis+Report+Minimum+Content) * [5.24 - Hazard Report Minimum Content](/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content) * [5.25 - Audit Report Minimum Content](/spaces/SWEHBVD/pages/140641711/5.25+-+Audit+Report+Minimum+Content) * [5.26 - Source Code Quality Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641734/5.26+-+Source+Code+Quality+Analysis+Report+Minimum+Content) * [8.51 - Software Assurance Plan](/spaces/SWEHBVD/pages/102695753/8.51+-+Software+Assurance+Plan) * [8.52 - Software Assurance Status Reports](/spaces/SWEHBVD/pages/102695754/8.52+-+Software+Assurance+Status+Reports) * [8.54 - Software Requirements Analysis](/spaces/SWEHBVD/pages/102695749/8.54+-+Software+Requirements+Analysis) * [8.55 - Software Design Analysis](/spaces/SWEHBVD/pages/102695748/8.55+-+Software+Design+Analysis) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Center Libraries](https://nen.nasa.gov/web/software/wiki)      * [Project Planning](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Project+Planning) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.01 Software Life Cycle Planning](/spaces/SWEHBVD/pages/133235376/A.01+Software+Life+Cycle+Planning) * [A.02 Software Assurance and Software Safety](/spaces/SWEHBVD/pages/133235378/A.02+Software+Assurance+and+Software+Safety) * [A.03 Software Requirements](/spaces/SWEHBVD/pages/133235379/A.03+Software+Requirements) * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) * [A.06 Software Testing](/spaces/SWEHBVD/pages/133235382/A.06+Software+Testing) * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) * [A.09 Software Risk Management](/spaces/SWEHBVD/pages/133235385/A.09+Software+Risk+Management) * [A.10 Software Peer Reviews and Inspections](/spaces/SWEHBVD/pages/133235386/A.10+Software+Peer+Reviews+and+Inspections) * [A.11 Software Measurements](/spaces/SWEHBVD/pages/133235387/A.11+Software+Measurements) * [A.12 Software Non-conformance or Defect Management](/spaces/SWEHBVD/pages/133235388/A.12+Software+Non-conformance+or+Defect+Management) |

# 3. Lessons Learned

### 3.1 NASA Lessons Learned

The NASA Lesson Learned database contains the following lessons learned related to software project documentation:

* **Mars Observer Inertial Reference Loss. Lesson Number 0310[501](#_tabs-<p>2</p>)**: Design for Maintenance, Lesson Learned No. 4: "Design flexibility of the flight computer and software is critical to the ability to uplink software patches for the correction of unexpected in-flight spacecraft anomalies." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Thrusters Fired on Launch Pad (1975) (Plan for safe exercise of command sequences). Lesson Number 0403[507](#_tabs-<p>2</p>):**  "When command sequences are stored on the spacecraft and intended to be exercised only in the event of abnormal spacecraft activity, the consequences should be considered of their being issued during the system test or the pre-launch phases." *Document Structure Reference:* [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
* **Interface Control and Verification. Lesson Number 0569[508](#_tabs-<p>2</p>):** Problems occurred during the Mars Pathfinder spacecraft integration and test due to out-of-date or incomplete interface documentation. (While this lesson involves a hardware-related problem, it illustrates the need for accuracy in interface documentation.) Investigation showed that the main wiring harness was built in accordance with documentation that had not been updated after design changes were made. In part, this was due to independently prepared Mechanical Interface Control Drawings by the Government and the contractor. The MICD s should have had periodic verification for accuracy and compatibility.  *Document Structure Reference:* [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description)
* **Consider Language Differences When Conveying Requirements to Foreign Partners (1997) (Diagrams may be useful in requirements specifications). Lesson Number 0608[511](#_tabs-<p>2</p>):**  "It is especially important when working with foreign partners to document requirements in terms that describe the intent very clearly; include graphics where possible." *Document Structure Reference:* [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
* **Mars Climate Orbiter Mishap Investigation Board - Phase I Report. Lesson Number 0641[513](#_tabs-<p>2</p>)**: "The MCO Mishap Investigation Board (MIB)...determined that the root cause for the loss of the MCO spacecraft was the failure to use metric units in the coding of a ground software file." The data in the ... file was required to be in metric units per existing software interface documentation, and the trajectory modelers assumed the data was provided in metric units per the requirements. In fact, the angular momentum (impulse) data was in English units rather than metric units. The failure to properly communicate what was in the interface documentation is a warning that the effective implementation of the IDD requirement includes adequate communication of its contents, not just the writing and recording.  *Document Structure Reference:* [5.02 - IDD - Interface Design Description](/spaces/SWEHBVD/pages/102695656/5.02+-+IDD+-+Interface+Design+Description)

* **Preliminary Design Review. Lesson Learned 0655[514](#_tabs-<p>2</p>):**  By not holding a PDR "one or a number of potential problems which could result in an adverse impact on the system, subsystem, and/or project might not be identified in a timely manner. This oversight might later result in a condition having a significant effect on quality, reliability, capability, schedule, and/or cost...Conduct a formal Preliminary Design Review (PDR) at the system and subsystem levels prior to the start of subsystem detail design, to assure that the proposed design and associated implementation approach will satisfy the system and subsystem functional requirements." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Critical Design Review for Unmanned Missions. Lesson Learned 0657[515](#_tabs-<p>2</p>):**  "In the absence of a CDR, potential problems with adverse impacts on the subsystem, system, or project may not be identified in a timely manner. This oversight may later result in a condition having a significant effect on quality, reliability, capability, schedule, or cost." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Fault Tolerant Design. Lesson Number 0707[517](#_tabs-<p>2</p>)**: "Systems which do not incorporate fault tolerant design (FTD) as a part of their development process will experience a higher risk of a severely degraded or prematurely terminated mission, or it may result in excessively large weight volume, or high cost to achieve an acceptable level of performance by using non-optimized redundancy or overdesign...Incorporate hardware and software features in the design of spacecraft equipment which tolerate the effects of minor failures and minimize switching from the primary to the secondary string. This increases the potential availability and reliability of the primary string." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Pre-Flight Problem/Failure Reporting Procedures. Lesson Number 0733[519](#_tabs-<p>2</p>):**  Impact of Non-Practice states: "Without ... formal reporting procedures, problems/failures, particularly minor glitches, may be overlooked or not considered serious enough to investigate or report to Project Management. This could result in recurrence of the problem/failure during the mission and result in a significant degradation in performance."  *Document Structure Reference:*[5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report)
* **Problem Reporting and Corrective Action System. Lesson Number 0738[520](#_tabs-<p>2</p>):**  Impact of Non-Practice states: "Hardware/software problems that require further investigation may not be identified and tracked. The development of corrective action and the need for improvement will not be highlighted in engineering. Opportunities for the early elimination of the causes of failures and valuable trending data can be overlooked." Practice states: "A closed-loop Problem (or Failure) Reporting and Corrective Action System ( PRACAS or FRACAS ) is implemented to obtain feedback about the operation of ground support equipment used for the manned spaceflight program."  *Document Structure Reference:*[5.01 - CR-PR - Software Change Request - Problem Report](/spaces/SWEHBVD/pages/102695655/5.01+-+CR-PR+-+Software+Change+Request+-+Problem+Report)
* **Software Design for Maintainability. Lesson Number 0838[526](#_tabs-<p>2</p>)**: Impact of Non-Practice: "Because of increases in the size and complexity of software products, software maintenance tasks have become increasingly more difficult. Software maintenance should not be a design afterthought; it should be possible for software maintainers to enhance the product without tearing down and rebuilding the majority of code." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Probable Scenario for Mars Polar Lander Mission Loss (1998) (Affects of an incomplete software requirements specification). Lesson Number 0938[529](#_tabs-<p>2</p>):**  "All known hardware operational characteristics, including transients and spurious signals, must be reflected in the software requirements documents and verified by test." *Document Structure Reference:* [5.09 - SRS - Software Requirements Specification](/spaces/SWEHBVD/pages/102695669/5.09+-+SRS+-+Software+Requirements+Specification)
* **Probable Scenario for Mars Polar Lander Mission Loss (1998)** **(Importance of including known hardware characteristics). Lesson Number 0938[529](#_tabs-<p>2</p>):**  "1. Project test policy and procedures should specify actions to be taken when a failure occurs during test. When tests are aborted, or known to have had flawed procedures, they must be rerun after the test deficiencies are corrected. When test article hardware or software is changed, the test should be rerun unless there is a clear rationale for omitting the rerun. 2. All known hardware operational characteristics, including transients and spurious signals, must be reflected in the software requirements documents and verified by test." *Document Structure Reference:* [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures)
* **MPL Uplink Loss Timer Software/Test Errors (1998) (Plan to test against full range of parameters). Lesson Number 0939[530](#_tabs-<p>2</p>):**  "Unit and integration testing should, at a minimum, test against the full operational range of parameters. When changes are made to database parameters that affect logic decisions, the logic should be re-tested." *Document Structure Reference:* [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
* ****Computer Software/Software Safety Policy Requirements/Potential Inadequacies (Cover essential requirements for the project). Lesson Learned 1021[532](#_tabs-<p>2</p>):****  "NASA is committed to assuring that required program management plans and any subordinate plans such as software or safety management plans cover the essential requirements for programs where warranted by cost, size, complexity, lifespan, risk, and consequence of failure." *Document Structure Reference:* [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
* **International Space Station (ISS) Program/Computer Hardware-Software/Software (Plan realistic but flexible schedules). Lesson Number 1062[536](#_tabs-<p>2</p>):**  "NASA should realistically reevaluate the achievable ... software development and test schedule and be willing to delay ... deployment if necessary rather than potentially sacrificing safety." *Document Structure Reference:* [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
* **Computer Hardware-Software/Software Development Tools/Maintenance. Lesson Number 1128[540](#_tabs-<p>2</p>)**: "NASA concurs with the finding that no program-wide plan exists addressing the maintenance of COTS software development tools. A programmatic action has been assigned to develop the usage requirements for COTS/modified off-the-shelf software including the associated development tools. These guidelines will document maintenance and selection guidelines to be used by all of the applicable program elements." *Document Structure Reference:* [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan)
* **Computer Hardware-Software/International Space Station/Software Development****(Plan for user involvement). Lesson Learned 1132[542](#_tabs-<p>2</p>):**  "The lack of user involvement results in increased schedule and safety risk to the program... follow a concurrent engineering approach to building software that involves users and other key discipline specialists early in the software development process to provide a full range of perspectives and improve the understanding of requirements before code is developed." *Document Structure Reference:* [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
* **International Space Station (ISS) Program/Computer Hardware-Software/International Partner Source Code (Maintenance Agreements.) Lesson Number 1153[543](#_tabs-<p>2</p>)**: The Recommendation states to "Solidify long-term source code maintenance and incident investigation agreements for all software being developed by the International Partners as quickly as possible, and develop contingency plans for all operations that cannot be adequately placed under NASA's control." *Document Structure Reference:* [5.04 - Maint - Software Maintenance Plan](/spaces/SWEHBVD/pages/102695658/5.04+-+Maint+-+Software+Maintenance+Plan)
* **Lack of Education and Training in the Use and Processes of Independent Verification & Validation (IV&V) for Software Within NASA (2001). Lesson Number 1173[544](#_tabs-<p>2</p>):**  "While NASA has made major changes to emphasize the need to utilize IV&V on safety-critical projects, the technology is not well understood by program managers and other relevant NASA personnel." *Document Structure Reference:* [5.15 - Train - Software Training Plan](/spaces/SWEHBVD/pages/102695676/5.15+-+Train+-+Software+Training+Plan)
* **Deep Space 2 Telecom Hardware-Software Interaction (1999) (Plan to test as you fly). Lesson Number 1197[545](#_tabs-<p>2</p>):**  "To fully validate performance, test integrated software and hardware over the flight operational temperature range." *Document Structure Reference:* [5.10 - STP - Software Test Plan](/spaces/SWEHBVD/pages/102695671/5.10+-+STP+-+Software+Test+Plan)
* **ADEOS-II NASA Ground Network (NGN) Development and Early Operations – Central/Standard Autonomous File Server (CSAFS/SAFS) Lessons Learned. Lesson Number 1346[550](#_tabs-<p>2</p>)**: Use of commercial off the shelf (COTS) products: "Match COTS tools to project requirements. Deciding to use a COTS product as the basis of system software design is potentially risky, but the potential benefits include quicker delivery, less cost, and more reliability in the final product. The following lessons were learned in the definition phase of the [software] development. *Document Structure Reference:*  [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)   
  + "Use COTS products and re-use previously developed internal products.
  + "Create a prioritized list of desired COTS features.
  + "Talk with local experts having experience in similar areas.
  + "Conduct frequent peer and design reviews.
  + "Obtain demonstration versions of COTS products.
  + "Obtain customer references from vendors.
  + "Select a product appropriately sized for your application.
  + "Choose a product closely aligned with your project's requirements.
  + "Select a vendor whose size will permit a working relationship.
  + "Use vendor tutorials, documentation, and vendor contacts during COTS evaluation period."
* ****Lessons Learned From Flights of "Off the Shelf" Aviation Navigation Units on the Space Shuttle, GPS (Importance of Accurate Interface Control Document.) Lesson Learned 1370[551](#_tabs-<p>2</p>):****  "If the integrator and user do not have access to firmware and firmware requirements, the ICD may be the only written source of information on unit parameters. Developers of software that will interface with the unit must examine the ICD closely. .... An inaccurate ICD will lead to software and procedural issues that will have to be addressed before a system can be certified as operational. An accurate ICD is also needed for instrumentation port data that is critical during the test and verification phase of a project...Short development schedules may result in changes to the ICD while host vehicle software requirements are being defined and software is in development and test. A disciplined process of checks must be in place to ensure that the ICD and software requirements for units that interface with the [hardware and instruments] are consistent. Individuals who have knowledge of both [hardware] requirements and requirements for other interfacing units must be able to communicate and be involved in any changes made to the ICD." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Kennedy Space Center (KSC) Projects and Resources Online (KPRO) Software Development and Implementation (Project team planning).****Lesson Learned 1384[552](#_tabs-<p>2</p>):**  "When planning and selecting team resources for a project, consider how the resources can work together and support each other, along with the skills required. This can be a factor in meeting or delaying software project milestones if an alternative resource has not been endorsed by the team members." *Document Structure Reference:* [5.08 - SDP-SMP - Software Development - Management Plan](/spaces/SWEHBVD/pages/102695668/5.08+-+SDP-SMP+-+Software+Development+-+Management+Plan)
* **Take CM Measures to Control the Renaming and Reuse of Old Command Files. Lesson Number 1481[556](#_tabs-<p>2</p>):**  The Mars Odyssey mission ran into a version control issue when they discovered an improperly named file call script. It was determined that the team had taken an old Mars Global surveyor file to reuse. The file was renamed, but its code creation time captured in the header was not changed. This caused the system to label the file as an old file. As a result, the operations team had to manually specify the correct file to use, until subsequent code fixes were implemented. *Document Structure Reference:* [5.16 - VDD - Version Description Document](/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document)
* **MER Spirit Flash Memory Anomaly (2004). Lesson Learned 1483[557](#_tabs-<p>2</p>):**  "Shortly after the commencement of science activities on Mars, an MER rover lost the ability to execute any task that requested memory from the flight computer. The cause was incorrect configuration parameters in two operating system software modules that control the storage of files in system memory and flash memory. Seven recommendations cover enforcing design guidelines for COTS software, verifying assumptions about software behavior, maintaining a list of lower priority action items, testing flight software internal functions, creating a comprehensive suite of tests and automated analysis tools, providing downlinked data on system resources, and avoiding the problematic file system and complex directory structure." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Develop and Test the Launch Procedure Early (1997).****Lesson Number****0609[565](#_tabs-<p>2</p>):**  The Abstract states: "During the terminal countdown for the first attempted launch of Cassini, spacecraft telemetry channels indicated a false alarm condition that delayed verification of spacecraft readiness for launch, and contributed to a delay on the first launch day. The anomaly was traced to erroneous telemetry documentation. Develop and release the launch procedure early enough for comprehensive testing before launch. Rigorously test and verify all telemetry channels and their alarms and ensure documentation such as telemetry definitions is kept up to-date." *Document Structure Reference:* [5.07 - SDD - Software Data Dictionary](/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary)
* **NASA Study of Flight Software Complexity. Lesson Learned 2050[571](#_tabs-<p>2</p>):**  "Flight software development problems led NASA to study the factors that have led to the accelerating growth in flight software size and complexity. The March 2009 report on the NASA Study on Flight Software Complexity contains recommendations in the areas of systems engineering, software architecture, testing, and project management." *Document Structure Reference:* [5.13 - SwDD - Software Design Description](/spaces/SWEHBVD/pages/102695674/5.13+-+SwDD+-+Software+Design+Description)
* **Place Flight Scripts Under Configuration Management Prior to ORT (Project attention to configuration control). Lesson Number 2476[574](#_tabs-<p>2</p>):**  "Project attention to the configuration control of flight scripts is likely to prevent the generation of unnecessary software iterations, improve the rigor of mission system engineering processes, and ensure consistency in the test and operations environments." *Document Structure Reference:* [5.06 - SCMP - Software Configuration Management Plan](/spaces/SWEHBVD/pages/102695666/5.06+-+SCMP+-+Software+Configuration+Management+Plan)

### 3.2 Other Lessons Learned

* “Both experience and research have shown that the parameters under control of the moderator have significant effect on the results of an inspection. Where teams do not have their own baselines of data, Agency-wide heuristics have been developed to assist in planning. *Document Structure Reference:* [5.03 - Inspect - Software Inspection, Peer Reviews, Inspections](/spaces/SWEHBVD/pages/102695657/5.03+-+Inspect+-+Software+Inspection+Peer+Reviews+Inspections)

For example, analyzing a database of over 2,400 inspections across the Agency, researchers have found that inspections with team sizes of 4 to 6 inspectors find 12 defects on average, while teams outside this range find on average only 7. [320](#_tabs-<p>2</p>)

Heuristics for how many pages can be reviewed by a team during a single inspection vary greatly according to the type of the document, which is to be expected since the density of information varies greatly between a page of requirements, a page of a design diagram, and a page of code. Similar to the heuristics for team size, inspection teams that follow the heuristics for document size also find on average significantly more defects than those which do not. [320](#_tabs-<p>2</p>) The recommended heuristics for document size are listed below. All of these values assume that inspection meetings will be limited to 2 hours.

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
