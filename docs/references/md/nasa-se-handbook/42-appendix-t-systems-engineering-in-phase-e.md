# Appendix T: Systems Engineering in Phase E

> NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2. Printed pages 254–259. Machine conversion from PDF; tables and figures may be flattened. Cite as `SE HB §T`.

Systems Engineering in Phase E T.1 Overview In general, normal Phase E activities reflect a reduced emphasis on system design processes but a continued focus on product realization and technical management. Product realization process execution in Phase E takes the form of continued mission plan generation (and update), response to changing flight conditions (and occurrence of in-flight anomalies), and update of mission operations techniques, procedures, and guidelines based on operational experience gained. Technical management processes ensure that appropriate rigor and risk management practices are applied in the execution of the product realization processes.

- Unforgiving schedule: Unlike pre-flight test
activities, it may be difficult or even impossible to pause mission execution to deal with technical issues of a spacecraft in operation. It is typically difficult or impossible to truly pause mission execution after launch. These factors must be addressed when considering activities that introduce change and risk during Phase E.

NOTE: When significant hardware or software changes are required in Phase E, the logical decomposition process may more closely resemble that

Successful Phase E execution requires the prior establishment of mission operations capabilities in four (4) distinct categories: tools, processes, products, and trained personnel. These capabilities may be developed as separate entities, but need to be fused together in Phase E to form an end-to-end operational capability. Although systems engineering activities and processes are constrained throughout the entire project life cycle, additional pressures exist in Phase E:
- Increased resource constraints: Even when
additional funding or staffing can be secured, building new capabilities or training new personnel may require more time or effort than is available. Project budget and staffing profiles generally decrease at or before entry into Phase E, and the remaining personnel are typically focused on mission execution.

exercised in earlier project phases. In such cases, it may be more appropriate to identify the modification as a new project executing in parallel—and coordinated with—the operating project.

T.2 Transition from Development to Operations An effective transition from development to operations phases requires prior planning and coordination among stakeholders. This planning should focus not only on the effective transition of hardware and software systems into service but also on the effective transfer of knowledge, skills, experience, and processes into roles that support the needs of flight operations. Development phase activities need to clearly and concisely document system knowledge in the form

of operational techniques, characteristics, limits, and constraints—these are key inputs used by flight operations personnel in building operations tools and techniques. Phase D Integration and Test (I&T) activities share many common needs with Phase E operations activities. Without prior planning and agreement, however, similar products used in these two phases may be formatted so differently that one set cannot be used for both purposes. The associated product duplication is often unexpected and results in increased cost and schedule risk. Instead, system engineers should identify opportunities for product reuse early in the development process and establish common standards, formats, and content expectations to enable transition and reuse. Similarly, the transfer of skills and experience should be managed through careful planning and placement of key personnel. In some cases, key design, integration, and test personnel may be transitioned into the mission operations team roles. In other cases, dedicated mission operations personnel may be assigned to shadow or assist other teams during Phase A–D activities. In both cases, assignees bring knowledge, skills, and experience into the flight operations environment. Management of this transition process can, however, be complex as these personnel may be considered key to both ongoing I&T and preparation for upcoming operations. Careful and early planning of personnel assignments and transitions is key to success in transferring skills and experience.

T.3 System Engineering Processes in Phase E T.3.1 System Design Processes In general, system design processes are complete well before the start of Phase E. However, events during operations may require that these processes be revisited in Phase E.

T.3.1.1 Stakeholder Expectations Definition

Stakeholder expectations should have been identified during development phase activities, including the definition of operations concepts and design reference missions. Central to this definition is a consensus on mission success criteria and the priority of all intended operations. The mission operations plan should state and address these stakeholder expectations with regard to risk management practices, planning flexibility and frequency of opportunities to update the plan, time to respond and time/scope of status communication, and other key parameters of mission execution. Additional detail in the form of operational guidelines and constraints should be incorporated in mission operations procedures and flight rules. The Operations Readiness Review (ORR) should confirm that stakeholders accept the mission operations plan and operations implementation products. However, it is possible for events in Phase E to require a reassessment of stakeholder expectations. Significant in-flight anomalies or scientific discoveries during flight operations may change the nature and goals of a mission. Mission systems engineers, mission operations managers, and program management need to remain engaged with stakeholders throughout Phase E to identify potential changes in expectations and to manage the acceptance or rejection of such changes during operations. T.3.1.2 Technical Requirements Definition

New technical requirements and changes to existing requirements may be identified during operations as a result of:
- New understanding of system characteristics
through flight experience;
- The occurrence of in-flight anomalies; or

- Changing mission goals or parameters (such as
mission extension). These changes or additions are generally handled as change requests to an operations baseline already under configuration management and possibly in use as part of ongoing flight operations. Such changes are more commonly directed to the ground segment or operations products (operational constraints, procedures, etc.). Flight software changes may also be considered, but flight hardware changes for anything other than human-tended spacecraft are rarely possible. Technical requirement change review can be more challenging in Phase E as fewer resources are available to perform comprehensive review. Early and close involvement of Safety and Mission Assurance (SMA) representatives can be key in ensuring that proposed changes are appropriate and within the project’s allowable risk tolerance.

Scarcity of time and resources during Phase E can make implementation of these design solutions challenging. The design solution needs to take into account the availability of and constraints to resources. T.3.1.5 Product Implementation

Personnel who implement mission operations products such as procedures and spacecraft command scripts should be trained and certified to the appropriate level of skill as defined by the project. Processes governing the update and creation of operations products should be in place and exercised prior to Phase E.

T.3.2 Product Realization Processes Product realization processes in Phase E are typically executed by Configuration Management (CM) and test personnel. It is common for these people to be “shared resources;” i.e., personnel who fulfil other roles in addition to CM and test roles.

T.3.1.3 Logical Decomposition

T.3.2.1 Product Integration

In general, logical decomposition of mission operations functions is performed during development phases. Additional logical decomposition during operations is more often applied to the operations products: procedures, user interfaces, and operational constraints. The authors and users of these products are often the most qualified people to judge the appropriate decomposition of new or changed functionality as a series of procedures or similar products.

Product integration in Phase E generally involves bringing together multiple operations products—some preexisting and others new or modified—into a proposed update to the baseline mission operations capability.

T.3.1.4 Design Solution Definition

Similar to logical decomposition, design solution definition tasks may be better addressed by those who develop and use the products. Minor modifications may be handled entirely within an operations team (with internal reviews), while larger changes or additions may warrant the involvement of program-level system engineers and Safety and Mission Assurance (SMA) personnel.

The degree to which a set of products is integrated may vary based on the size and complexity of the project. Small projects may define a baseline—and update to that baseline—that spans the entire set of all operations products. Larger or more complex projects may choose to create logical baseline subsets divided along practical boundaries. In a geographically disperse set of separate mission operations Centers, for example, each Center may be initially integrated as a separate product. Similarly, the different functions within a single large control Center—planning, flight dynamics, command and control, etc.—may be established as separately baselined products. Ultimately, however,

some method needs to be established to ensure that the product realization processes identify and assess all potential impacts of system changes.

procedures may not be impacted by environmental conditions at all. T.3.2.3 Product Validation

T.3.2.2 Product Verification

Product verification in Phase E generally takes the form of unit tests of tools, data sets, procedures, and other items under simulated conditions. Such “thread tests” may exercise single specific tasks or functions. The fidelity of simulation required for verification varies with the nature and criticality of the product. Key characteristics to consider include:
- Runtime: Verification of products during flight
operations may be significantly time constrained. Greater simulation fidelity can result in slower simulation performance. This slower performance may be acceptable for some verification activities but may be too constraining for others.
- Level of detail: Testing of simple plans and procedures may not require high-fidelity simulation
of a system’s dynamics. For example, simple state change processes may be tested on relatively low-fidelity simulations. However, operational activities that involve dynamic system attributes – such as changes in pressure, temperature, or other physical properties may require testing with much higher-fidelity simulations.
- Level of integration: Some operations may impact
only a single subsystem, while others can affect multiple systems or even the entire spacecraft.
- Environmental effects: Some operations products
and procedures may be highly sensitive to environmental conditions, while others may not. For example, event sequences for atmospheric entry and deceleration may require accurate weather data. In contrast, simple system reconfiguration

Product validation is generally executed through the use of products in integrated operational scenarios such as mission simulations, operational readiness tests, and/or spacecraft end-to-end tests. In these environments, a collection of products is used by a team of operators to simulate an operational activity or set of activities such as launch, activation, rendezvous, science operations, or Entry, Descent, and Landing (EDL). The integration of multiple team members and operations products provides the context necessary to determine if the product is appropriate and meets the true operations need. T.3.2.4 Product Transition

Transition of new operational capabilities in Phase E is generally overseen by the mission operations manager or a Configuration Control Board (CCB) chaired by the mission operations manager or the project manager. Proper transition management includes the inspection of product test (verification and validation) results as well as the readiness of the currently operating operations system to accept changes. Transition during Phase E can be particularly challenging as the personnel using these capabilities also need to change techniques, daily practices, or other behaviors as a result. Careful attention should be paid to planned operations, such as spacecraft maneuvers or other mission critical events and risks associated with performing product transition at times near such events.

T.3.3 Technical Management Processes Technical management processes are generally a shared responsibility of the project manager and

the mission operations manager. Clear agreement between these two parties is essential in ensuring that Phase E efforts are managed effectively. T.3.3.1 Technical Planning

Technical planning in Phase E generally focuses on the management of scarce product development resources during mission execution. Key decision-makers, including the mission operations manager and lower operations team leads, need to review the benefits of a change against the resource cost to implement changes. Many resources are shared in Phase E – for example, product developers may also serve other real-time operations roles– and the additional workload placed on these resources should be viewed as a risk to be mitigated during operations. T.3.3.2 Requirements Management

Requirements management during Phase E is similar in nature to pre-Phase E efforts. Although some streamlining may be implemented to reduce process overhead in Phase E, the core need to review and validate requirements remains. As most Phase E changes are derived from a clearly demonstrated need, program management may reduce or waive the need for complete requirements traceability analysis and documentation. T.3.3.3 Interface Management

It is relatively uncommon for interfaces to change in Phase E, but this can occur when a software tool is modified or a new need is uncovered. Interface definitions should be managed in a manner similar to that used in other project phases. T.3.3.4 Technical Risk Management

Managing technical risks during operations can be more challenging during Phase E than during other phases. New risks discovered during operations may

be the result of system failures or changes in the surrounding environment. Where additional time may be available to assess and mitigate risk in other project phases, the nature of flight operations may limit the time over which risk management can be executed. For this reason, every project should develop a formal process for handling anomalies and managing risk during operations. This process should be exercised before flight, and decision-makers should be well versed in the process details. T.3.3.5 Configuration Management

Effective and efficient Configuration Management (CM) is essential during operations. Critical operations materials, including procedures, plans, flight datasets, and technical reference material need to be secure, up to date, and easily accessed by those who make and enact mission critical decisions. CM systems—in their intended flight configuration— should be exercised as part of operational readiness tests to ensure that the systems, processes, and participants are flight-ready. Access to such operations products is generally time-critical, and CM systems supporting that access should be managed accordingly. Scheduled maintenance or other “downtime” periods should be coordinated with flight operations plans to minimize the risk of data being inaccessible during critical activities. T.3.3.6 Technical Data Management

Tools, procedures, and other infrastructure for Technical Data Management must be baselined, implemented, and verified prior to flight operations. Changes to these capabilities are rarely made during Phase E due to the high risk of data loss or reduction in operations efficiency when changing during operations.

Mandatory Technical Data Management infrastructure changes, when they occur, should be carefully reviewed by those who interact with the data on a regular basis. This includes not only operations personnel, but also engineering and science customers of that data. T.3.3.7 Technical Assessment

Formal technical assessments during Phase E are typically focused on the upcoming execution of a specific operational activity such as launch, orbit entry, or decommissioning. Reviews executed while flight operations are in progress should be scoped to answer critical questions while not overburdening the project or operations team.

phases. Phase E TPMs may focus on the accomplishment of mission events, the performance of the system in operation, and the ability of the operations team to support upcoming events. T.3.3.8 Decision Analysis

The Phase E Decision Analysis Process is similar to that in other project phases but may emphasize different criteria. For example, the ability to change a schedule may be limited by the absolute timing of events such as an orbit entry or landing on a planetary surface. Cost trades may be more constrained by the inability to add trained personnel to support an activity. Technical trades may be limited by the inability to modify hardware in operation.

Technical Performance Measures (TPMs) in Phase E may differ significantly from those in other project
