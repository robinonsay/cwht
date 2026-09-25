# 7.26 - Verification and Assurance Guidelines for Multicore Concurrent and Partitioned Software Systems

> NASA Software Engineering Handbook (SWEHB Ver D), page id 248774658. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/248774658/7.26+-+Verification+and+Assurance+Guidelines+for+Multicore+Concurrent+and+Partitioned+Software+Systems

7.26 - Verification and Assurance Guidelines for Multicore, Concurrent, and Partitioned Software Systems

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/248774658/7.26+-+Verification+and+Assurance+Guidelines+for+Multicore+Concurrent+and+Partitioned+Software+Systems#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=248774658)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=248774658&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Purpose](#tabs-1)
* [2. Scope](#tabs-2)
* [3. Overview of platforms](#tabs-3)
* [4. Expanded SWE Considerations](#tabs-4)
* [5. Expanded SA Considerations](#tabs-5)
* [6. Mitigation Strategies](#tabs-6)
* [7. References](#tabs-7)

# 1. Purpose

This topic provides NASA-specific verification and software assurance guidance for flight software operating on multicore, concurrent, and partitioned platforms. It addresses critical concerns such as deterministic timing, shared-resource interference, cross-core and inter-partition communication, concurrency robustness, and cybersecurity isolation. The guidance is aligned directly with SWEHB, NPR 7150.2, NASA-STD-8739.8, and relevant industry standards such as FAA AC 20-193 to ensure compliance with best practices for safety-critical systems.

# 2. Scope

This guidance applies to safety-critical software developed or managed by NASA for systems using multicore processor architectures, concurrent execution models, and partitioned avionics platforms. It is relevant to NASA software, where concurrency, cross-partition interactions, or multicore interference impact safety, performance, certification, or cybersecurity requirements.

# 3. Overview of Multicore, Concurrent, and Partitioned Platforms

**Multicore Platforms**

Multicore platforms refer to computing architectures that use processors with multiple cores integrated into a single physical chip. This design improves performance and enables parallel execution by distributing workloads across cores. Key multicore execution models include:

* **Symmetric Multiprocessing (SMP):** All cores share a single OS image, allowing threads to run on any core. SMP offers high performance but introduces higher interference risks due to shared resources.
* **Asymmetric Multiprocessing (AMP):** Each core operates independently, running its own OS or bare-metal application. This model improves predictability but still experiences hardware-level interference from shared resources.
* **Bound Multiprocessing (BMP):** A hybrid where tasks are statically bound to specific cores under a shared OS. This balances SMP flexibility with AMP-like predictability and scheduling stability.

Multicore processing should not be confused with multichip processing, while they share many of the same subjects, the distinction for this is that multicore is a single physical chip, while multichip processing is separate chips (similar or dissimilar) and there is the related topic of coprocessors.

**Concurrent Software Systems**

Concurrency refers to the ability of software systems to execute multiple tasks (threads or processes) simultaneously. In multicore systems, concurrency allows parallel execution to utilize multiple cores effectively. However, concurrency introduces challenges such as:

* Synchronization issues due to simultaneous access to shared resources.
* Timing unpredictability caused by interference between concurrent tasks.
* Faults like deadlocks, race conditions, or shared-memory misuse.

**Partitioned Platforms**

Partitioned platforms use architectures that isolate software functions in separate memory and CPU time segments to ensure robust fault containment and independent qualification. Common partitioning approaches include:

* **Integrated Modular Avionics (IMA):** A system architecture that consolidates multiple avionics functions onto shared hardware while providing for software partitions.
* **Time and Space Partitioning (TSP):** Mechanisms used in systems to allocate CPU time and isolate memory to ensure deterministic behavior across partitions.
* **Physical Partitioning:** Use of coprocessors or multiple chips to separate systems physically.  (Examples: peripheral cards, multiple socket boards, multiple computers)

Partitioning is critical for mixed-criticality systems—where low-criticality software must not interfere with high-criticality functions due to shared hardware.

# 4. Expanded Software Engineering Considerations

Multicore, concurrent, and partitioned platforms introduce unique engineering challenges that demand tailored solutions for verification and system reliability. NASA-specific considerations include:

**4.1 Deterministic Timing and Resource Management**

* Develop **timing-aware scheduling algorithms** and test for worst-case execution time (WCET) under interference conditions.
* Use measurement-based timing analysis tools to validate WCET with maximum concurrency (aligned with SWE-061).
  + WCET does not always happen at highest processing utilization (or computational complexity).  Cache misses for memory can significantly increase the execution time of software.  In multicore systems, there is more contention for cache resources and saturation of the bus from main memory, as discussed in the next section.

**4.2 Shared Resource Interference Analysis**

* Identify direct and indirect interference channels via platform characterization and profiling.

- Examples:  Processor core sharing, Schedulers and preemption, rate groups, cache and memory utilization, communications buses (Ethernet, Space Wire, Mil-STD-1553, Serial, SATA, InfiniBand, wireless …), data exchanges and source of truth, data partitioning and updates, Simultaneous Multi-threading (SMT) (e.g. Hyper-threading), compiler optimizations

* Use SWEHB practices aligned with SWE-134 to implement resource isolation (e.g., cache partitioning).

**4.3 Concurrency Correctness**

* Detect threading issues (e.g., race conditions, deadlocks, partitioning, and data replication) using tools such as thread analyzers and static/dynamic race detectors.
* SWE-065 should guide robustness testing for high-concurrency workloads to ensure thread-safety.

**4.4 Robust Partitioning**

* Validate CPU schedules and spatial isolation mechanisms to ensure independent operation in IMA and TSP architectures (per SWE-205).
* Use tools to verify time partitioning.
* Validate System isolation techniques such as virtualization, and coprocessors.

**4.5 Scalability and Dynamic Features**

* Treat configurations like Dynamic Voltage and Frequency Scaling (DVFS), efficient vs performance core offloading, SMT features, cut through/short circuit processing  as critical and monitor their runtime impact on timing determinism (aligned with SWE-087).

# 5. Expanded Software Assurance Considerations

Software assurance for multicore, concurrent, and partitioned systems must address challenges such as timing unpredictability, resource contention, and isolation verification. NASA-specific considerations include:

**5.1 Verification and Validation of Multicore Platforms**

* Design requirement-based tests to validate software behavior under interference conditions using interference generators.
* Environmental testing on representative hardware should replicate realistic interference scenarios (aligned with SWE-139).

**5.2 Robust Resource Partitioning**

* Validate spatial and temporal isolation to prevent unauthorized access and interference, consistent with SWE-205 requirements.
* Conduct inter-partition communication tests to ensure compliance with IMA/TSP fault containment goals.

**5.3 Cybersecurity and Covert Channel Analysis**

* Perform domain analysis for mixed-criticality systems focusing on shared hardware isolation (aligned with SWE-214).
* Prevent covert channels using runtime monitoring techniques to detect anomalous timing/resource behaviors.

**5.4 Assurance Evidence Requirements**

* Produce traceable artifacts to show interference mitigations, timing reliability, and partitioning validation.
* Align verification results with DO-178C and FAA AC deliverables (e.g., Accomplishment Summary for MCPs).

# 6. Hybrid Mitigations

* Apply time and space partitioning for mixed-criticality systems and validate using ARINC 653-compliant tools.
* Virtualization considering the underlying hardware may be shared
* Architect software with data locality as a critical requirement

# 7. References

* **NASA Software Engineering Handbook (SWEHB):** Guidelines for verifying and validating safety-critical and multicore systems (SWE-134, SWE-205, SWE-061, SWE-065, SWE-087, SWE-214).
* **NPR 7150.2:** Multicore processor and partitioning verification standards.
* **NASA-STD-8739.8:** Software assurance standards for distributed systems.
* **FAA AC 20-193:** Formal guidance for multicore and partitioned avionics systems.
