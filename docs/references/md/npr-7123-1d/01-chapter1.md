# NPR 7123.1D — Chapter1

> Source: https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter1
> Machine conversion; tables may be flattened.

# Chapter 1. Introduction

## 1.1 Background

**1.1.1** Systems engineering at NASA requires the application of a systematic, disciplined engineering approach that is quantifiable, recursive, iterative, and repeatable for the development, operation, maintenance, and disposal of systems integrated into a whole throughout the life cycle of a project or program. The emphasis of SE is on safely achieving stakeholder functional, physical, operational, and performance (including human performance) requirements in the intended use environments over the system's planned life cycle within cost and schedule constraints.

**1.1.2**  This NPR complements the NASA policy requirements for the administration, management, and review of all programs and projects, as specified in:

a. NPR 7120.5, NASA Space Flight Program and Project Management Requirements.

b. NPR 7120.7, NASA Information Technology Program and Project Management Requirements.

c. NPR 7120.8, NASA Research and Technology Program and Project Management Requirements.

d. NPR 7150.2, NASA Software Engineering Requirements.

e. NPR 8590.1, Environmental Compliance and Restoration Program.

f. NPR 8820.2, Facility Project Requirements (FPR).

**1.1.3** The processes described in this document build upon and apply best practices and lessons learned from NASA, other governmental agencies, and industry to clearly delineate a successful model to complete comprehensive technical work, reduce program and technical risk, and increase the likelihood of mission success. The requirements established in this NPR should be tailored and customized for criteria such as system/product size, complexity, criticality, acceptable risk posture, architectural level, development plans, and schedule following the guidance of Section 2.2.

**1.1.4** Changes from NPR 7123.1C for this revision include:

a. Adding requirements for an approach for Human Systems Integration (HSI) to be developed and documented, and adding a statement that HSI is co-owned by the Engineering Technical Authority, The Safety and Mission Assurance Technical Authority and the Health and Medical Technical Authority.

b. Adding a requirement for Integration plans to be baselined at Preliminary Design Review (PDR). The previous version had the update at System integration Review (SIR) as a requirement but did not say when it needed to be baselined.

c. Adding a requirement for the Verification and Validation plans to be baselined at PDR. The previous version had the results of the verification and validation activities as a requirement, but did not mention when the plan needed to be baselined.

d. Adding the above new requirements to Table 5-1, the Compliance Matrix in Appendix H, and Appendix G.

e. Adjusting Section 5.2.2.2 wording to bring timing into alignment with above requirements and Table 5-1.

f. Replacing all references to the Human System Integration Practitioner's Guide with references to the Human Systems Integration Handbook.

g. Clarifying that system security risks (including cybersecurity) are part of the technical risk process.

**1.1.5** Precedence

The order of precedence in case of conflict between requirements is the National Aeronautics and Space Act, 51 U.S.C. § 20113(a)(1); NPD 1000.0; NPD 1000.3; NPD 7120.4, NASA Engineering and Program/Project Management Policy; and NPR 7123.1, NASA Systems Engineering Processes and Requirements.

**1.1.6** Figures within this NPR are informational.

## 1.2 Framework for Systems Engineering Procedural Requirements

**1.2.1** Institutional requirements are the responsibility of the institutional authorities. They focus on how NASA does business and are independent of any particular program or project. These requirements are issued by NASA Headquarters and by Center organizations and are normally documented in NASA Policy Directives (NPDs), NASA Procedural Requirements (NPRs), NASA Standards, Center Policy Directives (CPDs), Center Procedural Requirements (CPRs), and Mission Directorate (MD) requirements. Figure 1-1 shows the flow down from NPD 1000.0 through Program and Project Plans.

**Figure 1-1 - Hierarchy of Related Documents**

**1.2.2** This NPR focuses on SE processes and requirements. It is one of several related Engineering and Program/Project NPRs that flow down from NPD 7120.4, as shown in
Figure 1-2.

**Figure 1-2 - Documentation Relationships**

## 1.3 Guiding Principles of Technical Excellence

**1.3.1** The Office of the Chief Engineer (OCE) provides leadership for technical excellence at NASA. As depicted in Figure 1-3, there are four pillars to achieving technical excellence and strengthening the SE capability. These pillars are intended to ensure that every NASA program and project meets the highest possible technical excellence.**Figure 1-3 - Technical Excellence - Pillars and Foundation**

a. **Clearly Documented Requirements, Policies, and Procedures.** Given the complexity and uniqueness of the systems that NASA develops and deploys, clear policies and procedures are essential to mission success. All NASA technical policies and procedures flow directly from NPD 1000.0. Policies and procedures are only as effective as their implementation, facilitated by personal and organizational accountability and effective training. OCE ensures policies and procedures are consistent with and reinforce NASA's organizational beliefs and values. OCE puts in place effective, clearly documented policies and procedures, supplemented by guidance in handbooks and standards to facilitate optimal performance, rigor, and efficiency among NASA's technical workforce.

b. **Effective Training and Development.** NASA is fortunate that the importance of its mission allows it to attract and retain the most capable technical workforce in the world. OCE bears responsibility for providing this workforce with the technical training and development necessary to carry out the Agency's missions. At the Agency level, NASA's Academy of Program/Project and Engineering Leadership (APPEL) provides for the development of engineering leaders and teams within NASA. APPEL is augmented by technical leadership development at many Centers. Training consists of more than just transferring a set of skills. In addition to ensuring that NASA's technical workforce is knowledgeable about standards, specifications, processes, and procedures, the training available through APPEL and other curricula is rooted in an engineering philosophy that grounds NASA's approach to technical work and decision making. These offerings give historical and philosophical perspectives that teach and reinforce NASA's organizational values and beliefs. OCE provides full support for training and development activities that will allow NASA to maximize the abilities of its technical workforce.

c. **Balancing Risk.**  Risk is an inherent factor in any spacecraft, aircraft, or technology development. Proper risk management entails striking a balance between the tensions of program/project management and engineering independence. Engineering rigor cannot be sacrificed for schedules and budgets, and likewise programmatic concerns cannot be overlooked in the development of the technical approach to a given program or project; technical risk will be consciously and deliberately traded against budget and schedule. The ETA is responsible for ensuring risks are considered and good engineering practices are followed in technical development and implementation. OCE oversees all activities related to the exercise of ETA across the Agency. Section 2.1.6 of this document contains additional information on the ETA responsibilities.

d. **Continuous Communications**. Communication lies at the heart of all leadership and management challenges. Most major failures in NASA's history have stemmed in part from poor communication. Among the Agency's technical workforce, communication takes a myriad of forms: continuous risk management (CRM)/risk-informed decision making (RIDM), data sharing, knowledge management, knowledge sharing, dissemination of best practices and lessons learned, and continuous learning to name but a few. The complexity of NASA's programs and projects demands a rigorous culture of continuous and open communication that flourishes within the context of policies and procedures and knowledge transfer, while empowering individuals at all levels to raise concerns without fear of adverse consequences. OCE promotes a culture of continuous communications.

**1.3.2** Personal and organizational accountability and responsibility lay the foundation for technical excellence.

a. **Personal Accountability.** Personal accountability means that each individual understands that he or she is responsible for the success of the mission. Each person, regardless of position or area of responsibility, contributes to success. What NASA does is so complex and interdependent that every component needs to work for the Agency to be successful. All of those who constitute NASA's technical community need to possess the knowledge and confidence to speak up when something is amiss in their or anyone else's area of responsibility to ensure mission success.

b. **Organizational Responsibility.**  NASA's technical organizations have a responsibility to provide the proper training, tools, and environment for technical excellence. Providing the proper environment for technical excellence means establishing regular and open communication so that individuals feel comfortable exercising their personal responsibility. It also requires ensuring that those who prefer to remain in the technical field (instead of management) have a satisfying and rewarding career track (e.g., NASA Technical Fellows, Senior Technical/Senior Level (ST/SL), or GS-15 technical leads).

**1.3.3** A central component of the environment for technical excellence is strengthening the SE capability.

## 1.4 Framework for Systems Engineering Capability

**1.4.1** The framework for SE capability consists of three elements—the common technical processes, tools and methods, and training for a skilled workforce. The relationship of the three elements is illustrated in Figure 1-4. The integrated implementation of the three elements of the SE framework is intended to strengthen and improve the overall capability required for the efficient and effective engineering of NASA systems. Each element is described below.

**Figure 1 4 - SE Framework**

a. **The common technical processes** of this NPR provide what has to be done to engineer quality system products and achieve mission success. These processes are applied to the integration of hardware, software, and human systems as one integrated whole. This NPR describes the common SE processes as well as standard concepts and terminology for consistent application and communication of these processes across the Agency. This NPR, supplemented by NASA/SP-6105, NASA Systems Engineering Handbook, and endorsed SE standards, also describes a structure for applying the common technical processes.

b. **Tools and methods** range from the facilities and resources necessary to perform the technical work to the clearly documented policies, processes, and procedures that allow personnel to work safely and efficiently. Tools and methods enable the efficient and effective completion of the activities and tasks of the common technical processes. The SE capability is strengthened through the infusion of advanced methods and tools into the common technical processes to achieve greater efficiency, collaboration, and communication among distributed teams. This NPR, supplemented by NASA/SP-6105, NASA Systems Engineering Handbook, and endorced SE standards and handbooks (e.g., NASA-HDBK-1009, NASA Systems Engineering Modeling Handbook for Systems Engineering), are resources for methods and tools to support the Centers' implementation of the required technical processes in their program/projects.

c. **A well-trained, knowledgeable, and experienced technical workforce** is essential for improving SE capability. The workforce will be able to apply NASA and Center tools and methods for the completion of the required SE processes within the context of the program or project to which they are assigned. In addition, they will be able to effectively communicate requirements and solutions to customers, other engineers, and management to work efficiently and effectively on a team. Issues of recruitment, retention, and training are aspects included in this element. The OCE will facilitate training the NASA workforce on the application of this and associated NPRs.

**1.4.2** Improvements to SE capability can be measured through assessing and updating the implementation of the common technical processes, use of adopted methods and tools, and workforce engineering training.

## 1.5 Document Organization

**1.5.1** This SE NPR is organized into the following chapters:

a. The Preface describes items such as the purpose, applicability, authority, and applicable documents of this NPR.

b. Chapter 1 describes the SE framework and document organization.

c. Chapter 2 describes the institutional and programmatic requirements, including roles and responsibilities. Tailoring of SE requirements and customizing SE practices are also addressed.

d. Chapter 3 describes the core set of common Agency-level technical processes and requirements for engineering NASA system products throughout the product life cycle.

e. Chapter 4 describes the activities and requirements to be accomplished by assigned NASA technical teams or individuals (NASA employees and NASA support contractors) when performing technical oversight of a prime or other external contractor.

f. Chapter 5 describes the life-cycle and technical review requirements throughout the program and project life cycles. Appendix G contains entrance/success criteria guidance for each of the reviews.

g. Chapter 6 describes the SEMP, including the SEMP role, functions, and content. Appendix J of NASA/SP-6105 provides details of a generic SEMP annotated outline.

  

|  |
| --- |
| | [TOC](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=main) | [ChangeLog](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=ChangeLog) | [Preface](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Preface) | [Chapter1](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter1) | [Chapter2](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter2) | [Chapter3](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter3) | [Chapter4](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter4) | [Chapter5](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter5) | [Chapter6](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=Chapter6) | [AppendixA](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixA) | [AppendixB](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixB) | [AppendixC](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixC) | [AppendixD](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixD) | [AppendixE](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixE) | [AppendixF](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixF) | [AppendixG](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixG) | [AppendixH](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixH) | [AppendixI](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixI) | [AppendixJ](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixJ) | [AppendixK](displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixK) | [ALL](displayAll.cfm?Internal_ID=N_PR_7123_001D_&page_name=ALL) | |
|  |
| | [NODIS Library](main_lib.html) | [Program Formulation(7000s)](lib_docs.cfm?range=7) | [Search](adv_search.cfm) | |

  

### DISTRIBUTION: NODIS

---

This document does not bind the public, except as authorized by law or as
incorporated into a contract. This document is uncontrolled when printed.
Check the NASA Online Directives Information System (NODIS) Library to
verify that this is the correct version before use:
[https://nodis3.gsfc.nasa.gov](https://nodis3.gsfc.nasa.gov/).

---
