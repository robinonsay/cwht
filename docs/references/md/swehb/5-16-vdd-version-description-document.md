# 5.16 - VDD - Version Description Document

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695677. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document

5.16 - VDD - Version Description Document

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695677/5.16+-+VDD+-+Version+Description+Document#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695677)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695677&showCommentArea=true&showComments=true#addcomment)

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

Minimum recommended content for the Version Description Document. 

a. Full identification of the system and software (e.g., numbers, titles, abbreviations, version numbers, and release numbers).

b. Executable software (e.g., batch files, command files, data files, or other software needed to install the software on its target computer).

c. Software life cycle data that defines the software product.

d. Archive and release data.

e. Instructions for building the executable software, including, for example, the instructions and data for compiling and linking and the procedures used for software recovery, software regeneration, testing, or modification.

f. Data integrity checks for the executable object code and source code.

g. Software product files (any files needed to install, build, operate, and maintain the software).

h. Open change requests and or problem reports, including any workarounds.

i. Change requests and/or problem reports implemented in the current software version since the last Software Version Description was published.

j. Confirmation that the software has been scanned for security defects and coding standard compliance.

# 2. Rationale

The Version Description Document (VDD) identifies and describes a software version consisting of one or more computer software configuration items (CSCI) (including any open source software). The software version description document is used to release, track, and control a software version. In the event that a project needs to analyze an event that happened in the past, an VDD is a concise record of the software that was delivered and executed.

The precision and completeness of the data entries called for in the recommended content assure that the correct software is made available and used in its intended application, whether it is being released to other software team members, testing, integration, or production. The VDD facilitates product implementation, testing, operations, and maintenance.

# 3. Guidance

The VDD is the definitive record of all components of a released software work product, whether it is for internal or external release. The VDD defines a set of dependencies among work products that are part of the complete software release. It describes the contents of a specific software work product release, the methods and resources needed to recreate the software work product, known changes, uncorrected problems, as well as differences from the prior software release(s).

Version information may come from the source code. Problem information may come from bug tracking or the results of static analysis. If a version control system is used, it typically includes the date, time, and size of each software work product.

The VDD includes a scheme for the identification and classification of software item records and information items and their versions, how to establish baselines, and version identification and control. The release record identifies, tracks, and controls a configuration item at the time a version (including the baseline version) is released. An VDD may consist of one or more types of software items. It lists items being delivered, including system and software item versions, traceability to specifications or previous releases, what has been changed, known problems, and workarounds. It may include installation or delivery instructions unique to the version described. Because an VDD document is released with each version of the software, there may be several VDD documents in circulation if different team members are working on different versions of the software work product. Configuration management and control are necessary for all versions to maintain control and to avoid misinformation. See the lessons learned for an example of when configurations were not properly managed. See also [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description), [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products), [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management). [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products), [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule), [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement), [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes),

## 3.1 VDD For Class A and B Software Products

Below are descriptions of the recommended content for the VDD for class A and class B software, along with examples and guidance for each.

* Full identification of the system and software.

* Include identification numbers, titles, abbreviations, version number(s), and release number(s).
* Identify intended recipients (source code might not be released to all participants).

* Executable software.

+ Include identification numbers, titles, abbreviations, version number(s), and release number(s).

* Identify the target computer, files, and source code.
* Identify any needed executable software necessary to install the software work product release.
* Include version descriptions for systems, CSCIs, etc., to the lowest configuration management unit.
* List any security and/or privacy considerations.

* Software life cycle data that defines the software product.

+ Requirements: what is satisfied by the release of the software?
+ Design: what design documents are fulfilled by the release of the software?
+ Test: test documents used during the software verification.
+ Configuration: maintenance and reproduction documents.
+ User: manuals for installing and using the released software.
+ Management: governing development plans for the software.
+ Quality: plans and procedures used to assure the quality of the software.

* Archive and release data.

+ Include identification numbers, titles, abbreviations, version number(s), and release number(s) in documents describing the software and the associated life cycle data.
+ Version control system and archival location information.

* Instructions for building the executable software.
  + Instructions and data for compiling and linking.
  + Procedures for software recovery, software regeneration, testing, or modification.

+ Minimum system requirements and needed user environment.
+ Installation instructions applicable to the version release.
+ Identification of other changes still required to make the code usable.
+ Security, privacy, and safety precautions, if any.
+ Installation verification procedures.
+ Details needed to build the executable software.

* Data integrity checks for the executable object code and source code.

+ Applicable security and privacy considerations.
+ Handling procedures and safeguards.

* Software product files.

+ Files needed to install, build, operate, and maintain the software work product.

* Open change requests and/or problem reports, including any workarounds.

+ Identify known errors or updates not yet installed for the current release.
+ Identify instructions or workarounds for handling these software work product deficiencies.
+ Document change request listings.
+ List known waivers that were approved.
+ List summarized effects of these waivers on the release version's operation and performance.

* Change requests and/or problem reports.

+ Describe the completed changes and their impact on performance and operation.
+ Identify known unsupported requirements for the current release version.
+ Describe interfaces to other software impacted by this version.
+ Identify changes affecting only the current version.

## 3.2 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

Use of a software version description applies equally to all projects, regardless of size. The project's software configuration management system can assist the developer in identifying software products and documentation that belong to a particular release.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-082)

  [NASA Space Flight Program and Project Management Requirements](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7120&s=5F "Click to open in new window")

  NPR 7120.5F, Office of the Chief Engineer, Effective Date: August 03, 2021,
  Expiration Date: August 03, 2026,
* (SWEREF-271)

  [NASA Software Safety Standard,](https://swehb.nasa.gov/download/attachments/16450126/nasa-std-8719.13c_0.pdf?api=v2 "Click to open in new window")

  NASA STD 8719.13 (Rev C ) , Document Date: 2013-05-07
* (SWEREF-273)

  [NASA Systems Engineering Handbook](https://www.nasa.gov/sites/default/files/atoms/files/nasa_systems_engineering_handbook_0.pdf "Click to open in new window")

  NASA SP-2016-6105 Rev2,
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-370)

  [Systems and software engineering -- Content of life-cycle information items,](https://www.iso.org/standard/71950.html "Click to open in new window")

  ISO/IEC/IEEE 15289:2017.  NASA users can access ISO standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of ISO standards.
* (SWEREF-556)

  [Take CM Measures to Control the Renaming and Reuse of Old Command Files (2002)](https://llis.nasa.gov/lesson/1481 "Click to open in new window")

  Public Lessons Learned Entry: 1481.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-046 - Supplier Software Schedule](/spaces/SWEHBVD/pages/102695420/SWE-046+-+Supplier+Software+Schedule) * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-075 - Plan Operations, Maintenance, Retirement](/spaces/SWEHBVD/pages/102695456/SWE-075+-+Plan+Operations+Maintenance+Retirement) * [SWE-077 - Deliver Software Products](/spaces/SWEHBVD/pages/102695457/SWE-077+-+Deliver+Software+Products) * [SWE-082 - Authorizing Changes](/spaces/SWEHBVD/pages/102695463/SWE-082+-+Authorizing+Changes) * [SWE-085 - Release Management](/spaces/SWEHBVD/pages/102695469/SWE-085+-+Release+Management) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Release, Sustain and Retire](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Release%3CCOMMA%3E+Sustain+and+Retire) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.07 Software Release, Operations, Maintenance, and Retirement](/spaces/SWEHBVD/pages/133235383/A.07+Software+Release+Operations+Maintenance+and+Retirement) * [A.08 Software Configuration Management](/spaces/SWEHBVD/pages/133235384/A.08+Software+Configuration+Management) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

* **Take CM Measures to Control the Renaming and Reuse of Old Command Files. Lesson Number 1481[556](#_tabs-<p></p>):**  The Mars Odyssey mission ran into a version control issue when they discovered an improperly named file call script. It was determined that the team had taken an old Mars Global surveyor file to reuse. The file was renamed, but its code creation time captured in the header was not changed. This caused the system to label the file as an old file. As a result, the operations team had to manually specify the correct file to use, until subsequent code fixes were implemented.

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
