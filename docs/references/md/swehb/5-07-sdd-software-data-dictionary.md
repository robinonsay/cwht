# 5.07 - SDD - Software Data Dictionary

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695667. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary

5.07 - SDD - Software Data Dictionary

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695667/5.07+-+SDD+-+Software+Data+Dictionary#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695667)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695667&showCommentArea=true&showComments=true#addcomment)

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

Minimum recommended content for the Software Data Dictionary. 

1. 1. **Channelization data** (e.g., bus mapping, vehicle wiring mapping, hardware channelization) – Provide a description of each data channel and where it maps to.
   2. **Input / Output (I/O) variables** – Provide a description of each I/O variable. Specify format, unit of measure, and definition.
   3. **Rate group data** – Provide a description and units of each data rate group (e.g., science data is collected at 1000 Hz.)
   4. **Raw and calibrated sensor data** – Provide a description of the format, units of measure, and definition of each sensor. Specify data reduction for transforming raw data into calibrated data.
   5. **Telemetry format/layout and data** – Provide a description of the telemetry mode, format, packetization and definition:
      1. Specify what types of packets are allowed to be sent for each of the telemetry modes.
      2. Specify maximum data rate for each mode.
      3. The telemetry format usually includes data type, data representation, data size, acceptable range values, unit of measure, and the meaning of the data for each field.
   6. **Data recorder format/layout and data**.
   7. **Command definitions** – Provide a description for each of the commands (e.g., onboard, ground, test specific) processed by the software work package. Include the purpose, function, the format of the command and its parameters, and any restrictions attendant to the command.
   8. **Effecter command information** – Provide information about the setting of names or flags that cause command executions in the software work products.
   9. **Operational limits** – Provide the operational limits e.g., maximum/minimum values, launch commit criteria information.
   10. **Scheduling procedures and inter-processor/inter-task communications mechanisms** – Include time-rigid sequencing, preemptive scheduling and interrupts.
   11. **Partitioning methods** – Provide the means of preventing partition breaches, partitioning faults and partitioning metric data.

# 2. Rationale

The preparation, documentation, and use of a Software Data Dictionary (SDD) enable uniform communication among the team members on a software development project. The SDD provides key information needed for the implementation, testing, and maintenance of the software product. The data dictionary allows developers, maintainers, and analysts to access information about the tables, fields, procedures, processes, and other information in the system. Customers and users have a ready reference of information about the software work product.

# 3. Guidance

The Software Data Dictionary (SDD) may be a stand-alone project document; it may be included as part of an electronic database; or it may be written as an appendix in one of the project's primary documents, e.g., the systems requirement specification or the software design description document. Either format (hardcopy or electronic) is compliant with the requirement. See also [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements), [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design). [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products), See also Topic [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures), [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews), 

A data dictionary includes a set of meta-data that contains the definition and representation of data elements. A data dictionary lists all data elements but does not say anything about the relationships between elements. It gives a single point of reference for a data repository of an organization.

Some of the typical components of a data dictionary entry are:

* Name of the table.
* Name of the fields in each table.
* Data type of the field (integer, date, text, etc.).
* Brief description of the expected data for each field.
* Length of the field.
* Default value for that field.
* Whether the field is Nullable or Not Nullable.
* Constraints that apply to each field, if any.

Not all of these fields will apply for every single entry in the data dictionary.

## 3.1 Users of the SDD

Designers, programmers, users, maintainers, and administrators of a computer system as an administrative resource are the main users of the SDD. Data dictionaries are used to maintain information on systems hardware and software configurations, documentation, application, and users, as well as other relevant information.

The SDD can be produced:

* Automatically, using a software tool to interrogate the database and to map its content.
* Manually, by examining the code to determine and record its content.
* By a combination of the two.

An electronic data dictionary is said to be active or passive. The term "passive" applies to the data dictionary that must be updated manually, whereas the term "active" applies to the data dictionary that is updated automatically by a database manager tool as data in the database is updated.

## 3.2 Organization of the SDD

The data in the SDD may be in the form of tables. Typically, the table definitions define the tables in the database, including a brief description of their use, the key fields, the primary key, and a list of the fields.

Guidance and examples for the required content of the SDD are included in the bullets below:

* Channelization data, e.g., bus mapping, vehicle wiring mapping, hardware channelization, provides a description of each data channel and where it maps to.
* Input / Output (I/O) variables provide a description of each I/O variable. Specify format, unit of measure, and definition.
* Rate group data, e.g., science data is collected at 1000 Hz, and health and status data is collected at 1 Hz.
* Raw and calibrated sensor data provide a description of the format, units of measure, and definition of each sensor. Specify data reduction for transforming raw data into calibrated data.
* Sensor data qualification criteria and senor data disqualification criteria.
* Telemetry format/layout and data provide a description of the telemetry mode, format, packetization and definition:

* Specify what types of packets are allowed to be sent for each of the telemetry modes.
* Specify maximum data rate for each mode.
* The telemetry format usually includes data type, data representation, data size, acceptable range values, unit of measure, and the meaning of the data for each field.

* Data recorder format/layout and data
* Command definition, e.g., onboard, ground, test specific, provides a description for each of the commands processed by the software work package. Include the purpose, function, the format of the command and its parameters, and any restrictions attendant to the command.
* Effecter command information provides information about the setting of names or flags that cause command executions in the software work products.
* Operational limits, e.g., maximum/minimum values, launch commit criteria information.
* Scheduling procedures and inter-processor/inter-task communications mechanisms, including time-rigid sequencing, preemptive scheduling and interrupts.
* Partitioning methods, means of preventing partition breaches, partitioning faults and partitioning metric data.

Other candidate information for the software data dictionary includes:

* Data channelization.
* Data description.
* Data location.
* Data relationships.
* Data sources and destinations.
* Data structure.
* Data type.
* Data units.
* Data use.
* Data values, e.g., range and calibration data.
* Database schema and database management systems.
* Object-oriented class and method descriptions.
* Entity-relationship diagrams.
* Input and output data conversions and units.

Finally, the SDD includes descriptions of each process carried by the database system, including:

* Where and how the data enters the system.
* What is done to the data, at what stage, and why.
* What the outputs of the system are (if any).
* How to control, update, and distribute the SDD.

When performing Class F software development, the appropriate Center Chief Information Officer is expected to provide appropriate guidance for the fulfillment of this requirement. In all cases, engineering judgment is expected to be used when finalizing the approach to develop the SDD.

## 3.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Small Projects

A software data dictionary is applicable to all projects regardless of size.  Small projects may be able to leverage SDDs, or portions of dictionaries, from previous projects, as long as those projects had similar data structures.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-219)

  [IEEE Standard for Software Reviews and Audits](https://ieeexplore.ieee.org/document/4601584 "Click to open in new window")

  IEEE Std 1028, 2008. IEEE Computer Society, NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
* (SWEREF-224)

  [Systems and software engineering - Software life cycle processes](https://ieeexplore.ieee.org/document/4475826 "Click to open in new window")

  ISO/IEC 12207, IEEE Std 12207-2008, 2008. IEEE Computer Society,  NASA users can access IEEE standards via the NASA Technical Standards System located at https://standards.nasa.gov/. Once logged in, search to get to authorized copies of IEEE standards.
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
* (SWEREF-373)

  [NPR 2210.1C - Release of NASA Software - Revalidated w/change 1](https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=2210&s=1C "Click to open in new window")

  NPR 2210.1C, Space Technology Mission Directorate, Effective Date: August 11, 2010, Expiration Date: January 11, 2022
* (SWEREF-565)

  [Develop and Test the Launch Procedure Early (1997)](https://llis.nasa.gov/lesson/609 "Click to open in new window")

  Public Lessons Learned Entry: 609.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-040 - Access to Software Products](/spaces/SWEHBVD/pages/102695417/SWE-040+-+Access+to+Software+Products) * [SWE-050 - Software Requirements](/spaces/SWEHBVD/pages/102695421/SWE-050+-+Software+Requirements) * [SWE-058 - Detailed Design](/spaces/SWEHBVD/pages/102695443/SWE-058+-+Detailed+Design)        * [5.14 - Test - Software Test Procedures](/spaces/SWEHBVD/pages/102695675/5.14+-+Test+-+Software+Test+Procedures) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) |

## 5.4 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p></p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 5.5 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

# 6. Lessons Learned

### 6.1 NASA Lessons Learned

* **Develop and Test the Launch Procedure Early (1997).** **Lesson Number** **0609[565](#_tabs-<p></p>):**  The Abstract states: "During the terminal countdown for the first attempted launch of Cassini, spacecraft telemetry channels indicated a false alarm condition that delayed verification of spacecraft readiness for launch, and contributed to a delay on the first launch day. The anomaly was traced to erroneous telemetry documentation. Develop and release the launch procedure early enough for comprehensive testing before launch. Rigorously test and verify all telemetry channels and their alarms and ensure documentation such as telemetry definitions is kept up to-date."

### 6.2 Other Lessons Learned

No other Lessons Learned have currently been identified for this requirement.
