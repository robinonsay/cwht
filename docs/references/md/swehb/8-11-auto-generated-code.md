# 8.11 - Auto-Generated Code

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695729. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code

8.11 - Auto-Generated Code

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695729/8.11+-+Auto-Generated+Code#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695729)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695729&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Introduction](#tabs-1)
* [2. Guidance](#tabs-2)
* [3. Practices](#tabs-3)
* [4. Lessons Learned](#tabs-4)
* [5. Resources](#tabs-5)

# 1. Introduction to Auto-Generated Code

Model-based software development uses a model as the centerpiece of the development process. Software engineers create a model of the system behavior that can then be translated into different languages such as C or Ada by the appropriate code generator. The model is continually refined throughout the development process and can even be executable. For maximum benefit, the generated code should not be modified by software engineers; when changes are desired, the model is revised, and code is generated from the revised model.

Both the modeling tool and the code generation tool are part of a toolset that makes up the model-based development system, referred to in this guidance as MBDS. The code resulting from MBDS is referred to as auto-generated code.

Efficiency is a key benefit of using MBDS, but there are many considerations to be reviewed when deciding whether MBDS is the right choice for a project.

The need for safe, reliable and secure execution of software is just as applicable to auto-generated software as to software developed by any other means.

# 2. Guidance for Assuring Auto-generated Code

Assurance for auto-generated code covers two main areas:

1. 1. assurance of the decision of *whether* to use auto-generation, and
   2. when it is used, *the assurance practices to follow*.

This NASA Software Engineering Handbook Topic addresses area (a) in its Sections 2.1 (Considerations for Choosing Auto-Generated Code -Usage and Needs) and 2.2 (Considerations for Choosing Auto-Generated Code - Pros and Cons), and area (b) in its sections 3.0 (Software Assurance Practices for Auto-Generated Code). Software assurance personnel should become familiar with the software recommendations on that topic.

Past projects have differed considerably in their approaches to, and use(s) of, auto-generation. Several relatively recent surveys: Torchiano et al, 2013 [660](#_tabs-<p>5</p>), Liebel et al, 2016 [656](#_tabs-<p>5</p>),  and Goseva-Popstojanova et al [647](#_tabs-<p>5</p>) all report this variety. It follows that appropriate assurance is very context-dependent.

## 2.1 Considerations for Choosing Auto-Generated Code-Usage and Needs

When deciding to use auto-generation it is also important to determine whether the generated code will be used as-is or require further (manual) modification. Some of the many factors to be considered, starting with this applicability and purposes are listed below:

* **Applicability**: the applicability of the requirements is determined by the **software classification** and the software **safety-criticality** and is specified by the requirements mapping table in Appendix A of NPR 7150.2 [083](#_tabs-<p>5</p>)
* **Purpose**: the auto-generated code can:
  + become (part of) operational code (for flight and/or ground facilities),
  + be used to test of operational code, or
  + be used for rapid prototyping or simulation.
* These different uses lead to different needs and constraints. For example, maintenance of operational code will extend through the lifetime of the mission, whereas maintenance of testing and prototyping code may no longer be needed once development has completed. Flight code’s runtime performance on the flight computer(s) will typically be important, whereas simulation code may be provided with additional computational resources as needed. Note that as per NASA-STD-8739.8A [278](#_tabs-<p>5</p>) (Software Assurance and Software Safety Standard), software that provides full or partial verification or validation of safety-critical systems, including hardware or software subsystems (e.g., this can include models and simulations) can also be safety-critical. Also, be aware of NASA-STD-7009 [272](#_tabs-<p>5</p>) (Standard for Models and Simulations) when considering the use of modeling and simulation. See also Topic [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009).
* **Generator technology**: the code generator may consist of, or combine, a commercial product, open-source technology, an institutional asset reused on multiple projects, or “homebrew” project-specific developments. Different implications stem from these, e.g., COTS-like considerations for commercial products, sustainment and maintenance considerations for “homebrew” technology.
* **Input**: the inputs to the code generator can be of different formats/representations (e.g., different modeling languages such as Stateflow, Simulink, or AADL, XML specifications, database schema, etc.). The choice of inputs to code generator could impact the flexibility (e.g., a proprietary format may restrict the ability for the input to be reused as input to other generator tools) and complexity of the resulting inputs. The suitability of the modeling representation with respect to domain and behavior modeled can affect the effort needed to create the inputs/models. Additionally, inputs to the code generator may be reused from other projects; and therefore, additional assurance activities to address concerns/risks similar to code reuse are needed.
* **Interface/Integration**: the generated code may be of fully executable code or only partially executable (e.g., form a skeleton of the software or implement a database). Additionally, generated code may be of a stand-alone code or integrated with legacy code.
* **Post-generation-editing**: a major distinction is between auto-generated code that is to be used “as-is” (i.e., once generated, it will not be further edited) vs, the anticipated need for further editing after generation.
* **V&V**: the amenability of generated code to V&V practices may vary (e.g., as mentioned earlier, auto-generated code may be more voluminous and/or harder to understand than would be the equivalent hand-developed code); similarly, the amenability of the auto generation’s inputs to V&V practices may also vary (e.g., offering opportunities for formal analysis)

## 2.2 Considerations for Choosing Auto-Generated Code-Pros and Cons

This section lists some of the advantages and disadvantages of using auto-generated code which also needs to be considered when deciding whether to use auto-generated code.

When trying to determine whether to use MBDS and auto-generated code, it is useful to consider the characteristics usually thought of as advantages (or pros) as well as those characteristics which have been identified as disadvantages (or cons.) The most commonly sited pros are productivity, simplification, portability, and consistency.1

**Productivity**: The developer provides inputs to the code generator, and it generates the code, based on the model and the inputs, usually producing code at a much faster rate than can usually be done with hand-coding. In addition, once the code generator is set up, it can be used many times.

**Simplification**: Code is generated from an abstract description or model. Typically, it is easier to analyze the abstract description or model then it is to analyze the code. Changes can be made in the models and then the code generator can be rerun to produce code with the correct changes.

**Portability**: Once there is a process for generating code in one language, the code can be changed to another language by changing the code generator being used.

**Consistency**: When using a code generator, the generated code always follows the principles, types, and rules set up for the generator. Thus, the quality of the code is consistent.

The most common disadvantages or cons of auto-generated code are maintenance and complexity.

**Maintenance**: Once the code has been generated, the users are dependent on the code generator and it will need to be updated periodically to stay up to date. There are often issues with finding/keeping a developer who can maintain the code generators.

**Complexity**: The auto-generated code tends to be more complex than the hand-generated code. It is also less optimized than the hand-generated code. This bulk and complexity may make it more difficult to analyze and correct the code if the code generated is not producing the expected results.

## 2.3 Assurance of the decision of whether to use auto-generation

The role of Software Assurance should be to check that a project’s decision to use auto-generation is well-founded, i.e., the project has identified, understood and appropriately taken into account the full range of relevant considerations. This should cover how the project plans to address any additional challenges that auto-generation might pose, as well as how the project may be able to take advantage of additional opportunities. In the course of this, Software Assurance may be of help by offering advice and recommendations as appropriate.

A good starting point and a rich source of information on this topic are the SEI’s Technical Report “Model-Driven Engineering: Automatic Code Generation and Beyond” Klein et al, 2015 [655](#_tabs-<p>5</p>). From its abstract: “*This report focuses on the application of MDE [model-driven engineering] tools for automatic code generation when acquiring systems built using these software development tools and processes.*” Although worded in terms of the acquisition, the report’s material is equally informative to the supplier building the system. Whichever the role of Software Assurance (Acquirer SA, or Supplier SA), this report should prove useful when auto-generation of code is being considered. In addition to the report’s expository material, Appendix A contains tables listing risk areas as they pertain to auto code generation, and Appendix B contains a questionnaire with which to collect information about a particular MDE auto-code generation tool.

See also [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software).

## 2.4 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

For Testing Analysis related to auto-generated code see Topic [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis).

# 3.0 Software Assurance Practices for Auto-Generated Code

## 3.1 Assurance practices to follow when auto-generation is used

Assurance practices specifically required in the NASA-STD-8739.8 [278](#_tabs-<p>5</p>) for models or auto-generated code include the assurance tasks associated with

* [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools)
* [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items)
* [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code)
* [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements)
* [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs)

The assurance for these tasking requirements will be tailored by the software classification and safety-criticality. Many other tasking requirements that do not specifically mention auto-generated code or models may still apply and the amount of assurance applied for these requirements will depend on the software assurance personnel’s best judgment. Guidance for the tasking requirements specifically mentioned is below:

Tasking for [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) calls for confirming the software models has been validated and accredited. Software engineering is responsible for the actual validation and accreditation of the models, and assurance just needs to confirm that this has been done. In the case of the models associated with the auto-generation of code, it is important to make sure that the model is correct as well as the code-generator and that the inputs being used produce the expected results when the code generation tools re being used.

Tasking for [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) lists models as an example item is included in those items that are identified to be configuration managed. The models associated with auto-generated code should definitely be configuration managed. [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code), part g also calls for the inputs to the auto-generation tool, the outputs of the auto-generation tool and any modifications to the outputs of the auto-generation tool to be configuration managed. Software assurance will confirm that all of these are identified as configuration items and are being configuration managed.

Tasking for [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) calls for software assurance to assess the software plans, processes, and procedures for the approaches that satisfy the bulleted list of conditions in SWE-146. Software assurance will review the software plans, processes and procedures and

1. Confirm that approaches have been developed for the use of auto-generated code and that they include the process of validating and accrediting the auto-generation tools. The process for validating these tools should be consistent with the standard being used to validate and accredit any tools for hand-generated code.
2. Monitor the planned use of auto-generated code versus the actual use of it.
3. Confirm that the limits of the allowable scope of use for the auto-generated code have been described
4. Confirm the following items are identified as configuration items and are being kept under configuration management: models and code generators for auto-generated code as well as the inputs to the tools, the outputs of the tools and any modifications to the output of the tools.
5. Confirm that the processes and procedures include those needed for making manual changes to the auto-generated source code.

Tasking for [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) calls for a confirmation that the auto-generated tools have been considered for reusability.

Tasking for [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs) calls for software assurance to confirm that NASA engineering, project, software assurance, and IV&V have electronic access to the auto-generation tools, including the models, simulations, and associated data that is used as inputs for auto-generated code.

In some cases, the generated code is more voluminous and/or harder to understand than a hand-developed code. Hence, there is the need to complement the code review activity by also scrutinizing its inputs (models or specifications) and the code generator tool itself. This is aided by the fact that the input is simultaneously rigorous (i.e., has a formal semantics) yet concise and clear (e.g., in a modeling notation well suited to expressing the software’s requirements). These considerations motivate the requirement to configuration to manage the inputs and outputs of the auto-generation of software ([SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code), part g ) and the requirement to describe the limits and allowable scope of the auto-generated code ([SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code), part c). Auto-generation tools can assist a project in developing a large amount of code in a relatively short period of time, but it is critical to know exactly how to specify the inputs to generate the desired resulting code.

Requirements pertaining to the code itself (e.g., analysis and testing) apply to auto-generated code just as they would for code created by any other means. The testing of auto-generated code is much like the testing of COTS, and it should be tested to the same degree as any hand-developed code.

More information on guidance for these specific tasking requirements can be found in the Guidance section for each of the associated SWE requirements.

In addition to these assurance tasks, software assurance should consider the following section that lists lessons learned associated with the use and assurance of auto-generated code.

## 3.2 Assurance Practices and Considerations obtained from Lessons Learned on NASA Projects

This section presents a series of lessons learned from several NASA flight projects employing auto-generation. These cover many topics that assurance should be aware of.

Areas of decreased concern (and hence potentially in less need of assurance):

* There may be less need for human scrutiny of the auto-generated code as compared to manually crafted code, with attention instead shifted to the inputs to auto-generation. e.g., formal inspections of auto-generated code may no longer be conducted, with reviews instead focused on the models' input to auto-generation.
* Similarly, since the structure and the formatting of the auto-generated code are somewhat dependent on the generator tool, the project may consider relaxing or adjusting the required coding standard. However, the focus may shift to establishing standards for the inputs (model) instead. It is still important to ensure that the generated code is free of coding vulnerabilities (including security-related vulnerabilities), such as buffer overflow, etc., by running the code against static analysis tools. This concern may be less important when a more mature or certified code generator is used.

Areas of new or increased concern (and hence potentially in need of additional assurance):

* The learning curve for engineers not already familiar with the auto-code tooling (e.g., the modeling environment) should not be underestimated.
* Auto-code generation shifts the development effort from coding implementation to generating inputs to a code generator (modeling). While the average effort needed for coding implementation is generally understood (via extensive metrics collection and industry benchmark available), modeling effort is less well understood. This could pose a risk when evaluating the feasibility of the evaluation plan. Greater monitoring and comparison between planned vs actual may be needed.
* With increased emphasis on the inputs to auto-generation, standards on the form of those inputs may need to be developed and applied; such standards should be appropriate to the project and form of auto-generation.
* A common recommendation is that the auto-generated code not be manually edited after generation. Instead, if there is a need to change the code, the recommended practice is to change the model and re-generate the code. However, if manual editing of auto-generated code is performed, it is best to treat that code in the same way as manually created code.
* Reverse engineering (also referred to as “round-trip engineering”), in which manual edits to the auto-generated code are used to automatically update the inputs to auto-generation (thus keeping the inputs and outputs in sync), is sometimes claimed as a capability (e.g., Hinchey at al [653](#_tabs-<p>5</p>)). In general, this is difficult to do, so this capability should be assured if it is to be relied upon.
* Similar to the above concern, establishing traceability between the generated code and the inputs (models) can be useful for debugging and maintenance (especially if auto-generated code is to be manually edited after generation).
* Ideally, auto-generated code not subject to further editing would not be checked into a Configuration Management repository – just the inputs from which to generate the code would be checked in. However, experience has shown that code generation can be time-consuming. Checking in auto-generated code is a means to save on build time – but in such a case be especially careful with its configuration management!
* Configuration management of the graphical models that often serve as input to auto-generation poses some increased challenges, as outlined in section 5.3.2.
* Compatibility between auto-generated code and other forms of code should be considered early, given that the auto-generation process may offer less flexibility in adjusting the form of the code it generates.

## 3.3 Best Practices

Orion Modeling Guideline – designed for modeling using Simulink, the joint Orion NASA/contractor team developed this from the starting point of the Mathworks Automotive Advisory Board (MAAB) guidelines document [648](#_tabs-<p>5</p>).

Below is an illustration of modeling best practices, abstracted from the aforementioned Orion Modeling Guideline.

|  |  |  |
| --- | --- | --- |
| **Desiderata** | | **Guideline** |
| Correctness | Tool compatibility | Be aware of compiler limits when naming model elements that will be turned into variables in the software, e.g., some compilers have 32-character limits for variables, and will truncate longer-than-32 characters which may result in the same variable name for two *different* variables |
| Simplicity | Appropriate language and constructs | Use the appropriate languages and constructs (Stateflow vs Simulink, if-else vs switch) depending on the nature of the behavior being modeled, e.g., do not use construct intended for numerical operation for logical operations. For example: if excessive (more than 10) if-else/switch cases were needed for implementation, consider using Stateflow instead of Simulink |
| Ease of testing | Use an enumeration type instead of an integer type (and constants) to select from a limited series of choices, to reduce the space of testing |
| Traceability | Configuration Management | Maintain a unique identification trace tag within the model with a version number which matches the version in the Configuration Management system, modification date, and author |
| Naming consistency | Maintain naming consistency for related elements, e.g., import and outport blocks in Simulink model should match with the signal or bus names, the name of the one import or outport should be the same throughout its use in the different layers of the model |
| Understandability | Export | Ensure that a printed-out model includes all the necessary information for engineering, assurance and IV&V personnel to review the model. This includes: selecting font style and size for legibility, requiring that the name of important elements (e.g., import and outport blocks) are visible in the printout, using color convention for different element types, documenting the model with rationale, assumption, intent as well as revision version of the model, displaying important parameters with values other than default |
| Naming rules and patterns | Specify naming rules/patterns, allowable characters, and uniqueness constraints (e.g., unique block name in one model) for each element types of the model (e.g., input and output, signal, block, layer, etc.). |
| Structure and organization | For a modeling language that allows groupings/factoring (e.g., through sub-systems), encourage the use of groupings to reduce replication or to simplify too complex of a layer. However, ensure that elements are grouped according to the functional decomposition of the algorithm |
| Units | Be specific to what computation units are used in the model's elements |

## 3.4 Assurance Considerations for Small Projects

Small projects may not need to be as concerned with elaborate configuration management practices of the input models to auto-generation, especially if they are conducted by a small, cohesive co-located team. If projects are short-term in nature, they may be relatively invulnerable to revisions of third-party auto-generation tools, able to stick with the same version for the duration of the effort. An informal approach to determining and promulgating best practices among the development team may suffice (as compared to developing rigorous standards). The models themselves may be relatively simple (e.g., have fewer instruments and less redundancy to control).

## 3.5 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 4. Lessons Learned for Consideration

There are many other lessons learned from NASA projects which software assurance personnel should be aware of and make use of when performing software assurance on projects that are making use of auto-generated code.

## 4.1 Auto-generation to achieve productivity and reviewability

JPL’s 1997-1998 auto-generation of fault protection code for the DS1 spacecraft, described in Rouquette et al [650](#_tabs-<p>5</p>), is the source for the following lessons learned, with italics denoting quotations extracted from there.

* **The clear motivation for use of auto-generation**. Schedule pressure (short timeframe and “*too few software engineers available*”) would have made conventional software development “*challenging*.” Code generation was chosen in part because it “*allowed us to make an important separation of concerns between what system-level FP [Fault Protection] should do (design) and how it should do it (implementation)*.”It was not just the productivity gain from avoiding a manual coding step (a benefit widely claimed for auto-generation). It also made the functionality being implemented more reviewable by virtue of the form of the input to auto-generation: “*We needed a design notation sufficiently clear to allow several people to follow an analysis discourse and sufficiently compact to facilitate such reviews”.* And later“*…reviewable functionality was the most important criteria to enable the kind of high-level peer design reviews necessary to meet our schedule.*”
* **Feasibility of the approach**. One set of concerns was whether the auto-generation approach they had in mind (using an existing commercial code-generation tool) would be feasible. Included in this were questions of whether the input format would be adequate to represent the richness of behaviors, whether the generator could be trusted to implement the desired logic, and whether much of the team’s time would be spent debugging the code generator. Their solution was to “*rapidly prototype the most complex behavior required … and exhaustively test its generated software.*”
* **Code generation issues / Avoidance of post-generation manual editing**. The generated code must be compatible with the project, both with the project’s processes and with other code in the project. In the case of incompatibility, the code generator must be sufficiently customizable and/or the project must adapt. The DS1 fault protection effort “… *chose a code-generation approach that espoused a zero customization policy towards the generated software.*” As they put it, “*Custom code becomes one more source of information that needed to be managed.*” The customization they needed was attained by using the “template” capability provided by the commercial code generator they employed, and they also modified the (commercial) code generator itself(!).

## 4.2 Development of an in-house auto-coder

The success of DS1’s auto-generation of fault protection code led to its use in a similar effort, to develop the fault protection code for the Deep Impact (DI) mission. However, by the time of DI the commercial auto-coder had been updated (involving a changed file format), and DI had different requirements for auto-coder output (e.g., required C++ instead of C code). To address this, the DI team wrote a new postprocessor to convert the auto-generated code into the flight C++ code. Following the DS1 and DI experiences, JPL decided to develop an in-house auto-coder. While this had not been practical for the schedule-challenged DS1 mission, time and resources later permitted its consideration.

* The rationale for developing an in-house auto-coder. As stated in Wagstaff et al [651](#_tabs-<p>5</p>), these were to provide:
  + “*a non-proprietary file format in which the state charts [the input to the code generation] are stored*”,
  + “*precise control over which programming constructs are used, to ensure adherence with flight software requirements*”, and
  + “*the ability to plug in different front-end state chart drawing tools and different back-end output modules*”. The “back-end output modules” were to allow not only code (either C or C++) to be generated, but also, from the same inputs, simulator output for execution in simulation via an interactive interface, and Promela output for feeding into the model-checker SPIN.
* Benefits to quality assurance. The following beneficial influences on quality assurance are reported in Wagstaff et al[651](#_tabs-<p>5</p>):
  + “*Code reviews can be made more efficient when an accompanying state chart is available, especially one that can be examined dynamically (in simulation). In addition, after thorough review and validation of the automatic code generation tool, review efforts for an individual project can be focused on the designs (state charts) rather than the implementation*.” and along these lines:
  + “*During a Preliminary Design Review … [the] simulator was used to catch, and later resolve, divergent design interpretations by designers and implementers*”
* V&V of the auto-coder itself. The JPL developed auto-coder software is classified as NASA Class B (mission-critical) code. It seems that few commercial auto-coders have been rigorously qualified, a rare but notable exception being the SCADE Suite ® described as “qualified as a development tool for DO-178B software up to Level A, etc. (see ansys.com - products/embedded-software/ansys-scade-suite [383](#_tabs-<p>5</p>)  for the full list of such).

Model-checking using auto-generated output specifically for this purpose is alluring as a means to validate a model against correctness properties (expressed as assertions to the model checker). This seems to have been successful as the means to guarantee some straightforward properties (e.g., to show all states in the state chart are reachable), but not necessarily all the properties one might wish to check, due to scalability issues of model-checking. The interested reader is referred to Oh et al, 2008 [658](#_tabs-<p>5</p>) and Gibson et al, 2014 [646](#_tabs-<p>5</p>) for discussions covering two different model checkers used in the manner.

JPL also did in-house development of an auto-coder to generate common tasking, messaging and interconnection logic Watney et al, 2014 [661](#_tabs-<p>5</p>). This auto-coder supported a component-based architecture, the pros, and cons of which, while interesting, would be a separate topic. From an auto-coding perspective, the following quotations reinforce some of the lessons learned above:

* “*Modeling enables the software engineer to focus on the architectural constructs as opposed to the implementation details. Potential problems with the architectural connection of the components can be detected early via the use of modeling before the detailed implementation begins*.”
* “… *demonstrated by making a number of changes [to the inputs leading to regeneration of the auto-generated code] that did not result in any change to the manual component code*.”
* “*Code generation … generate[s] common tasking, messaging and interconnection logic that is defect-free.*”

## 4.3 Large-scale auto-generated code

Two projects that employed auto-generated code in their large-scale software development efforts serve as sources of lessons learned in this subsection: MSL (section 4.3.1) and Orion’s GN&C code (section 4.3.2).

### 4.3.1 MSL

Table 1. MSL’s eight in-house auto-coders [645](#_tabs-<p>5</p>)

| Category | MSL Autocoder | Comments |
| --- | --- | --- |
| State Machine Generators |  | * Utilizes a MagicDraw graphical input, with legacy. * Uses a textual input and legacy from the technology project. The output is C. |
| Parameters, cmd/tlm, etc |  | * Each autocoder performs or supports one of the following five functions: Parameter handling, Commanding, Telemetry, Event Reporting, Data Product Generation * These autocoders utilize actual xml or xml-like inputs. * Outputs are c-code, xml files, some csv files are used for FSW code, and/or Ground interfacing databases, and/or inputs to other autocoders. |
| Instrument Interface |  | Uniquely, code from this autocoder can be hand modified. This code is treated as a hand code. The output is C code. |

MSL, including the Curiosity rover, landed on Mars, made substantial use of auto-generated code. JPL’s State of Software Report 2014 states that of the launch load’s 2.8 million SLOC, 2.2 million (78%) were auto-generated. Different auto- coders were used for different purposes, summarized in Table 1.

IV&V’s analysis of MSL code [645](#_tabs-<p>5</p>) , with comments:

#### For syntactic analysis of the code:

* “*All the warnings associated with auto-coded files were found to be false positives” and “Auto-generated code had predictable warning patterns*”
* “*Auto-generators are consistent in ways that a human is not. An auto-generator would repeat a mistake with similar input (facilitates identifying defects in the generated code, and possibly the generator itself)*”
* “*Auto-generated code contained far fewer errors than hand-generated code*”

**For semantic analysis of the code**:

* “*Auto-generated code: readability standards are not necessarily enforced and code reviews are not typically used. Code generator outputs can be complex and/or cryptic*”
* *“Autocode generator inputs (incorrect spec development) or a generator can introduce semantic errors*”

describes the auto-coding on MSL and its continuation on SMAP [644](#_tabs-<p>5</p>), reporting:

#### As a means to achieve consistency between the flight code and ground code:

“*Auto-code flight/ground interfaces when*

* *The generated code is well defined, repetitive*
* *There is a need to synchronize definitions between flight and ground”*
* **Whether to always regenerate or to sometimes check in, auto-generated code**: From the MSL experience *“Running auto-code tools for every checkout increased build times dramatically” which led to a change of practice in SMAP: “Auto-generated code checked in (not regenerated) saved on build time.”*

### 4.3.2 Orion GN&C

The Orion Guidance Navigation and Control (GN&C) team are developing GN&C algorithms for the Orion Spacecraft, NASA’s vehicle for manned exploration outside of low Earth orbit. The initial use will be on the Exploration Flight Test One (EFT-1) vehicle. Aspects of this project described as pertinent to its use of Model-Based Design, of which auto-generated code plays a key role, are the GN&C application’s size and complexity (the final GN&C application is predicted to produce well over 100,000 lines of auto code), its development by a large, geographically dispersed team, and legacy tools (notably for simulation). The effort is described extensively in Tamblyn et al, 2010 [659](#_tabs-<p>5</p>), Jackson&Henry, 2012 [654](#_tabs-<p>5</p>), and Odegard et al, 2014 [657](#_tabs-<p>5</p>), from which the following quotations are taken.

* **The clear motivation for use of auto-generation** (the same lesson as listed in 5.1). Reliance on efficiency gains from auto-coding was a factor: “*The prime contractor’s FSW [Flight Software] team was staffed under the assumption that auto-code would be used to generate the GN&C algorithms – so there were insufficient resources to allow manual coding of algorithms from detailed written requirements.*” In addition, the benefit of bridging the system/software gap is reported: “*The first and foremost benefit is that the GN&C designers are directly involved in the flight implementation of the algorithms. This eliminates the traditional “translation” phase of having FSW engineers interpret a written FSSR from which to build the code, thus eliminating a potential source of error.*”
* **Longevity**. The project selected the MathWorks toolset, describing it as “*fast-becoming an industry standard. … Matlab programming has become the latest “language” being instituted rather than C or FORTRAN. This bodes well for a project like Orion that is expected to have a 30-year life span*.”  
    
  To insulate themselves from changes to the auto-generator, the project at one time was “*frozen on the R2008b version of the product*” yet anticipated managing upgrades: “*More recent versions of the tool have some vast improvements with respect to the efficiency of the auto-generated code and team-wide upgrades will be considered at coordinate project schedule milestones*.”
* **Configuration Management**. The switch from textual representations of code to the graphical form of models has implications for configuration management in multi-developer settings. “*Early versions … included all functionality in a single model file … This was not practical for a large project, since all developers operated on a single configuration managed object, even though they may have been making changes to separate subsystems within the model*.” The project found ways to use modeling capabilities (some of which evolved over time) to allow the development and editing of separately managed objects.  
    
  When multiple developers are making changes to the same model file, merging their changes is needed. The project reports that at the time “*Text merge tools are highly effective for hand-coded applications, but graphical merge tools are more expensive and less effective than their text counterparts*.”
* **Code and model metrics**. The project found it necessary to modify the traditional cyclomatic complexity (CC) metric for application to auto-generated code. This was because “… *automatically generated code often had higher CC than hand-coding*” due to the use of static loops in the auto-code, which increased the CC count yet did not add to the complexity of the code. The project also made use of a “Model Complexity” metric, which could be calculated on the models to be input to auto-generation without actually generating the code and analyzing its CC. The project found that their “*[modified] CC for auto-coded functions closely matched the source model complexity.*”

For purposes of estimating progress, “… the *model size is a better metric than lines of code. The SLOC count of the auto-code was not consistently proportional to the size of the Model…*” and the project developed a “Model Size” metric instead.

* **Modeling standards**. The project developed standards on the MATLAB and Simulink models themselves. Their purpose was to “…*enhance the consistency, readability, efficiency, and compatibility of the many models that were being developed amongst a large group of developers.*” Analogous to the automated checking of coding standards, the project developed automated checks of the model standards.  
  + The standards are described on the MathWorks site [649](#_tabs-<p>5</p>), which links to the standards document [648](#_tabs-<p>5</p>)
  + The project also developed a checklist to give developers “a better picture of the maturity of the models and helped increase the quality of the models that were being reviewed.”
* **Reviewability**. The project considered the challenges of reviewing the models input to auto-generation, espousing the position that “*A reviewer should ideally be able to review a model and understand all of the details of the algorithm being modeled without having to click inside a block and review the block settings or have prior knowledge of a block’s functionality.*” The project stance was that “models … should be as readable, descriptive and transparent as possible.” Some of the modeling standards were crafted to support readability, e.g., “*color-coded to distinguish between block types and enhance readability.*”  
    
  Although the project did not require formal inspections of the auto-generated code, auto-generation settings that would lead to its readability were encouraged: “*it is … very useful to maintain traceability for debugging purposes, so readability is still important*”.
* **Matching language(s) to use**. The project recognized that “*Not all algorithms benefit from graphical dataflow implementation*” and made successful use of a mix of languages. Table 1 “Standards for Use of Simulink Language Tools” in Jackson & Henry, 2012 [654](#_tabs-<p>5</p>) was “*created to help aid developers to use the most suitable tool for the algorithm being modeled.*”

### 4.3.3 ESA’s “AUTOCOGEQ”

The European Space Agency (ESA) presentation “AUTOCOGEQ: End-to-end process for the production of automatically generated mission-critical software” [662](#_tabs-<p>5</p>) included the following Lessons learned (see the presentation for the accompanying description):

* Flight software developed using model-based design and auto-coding techniques shall consider a well-defined **methodology** for the **complete lifecycle**.
* **Re-use** of models not implemented for generating flight code leads to a **big adaptation effort**: starting the SW development from scratch might be the best solution.
* **Tailoring** of the code generation settings, modeling rules and coding standards (e.g. MISRA-C) is needed according to the project’s needs.
* **Tools** and automatic generation **cannot guarantee** the **qualification** of generated code as category B: tools support and complement the ECSS processes.
* Still, **additional manual activities** have to be performed to cover the complete ECSS processes for flight code qualification.
* **Wizard** allows a quick check of the rules and let the SW development process to be more flexible and recursive during all phases.

## 4.4 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-5) in the Resources tab.

# 5. Resources

## 5.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-083)

  [NPR 7150.2 NASA Software Engineering Requirements,](https://swehb.nasa.gov/download/attachments/16450224/N_PR_7150_002D_.pdf?api=v2 "Click to open in new window")

  NPR 7150.2D, Effective Date: March 08, 2022, Expiration Date: March 08, 2027
    https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7150&s=2D Contains link to full text copy in PDF format. Search for "SWEREF-083" for links to old NPR7150.2 copies.
* (SWEREF-272)

  [NASA Standard for Models and Simulations,](https://standards.nasa.gov/standard/nasa/nasa-std-7009 "Click to open in new window")

  NASA-STD-7009A w/ CHANGE 1: ADMINISTRATIVE/ EDITORIAL CHANGES 2016-12-07
* (SWEREF-278)

  [SOFTWARE ASSURANCE AND SOFTWARE SAFETY STANDARD](https://standards.nasa.gov/sites/default/files/standards/NASA/B/0/NASA-STD-87398-Revision-B.pdf "Click to open in new window")

  NASA-STD-8739.8B, NASA TECHNICAL STANDARD, Approved 2022-09-08
  Superseding "NASA-STD-8739.8A"
* (SWEREF-383)

  [Ansys SCADE Suite
  Model-Based Development Environment for Critical Embedded Software,](https://www.ansys.com/products/embedded-software/ansys-scade-suite "Click to open in new window")

  Model-based development environment for reliable embedded software, which provides linkage to requirements management, model-based design, verification, qualifiable/certified code generation capabilities and interoperability with other development tools and platforms.
* (SWEREF-644)

  [Autocoding and Dictionaries on SMAP and MSL.](https://trs.jpl.nasa.gov/bitstream/handle/2014/45507/14-5320_A1b.pdf "Click to open in new window")

  Benowitz, Ed, and Chris Swan. 2014
* (SWEREF-645)

  [MSL Code Analysis,](https://www.nasa.gov/sites/default/files/482444main_1000_-_IVV_Workshop_CodeChallenges.pdf "Click to open in new window")

  Cox, Jake; 2010 IV&V Annual Workshop, September 2010,
* (SWEREF-646)

  [Formal Validation of Fault Management Design Solutions](https://trs.jpl.nasa.gov/bitstream/handle/2014/44368/13-4262_A1b.pdf "Click to open in new window")

  Gibson, C., Karban, R., Andolfato, L., and Day, J., 2014 ACM SIGSOFT Software Engineering Notes, 39(1), 1-5, 2014,
* (SWEREF-647)

  [Report: Survey on Model-Based Software Engineering and Auto-Generated Code](https://ti.arc.nasa.gov/publications/36691/download "Click to open in new window")

  Goseva-Popstojanova, K., Kahsai, T., Kyanko, T., Nkwocha, N., Knudson, M., and Schumann, J., September 2016. NASA report, TM-2016-219443,
* (SWEREF-648)

  [Orion GN&C MATLAB/Simulink Standards](https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/solutions/aerospace-defense/standards/FltDyn-CEV-08-148_MATLAB_Standards_v9_20111202.pdf "Click to open in new window")

   Henry, J., 2011. Document Number: FlyDyb-CEV-8-148, 2011.
* (SWEREF-649)

  [NASA - Orion GN&C: MATLAB and Simulink Standards](https://www.mathworks.com/solutions/aerospace-defense/standards/nasa.html "Click to open in new window")

  The Orion Guidance, Navigation, and Control MATLAB and Simulink Standards document describes the modeling standards and guidelines that the Orion Crew Exploration Vehicle (CEV) Flight Dynamics Team (FDT) are using while developing and coding the GN&C algorithms using Simulink, Stateflow, MATLAB language for code generation, and Embedded Coder.
* (SWEREF-650)

  [The 13th Technology of Deep Space One](https://trs.jpl.nasa.gov/bitstream/handle/2014/16684/99-0078.pdf?sequence=1 "Click to open in new window")

   Rouquette, N.F., Neilson, T., and Chen, G., 1999. Proceedings of the 1999 IEEE Aerospace Conference,Vol 1, March 1999, pp. 477-487.
* (SWEREF-651)

  [AUTOMATIC CODE GENERATION FOR INSTRUMENT FLIGHT SOFTWARE](https://trs.jpl.nasa.gov/bitstream/handle/2014/41374/07-4374.pdf "Click to open in new window")

  Wagstaff, K. L., Benowitz, E., Byrne, D. J., Peters, K., and Watney, G., 2008. Jet Propulsion Laboratory, California Institute of Technology
* (SWEREF-652)

  [A Guide to Code Generation (blog)](https://tomassetti.me/code-generation/ "Click to open in new window")

  Tomassetti, G., (blog), May 9, 2018.
* (SWEREF-653)

  [Requirements to Design to Code: Towards a Fully Formal Approach to Automatic Code Generation](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20050136631.pdf "Click to open in new window")

  Hinchey, M.G., Rash, J., and Rouff, C.A., 2005. NASA-TM-2005-212774.
* (SWEREF-654)

  [ORION GN&C MODEL BASED DEVELOPMENT: EXPERIENCE AND LESSONS LEARNED](https://arc.aiaa.org/doi/abs/10.2514/6.2012-5036 "Click to open in new window")

   Jackson, M. C., & Henry, J. R., AIAA Guidance, Navigation and Control Conference, 2012. Also available from the NASA Technical Reports Server, Document ID: 20120013073.
* (SWEREF-655)

  [Model-Driven Engineering: Automatic Code Generation and Beyond](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=435414 "Click to open in new window")

  Klein, J., Levinson, H., and Marchetti, J., Technical Report CMU/SEI-2015-TN-005, March 2015.
* (SWEREF-656)

  [Model-based engineering in the embedded systems domain: an industrial survey on the state-of-practice](https://link.springer.com/article/10.1007%2Fs10270-016-0523-3 "Click to open in new window")

  Liebel, G., Marko, N., Tichy, M., Leitner, A., and Hansson, J., 2016, Software & Systems Modeling, 1-23, 2016.
* (SWEREF-657)

  [Model-Based GN&C Simulation and Flight Software Development for Orion Missions beyond LEO](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20140003581.pdf "Click to open in new window")

  Odegard, R., Milenkovic, Z., Henry, J., & Buttacoli, M., IEEE Aerospace Conference, (pp. 1-13). IEEE, 2014. Available from the NASA Technical Reports Server, Document ID: 20140003581.
* (SWEREF-658)

  [Software Assurance for Model-Based Design](https://ieeexplore.ieee.org/document/4526596 "Click to open in new window")

  Oh, J. M., Watney, G. J., and Benowitz, E. G., IEEE Aerospace Conference, (pp. 1-6), IEEE, 2008.
* (SWEREF-659)

  [A model-based design and testing approach for Orion GN&C flight software development](https://ieeexplore.ieee.org/document/5446802 "Click to open in new window")

  Tamblyn, S., Henry, J., & King, E., IEEE Aerospace Conference, (pp. 1-12). IEEE, 2010.
* (SWEREF-660)

  [Relevance, benefits, and problems of software modelling and model driven techniques - A survey in the Italian industry](https://www.semanticscholar.org/paper/Relevance%2C-benefits%2C-and-problems-of-software-and-A-Torchiano-Tomassetti/0f7093cafff42ae29d81dd131b4942743b09f7a4 "Click to open in new window")

  Torchiano, M., Tomassetti, F., Ricca, F., Tiso, A., and Reggio, G., Journal of Systems and Software, 86(8), pp. 2110-2126, 2013.
* (SWEREF-661)

  [Modeling for Partitioned and Multi-core Flight Software Systems:(Instrument Software Framework)](https://ieeexplore.ieee.org/document/6979145 "Click to open in new window")

  Watney, G., Reder, L. J., and Canham, T., IEEE International Conference on Space Mission Challenges for Information Technology (SMC-IT), pp. 54-61, 2014. An abbreviated description of this work is found in NASA Tech Brief NPO-49403.
* (SWEREF-662)

  [AUTOCOGEQ: End-to-end process for the production of automatically generated mission critical software](https://nsc.nasa.gov/docs/default-source/event-docs/trismac-2018/trismac-presentations/casas_autocogeq.pdf "Click to open in new window")

  Casas, M.F., Trilateral SMA Conference (TRISMAC), June 2018. Requires special access into NSC resources.

## 5.2 Tools

Tools to aid in compliance with this SWE, if any, may be found in the Tools Library in the NASA Engineering Network (NEN). 

NASA users find this in the [Tools Library](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Tool+Library) in the Software Processes Across NASA (SPAN) site of the Software Engineering Community in NEN.

The list is informational only and does not represent an “approved tool list”, nor does it represent an endorsement of any particular tool.  The purpose is to provide examples of tools being used across the Agency and to help projects and centers decide what tools to consider.

## 5.3 Auto-Generated Code Specific Tools

As mentioned earlier, a good starting point for considerations when choosing auto-coding is Klein et al, 2015 [655](#_tabs-<p>5</p>)

The following two tools and documentation are available for download from the Software Assurance Research Program sub-community on the NASA Engineering Network. These tools are available only to NASA Civil Servants and Contractors.

**Model-Based Software Development (MBSD) Checklist Tool** – A dynamic checklist of context-driven software assurance concerns and practices:

1. [Documentation](https://nen.nasa.gov/documents/909012/2289724/MBSD+Checklist+Tool+v2-c+Documentation.docx/e4e5462e-0969-075f-eff5-1f81e8134040?version=1.0&download=true)
2. [Checklist tool](https://nen.nasa.gov/documents/909012/2289724/MBSD+Checklist+v2-c.xlsm/71007331-1002-6ad3-e86c-efb228b81a91?version=1.0&download=true) (Excel .xlsm file, including macros)

**Complexity Metrics for Simulink Models** – A script to calculate several metrics of Simulink models

1. [Documentation](https://nen.nasa.gov/documents/909012/2289724/Complexity+Metrics+for+Simulink+Models.docx/7c31c27a-898e-6de9-9fca-aafed37179f2?version=1.0&download=true)
2. [Script (.zip file)](https://nen.nasa.gov/documents/909012/2289724/Model+Complexity+Script.zip/3a13a416-8126-e16f-02c3-f8547ceb66a3?version=1.2&download=true)

## 5.4 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
| * [SWE-060 - Coding Software](/spaces/SWEHBVD/pages/102695444/SWE-060+-+Coding+Software) * [SWE-070 - Models, Simulations, Tools](/spaces/SWEHBVD/pages/102695452/SWE-070+-+Models+Simulations+Tools) * [SWE-081 - Identify Software CM Items](/spaces/SWEHBVD/pages/102695461/SWE-081+-+Identify+Software+CM+Items) * [SWE-146 - Auto-generated Source Code](/spaces/SWEHBVD/pages/102695503/SWE-146+-+Auto-generated+Source+Code) * [SWE-147 - Specify Reusability Requirements](/spaces/SWEHBVD/pages/102695504/SWE-147+-+Specify+Reusability+Requirements) * [SWE-206 - Auto-Generation Software Inputs](/spaces/SWEHBVD/pages/102695540/SWE-206+-+Auto-Generation+Software+Inputs)        * [7.15 - Relationship Between NPR 7150.2 and NASA-STD-7009](/spaces/SWEHBVD/pages/102695649/7.15+-+Relationship+Between+NPR+7150.2+and+NASA-STD-7009) * [8.57 - Testing Analysis](/spaces/SWEHBVD/pages/102695752/8.57+-+Testing+Analysis) |

## 5.5 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>5</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Code and Integration](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Code+and+Integration) |

## 5.6 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.05 Software Implementation](/spaces/SWEHBVD/pages/133235381/A.05+Software+Implementation) |
