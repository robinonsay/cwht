# 5.24 - Hazard Report Minimum Content

> NASA Software Engineering Handbook (SWEHB Ver D), page id 140641682. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/140641682/5.24+-+Hazard+Report+Minimum+Content

The following minimum information on software related hazards will be collected over the phases of the safety analyses and captured in the Hazard Analysis Report (Sometimes called the Safety Data Package)

1. **Description of software incident** scenarios depicting the event(s) or causations **leading to a hazard**, when software is one of the causes or events leading to one or more hazards,
   * Any additional environmental or causational conditions,
   * Any state or mode conditions,
   * Any thresholds or ranges of operation which would trigger a software and/or hardware response
2. **Risk related to the hazard**,
   * The likelihood of each scenario,
   * The potential severity of each scenario,
   * Overall potential risk,
3. **Controls and mitigations,** (including any possible fault or failure tolerance levels to be met)
   * Any barriers, alerts or warnings that are needed
   * Any operational workarounds or controls or other human interactions needed
4. **Verifications needed to prove controls and mitigations work**
   * Proof that the necessary verifications were executed and the results were satisfactory
     + Hazard reports are usually divided into at least 3, often 4, deliveries over the course of project development. These are called “Safety Phases.” Phase 0 delivery includes an introduction to the project and the top hazards and causes. Phase 1 has all known, derived, hazards along with their causes, controls, mitigations and risk assignments.  Phase 2 Hazard Analyses deliveries have the approved controls and mitigations along with the verification and testing methods needed to prove that the controls and mitigations work and that the accepted hazards do not cause problems beyond the expected.  The last delivery of the Hazard Analyses Reports, Phase 3, shows where the planned verifications have been performed and that the controls, mitigations, warnings, barriers, or other safety designs put in place have successfully worked.  For small projects, Phases 0 & 1 are often combined.
