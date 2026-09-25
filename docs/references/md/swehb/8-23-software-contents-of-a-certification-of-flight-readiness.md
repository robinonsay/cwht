# 8.23 - Software Contents of a Certification of Flight Readiness

> NASA Software Engineering Handbook (SWEHB Ver D), page id 116293813. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/116293813/8.23+-+Software+Contents+of+a+Certification+of+Flight+Readiness

8.23 - Software Contents of a Certification of Flight Readiness

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/116293813/8.23+-+Software+Contents+of+a+Certification+of+Flight+Readiness#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=116293813)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=116293813&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Resources](#tabs-2)

# 1. Introduction

## 1.1 Certification of Flight Readiness (CoFR)

When a project or mission reaches a Certification of Flight Readiness (CoFR), the project/mission needs to be able to show that every element of the system is ready to execute launch, flight, and planned operations in a safe  and successful manner. This is the final point where  every element of the system must be certified and  have no outstanding issues that would prevent a successful mission. If an issue or issues remain at this point, exceptions may be granted if resolutions can be completed and certified by the planned launch date or if the exceptions are minor enough that it is determined there will not cause a significant risk to the safety or success of the mission.

In this topic, the focus is on the products that are needed for the software in the system. The path taken to get to a CoFR may vary considerably, depending on the size, number, and complexity of the elements in the particular mission flight.

For a CoFR on a smaller project, where there is only one hardware/software system to consider (for example, a single launch vehicle carrying a scientific satellite into orbit), there may only be a few formal reviews leading up to the CoFR.  The reviews will discuss outstanding issues that need resolution before the launch. As needed, the reviews may only consist of a Flight Readiness Review (FRR) and an Operational Readiness Review (ORR). See [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria).

## 1.2 Minimum Software Contents

The list below is intended to provide the recommended minimum software contents, provided by an individual element or for a smaller project, for reviews leading up to the CoFR. In similar cases, the proceeding reviews might only be the Flight Readiness Review (FRR) and the Operational Readiness Review (ORR). If there are discrepancies or issues in these reviews that need to be completed before a launch, these would be recorded and should be tracked to closure prior to a CoFR. These would be followed by the  Confirmation of Flight Readiness (CoFR) Review where final records are examined and the Certification of Flight Readiness can be signed, and endorsed by an accountable person or board, approving the launch of the flight.

For large, complex projects with multiple elements, each element may prepare their own certification information and may even plan to do individual element preliminary reviews.  During the series of reviews leading up to the CoFR, the minimum contents in the list below will be reviewed and evaluated for each element of the project. The series of reviews might possibly begin with Incremental Acceptance Package Reviews and Certified Principle Engineer (CPE) Certification Reviews. This will assure that a contractor package has been verified to meet all technical requirements and is ready for the next level  System Acceptance Review/Design Certification Review(s). The information from these Incremental Package Acceptance Reviews/CPE Certification Reviews along with the verification closures and the final as-built configuration audit information is fed into the System Acceptance Review/ Design Certification Review and results in design certification and system acceptance. Any non-compliances, issues and incomplete work will be addressed and reviewed at the appropriate CoFR element reviews.

There may also be multiple element preliminary Flight Readiness Reviews(FRRs) which confirm that individual elements of the mission have completed their individual CoFRs and are ready to support safe and successful accomplishment of the mission. The final CoFR for the entire set of elements will be a combination of all the different individual reviews performed.

When preparing for a CoFR, some projects use Statements of Readiness (SoRs) and Records of Completion (RoCs). The SoRs indicate that the element is ready to go to the CoFR and the RoCs indicate the successful completion of the CoFR requirements. These are signed or endorsed by an accountable person who can attest or certify the completions.

Regardless of the exact review path the elements of a larger, more complex program have taken, the preliminary reviews for the individual elements should cover the recommended minimum software  contents listed below leading up to the CoFR. If there are discrepancies or issues in these preliminary reviews that need to be completed before a launch, these would be recorded and should be tracked to closure prior to a CoFR. These would be followed by the  Confirmation of Flight Readiness (CoFR) Review where final records are examined and the Certification of Flight Readiness can be signed, and endorsed by an accountable person or board, approving the launch of the flight.

Recommended Minimum Contents (Many of these may be included in the acceptance package for the software):

* Bidirectional Traceability matrices showing requirements trace to/from tests
* Test records showing that all tests have been successfully completed
* Records showing test coverage for safety-critical portions of the system
* Test discrepancy records showing that all discrepancies are closed or have operational work-arounds
* Verification log showing that all hazard verifications have been successfully completed
* Certificate of Conformance to requirements, validated by Quality Assurance organization and the IV & V organization (if applicable)
* Lists of any previously approved waivers of safety requirements, and copies of the waiver forms
* Description of the operational constraints/work-arounds for hazardous activities. List all open, corrected but not tested, or uncorrected safety-related problem reports. Describe environmental limitations of use and the allowable operational envelope.
* Description of all operational procedures and operator interfaces. Include failure diagnosis and recovery procedures.

## 1.3 Additional Items for Readiness and Certification Reviews

Additional items that may need to be considered when preparing for the final series of readiness and certification reviews:

* Do you need to provide status on any changes since the last status (e.g., external network interface changes, new software capabilities that were added, new voice communication system, operating system changes or upgrades)?
* If there were changes in the operating system since the last review, are all the other interfacing applications compatible with the new operating system? Have there been changes in the security software?
* Are software and facility backups in-place in case of emergencies? (fire, hurricanes, etc.,)
* Has the training and certification of the personnel been completed ? (Include operators, maintenance team, Support Center)
* Is there any open work outstanding? What is the plan for completion? How much risk is involved if it cannot be completed in time?
* Are there any security risks not previously identified? (Example: Software vendor is no longer providing security patches for the upgraded operating system.)

## 1.4 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-2) in the Resources tab.

# 2. Resources

## 2.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-337)

  [Guide to Enterprise Patch Management Planning: Preventive Maintenance for Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf "Click to open in new window")

  Souppaya, Murugiah, Scarfone, Karen, NIST Special Publication NIST SP 800-40r4, April, 2022

## 2.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 2.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [7.09 - Entrance and Exit Criteria](/spaces/SWEHBVD/pages/102695639/7.09+-+Entrance+and+Exit+Criteria) |

## 2.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>2</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

## 2.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) |
