# Appendix G: Technology Assessment/Insertion

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 206–213. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §G`.

Technology Assessment/Insertion G.1 Introduction, Purpose, and Scope In 2014, the Headquarters Office of Chief Engineer and Office of Chief Technologist conducted an Agency-wide study on Technical Readiness Level (TRL) usage and Technology Readiness Assessment (TRA) implementation. Numerous findings, observations, and recommendations were identified, as was a wealth of new guidance, best practices, and clarifications on how to interpret TRL and perform TRAs. These are presently being collected into a NASA TRA Handbook (in work), which will replace this appendix. In the interim, contact HQ/Steven Hirshorn on any specific questions on interpretation and application of TRL/TRA. Although the information contained in this appendix may change, it does provide some information until the TRA Handbook can be completed. Agency programs and projects frequently require the development and infusion of new technological advances to meet mission goals, objectives, and resulting requirements. Sometimes the new technological advancement being infused is actually a heritage system that is being incorporated into a different architecture and operated in a different environment from that for which it was originally designed. It is important to recognize that the adaptation of heritage systems frequently requires technological advancement. Failure to account for this requirement can result in key steps of the development process being given short shrift—often to the detriment of the program/project. In both contexts of technological advancement (new and adapted heritage), infusion is

a complex process that is often dealt with in an ad hoc manner differing greatly from project to project with varying degrees of success. Technology infusion frequently results in schedule slips, cost overruns, and occasionally even in cancellations or failures. In post mortem, the root cause of such events is often attributed to “inadequate definition of requirements.” If such is indeed the root cause, then correcting the situation is simply a matter of defining better requirements, but this may not be the case—at least not totally. In fact, there are many contributors to schedule slip, cost overrun, and project cancellation and failure—among them lack of adequate requirements definition. The case can be made that most of these contributors are related to the degree of uncertainty at the outset of the project and that a dominant factor in the degree of uncertainty is the lack of understanding of the maturity of the technology required to bring the project to fruition and a concomitant lack of understanding of the cost and schedule reserves required to advance the technology from its present state to a point where it can be qualified and successfully infused with a high degree of confidence. Although this uncertainty cannot be eliminated, it can be substantially reduced through the early application of good systems engineering practices focused on understanding the technological requirements; the maturity of the required technology; and the technological advancement required to meet program/project goals, objectives, and requirements.

TABLE G.1-1 Products Provided by the TA as a Function of Program/Project Phase

Gate

Product

KDP A: Transition from Pre-Phase A to Phase A

Requires an assessment of potential technology needs versus current and planned technology readiness levels, as well as potential opportunities to use commercial, academic, and other government agency sources of technology. Included as part of the draft integrated baseline. Technology Development Plan is baselined that identifies technologies to be developed, heritage systems to be modified, alternative paths to be pursued, fallback positions and corresponding performance descopes, milestones, metrics, and key decision points. Initial Technology Readiness Assessment (TRA) is available.

KDP B: Transition from

Technology Development Plan and Technology Readiness Assessment (TRA) are updated. Incorporated in the preliminary project plan.

KDP C: Transition from

Requires a TRAR demonstrating that all systems, subsystems, and components have achieved a level of technological maturity with demonstrated evidence of qualification in a relevant environment.

Phase A to Phase B

Phase B to Phase C/D

Source: NPR 7120.5.

A number of processes can be used to develop the appropriate level of understanding required for successful technology insertion. The intent of this appendix is to describe a systematic process that can be used as an example of how to apply standard systems engineering practices to perform a comprehensive Technology Assessment (TA). The TA comprises two parts, a Technology Maturity Assessment (TMA) and an Advancement Degree of Difficulty Assessment (AD2). The process begins with the TMA which is used to determine technological maturity via NASA’s Technology Readiness Level (TRL) scale. It then proceeds to develop an understanding of what is required to advance the level of maturity through the AD2. It is necessary to conduct TAs at various stages throughout a program/project to provide the Key Decision Point (KDP) products required for transition between phases. (See TABLE G.1-1.)

systems, subsystems, and components demonstrated through test and analysis. The initial AD2 provides the material necessary to develop preliminary cost and to schedule plans and preliminary risk assessments. In subsequent assessments, the information is used to build the Technology Development Plan and in the process, identify alternative paths, fallback positions, and performance descope options. The information is also vital to preparing milestones and metrics for subsequent Earned Value Management (EVM).

The initial TMA provides the baseline maturity of the system’s required technologies at program/project outset and allows monitoring progress throughout development. The final TMA is performed just prior to the Preliminary Design Review (PDR). It forms the basis for the Technology Readiness Assessment Report (TRAR), which documents the maturity of the technological advancement required by the

It is extremely important that a TA process be defined at the beginning of the program/project and that it be performed at the earliest possible stage (concept development) and throughout the program/project through PDR. Inputs to the process will vary in level of detail according to the phase of the program/ project, and even though there is a lack of detail in Pre-Phase A, the TA will drive out the major critical

The TMA is performed against the hierarchical breakdown of the hardware and software products of the program/project PBS to achieve a systematic, overall understanding at the system, subsystem, and component levels. (See FIGURE G.1-1.)

G.2 Inputs/Entry Criteria

1.3 Crew Launch Vehicle 1.3.8 Launch Vehicle ... 1.3.8.1 First Stage

1.3.8.2 Upper Stage

1.3.8.3 Upper Stage Engine

...

... 1.3.8.2.4 MPS

1.3.8.2.5 US RCS

1.3.8.2.6 FS RCS

1.3.8.2.7 TVCS

1.3.8.2.8 Avionics

1.3.8.2.9 Software

1.3.8.2.10 Integrated ... H/W Test

.1: Integ MPS

.1: Integ RCS

.1: Integ RCS

.1: Integ TVCS

.1: Integ Avionics

.1: MPTA

.2: LH System

.2: Integ Energy Support

.2: Actuator

.2: C&DH System

.1: Integ S/W System

.3: Hydraulic Power

.3: GN&C H/W

.3: O2 Fluid Sys. .4: Pressure & Pneumatic Sys.

.4: APU

.2: Flight S/W

.4: Radio Frequency System .5: EPS

.5: Umbilicals & Disconnect

.6: Electrical Integration .7: Develop Flight Instrument

.2: GVT .3: STA .4: US for DTF-1 .5: US for VTF-2 .6: US for RRF-3 .7: Struc. Thermal Component Test

.8: Sensor & Instrument System .9: EGSE .10: Integ CLV Avionics System Element Testing .11: Flight Safety System

FIGURE G.1-1 PBS Example

technological advancements required. Therefore, at the beginning of Pre-Phase A, the following should be provided:
- Refinement of TRL definitions.
- Definition of AD2.
- Definition of terms to be used in the assessment
process.
- Establishment of meaningful evaluation criteria
and metrics that will allow for clear identification of gaps and shortfalls in performance.
- Establishment of the TA team.
- Establishment of an independent TA review team.

G.3 How to Do Technology Assessment The technology assessment process makes use of basic systems engineering principles and processes. As mentioned previously, it is structured to occur within the framework of the Product Breakdown Structure (PBS) to facilitate incorporation of the results. Using the PBS as a framework has a twofold benefit—it breaks the “problem” down into systems, subsystems, and components that can be more accurately assessed; and it provides the results of the assessment in a format that can be readily used in the generation

of program costs and schedules. It can also be highly beneficial in providing milestones and metrics for progress tracking using EVM. As discussed above, it is a two-step process comprised of (1) the determination of the current technological maturity in terms of TRLs and (2) the determination of the difficulty associated with moving a technology from one TRL to the next through the use of the AD2. Conceptual Level Activities The overall process is iterative, starting at the conceptual level during program Formulation, establishing the initial identification of critical technologies, and establishing the preliminary cost, schedule, and risk mitigation plans. Continuing on into Phase A, the process is used to establish the baseline maturity, the Technology Development Plan, and the associated costs and schedule. The final TA consists only of the

TMA and is used to develop the TRAR, which validates that all elements are at the requisite maturity level. (See FIGURE G.3-1.) Even at the conceptual level, it is important to use the formalism of a PBS to avoid allowing important technologies to slip through the cracks. Because of the preliminary nature of the concept, the systems, subsystems, and components will be defined at a level that will not permit detailed assessments to be made. The process of performing the assessment, however, is the same as that used for subsequent, more detailed steps that occur later in the program/project where systems are defined in greater detail. Architectural Studies Once the concept has been formulated and the initial identification of critical technologies made, it is

Identify systems, subsystems, and components per hierarchical product breakdown of the WBS

Assign TRL to all components based on assessment of maturity

Assign TRL to subsystems based on lowest TRL of components and TRL state of integration

Baseline technology maturity assessment

Identify all components, subsystems, and systems that are at lower TRLs than required by program

Assign TRL to systems based on lowest TRL of subsystems and TRL state of integration

Perform AD2 on all components, subsystems, and systems that are below requisite maturity level

Technology Development Plan Cost Plan Schedule Plan Risk Assessment FIGURE G.3-1 Technology Assessment Process

necessary to perform detailed architecture studies with the Technology Assessment Process intimately interwoven. (See FIGURE G.3-2.) Requirements

Concepts

Architectural Studies

System Design

TRL/AD2 Assessment

Technology Maturation

FIGURE G.3-2 Architectural Studies and Technology Development

The purpose of the architecture studies is to refine end-item system design to meet the overall scientific requirements of the mission. It is imperative that there be a continuous relationship between architectural studies and maturing technology advances. The architectural studies should incorporate the results of the technology maturation, planning for alternative paths and identifying new areas required for development as the architecture is refined. Similarly, it is incumbent upon the technology maturation process to identify requirements that are not feasible and development routes that are not fruitful and to transmit that information to the architecture studies in a timely manner. It is also incumbent upon the architecture studies to provide feedback to the technology development process relative to changes in requirements. Particular attention should be given to “heritage” systems in that they are often used in architectures and environments different from those in which they were designed to operate.

G.4 Establishing TRLs A Technology Readiness Level (TRL) is, at its most basic, a description of the performance history of a given system, subsystem, or component relative to a set of levels first described at NASA HQ in the

1980s. The TRL essentially describes the state of a given technology and provides a baseline from which maturity is gauged and advancement defined. (See FIGURE G.4-1.) Programs are often undertaken without fully understanding either the maturity of key technologies or what is needed to develop them to the required level. It is impossible to understand the magnitude and scope of a development program without having a clear understanding of the baseline technological maturity of all elements of the system. Establishing the TRL is a vital first step on the way to a successful program. A frequent misconception is that in practice, it is too difficult to determine TRLs and that when you do, it is not meaningful. On the contrary, identifying TRLs can be a straightforward systems engineering process of determining what was demonstrated and under what conditions it was demonstrated. Terminology At first glance, the TRL descriptions in FIGURE G.4-1 appear to be straightforward. It is in the process of trying to assign levels that problems arise. A primary cause of difficulty is in terminology; e.g., everyone knows what a breadboard is, but not everyone has the same definition. Also, what is a “relevant environment?” What is relevant to one application may or may not be relevant to another. Many of these terms originated in various branches of engineering and had, at the time, very specific meanings to that particular field. They have since become commonly used throughout the engineering field and often acquire differences in meaning from discipline to discipline, some differences subtle, some not so subtle. “Breadboard,” for example, comes from electrical engineering where the original use referred to checking out the functional design of an electrical circuit by populating a “breadboard” with components to verify that the design operated as anticipated. Other terms come from mechanical engineering, referring

System test, launch, and operations

System/subsystem development

Technology demonstration

Technology development

Research to prove feasibility

Basic technology research

TRL 9 __

Actual system “flight proven” through successful mission operations

TRL 8 __

Actual system completed and “flight qualified”” through test and demonstration (ground or flight)

TRL 7

System prototype demonstration in a target/space environment

__ TRL 6 __

System/subsystem model or prototype demonstration in a relevant environment (ground or space)

TRL 5 __

Component and/or breadboard validation in relevant environment

TRL 4 __

Component and/or breadboard validation in laboratory environment

TRL 3 __

Analytical and experimental critical function and/or characteristic proof-of-concept

TRL 2 __

Technology concept and/or application formulated

TRL 1

Basic principles observed and reported

FIGURE G.4-1 Technology Readiness Levels

primarily to units that are subjected to different levels of stress under testing, e.g., qualification, protoflight, and flight units. The first step in developing a uniform TRL assessment (see FIGURE G.4-2) is to define the terms used. It is extremely important to develop and use a consistent set of definitions over the course of the program/project. Judgment Calls Having established a common set of terminology, it is necessary to proceed to the next step: quantifying “judgment calls” on the basis of past experience. Even

with clear definitions, judgment calls will be required when it comes time to assess just how similar a given element is relative to what is needed (i.e., is it close enough to a prototype to be considered a prototype, or is it more like an engineering breadboard?). Describing what has been done in terms of form, fit, and function provides a means of quantifying an element based on its design intent and subsequent performance. The current definitions for software TRLs are contained in NPR 7123.1, NASA Systems Engineering Processes and Requirements.

Assessment Team A third critical element of any assessment relates to the question of who is in the best position to make judgment calls relative to the status of the technology in question. For this step, it is extremely important to have a well-balanced, experienced assessment team. Team members do not necessarily have to be discipline experts. The primary expertise required for a TRL assessment is that the systems engineer/user understands the current state of the art in applications. User considerations are evaluated by HFE personnel who understand the challenges of technology insertions at various stages of the product life cycle. Having established a set of definitions, defined a process for quantifying judgment calls, and assembled an expert assessment team, the process primarily consists of asking the right questions. The flowchart depicted in FIGURE G.4-2 demonstrates the questions to ask to determine TRL at any level in the assessment. Heritage Systems Note the second box particularly refers to heritage systems. If the architecture and the environment have changed, then the TRL drops to TRL 5—at least initially. Additional testing may need to be done for heritage systems for the new use or new environment. If in subsequent analysis the new environment is sufficiently close to the old environment or the new architecture sufficiently close to the old architecture, then the resulting evaluation could be TRL 6 or 7, but the most important thing to realize is that it is no longer at TRL 9. Applying this process at the system level and then proceeding to lower levels of subsystem and component identifies those elements that require development and sets the stage for the subsequent phase, determining the AD2.

Has an identical unit been successfully operated/launched in identical configuration/environment?

YES

NO Has an identical unit in a different configuration/ system architecture been successfully operated YES in space or the target environment or launched? If so, then this initially drops to TRL 5 until differences are evaulated.

TRL 5

NO Has an identical unit been flight qualified but not yet operated in space or the target environment or launched?

YES

TRL 8

NO Has a prototype unit (or one similar enough to be YES considered a prototype) been successfully operated in space or the target environment or launched?

TRL 7

NO Has a prototype unit (or one similar enough to be considered a prototype) been demonstrated in a relevant environment?

YES

TRL 6

NO Has a breadboard unit been demonstrated in a relevant environment?

YES

TRL 5

NO Has a breadboard unit been demonstrated in a laboratory environment?

YES

TRL 4

NO Has analytical and experimental proof-of-concept been demonstrated?

YES

TRL 3

NO Has concept or application been formulated?

YES

TRL 2

NO Have basic principles been observed and reported?

YES

NO RETHINK POSITION REGARDING THIS TECHNOLOGY!

FIGURE G.4-2 TMA Thought Process

TRL 9

TRL 1

the system is at TRL 2. The problem of multiple elements being at low TRLs is dealt with in the AD2 process. Note that the issue of integration affects the TRL of every system, subsystem, and component. All of the elements can be at a higher TRL, but if they have never been integrated as a unit, the TRL will be lower for the unit. How much lower depends on the complexity of the integration. The assessed complexity depends upon the combined judgment of the engineers. It is important to have a good cross-section of senior people sitting in judgment.

X

X

X

X

### 1.0 System

### 1.1 Subsystem X

#### 1.1.1 Mechanical Components

#### 1.1.2 Mechanical Systems

#### 1.1.3 Electrical Components

X

X

#### 1.1.4 Electrical Systems

#### 1.1.5 Control Systems

#### 1.1.6 Thermal Systems

X

#### 1.1.7 Fluid Systems

X

#### 1.1.8 Optical Systems

#### 1.1.9 Electro-Optical Systems

1.1.10 Software Systems 1.1.11 Mechanisms

X

1.1.12 Integration
### 1.2 Subsystem Y

#### 1.2.1 Mechanical Components

FIGURE G.4-3 TRL Assessment Matrix

Overall TRL

Function

X

Appropriatae Scale

Fit

Unit Description

Form

Space Launch Operation

Space Environment

Flight Qualified

Brassboard

Concept

Breadboard

White = Unknown X = Exists

Protogype

Green = TRL 6 and above

Developmental Model

Yellow = TRL 3, 4 & 5

Environment Laboratory Environment

Demonstration Units

Red = Below TRL 3

Relevant Environment

Formal Process for Determining TRLs A method for formalizing this process is shown in FIGURE G.4-3 . Here, the process has been set up as a table: the rows identify the systems, subsystems, and components that are under assessment. The columns identify the categories that will be used to determine the TRL; i.e., what units have been built, to what scale, and in what environment have they been tested. Answers to these questions determine the TRL of an item under consideration. The TRL of the system is determined by the lowest TRL present in the system; i.e., a system is at TRL 2 if any single element in
