# 8.56 - Source Code Quality Analysis

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695751. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis

8.56 - Source Code Quality Analysis

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695751/8.56+-+Source+Code+Quality+Analysis#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695751)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695751&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Code Quality Practices](#tabs-2)
* [3. Code Quality Analysis Techniques](#tabs-3)
* [4. Safety Analysis During Code](#tabs-4)
* [5. Code Quality Risk Assessment (CQRA)](#tabs-5)
* [6. Code Quality Analysis Reporting](#tabs-6)
* [7. Resources](#tabs-7)

Return to [8.16 - SA Products](/spaces/SWEHBVD/pages/102695744/8.16+-+SA+Products)

# 1. Introduction

The Source Code Quality Analysis product focuses on the implementation of the software requirements and design in the software source code. This topic describes some of the methods and techniques Software Assurance and Software Safety personnel may use to evaluate the quality and risk of the implementation and source code that was developed.

The purpose of performing source code analysis during the implementation phase of the life cycle is two-fold. The first is to determine whether the source code generated correctly implements the verified requirements and design. The second is to determine if the source code meets the quality standards desired by the project such as few or no defects, reliability, maintainability, efficiency, understandable, etc.

Some of the source code analysis methods and techniques mirror those used in design analysis. However, the results of the design techniques might be significantly different than those done earlier in the development phases because the final code may differ significantly from what was expected or predicted. Even though these analyses seem like repeats, during implementation they are run on actual code where previously, they were probably used on detailed design code-like products.

There are also attributes that cannot be analyzed until the source code and/or executables are available, such as code size, complexity, security weaknesses, vulnerabilities, timing, resource usage, etc. Some analysis may need to be performed repeatedly throughout the implementation phase to monitor for potential issues as the code base grows (e.g., static code analysis). This is particularly true if the early analyses uncover issues in the requirements or design that require rework. To aid in performing these analyses, there are tools available (free and commercial); however, many of them require compilable code.

The information on this topic is divided into several tabs as follows:

* Tab 1 – Introduction
* Tab 2 – Code Quality Guidance – provides general guidance for implementation
* Tab 3 – Code Quality Analysis Techniques and methods that can be used to improve the quality of the software
* Tab 4 – Safety Code Analysis – provides additional guidance when safety-critical software is involved with analysis emphasis on safety features
* Tab 5 - Code Quality Risk Assessment (CQRA)
* Tab 6 – Analysis Reporting Content
* Tab 7 – Resources for this topic

The following is a list of the applicable SWE requirements that relate to the source code quality analysis product:

| **SWE #** | **NPR 7150.2 [083](#_tabs-<p>7</p>) Requirement** | **NASA-STD-8739.8   Software Assurance and Software Safety Tasks** [278](#_tabs-<p>7</p>) |
| --- | --- | --- |
| 034 | 3.1.5 The project manager shall define and document the acceptance criteria for the software. | 1. Confirm software acceptance criteria are defined and assess the criteria based on guidance in the NASA Software Engineering Handbook, NASA-HDBK-2203. |
| 134 | 3.7.3 If a project has safety-critical software or mission-critical software, the project manager shall implement the following items in the software:   a. The software is initialized, at first start and restarts, to a known safe state. b. The software safely transitions between all predefined known states. c. Termination performed by software functions is performed to a known safe state. d. Operator overrides of software functions require at least two independent actions by an operator. e. Software rejects commands received out of sequence when execution of those commands out of sequence can cause a hazard. f. The software detects inadvertent memory modification and recovers to a known safe state. g. The software performs integrity checks on inputs and outputs to/from the software system. h. The software performs prerequisite checks prior to the execution of safety-critical software commands. i. No single software event or action is allowed to initiate an identified hazard. j. The software responds to an off-nominal condition within the time needed to prevent a hazardous event. k. The software provides error handling. l. The software can place the system into a safe state. | 1. Analyze the software requirements and the software design and work with the project to implement NPR 7150.2 requirement items "a" through "l."  2. Assess that the source code satisfies the conditions in the NPR 7150.2 requirement "a" through "l" for safety-critical and mission-critical software at each code inspection, test review, safety review, and project review milestone.  6. Ensure the SWE-134 implementation supports and is consistent with the system hazard analysis. |
| 159 | 3.11.5 The project manager shall test the software and record test results for the required software cybersecurity mitigation implementations identified from the security vulnerabilities and security weaknesses analysis. | 2. Assess the quality of the cybersecurity mitigation implementation testing and the test results. |
| 207 | 3.11.6 The project manager shall identify, record, and implement secure coding practices. | 1. Assess that the software coding guidelines (e.g., coding standards) includes secure coding practices. |
| 185 | 3.11.7 The project manager shall verify that the software code meets the project’s secure coding standard by using the results from static analysis tool(s). | 1. Analyze the engineering data or perform independent static code analysis to verify that the code meets the project’s secure coding standard requirements. |
| 061 | 4.4.3 The project manager shall select, define, and adhere to software coding methods, standards, and criteria. | 1. Assure the project manager selected and/or defined software coding methods, standards, and criteria.    2. Analyze that the software code conforms to all required software coding methods, rules, and principles. |
| 135 | 4.4.4 The project manager shall use static analysis tools to analyze the code during the development and testing phases to, at a minimum, detect defects, software security, code coverage, and software complexity. | 1. Analyze the engineering data or perform independent static code analysis to check for code detects defects, software quality objectives, code coverage objectives, software complexity values, and software security objectives.      3. Assess that the project addresses the results from the static analysis tools used by software assurance, software safety, engineering, or the project. |
| 080 | 5.1.3 The project manager shall track and evaluate changes to software products. | 1. Analyze proposed software and hardware changes to software products for impacts, particularly safety and security. |
| 081 | 5.1.4 The project manager shall identify the software configuration items (e.g., software records, code, data, tools, models, scripts) and their versions to be controlled for the project. | 2. Assess that the software safety-critical items are configuration-managed, including hazard reports and safety analysis. |
| 203 | 5.5.3 The project manager shall implement mandatory assessments of reported non-conformances for all COTS, GOTS, MOTS, OSS, and/or reused software components. | 2. Assess the impact of non-conformances on the project software's safety, quality, and reliability. |

## 1.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 2. Code Quality Practices

During implementation, source code is generated to reflect the software requirements and design. Whether interpreted or compiled, the source code is turned into executable software that can be analyzed and tested. There are many ways to assess and analyze the quality of the generated source code and its associated executables. Some of this guidance is sprinkled throughout this Handbook. The information discussed below provides a roadmap to those locations.

There are also a number of requirements in NPR 7150.2[83](#_tabs-<p>7</p>) and NASA-STD-8739.8[278](#_tabs-<p>7</p>) that require specific practices to be used during the code implementation phase. They include:

* [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices): Use of secure coding practices
* [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation): Use of validated and accredited tools
* [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis): Use of SCA, security scanning, cyclomatic complexity, and code coverage tools
* [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification): Perform SCA
* [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description): Use of security scans.
* [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test): Perform unit testing
* [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability): Create repeatable unit tests
* [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) via NASA-STD-1006: Implement command encryption and authentication, protect the confidentiality of command links, report interference, and train for unexplained interference.

 This sub-topic discusses the implementation guidance and requirements for these SWEs that touch on these specific practices. A generic list of “best coding practices” which can be considered during implementations is also provided.

## 2.1 Specific Required SWE Practices for Implementation

**2.1.1: Coding Standards:** are discussed in [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards), [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification), and [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices). Coding standards establish a set of rules, uniform coding practices, and quality guidelines, that make it easier to read, maintain, and debug the finished code. Their use should also help reduce complexity. Typically, most coding standards are comprised of industry-standard programming best practices, are language-specific, and often include best practices for other attributes such as safety and security. For example, the [Cert C Secure Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c) includes secure coding practices that could be used to improve the software’s security profile. Projects with safety-critical software should use a coding standard that includes both safety and security, if possible.

**2.1.2:****Use of Validated and Accredited Tools**: provides guidance on using validated and accredited tools for development and/or maintenance. The SWE tabs discuss how these tools can contribute significantly to the quality and safety of the software. They also provide information on how to get the tools accredited. Many of the tools listed below may be accredited, but this should be verified before use. Note: Version changes of tools may require reaccreditation. Examples of the types of tools that need to be validated and accredited include:

**Integrated Development Environment (IDE):** The guidance in [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) recommends the use of an IDE, particularly for larger projects. This provides the development team with the same integrated toolset, which may enhance productivity and improve communication. Examples of IDEs include Visual Studio, Eclipse, NetBeans, Vim/vi, and Emacs.

**Compilers and/or Interpreters:**  Compilers and interpreters transform source code written in a programming language (the source language) into object code. They may be included in an IDE but can be standalone (e.g., Intel compilers) or integrated into the OS (e.g., Gnu).

**Build automation tools:** Build automation tools are tools that automate the software build process. Depending on the coding language, this could include extracting the code from the source code repository, compiling and linking the code, creating the executable, and executing automated tests. They may be integrated into an IDE but can be standalone. Examples of build automation tools are makefiles, Jenkins, Gradle, Bamboo, and Apache Ant.

**Debuggers:** A debugger is a program used to step through the source code to help identify coding errors or other software work product issues. They are typically integrated into an IDE but can be standalone. Examples of debuggers are Polyspace, Bug Finder, IBM Rational Software Analyzer, and SonarLint.

These are examples of tools available commercially or as freeware. However, some tools that assist with developing and maintaining software may be created in-house (e.g., test tools). Tools originating in-house are expected to be validated in the same manner as other NASA software with a similar software classification.

**Note:**Keep in mind that whether tools are purchased commercially or are freeware, they need to be on the CIO list of approved software. The tools mentioned in this section are to give the reader context. They are not an endorsement.

**2.1.3:****Static Analysis**: [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) and [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) contain guidance on static analysis tools (a.k.a. static code analysis (SCA) or source code analysis tools) which are very useful for identifying coding errors and other potential issues including security weaknesses and safety issues. Static analysis tools are usually language-specific so projects must select tools for the coding languages used. In addition, the tools tend to have different features (e.g., safety, and security). Some static analysis tools are better at finding different problems so no single tool will find every issue. It is best to use a combination of tools. If engineering uses one SCA tool, then SA and Software Safety should use something different when performing their independent analysis. Examples of SCA tools are Klocwork, HP Fortify, CodeSonar, and Understand.

Depending on the static analysis tool(s) chosen, additional software engineering requirements may be met. For example:

**Cyclomatic Complexity**: [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software), [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) (Tab 7), and [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) provide additional guidance on Cyclomatic Complexity. By definition, it is a software metric used to indicate the complexity of a program. It is a quantitative measure of the number of linearly independent paths through a function’s source code. Currently, all safety-critical software components are required to have a cyclomatic complexity value of 15 or lower. Some static analysis tools and IDEs are able to calculate and provide this information. Look for the complexity numbers from one of these sources. Examples of tools that calculate cyclomatic complexity are SonarQube, JaCoCo, and the Eclipse Metrics plugin.

**Security Weaknesses and Vulnerabilities**SWE-139 and SWE-159 provide guidance on the use of a static analysis tool to detect cybersecurity security errors and defects.

Common Vulnerabilities and Exposures (CVE®)

Common Weakness Enumeration (CWE™)

**2.1.4: Security Scans:**[SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description), tab 7 and [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) provides minimal guidance on security scans, which includes performing a software composition analysis on the source code and examining the executables being released. The scans should be performed on software before it is deployed to its operational environment. Examples of tools to perform these scans include Black Duck, WhiteSource, Fortify on Demand, and WhiteHat. Additional information is available on the NASA Engineering Network (NEN) Software Security site.

**2.1.5: Unit Testing**: Unit testing is discussed in the [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) and [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) It is an important part of the implementation and is required for all software classes except Class E. Unit testing is particularly important for safety-critical software since it is often not possible to check some of the safety features once the system is integrated. For safety-critical software, the unit tests should be carefully planned and documented with the results recorded. Any errors, defects, or problems noted during testing should be captured in a defect/issue tracking system and tracked to closure. Unit tests should be repeatable as they must be able to reproduce the results.

**Code Coverage**: [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) and [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) discuss code coverage which is the percentage of the code that has been tested. For class A and B software, the code coverage should be 100%. If the code coverage is not 100%, an analysis of the uncovered code should be done. Uncovered code increases the risk of problems with the software. Usually, if code was not covered during testing, the reason is described by one of the categories below:

-Requirement missing - the code that hasn’t been covered is performing an essential activity, but no requirement indicates that this should be done.

-Test missing - the code that hasn’t been covered relates to an existing requirement, but no test was implemented for it.

-Extraneous/dead code - The code that hasn’t been covered is not traceable to any requirement and isn’t needed by the software. See also Topic [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software).

-Deactivated code - the code that hasn’t been covered isn’t traceable to any requirements for the current system but is intended to be executed in certain configurations.

The first two of these categories should be examined to see if they could be corrected by the addition of a test or requirement. If the uncovered code falls into the last two categories, a risk analysis should be done to determine whether the code should be removed from the component or not. For units of safety-critical software, code coverage should be measured during unit testing since many tests may not be feasible to run when more of the system is integrated. Examples of tools that can help determine the code coverage are gcov, ccov, coverture, Jenkins, and sonarqube.

## 2.2 **General Coding Best Practices**

When reviewing source code, some general coding best practices to look for are included in the Programming Practices Checklist [PAT-022](#_tabs-<p>7</p>) below:

Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.

**PAT-022 - Programming Practices Checklist**

## 2.3 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 3. Code Quality Analysis Techniques

There are many ways to evaluate the quality of the generated code and to determine whether the code meets the necessary capabilities and requirements for the project. Some of these techniques are already required by  NPR 7150.2[083](#_tabs-<p>7</p>) and/or NASA-STD-8739.8 [278](#_tabs-<p>7</p>) and quite a few others are listed in the guidance for various requirements in this Handbook.  Some of these are discussed below. These techniques may be used on all types of code, including safety-critical code. See tab 2 for general guidance on good coding practices that apply to both safety-critical and non-safety-critical software. See tab 4 for more information on analysis techniques for safety-critical software.

1. **Peer Reviews, Code Walk-throughs, or Inspections** – The requirements for peer reviews and inspections are addressed in [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management), [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures), and [SWE-089 - Software Peer Reviews and Inspections - Basic Measurements](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) of NPR 7150.2 [083](#_tabs-<p>7</p>). The primary purpose of these types of reviews is to identify errors in the code or to familiarize the stakeholders with the code. For code, these types of reviews are required as documented in the Project Plan or Development Plan and are often limited to critical portions of the code or complex sections. Characteristics of these reviews are: 1) advance preparation by attendees 2) use of a checklist 3) verify the product meets the requirements 4) participants usually include both team members and other peers 5) results are documented and errors and issues are addressed following the reviews. Much more information on these can be found under the guidance of the requirements above and in Topic 7.10 in this Handbook. These types of reviews are recommended for safety-critical areas of the code. See also Topic [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists).
2. **Checklists –** Checklists can be used to verify whether certain practices or processes have been during the code development of the software. One such checklist, Checklist of C Programming Practices for Safety, is found in the software guidance tab (tab 3) of [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) in this Handbook. This checklist was designed for safety-critical software and will help determine whether any of the safety-related best practices have been followed.
3. **Static Code Analysis –** [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) in NPR 7150.2 [083](#_tabs-<p>7</p>) requires the use of static analyzer tools during development and testing. Modern static code analysis tools can identify a variety of issues and problems, including but not limited to dead code, non-compliances with coding standards, security vulnerabilities, race conditions, memory leaks, and redundant code. Software peer reviews/inspections of code items can include reviewing the results from static code analysis tools. One issue with static code analyzers is they may generate a number of false positives that will need to be resolved and can be very time-consuming. Static code analyzers are not available for all platforms or languages. For critical code, it is essential to use sound and complete static analyzers. Sound and complete analyzers guarantee that all errors are flagged and that no false negatives (i.e., an erroneous operation is classified as safe) are generated. Such commercial analyzers are expensive but necessary for critical applications. Note that sound and complete static analyzers are now available free of charge for C and C++ software systems. More information can be found on static analyzers in the software guidance tab (tab 3) of [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) in the Software Engineering Handbook. The use of static code analyzers is required for safety-critical software.
4. **Bi-Directional Traceability** – The bi-directional traceability of the software requirements to the design components and the design components to the software code required in [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) will provide the information to help determine whether all of the requirements have been included in the design and code.
5. **Interface Analysis –** While interface analysis is not always done, it can identify many problems earlier in the life cycle. Interface errors are one of the most common types of errors. The coded interface should be checked against the interface definition documentation to be sure it has been coded correctly.
6. **Security Source Code Review –** This is a targeted review for security where the reviewer launches a code analyzer that checks for potential security issues and steps through the code line by line to evaluate any potential issues.
7. **Analysis for COTS, GOTS, OSS, and reuse code –** All the categories of reused code should be checked for a number of potential problems before being included in the final code base. Items to look for are: 1) unused code/dead code 2) unnecessary functionality 3) Does the reused code work properly using the same assumptions and constraints as the system being developed? (Think about boundary conditions.) 4) Are there potential security problems? There are tools that can help with some of these questions, but some additional vendor information may be necessary. For COTS or OTS where the source code is not available, it may be possible to get some security information by reviewing the version history and looking for previous security problems.
8. **Unit Testing –** Unit testing is considered part of the implementation. It is required in [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) and is very important for checking the individual functionality of each unit of code. It must be done before code integration since, after integration, the individual component inputs and outputs are often no longer accessible.
9. **Code Analysis for Architecture, Quality, and Security Assessments /CQRA)–** This code analysis is an approach to evaluate code quality by using an automated analysis of the software to assess the degree to which it satisfies one or more desired quality attributes. The NASA team has completed the prototyping as well as testing the adapted tool on several NASA projects. The process can be used to assess the risk associated with certain code quality attributes. A Code Quality Risk Assessment (CQRA) process and set of tools are available for use to determine the risk associated with any project's source code.  There is a description of the tool with an example of its output in the Code Quality Risk Assessment (CQRA) tab 5 in this Topic 8.16 - Code Quality Risk Assessment (CQRA)

## 3.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 4. Safety Analysis During Code

Some of the same analysis techniques listed in Tabs 2 and 3 are also applicable and many are recommended or required for safety-critical software. For some of the techniques in the previous tab, the Software Assurance team may be using some of these techniques such as the use of **Checklists**. It is during software implementation (coding) that software controls of safety hazards are actually realized.  Safety requirements have been passed down through the designs to the coding level. Programmers must recognize not only the specific safety-related design elements but should also be aware of the types of errors that can be introduced into the non-safety code which can compromise safety controls. **Coding checklists** should be provided to check for common errors.  **Safety Checklists** can be used to verify that all the safety features and safety requirements have been included in the code. **Programming Checklists** (See the section on Programming Checklists under the Topics in this Handbook may be used to check for best practices, compliance to coding standards, common errors, and problems noted in lessons learned. When checklists are used, the Software Safety personnel should be reviewing the results and make sure that any issues found have been addressed.

Similarly, with the **static code analysis**, the Software Safety personnel will generally be reviewing the results, particularly noting any issues that might cause safety problems and verifying they have been addressed. Safety Personnel should be attending the **peer reviews** of any safety-critical modules. Software Safety Personnel should also be looking at the **bi-directional traceability** to ensure that all of the safety-related requirements have been correctly designed and correctly converted from the design into the code.

1. **Unit Test Analysis** – The Software Safety Personnel should review or witness the unit testing of the safety-critical modules to be sure they produce the expected results. Unit testing is particularly important with safety-critical software since many of the safety features are very difficult to test once the whole system has been integrated. Also, see the information in Topic 8.16 - Tab 5 on unit testing safety-critical software.
2. **Code Logic Analysis** – Code logic analysis evaluates the sequence of operations represented by the coded program to detect logic errors in the coded software. Generally, this analysis is only applied to safety-critical software modules as it is a time-consuming activity. To do this, flow charts are developed from the actual code and compared with the design descriptions and flow diagrams. Similarly, the equations in the code are compared with the equations in the design materials. Finally, memory decoding is used to identify critical instruction sequences even when they may be disguised as data. The analyst should determine whether each instruction is valid and if the conditions under which it can be executed are valid.  Memory decoding should be done on the final code.
3. **Code Data Analysis** – The objective of code data analysis is to ensure that the data is being defined correctly and used properly. The usage and value of the data items in the code should be compared with their descriptions in the design. Another concern is to ensure that the data is not being altered inadvertently or over-written. Also, check to see that interrupt processing is not interfering with the safety-critical data.
4. **Code Interface Analysis** – Code interface analysis is intended to verify that the interfaces have been implemented properly. Check that the parameters are properly passed across interfaces.  Verify that data size, measurement unit, byte sequence, and bit order within bytes are the same on all sides of the interface.
5. **Unused Code Analysis** –Unused code is a problem because it can contain routines that might be hazardous if inadvertently executed and because it may cause unnecessary complexity and usage of resources. Unused code can generally be identified by using static code analyzers.
6. **Final Timing, Throughput, and Sizing Analysis -**With the completion of the coding phase, the timing, throughput, and sizing parameters can be measured. The size of the executable component (storage size) is easily measured, as is the amount of memory space used by the running software.  Special tests may need to be run to determine the maximum memory used, as well as timing and throughput parameters.  Some of these tests may be delayed until the testing phase, when they may be formally included in functional or load/stress tests.  However, simple tests should be run as soon as the appropriate code is stable, to allow verification of the timing, throughput, and sizing requirements.
7. **Interrupt Analysis** –This analysis focuses on the effect of interrupts on program flow and potential data corruption. For example, can an interrupt keep a safety-critical task from completing? Can a low-priority process interrupt a high-priority task and change data? When analyzing interrupts, think about the following: program segments where interrupts are locked out, re-entrant code, interruptible code segments (protect a timing-critical component from interrupts if a delay would be unacceptable), priorities, and undefined interrupts. See the checklist below for many more questions to be considered when checking the use of interrupts.

**PAT-032 - Considerations for Interrupt Analysis [PAT-032](#_tabs-<p>7</p>)**

**Click on the image to preview the file. From the preview, click on Download to obtain a usable copy.**

****PAT-032 - Considerations When Using Interrupts****

Performing these types of analyses will likely result in finding a number of coding errors in addition to areas where changes or additions need to be made to the requirements. All errors found should be documented in a tracking system and tracked to closure. If errors are found in the requirements, these requirements changes should go through the formal change process and when approved the design and code should be changed accordingly. Hazard analyses should be updated to reflect the changes.

Any safety analysis done should be reported at reviews and regular status meetings with the project. Reporting should include the identification of the source code analyzed, the types of analyses performed, the types and numbers of errors/issues found, the timeframe for resolutions of the issues, and the overall status of the code, based on the analyses done. Include an assessment of any risks identified.

## 4.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 5. Code Quality Risk Assessment (CQRA)

## 5.1 Introduction

**How can we determine the risk and quality of software code?**

**There are risks that any organization takes on in creating new software.**

Drilling down a level – and particularly for mission- and safety-critical systems, the code itself entails risks. For  example, consider the risk that a code base is:

* Hard to test thoroughly
* Prone to critical failures/crashes
* Unmaintainable over its expected lifecycle
* Tough to extend new capabilities
* Exploitable to cyber attacks
* Difficult to harvest for reuse
* Plagued with a multitude of latent defects
* Hard to change without adding new defects

Code Quality Risk Assessment – Objectives

The goals of the Code Quality Risk Assessment are to create a simple framework to guide code risk estimations, where:

* The analyst is presented with code-level questions to consistently direct the analysis
* Questions are answerable using static analysis (SA) tools and by reading the code
* The questions are intended to be SA tool agnostic
* The framework is directly applicable to critical embedded systems coded in C/C++
* Detailed code-centric questions aim to objectify the risk estimation as much as possible
* Risk is estimated statistically – i.e. no question or referenced metric is “make or break”
* Questions of differing types can be scored and combined to derive a resulting risk
* Questions and scoring remain constant over numerous projects in order to gather historical perspective over time

The Code Quality Risk Assessment is a new process and set of tools now available to help in the evaluation of source code risk. It is an adapted technique measuring the structural code quality adapted from a pre-existing Carnegie Mellon University (CMU) Software Engineering Institute (SEI). Through the evaluation of a number of questions in 6 main aspect areas, it is able to provide direct insight into the strengths and weaknesses in the quality of the source code. These insights can be particularly useful for the success of the software for NASA missions and for future reuse purposes. The main goal of the technique is: To consider just the source code and estimate the degree of risk in the software. The target is to determine the Structural Code Quality (the quality of the code itself), rather than the Functional Code Quality (how well the code fulfills the mission requirements.

## 5.2 Steps in Code Quality Risk Assessment

The code risk assessment process consists of several steps:

* It employs a set of code-centric questions specific to 6 aspects of the code and 31 foci among the aspects. These aspects and foci are shown in the picture below. Another set of tables shows each aspect and why it is important.
* Static analysis tools are applied to help the analyst answer the questions.
* Finally, the answers are scored to arrive at a risk level for each focus, and

  aspect, and then results are rolled up to an overall risk level. The risk is rated on a numerical scale from 1 (for low risk) to 5 (for high risk). The tool reflects this numerical scale pictorially using color changes from green (1) to red (5).

The diagram below shows the 6 aspects evaluated and the foci evaluated in each aspect

  

The following table lists the aspects and the importance of each:

| **Aspects** | **Why it is important** |
| --- | --- |
| Architecture | In most successful software projects, the expert developers working on that project have a shared understanding of the system design. This shared understanding is called ‘architecture.’— Martin Fowler CQRA seeks for built-in evidence that there is a shared & demonstrated mutual understanding of the SW’s design principles. Similarly, CQRA looks for abnormalities in software architecture to help ensure the longevity of the software’s internal quality. |
| Maintainability | SW maintainability is a direct indicator of how easy SW will be to reuse, repair, and fix in the future  The modification of a software product after delivery to correct faults, improve performance or other attributes, or adapt the product to a modified environment. – IEEE 1219 Poor code maintainability means more time and cost required to modify and fix issues that emerge later in the lifecycle or mission. |
| Testability | The testability component of CQRA seeks to identify the quality of unit tests as well as the complexity of the code (to identify the level of testability). |
| Standards | CQRA leverages an overlap of safety-critical coding standards to identify key risks to mission software. |
| Fault Tolerance | CQRA Fault Tolerance quantifies the level of risk in:  The number/quality of exceptions/errors that are logged  How descriptive logs are  The code has evidence of mitigations (watchdog timers, health & safety)  Checked return values  Checked user inputs CQRA Fault Tolerance can identify pathways to more stable code in off-nominal conditions (from a structural perspective). |
| Security | CQRA Security addresses potential security concerns within code. The SEI CERT Secure Coding Standard is leveraged in addition to preventative questions connected to SCA tools/analyst code analysis. |

## 5.3 Viewing the CQRA output

The picture below shows a sample of the CQRA output. Column 1 gives the numeric value for the aspect risk. Column 2 shows the numeric risk for the Focus area in column 3. Column 4 details the strong points of the code for that aspect and column 5 lists areas where the aspect could be improved.

## 5.4 Obtaining CQRA for use on your project (NASA only)

The team that adapted the CMU/SEI process for NASA has completed several prototypes and decided that the method is ready to be used more widely across NASA. If your team is interested in using this method of evaluating to evaluate your existing source code, contact the Software Assurance Tech Fellow. The name and contact information can be obtained by going to the SMA home page at <https://sma.nasa.gov/>. Expand the size of your window so you can see the Search option in the upper right corner (or use the three little lines in the upper right-hand side of the page to drop down the menu of options). Choose "SMA Disciplines and Programs", then scroll down and choose "Software Assurance and Safety." Scroll down to the people section and look for the Tech Fellow.

Another potential point of contact for obtaining the tool is to contact the Lead of the Software Support Outreach (SSO) Office of the NASA IV&V Facility.

## 5.5 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-7) in the Resources tab.

# 6. Code Quality Analysis Reporting

## 6.1 Documenting and Reporting of Analysis Results

When the design is analyzed, the ***Source Code Quality Analysis*** work product is generated to document the results. It should include a detailed report of the source code analysis results. Analysis results should also be reported in a high-level summary and conveyed as part of weekly or monthly SA Status Reports. The high-level summary should provide an overall evaluation of the analysis, any issues/concerns, and any associated risks. If a time-critical issue is uncovered, it should be reported to management immediately so that the affected organization may begin addressing it at once.

When a project has safety-critical software, analysis results should be shared with the Software Safety personnel. The results of an analysis conducted by Software Assurance personnel and those done by Software Safety personnel may be combined into one analysis report if desired.

## 6.2 High-Level Analysis Content for SA Status Report

Any source code quality analysis performed since the last SA Status Report or project management meeting should be reported to project management and the rest of the Software Assurance team. When a project has safety-critical software, any analysis done by Software Assurance should be shared with the Software Safety personnel.

When reporting the results of an analysis in a SA Status Report, the following defines the minimum recommended contents:

* Identification of what was analyzed: Mission/Project/Application
* Period/Timeframe/Phase analysis performed during
* Summary of analysis techniques used
* Overall assessment of design, based on analysis
* Major findings and associated risk
* Current status of findings: open/closed; projection for closure timeframe

## 6.3 Detailed Content for Analysis Product

The detailed results of all source code quality analysis activities are captured in the ***Source Code Quality Analysis*** product. This document is placed under configuration management and delivered to the project management team as the Software Assurance record for the activity. When a project has safety-critical software, this product should be shared with the Software Safety personnel.

When reporting the detailed results of the software design analysis, the following defines the minimum recommended content:

* Identification of what was analyzed: Mission/Project/Application
* Person(s) or group performing the analysis
* Period/Timeframe/Phase analysis performed
* Documents and Tools used in the analysis (e.g., architectural and detailed design, Klocwork)
* Description or identification of analysis techniques used. Include an evaluation of the techniques used.
* Overall assessment of source code quality, based on analysis results
* Major findings and associated risk – Detailed reporting should include where the finding, issue, or concern was discovered and an assessment of the amount of risk involved with the finding.
* Minor findings
* Current status of findings: open/closed; projection for closure timeframe
* Include counts for those discovered by SA and Software Safety
* Include overall counts from the Project’s problem/issue tracking system.

# 7. Resources

## 7.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"

## 7.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 7.3 Process Asset Templates

Click on a link to download a usable copy of the template. (SASource)

* (PAT-022 - )

  [PAT-022 - Programming Practices Checklist,](https://swehb.nasa.gov/download/attachments/115933208/Programming%20Practices%20Checklist.docx?api=v2 "Click to open in new window")

  Topic 8.56 - Source Code Quality Analysis, tab 2.2,
* (PAT-032 - )

  [PAT-032 - Considerations When Using Interrupts](https://swehb.nasa.gov/download/attachments/123600994/Considerations%20for%20Interrupt%20Analysis.docx?api=v2 "Click to open in new window")

  Source Code Quality Analysis, tab 4, Also found in Hazard Analysis Assets Process Asset Templates, Implementation Assets Process Asset Templates, and Safety Specific Assets Process Asset Templates

## 7.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-052 - Bidirectional Traceability](/spaces/SWEHBVD/pages/102695427/SWE-052+-+Bidirectional+Traceability) * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-061 - Coding Standards](/spaces/SWEHBVD/pages/102695445/SWE-061+-+Coding+Standards) * [SWE-062 - Unit Test](/spaces/SWEHBVD/pages/102695446/SWE-062+-+Unit+Test) * [SWE-063 - Release Version Description](/spaces/SWEHBVD/pages/102695447/SWE-063+-+Release+Version+Description) * [SWE-086 - Continuous Risk Management](/spaces/SWEHBVD/pages/102695470/SWE-086+-+Continuous+Risk+Management) * [SWE-087 - Software Peer Reviews and Inspections for Requirements, Plans, Design, Code, and Test Procedures](/spaces/SWEHBVD/pages/102695472/SWE-087+-+Software+Peer+Reviews+and+Inspections+for+Requirements+Plans+Design+Code+and+Test+Procedures) * [SWE-089 - Software Peer Reviews and Inspections - Basic Measurement](/spaces/SWEHBVD/pages/102695474/SWE-089+-+Software+Peer+Reviews+and+Inspections+-+Basic+Measurements) * [SWE-135 - Static Analysis](/spaces/SWEHBVD/pages/102695494/SWE-135+-+Static+Analysis) * [SWE-136 - Software Tool Accreditation](/spaces/SWEHBVD/pages/102695495/SWE-136+-+Software+Tool+Accreditation) * [SWE-157 - Protect Against Unauthorized Access](/spaces/SWEHBVD/pages/102695513/SWE-157+-+Protect+Against+Unauthorized+Access) * [SWE-185 - Secure Coding Standards Verification](/spaces/SWEHBVD/pages/102695521/SWE-185+-+Secure+Coding+Standards+Verification) * [SWE-186 - Unit Test Repeatability](/spaces/SWEHBVD/pages/102695522/SWE-186+-+Unit+Test+Repeatability) * [SWE-189 - Code Coverage Measurements](/spaces/SWEHBVD/pages/102695524/SWE-189+-+Code+Coverage+Measurements) and [SWE-190 - Verify Code Coverage](/spaces/SWEHBVD/pages/102695525/SWE-190+-+Verify+Code+Coverage) * [SWE-207 - Secure Coding Practices](/spaces/SWEHBVD/pages/102695541/SWE-207+-+Secure+Coding+Practices) * [SWE-220 - Cyclomatic Complexity for Safety-Critical Software](/spaces/SWEHBVD/pages/105709643/SWE-220+-+Cyclomatic+Complexity+for+Safety-Critical+Software)       * [5.26 - Source Code Quality Analysis Report Minimum Content](/spaces/SWEHBVD/pages/140641734/5.26+-+Source+Code+Quality+Analysis+Report+Minimum+Content) * [7.08 - Maturity of Life Cycle Products at Milestone Reviews](/spaces/SWEHBVD/pages/102695638/7.08+-+Maturity+of+Life+Cycle+Products+at+Milestone+Reviews) * [7.10 - Peer Review and Inspections Including Checklists](/spaces/SWEHBVD/pages/102695640/7.10+-+Peer+Review+and+Inspections+Including+Checklists) * [8.19 - Dead / Dormant Code and Safety-Critical Software](/spaces/SWEHBVD/pages/102695759/8.19+-+Dead+Dormant+Code+and+Safety-Critical+Software) * [PAT-032 - Considerations When Using Interrupts](/spaces/SITE/pages/123600994/PAT-032+-+Considerations+When+Using+Interrupts) |

## 7.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>7</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

## 7.6 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |
