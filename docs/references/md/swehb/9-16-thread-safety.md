# 9.16 Thread Safety

> NASA Software Engineering Handbook (SWEHB Ver D), page id 102695807. Source: https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety

9.16 Thread Safety

*Web Resources*

 [View this section on the website](https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety#_tabs-1)  
 [See edit history of this section](https://swehb.nasa.gov/pages/viewpreviousversions.action?pageId=102695807)  
 [Post feedback on this section](http://swehb.nasa.gov/pages/viewpage.action?pageId=102695807&showCommentArea=true&showComments=true#addcomment)

[Section Labels](https://swehb.nasa.gov/display/7150/Tag+Multi-Select):

Unknown macro: {page-info}

* [1. Principle and Rational](#tabs-1)
* [2. Examples](#tabs-2)
* [3. Inputs](#tabs-3)
* [4. Resources](#tabs-4)
* [5. Lessons Learned](#tabs-5)

# 1. Principle

[9.01 Software Design Principles](/spaces/SWEHBVD/pages/102695790/9.01+Software+Design+Principles)

* [9.03 Coding Standards](/spaces/SWEHBVD/pages/102695794/9.03+Coding+Standards)
* [9.04 Command Receipt Acknowledgement](/spaces/SWEHBVD/pages/102695795/9.04+Command+Receipt+Acknowledgement)
* [9.05 Data Interface Integrity](/spaces/SWEHBVD/pages/102695796/9.05+Data+Interface+Integrity)
* [9.06 Dead Code Exclusion](/spaces/SWEHBVD/pages/102695797/9.06+Dead+Code+Exclusion)
* [9.07 Fault Detection and Response](/spaces/SWEHBVD/pages/102695798/9.07+Fault+Detection+and+Response)
* [9.08 Flight Software Modification](/spaces/SWEHBVD/pages/102695799/9.08+Flight+Software+Modification)
* [9.09 Incorrect Memory Use or Access](/spaces/SWEHBVD/pages/102695800/9.09+Incorrect+Memory+Use+or+Access)
* [9.10 Initialization - Safe Mode](/spaces/SWEHBVD/pages/102695801/9.10+Initialization+-+Safe+Mode)
* [9.11 Invalid Data Handling](/spaces/SWEHBVD/pages/102695802/9.11+Invalid+Data+Handling)
* [9.12 Resource Margins](/spaces/SWEHBVD/pages/102695803/9.12+Resource+Margins)
* [9.13 Resource Oversubscription](/spaces/SWEHBVD/pages/102695804/9.13+Resource+Oversubscription)
* [9.14 Resource Usage Measurement](/spaces/SWEHBVD/pages/102695805/9.14+Resource+Usage+Measurement)
* [9.15 Safe Transitions](/spaces/SWEHBVD/pages/102695806/9.15+Safe+Transitions)
* [9.16 Thread Safety](/spaces/SWEHBVD/pages/102695807/9.16+Thread+Safety)
* [9.17 Toggle Commands](/spaces/SWEHBVD/pages/102695808/9.17+Toggle+Commands)

Design interaction between threads to prevent inappropriate interference.

## 1.1 Rationale

Multithreaded software typical of mission-critical embedded applications is vulnerable to incorrect or unpredictable behavior if the interaction between threads has not been adequately designed to prevent inappropriate interference.

## 2. Examples and Discussion

Multitasking operating systems enable flight software developers to partition functionality into separate domains that operate semi-autonomously from other domains. This simplifies the design problem, while creating a new set of issues for the developer. Most threads of execution either supply other threads with information and services, receive data and services, or both. All threads require system resources, which may be scarce under certain circumstances.

Areas of dependence and the potential for resource contention are the main source of problems in multithreaded applications. Thus, it is important to minimize the dependencies between threads wherever possible. Where different threads must share data, employ guard mechanisms to ensure that shared data structures and arrays are modified atomically (i.e., in a single, uninterrupted operation) such that it is never possible that one thread will attempt to modify data while another is attempting to use it. Lock out interrupts and mutual exclusion semaphores are two common mechanisms used. Other solutions may be more appropriate depending on the application and operating environment.

Priority-based task scheduling is a common feature of commercial real-time operating systems. This approach is sufficient to ensure that many software functions are executed within a specified time and in a particular order, but may not work in all cases. Priority inversion (where a low-priority task holds a resource that a higher-priority task depends on) can be a problem in some situations, and care must be taken to avoid these situations. Some operations require tighter time constraints or ordering rules that can be difficult or impossible to guarantee with a pure priority-based scheme. In these situations additional design features, such as using a master task that controls the execution order of other tasks, may be needed. It should be emphasized that the notion of a thread of execution discussed here need not correspond to an operating system-supported thread or task; it may be a related group of operations that are controlled by mechanisms designed into the software that do not rely on operating system facilities.

Conditions that could prevent a thread of execution from completing its work within the anticipated amount of time need to be designed into the software. Design threads that operate with looping constructs to limit the number of iterations of that loop in any given invocation., Use timeouts on threads that perform operations that may block, such as I/O or the taking of a semaphore, and use appropriate error handling to prevent the thread from becoming “hung” indefinitely. Using a heartbeat scheme that allows other parts of software to know when a task upon which they depend has stopped functioning will allow the dependent parts of flight software to take appropriate action rather than becoming hung themselves.

## 2.1 Additional Guidance

Links to Additional Guidance materials for this subject have been compiled in the Relevant Links table. Click here to see the [Additional Guidance](#tabs-4) in the Resources tab.

# 3. Inputs

### 3.1 ARC

* **3.7.2.4.4 Predictable Behavior When Stressed** - Software algorithms and their implementation should be designed to behave predictably when stressed beyond their performance limitations. Some examples include:  
       a. Being sensitive to identified uncertainties.  
       b. Precluding an undesired response to mathematical singularities or limitations.  
       c. Responding predictably to possible events that exceed capabilities.
* **3.7.2.4.5** Response to Resource Over-Subscription - The software design should accommodate unintended situations where resource usage is oversubscribed. The action to be taken in such situations should be specified as part of the requirements on the design.  
    
  *Note: Examples of these situations include buffers overflowing, exceeding a rate group time boundary, and excessive inputs or interrupts. There are several common methods for tolerating these situations, most of which relate to reducing demand from non-essential items, especially if they are the source of over subscription:*

1. 1. *Generate warning messages when appropriate.*
   2. *Instruct external systems to reduce their demands.*
   3. *Lock out interrupts.*
   4. *Change operational behavior to handle the load. For example, the software may use faster but less accurate algorithms to keep up with the load.*
   5. *Reduce the functionality of the software, or even halt or suspend a process or shutdown a computer.*

* **3.7.2.4.6 Response to Missing Inputs** - Software should be designed to tolerate and continue functioning in situations where inputs are temporarily missing.

### 3.2 GSFC

None

### 3.3 JPL

* **4.11.4.5 Response to resource over-subscription** - The software design shall contain a robust response to situations where computer resources are oversubscribed. The action to be taken in such situations shall be specified as part of the requirements on the design.

*Note: Examples of these situations include buffers overflowing, exceeding a rate group time boundary, and excessive inputs or interrupts. There are several common methods for tolerating these situations, most of which relate to reducing demand from non-essential items, especially if they are the source of over subscription:*

1. 1. *Generate warning messages when appropriate.*
   2. *Instruct external systems to reduce their demands.*
   3. *Lock out interrupts.*
   4. *Change operational behavior to handle the load. For example, the software may use faster but less accurate algorithms to keep up with the load.*
   5. *Reduce the functionality of the software, or even halt or suspend a process or shutdown a computer.*

* **4.11.4.7 Use of time-outs** - Software shall be designed to detect and respond appropriately to failures to complete required activities on time.  
    
  *Note: Watchdog timers are commonly used for this purpose. Upon completion of a defined processing path, the software resets a watchdog timer. If the processing gets lost, or fails to make progress, the timer times-out. The timer directs the software to a known point where the processing is restored.*
* **4.11.4.12 Data set consistency** - Software shall be designed to ensure that data sets and parameter lists are consistent when passed among threads such that data is known to be complete when used, and that there is no danger of using a mixture of old and new data.  
    
  *Note: For example, software should not be interrupted in a manner that permits it to use both old and new components of a vector.*
* **4.11.4.13 Thread-safe operations** - Software shall be demonstrated to be free of deadlocks, failures to make progress, race conditions, and other threats to multi-threaded operations.  
    
  *Note: A deadlock is the condition where two processes cannot proceed because each is waiting to use a shared resource held by the other.*  
  *A race condition is anomalous behavior due to unexpected critical dependence on the relative timing of events.*  
  *Non-progress cycles exist if a potentially infinite execution cycle does not include a state indicating that progress is being made.*  
  *Thread-safe is defined as code which functions correctly during simultaneous execution by multiple threads.*  
  *Model-based techniques are recommended wherever possible as a means of demonstrating compliance with this requirement.*

[POWER of 10](http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0CDIQFjAA&url=http%3A%2F%2Fspinroot.com%2Fgerard%2Fpdf%2FPower_of_Ten.pdf&ei=1jc5UbOCBOnlyQHRrICICg&usg=AFQjCNHRZTxeY2kSBGQnOzBBKtnSDy4Xaw&bvm=bv.43287494,d.aWc&cad=rja) (Document used as a reference in the JPL coding standards) [417](#_tabs-<p>4</p>)

* 1. *Rule*: Restrict all code to very simple control flow constructs – do not use *goto* statements, *setjmp* or *longjmp* constructs, and direct or indirect *recursion*.
  2. *Rule*: All loops must have a fixed upper-bound. It must be trivially possible for a checking tool to *prove* statically that a preset upper-bound on the number of iterations of a loop cannot be exceeded. If the loop-bound cannot be proven statically, the rule is considered violated.
  3. *Rule*: Do not use dynamic memory allocation after initialization.
  4. *Rule*: Data objects must be declared at the smallest possible level of scope.

### 3.4 MSFC

None

# 4. Resources

## 4.1 References

[Click here to view master references table.](/spaces/SWEHBVD/pages/101810240/References+Table "References Table")

* (SWEREF-417)

  ["The Power of 10: Rules for Developing Safety-Critical Code"](http://spinroot.com/gerard/pdf/Power_of_Ten.pdf "Click to open in new window")

  Holzmann, G.J., NASA Jet Propulsion Laboratory (JPL), 2006.
* (SWEREF-439)

  [NASA Public Lessons Learned System](https://llis.nasa.gov/ "Click to open in new window")

  The NASA Lessons Learned system.  The system provides access to official, reviewed lessons learned from NASA programs and projects.

## 4.2 Additional Guidance

Additional guidance related to this requirement may be found in the following materials in this Handbook:

| Related Links |
| --- |
|  |

## 4.3 Center Process Asset Libraries

**SPAN - Software Processes Across NASA**  
SPAN contains links to Center managed Process Asset Libraries. Consult these Process Asset Libraries (PALs) for Center-specific guidance including processes, forms, checklists, training, and templates related to Software Development. See SPAN in the Software Engineering Community of NEN. Available to NASA only. <https://nen.nasa.gov/web/software/wiki> [197](#_tabs-<p>4</p>)

See the following link(s) in SPAN for process assets from contributing Centers (NASA Only). 

| SPAN Links |
| --- |
| * [Design](https://nen.nasa.gov/web/software/wiki/-/wiki/SPAN/Design) |

## 4.4 Related Activities

This Topic is related to the following Life Cycle Activities:

| Related Links |
| --- |
| * [A.04 Software Design](/spaces/SWEHBVD/pages/133235380/A.04+Software+Design) |

## 5. Lessons Learned

No Lessons Learned [439](#_tabs-<p>4</p>)  have currently been identified for this principle.
