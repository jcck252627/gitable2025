# [Domain-8](#domain-8-software-development-security) **Software Development Security**

- Domain 8 has a ~10% exam weighting, and is focused on helping security professionals understand and apply software or application security
  - Applications can present significant risks, and we need to understand and balance these risks with business requirements and implement appropriate risk mitigation; if a company develops custom software, the custom solution can present additional, unique risks and vulns
    - orgs with custom solutions should be on the lookout for logic weaknesses (e.g. buffer overflow vulns), and guard against malicious changes (e.g. backdoors) that can leave the system vulnerable to attacks
  - As software development environments have become increasingly complex, it's important to review this area -- one of the biggest threats to an organization's security

- In this domain you'll learn the basic principles behind securely designing, building, testing, operating and even decommissioning enterprise apps
- Security should be part of the design, and incorporated into the architecture, with the level of protection based on requirements and operating environment
- The Software Development LifeCycle consists of the following steps:
  - Requirements gathering: why create the software, what it will do, and for whom it will be created
  - Design: encapsulating how the software will meet requirements
  - Development: creating/coding the software to meet spec, and integrating with other systems as required
  - Testing: verifying/validating software meets requirements
  - Operations and Maintenance: deploying, and ensuring it's appropriately configured, patched, and monitored

##
**domain 8 - video 42 - Designing Security into software** 
-   It is common for programmers to make 15-50 mistakes per 1,000 lines of code. If using a programming maturity framework, we can lower that to 1 error per 1,000 lines of code.
-   Most of the errors are not a vulnerability, or really a concern, but the more we use software in everything, the more critical the vulnerabilities beco
-   Software-Defined Security (SDS):
    - Security functions are removed from the hardware and become virtual network functions (VNFs).
    - SDS is software-managed, policy-driven, and governed security where most of our security controls (IDS/IPS, network segmentation, access controls, …) are automated and monitored by the software
-   Auditing and Logging of Changes:
    - We need to be clear on change and configuration management
    - How changes are requested (Request, formal assessment, planning, design and testing, implementation, final assessment), the controls we have in place (request control, change control, and release control) and how they contribute to security. 
    - How does our configuration management control the versions of software used in an organization.
-   Risk Analysis and Mitigation: (Idenify  --> Analyze --> Mitigate)
    - With risk analysis and mitigation we identifying, assessing and mitigating the risks, understanding how they might affect our (software) project, and figure out what we can do to minimize the effects on our scope, schedule, cost, and quality.
    - Risks can be either opportunities or threats; they are scored on the likelihood of occurrence and impact on a project.

**domain 8 - video 43 - Programming Concepts part 1** 
-   Machine Code:			Software executed directly by the CPU, 0's and 1's understood by the CPU
-   Source Code:			Computer programming language, written in text and is human understandable, that is translated into machine code
-   Assembler Languages:			Short mnemonics like ADD/SUB/JMP, which are matched with the full length binary machine code; assemblers convert assembly language into machine language. A disassembler does the reverse
-   Compiler Languages:			Translates the higher level language into machine code and saves, often as executables, compiled once and run multiple times. 
-	Interpreted Languages:			Similar to compiler languages, but interprets the code each time it is run into machine code
-	Bytecode:			An interpreted code, in intermediary form, converted from source code to interpreted, but still needs to be converted into machine code before it can run on the CPU.
-	Procedural Languages (Procedure-oriented):			Uses subroutines, procedures and functions.
-   Object-oriented Programming (OOP):
		- Based on the concept of objects, which may contain data, in the form of fields, often known as attributes, and code, in the form of procedures, often known as methods.
		- An object's procedures can access and often modify the data fields of the objects with which they are associated.
		- In OOP,  computer programs are designed by making them out of objects that interact with one another.

-   Object-oriented Programming (OOP)
    - Based on the concept of objects, which may contain data, in the form of fields, often known as attributes, and code, in the form of procedures, often known as methods.
		- Anobject's procedures can access and often modify the data fields of the objects with which they are associated.
		- In OOP, computer programs are designed by making them out of objects that interact with one another.

-   4th Generation languages (4GL):
    - Fourth-generation languages are designed to reduce programming effort and the time it takes to develop software, resulting in a reduction in the cost of software development.
    - Increases the efficiency by automating the creation of machine code.
    - Often uses a GUI, drag and drop, and then generating the code, often used for websites, databases and reports.

-   Programming Languages and Generations:
    - 1st generation: Machine Code
    - 2nd Generation: Assembler languages
    - 3rd Generation: C, C++, Java, Python, PHP, Perl, C#, BASIC, Pascal, Fortran,ALGOL, COBOL, …
    - 4th Generation: ABAP, Unix Shell, SQL, PL/SQ
    - 5th Generation: Prolog, OPS5, Mercury, …  AI research

-   CASE (Computer-Aided Software Engineering): - 4th GL also an 4th generation environment, similiar to CAD but for software design
    - Similar to and were partly inspired by computer-aided design (CAD) tools use for designing hardware products.
    - Used for developing high-quality, defect-free, and maintainable software.
    - Often associated with methods for the development of information systems together with automated tools that can be used in the software development process.
    - CASE software is classified into 3 categories:
        - Tools support specific tasks in the software life-cycle.
        - Workbenches combine two or more tools focused on a specific part of the software life-cycle.
        - Environments combine two or more tools or workbenches and support the complete software life-cycle.

**domain 8 - video 44 - Programming Concepts part 2** 
-   **Top-Down Programming:**  ....start out with big picture/overview then break into pieces
    - Starts with the big picture, then breaks it down into smaller segments.
    - An overview of the system is formulated, specifying, but not detailing, any firstlevel subsystems.
    - Each subsystem is then refined in yet greater detail, sometimes in many additional subsystem levels, until the entire specification is reduced to base elements.
    - Procedural programming leans toward Top-Down, you start with one function and add to it.
-   **Bottom-Up Programming:**  .... start with the specific item, build on and around it
    - Piecing together of systems to build more complex systems, making the original systems a sub-system of the overarching system.
    - The individual base elements of the system are first specified in great detail, they are then linked together to form larger subsystems, which then in turn are linked, sometimes in many levels  until a complete top-level system is formed.
    - OOP leans tends toward Bottom-Up, you start by developing your objects and build up.

-   **Type of software release:**
    - Open source:
      - We release the code publicly, where it can be tested, improved and corrected, but it also allows attackers to find the flaws in the code.
    - Closed Source:
      - We release the software, but keep the source code a secret, may be sound business practice, but can also be security through obscurity.
    - Proprietary Software:
      - Software protected byintellectual property and/or patents, often used interchangeably with Closed Source software, but it really is not. It can be both Open and Closed Source software.
      - Any software not released into the public domain is protected by copyright
      - "We OWN the software" ... thats what it means by "proprietary"

    - Free Software:
      - Freeware:  Actually free software, it is free of charge to use.
    - Shareware: 
      - Fully functional proprietary software that is initially free to use.
      - Often for trials to test the software, after 30 days you have to pay to continue to use.
    - Crippleware:
      - Partially functioning proprietary software, often with key features disabled.
      - The user is required to make a payment to unlock the full functionality.
    - EULAs (End-User License Agreements):
      - Electronic form where the user clicks “I agree” to the software terms and conditions while installing the software.

-   ** Type of Software Licenses:**
    - **Open source software** can be protected by a variety of licensing agreement.
      - **GNU (General Public License) also called GPL:**
        - Guarantees end users the freedom to run, study, share and modify the software.
        - A "copyleft" license, which means that derivative work can only be distributed under the same license terms.
    - **BSD (Berkeley Software Distribution):**
        - A family of permissive free software licenses, imposing minimal restrictions on the use and redistribution of covered software.
        - This is different than copyleft licenses, which have reciprocity share-alike requirements.
    - **Apache:**
        - Software must be free, distribute, modify and distribute the modified software.
        - Requires preservation of the copyright notice and disclaimer

##
- **Acceptance**: formal, structured hand-off of the completed software system to the customer org; usually involves test, analysis and assessment activities
- **Accreditation**: AKA Security Accreditation a formal declaration by a designated accrediting authority (DAA) that an information system is approved to operate at an acceptable level of risk, based on the implementation an approved set of technical, managerial, and procedural safeguards
- **ACID Test**: data integrity provided by means of enforcing atomicity, consistency, isolation, and durability policies
- **Aggregation**: ability to combine non-sensitive data from separate sources to create sensitive info; note that aggregation is a "security issue", where as inference is an attack (where an attacker can pull together pieces of less sensitive info to derive info of greater sensitivity)
- **Arbitrary code**: alternate set of instructions and data that an attacker attempts to trick a processor into executing
- **Buffer overflow**: source code vulnerability allowing access to data locations outside of the storage space allocated to the buffer; can be triggered by attempting to input data larger than the size of the buffer
- **Bypass attack**: attempt to bypass front-end controls of a database to access information
- **Certification**: comprehensive technical security analysis of a system to ensure it meets all applicable security requirements
- **CAB**: Change Advisory Board purpose is to review and approve/reject proposed code changes
- **Citizen programmers**: organizational members who codify work-related knowledge, insights, and ideas into (varying degrees of) usable software; the process and result is ad hoc, difficult to manage, and usually bereft of security considerations
- **Code protection/logic hiding**: prevents one software unit from reading/altering the source/intermediate/executable code of another software unit
- **Code reuse**: reuse of code, rather than re-invented code means units of software (procedures/objects) means higher productivity toward development requirements using correct, complete, safe code
- **Complete coverage**: testing all of the functions of software
- **Concurrency**: using a lock to allow an authorized user to make changes, then unlock the data element after changes are complete
- **Object/Memory reuse**: systems allocate/release and reuse memory/resources as objects to requesting processes; data remaining in the object when it is reused is a potential security violation (i.e. data remanence)
- **CORBA**: Common Object Request Broker Architecture is a set of standards addressing interoperability between software and hardware products, residing on different machines across a network; providing object location and use across a network
- **Configuration Control**: process of controlling modifications to hardware, firmware, software, and documentation to protect the information system against improper modifications prior to, during, and after system implementation
- **Configuration Management (CM)**: collection of activities focused on establishing and maintaining integrity of IT products and information systems, through the control of processes for initialization, changing and monitoring the configurations of those products and systems throughout the system development lifecycle
- **Covert Channels/Paths**: a method used to pass information over a path that is not normally used for communication; communication pathways that violate security policy or requirement (deliberately or unwittingly); basic types are timing and storage
- **Data Contamination**: attackers attempt to use malformed inputs, at the field, record, transaction, or file level, in an attempt to disrupt the proper functioning of the system
- **Data Lake**: a data warehouse incorporating multiple types of streams of unstructured or semi-structured data
- **Data Mining**: analysis and decision-making technique that relies on extracting deeper meanings from many different instances and types of data; often applied to data warehouse content
- **Data Modeling**: design process that identifies all data elements that the system will need to input, create, store, modify, output, and destroy during operational use; should be one of the first steps in analysis and design
- **Data Protection and Data Hiding**: restricts or prevents one software unit from reading or altering the private data of another software unit or in preventing data from being discovered or accessed by a subject
- **Data Type Enforcement**: how a language protects a developer from trying to perform operations on dissimilar types of data, or in ways that would lead to erroneous results
- **Data Warehouse**: collection of data sources such as separate internal databases to provide a broader base of info for analysis, trending and reference; may also involve databases from outside the org
- **Data-centric Threat Modeling**: methodology and framework focusing on the authorized movements and data input/output into and from a system; corresponds with protecting data in transit, at rest, and in use when classifying organizational data
- **Defensive Programming**: design/coding allowing acceptable but sanitized data inputs to a system; lack of defensive programming measures can result in arbitrary code execution, misdirection of the program to other resources/locations, or reveal info useful to an attacker
- **Design Reviews**: should take place after the development of functional and control specifications but before the creation of code
- **Dirty read**: occurs when one transaction reads a value from a database that was written by another transaction that didn't commit
- **Emerging Properties**: an alternate/more powerful way of looking at systems-level behavior characteristics such as safety and security; helps provide a more testable, measurable answer to questions such as "how secure is our system?"
- **Encapsulation**: note see network Encapsulation in [Domain 4](https://github.com/jefferywmoore/CISSP-Study-Resources/blob/main/CISSP-Domain-4-20204+Objectives) (disambiguation); enforcement of data/code hiding during all phases of software development and operational use; bundling together data and methods is the process of encapsulation (opposite of unpacking/revealing)
- **Executable/Object Code**: binary representation of the machine language instruction set that the CPU and other hardware of the target computer can directly execute
- **XML**: Extensible Markup Language is a set of HTML extensions providing for data storage and transport in networked environments; frequently used to integrate web pages with databases; XML is often embedded in the HTML files making up elements of a web page
- **Functional requirements**: describes a finite task or process the system must perform; often directly traceable to specific elements in the final system's design and construction
- **Hierarchical database model**: data elements and records are arranged in tree-like parent-child structures
- **Instance**: in object-oriented programming, an "instance of a class" refers to a specific object created from that class, which is a blueprint or template defining the characteristics and behaviors of objects
- **Integrated Product and Process Development (IPPD)**: management technique that simultaneously integrates essential acquisition activities through the use of multidisciplinary teams to optimize the design, manufacturing, and supportability processes
- **Integrated Product Team**: team of stakeholders and individuals that possess different skills and who work together to achieve a defined process or product
- **Infrastructure as Code (IaC)**: instead of viewing hardware config as a manual, direct hands-on, one-on-one admin hassle, it is viewed as just another collection of elements to be managed in the same way that software and code are managed under DevSecOps
- **Interactive Application Security Testing (IAST)**: testing that combines or integrates SAST and DAST to improve testing and provide behavioral analysis capabilities to pinpoint the source of vulnerabilities
- **Knowledge Discovery in Database (KDD)**: mathematical, statistical, and visualization method of identifying valid and useful patterns in data
- **Knowledge Management**: efficient/effective management of info and associated resources in an enterprise to drive business intelligence and decision-making; may include workflow management, business process modeling, doc management, db and info systems and knowledge-based systems
- **Level of abstraction**: how closely a source-code/design doc represents the details of the underlying object/system/component; lower-level abstractions generally have more detail than high-level ones
- **Living off the land** (non-malware based ransom attack): system attack where the system/resources compromised are used in pursuit of additional attacks (i.e. the attacker's agenda); anti-malware defense doesn't detect/prevent the attack given the attacker's methodology
- **Malformed input attack**: not currently handling input data is a common source of code errors that can result in arbitrary code exec, or misdirection of the program to other resources/locations
- **Markup Language**: non-programming language used to express formatting or arrangement of data on a page/screen; usually extensible, allowing users to define additional/other operations to be performed; they extend the language into a programming language (e.g. in the same way JavaScript extends HTML)
- **Metadata**: info that describes the format or meaning of other data, which can be used to provide a systematic method for describing resources and improving info retrieval
- **Mobile code (executable content)**: file(s) sent by a system to others, that will either control the execution of systems/applications on that client or be directly executed
- **Modified prototype model**: approach to system design/build that starts with a simplified version of the application; feedback from stakeholders is used to improve design of a second version; this is repeated until owners/stakeholders are satisfied with the final product
- **Network database model**: database model in which data elements and records are arranged in arbitrary linked fashion (.e.g lists, clusters, or other network forms)
- **Nonfunctional requirements**: broad characteristics that do not clearly align with system elements; many safety, security, privacy, and resiliency can be deemed nonfunctional
- **Object**: encapsulation of a set of data and methods that can be used to manipulate that data
- **Object-oriented database model**: database model that uses object-oriented programming concepts like classes, instances, and objects to organize, structure, and store data and methods; schemas define the structure of the data, views specify table, rows, and columns that meet user/security requirements
- **Object-oriented security**: systems security designs that make sue of object-oriented programming characteristics such as encapsulation, inheritance, polymorphism, and polyinstantiation
- **Open-source software**: source code and design info is made public, and often using licenses that allow modification and refactoring
- **Pair programming**: requires two devs to work together, one writing code, and the other reviewing and tracking progress
- **Pass-around reviews**: often done via email or code review system, allows devs to review code asynchronously
- **PERT**: chart that uses nodes to represent milestones or deliverables, showing the estimated to to move between milestones
- **Polyinstantiation**: creates a new instance (copy) of a data item, with the same identifier or key, allowing each process to have its own version of that data; useful for enforcing and protecting different security levels for a shared resource; polyinstantiation also allows the storage of multiple different pieces of info in a database at different classification levels to prevent attackers from inferring anything about the absence of info
- **Procedural programming**: emphasizes the logical sequence of steps to be performed, where a procedure is a set of software that performs a particular function, requiring specific input data, producing a specific set of outputs, and procedures can invoke other procedures
- **Query attack**: use of query tools to access data not normally allowed by the trusted front end, including the views controlled by the query application; could also result from malformed queries using SQL to bypass security controls; improper/incomplete checks on queries can be used in a similar way to bypass access controls
- **Ransom attack**: form of attack that threatens destruction, denial, or unauthorized public release/remarketing of private information assets; usually involves encrypting assets and withhold the decryption key until a ransom is paid by the victim
- **Refactoring**: partial or complete rewrite of a set of software to perform the same functions, but in a more straightforward, more efficient, or more maintainable form
- **Regression testing**: test a system to ascertain whether recently approved modifications have changed performance of other approved functions or introduced other unauthorized behavior;testing that runs a set of known inputs against an app and compares to results previously produced (by an earlier version of the software)
- **Relational database model**: AKA relational database management system (RDBMS), data elements and records arranged in tables which are related or linked to each other to implement business logic, where data records of different structures or types are needed together in the same activity
- **Representational State Transfer (REST)**: software architectural style for synchronizing the activities of two or more apps running on different systems on a network; REST facilitates these processes exchanging state information, usually via HTTP/S
- **Reputation monitoring**: defensive tactic that uses the trust reputation of a website or IP address as a means of blocking an org's users, processes or systems from connecting to a possible source of malware or exploitations; possibly the only real defense against zero-day exploits; involves monitoring URLs, domains, IP addresses or other similar info to separate untrustworthy traffic
- **Runtime Application Security Protection (RASP)**: security agents comprised of small code units built into an app which can detect set of security violations; upon detection, the RASP agent can cause the app to terminate, or take other protective actions
- **Security Assessment**: testing, inspection, and analysis to determine the degree to which a system meets or exceeds the required security posture; may assess whether an as-built system meets the requirements in its specs, or whether an in-use system meets the current perception of the real-world security threats
- **Software Quality Assurance**: variety of formal and informal processes that attempt to determine whether a software app or system meets all of its intended functions, doesn't perform unwanted functions, is free from known security vulns, and is free from insertion or other errors in design and function
- **SDLC**: Software Development LifeCycle is a framework and systematic associated with tasks that are performed in a series of steps for building, deploying, and supporting software apps; begins with planning and requirements gathering, and ends with decommissioning and sunsetting; there are many different SDLCs, such as agile, DevSecOps, rapid prototyping, offering different approaches to defining and managing the software lifecycle
- **Source code**: program statements in human-readable form using a formal programming language's rules for syntax and semantics
- **Spyware/Adware**: software that performs a variety of monitoring and data gathering functions; AKA potentially unwanted programs/applications (PUP/PUA), may be used in monitoring employee activities/use of resources (spyware), or advertising efforts (adware); both may be legit/authorized by system owners or unwanted intruders
- **Strong data typing**: feature of a programming language preventing data type mismatch errors; strongly typed languages will generate errors at compile time
- **Threat surface**: total set of penetrations of a boundary or perimeter that surrounds or contains system elements
- **TOCTOU attack**: time of check vs time of use (TOCTOU) attack takes advantage of the time delay between a security check (such as authentication or authorization) being performed and actual use of the asset
- **Trapdoor/backdoor**: AKA maintenance hook; hidden mechanism that bypasses access control measures; an entry point into an architecture or system that is inserted in software by devs during development to provide a method of gaining access for modification/support; can also be inserted by an attacker, bypassing access control measures designed to prevent unauthorized software changes
- **UAT**: User Acceptance Testing typically the last phase of the testing process; verifies that the solution developed meets user requirements, and validates against use cases

## [8.1](#81-understand-and-integrate-security-in-the-software-development-life-cycle-sdlc-osg-10-chpt-20) Understand and integrate security in the Software Development Life Cycle (SDLC) (OSG-10 Chpt 20)

**domain 8 - video 45- Software Development Methodologies part 1**

- Past: Waterfall method
    - very linear ... not expecting any changes, building a software is unlike when building a house
- Current: Spiral, Sashimi, Agile and Scrum

-   **Waterfall**  
    - Linear apporches ... each phase leading into directly the next phase
    - The unmodified waterfall model does not allow us to go back to the previous phase.
    - Also referred as unmodified waterfall (cannot go back at all) vs modified waterfall (can go back but only one step)
    - Still used in some situation ... but very linear and not adopted to changes 
-   **Sashimi Model (Waterfall with overlapping phases or modified waterfall...):**  
    - Similar to waterfall, but we always have 2 overlapping phases, if we close one phase, we add the next phase.
    - The modified waterfall model allows us to go back to the previous phase but no further.  (one back or one forward no further)

**domain 8 - video 46- Software Development Methodologies part 2**
-   **Agile Software Development:**  
    - Describes a set of values and principles for software development under which requirements
    - Solutions evolve through the collaborative effort of self-organizing cross-functional teams.
    - Uses adaptive planning, evolutionary development, early delivery, and continuous improvement, and it encourages rapid and flexible response to change.
    - Adaptive planning ... plan is not fixed ... adapt when change occurs then evolve ... deliver early and often
    - Adaptive also to customer changes ... dont design something they dont want from the beginning 
    - Based on Agile Manifesto ... about picking better solution/path to design software ...
      - Individuals and Interactions are more than processes and tools.
      - Working Software is more than comprehensive documentation.
      - Customer Collaboration is more than contract negotiation.
      - Responding to Change is more than following a plan.
      - CISSP‑exam–focused explanation of the **12 Agile Manifesto principles**, why they matter, and how ISC² expects you to think about them from a security, governance, and risk perspective.
        - **the highest priority is to satisfy the customer through early and continuous delivery of valuable software**
          - Why it exists:    Deliver value fast and often
          - CISSP importance:   Frequent releases = frequent security risk introduction .......Requires continuous security review
          - CISSP takeaway:   Early delivery is acceptable only when security testing is continuous

        - **Welcome changing requirements, even late in development; Agile processes harness change for the customer’s competitive advantage**
          - Why:    Business needs evolve rapidly
          - Security risk (CISSP angle) Late changes can: 
              - Bypass security review
              - Break threat models
              - Violate compliance
          - CISSP answer mindset:   Changes must still follow formal change control and risk assessment, even in Agile
        - **Deliver working software frequently, from a couple of weeks to a couple of months, with a preference for the shorter timescale**
          - Why:  Short feedback loops and Early defect detection
          - Security impact:  Automation becomes mandatory .......Manual security reviews won’t scale
          - CISSP best practice:    Use automated security testing (SAST, DAST, dependency scans)
        - **Business people and developers must work together daily throughout the project**
          - Why:  Reduce miscommunication
          - CISSP concern:  Business may deprioritize security under deadline pressure
          - CISSP principle:  Security requirements must be non‑negotiable functional requirements
        - **Build projects around motivated individuals; give them the environment, support, and tools and trust them to build**
          - Why:  Empower teams and Increase productivity
          - Security risk:  Over‑trusting individuals creates insider risk ....and Lack of segregation of duties
          - CISSP must‑know:    Agile does NOT eliminate least privilege or separation of duties
        - **Emphasizing face-to-face conversation**
          - Why: Faster understanding ... and Less bureaucracy
          - CISSP risk:  Verbal agreements ≠ audit trail
          - Exam tip:   Lack of documentation is a major Agile compliance weakness
        - **Working software is the primary measure of progress**
          - Why:  Results over paperwork
          - CISSP challenge:  “Working” does not mean “secure” .... and ..Security defects may be invisible
          - CISSP lens: Progress must include security acceptance criteria
        - **Agile processes promote sustainable development; the them should be able to maintain a constant pace indefinitely**
          - Why:  Avoid burnout ... and Maintain quality long‑term
          - Security angle: Rushed development increases Coding errors...Vulnerabilities... and Misconfigurations
          - CISSP alignment:  Stable pace improves secure coding discipline
        - **Continuous attention to technical excellence and good design enhances agility**
          - Why:  Maintain long‑term agility
          - Why CISSP cares: Secure architecture reduces attack surface .... also ...Technical debt = future vulnerabilities
          - High‑value CISSP phrase:  ....“Security by design” and defense‑in‑depth
        - **Simplicity, or the art of maximizing the amount of work not done, is essential**
          - Why:  Less complexity, fewer bugs
          - Security benefit: Smaller attack surface .... and ....Fewer dependencies
          - CISSP sweet spot: Simplicity improves availability, integrity, and maintainability
        - **The best architectures, requirements, and designs emerge from self-organizing teams**
          - Why:  Teams adapt faster ..... AND Less micromanagement
          - CISSP red flag: Lack of centralized security governance ...AND Inconsistent controls across teams
          - CISSP principle:  Security policy remains centralized, even if execution is decentralized
        - **At regular intervals, the team reviews their effective and adjusts for improvement**
          - Why: Continuous improvement
          - Security relevance:  Post‑incident reviews ....Lessons learned ....Threat model updates
          - CISSP alignment:  Supports continuous risk management and improvement

      - High‑Probability CISSP Exam Themes ....Correct mindset answers
        - “Security must be integrated into every sprint”
        - “Frequent releases increase risk without automation”
        - “Agile requires stronger—not weaker—governance”

      - CISSP One‑Paragraph Memory Summary
        **The 12 Agile Manifesto principles emphasize flexibility, frequent delivery, and collaboration. From a CISSP perspective, Agile increases the need for continuous security testing, strong governance, automated controls, and integrated risk management to compensate for reduced documentation and frequent change.**

-   **Agile Software Development - Scrum**  
    - Scrum is an Agile project management framework that delivers products in short, iterative cycles called sprints, emphasizing collaboration, adaptability, and continuous improvement
    - Also enabling security requirements to be identified, prioritized, and addressed throughout the system development life cycle (SDLC).
    - Designed for small teams each about 10 people
    - Rely on generally 2-week development cycles ... called "sprints"
    - Daily short stand-up meeting get to the point ... no sitting for efficency and effectiveness 
    - 3 core roles in Scrum
      - Product Owner:  product stakeholders, voice of the customer ... explain what we are doing... accountable for end result/delierables
      - Development Team: responisble for delivering the product at end of each sprint ... 3 to 9 people doing the actual work
      - Scrum Master: team lead or project manager ensure the framework is followed ... remove any roadblocks

-   **Agile Software Development - XP(Extreme Programming)**  
    - Intended to improve software quality and responsiveness to changing customer requirements.
    - Iterative ... responses to frequent changes and based on short development cycles
    - uses programming pairs ... two programmers coding together ...excessive code review (unit test) on all code
    - avoiding building of features until they are actually needed
    - Uses advocates frequent releases in short development cycles, intended to improve productivity and introduce checkpoints at which new customer requirements can be adopted.

-   **Spiral Model (NOT considered an Agile methodology)**  
    - shares some Agile‑like characteristics
    - heavy on documentation
    - risk‑driven, iterative SDLC model, originally proposed by Barry Boehm.
    - The spiral model has four phases: Planning, Risk Analysis, Engineering and Evaluation.
    - A software project repeatedly passes through these phases in iterations (called Spirals in this model).
    - The baseline spiral, starting in the planning phase, requirements are gathered and risk is assessed.
    - Each subsequent spiral builds on the baseline spiral.
    - CISSP Exam‑Safe Statements (Memorize These) ---Correct statements
      - **“The Spiral Model is an iterative, risk‑driven development model.”**
      - **“Spiral is suitable for high‑risk systems requiring strong governance.”**
      - **“Agile emphasizes customer collaboration and rapid delivery, while Spiral emphasizes risk management.”**

-   **RAD (Rapid Application Development):**  
    - Puts an emphasis on adaptability and the necessity of adjusting requirements in response to knowledge gained as the project progresses.
    - Prototypes are often used in addition to or sometimes even in place of design specifications.
    - Very suited for developing software that is driven by user interface requirements.
    - GUI builders are often called rapid application development tools.

-   **Prototyping**  
    - Breaks projects into smaller tasks, creating multiple prototypes of system design features.
    - A working model of software with some limited functionality, rather than designing the full software up front.
    - Has a high level of customer involvement, the customer inspects the prototypes to ensure that the project is on track and meeting its objective.

**domain 8 - video 47- Software Development Methodologies part 3**

-   **SDLC (Software Development Life Cycle):**  
    - The SDLC is not really a methodology, but a description of the phases in the life cycle of software development.
    - if an answer option in the SDLC doesnt include secure/security as a key component then its the WRONG option
    - These phases are (in general), investigation, analysis, design, build, test, implement, maintenance and support (and disposal).
    - Can have security built into each step of the process, for the exam it always does.
    - If an answer about SDLC does not list secure or security, it would be wrong and can be eliminated.
    - Has a number of clearly defined and distinct work phases which are used by systems engineers and systems developers to plan for, design, build, test, and deliver information systems.

    - The aim is to produce high-quality systems that meet or exceed customer expectations, based on customer requirements, by delivering systems which move through each clearly defined phase, within scheduled time frames and cost estimates.

    - SDLC is used during the development of a project, it describes the different stages involved in the project from the drawing board, through the completion of the project.
    - All software development methodologies follow the SDLC phases but the method of doing that varies vastly between methodologies.
    - Many different SDLC methodologies have been created, Waterfall, Spiral, Agile, Rapid Prototyping,...
    - In Scrum project a single user story goes through all the phases of the SDLC within a single two-week sprint, where Waterfall projects can take many months or several years to get through the phases.
    - While very different they both contain the SDLC phases in which a requirement is defined, then pass through the life cycle phases ending in the final phase of maintenance and support.

-   **Projects, Programs and Protfolios :**  
    - A **project** is a temporary and unique endeavor, with a finite start and end, that is focused on creating a unique product, service, or result.
    - A **program** is a collection of related projects. Like a project, a program is temporary, when the collection of projects are complete, the program is complete.
    - A **portfolio** is a collection of projects and programs that are managed as a group to achieve strategic objectives.

-   **IPT (Integrated Product Team): .... used in a project**  
    - identify the stakeholders (people who are impacted by this project) early on in the project, not normally part of the project but important on input
    - A multidisciplinary group of people who are collectively responsible for delivering a defined product or process.
    - IPTs are used in complex development programs/projects for review and decision making.
    - The emphasis of the IPT is on involvement of all stakeholders (users, customers, management, developers, contractors) in a collaborative forum.
    - IPTs can be addressed at the program level, there may also be Oversight IPTs (OIPTs), or Working-level IPTs (WIPTs).
    - IPTs are created most often as part of structured systems engineering methodologies, focusing attention on understanding the needs and desires of each stakeholder.

-   **domain 8 - video 48- Software Development Methodologies part 4**
-   **Source Code Escrow:**  
    - The deposit of the source code of software with a third party escrow agent.
    - If say the software vendor went out of business or abandent the software source escrowing might mitigate some risks
    - Escrow is typically requested by a party licensing software (the licensee), to ensure maintenance of the software instead of abandonment or orphaning.
    - The software source code is released to the licensee if the licensor files for bankruptcy or otherwise fails to maintain and update the software as promised in the software license 
    agreement.
    - Strong contractual obligation
    - Released only under contract
    - CIA focus on Availability and BC / Domain 8

    - **Primary CISSP Objectives**
      - Availability – Ensures continued access to critical software
      - Risk mitigation – Addresses vendor lock‑in risk
      - Business continuity – Supports contingency and resilience planning
    - **CISSP Security Considerations**
      - Code is usually: Encrypted ...AND Stored offline or in controlled environments
      - Escrow does not support active development
      - Focus is legal and operational, not technical collaboration
    - **CISSP Exam‑Safe Statement**
      - Source code escrow is a business continuity control designed to reduce dependency on third‑party vendors.

-   **Source Code Repositories:**  
    - Store and manage source code, version contorl, enable collaboration amount developers  ... Github,Gitlab,Bitbucket
    - Using public third party code repositories comes with some security concerns.
    - Other than the provider security, one of the most important controls is using multi-factor authentication.
    - File archive and web hosting facility where a large amount of source code, for software or for web pages, is kept, either publicly or privately.
    - They are often used by open-source software projects and other multi-developer projects to handle various versions. They help developers submit patches of code in an organized fashion.
    - Repositories are not designed for business continuity guarantees
    - Availability risk exists if the provider becomes unavailable
    - Minimal contractual obligation
    - Used by developers
    - CIA focus on Integrity and Accountability / Domain 1, 8
    - **Primary CISSP Objectives**
      - Integrity – Version control prevents unauthorized or accidental changes
      - Accountability – Commit history provides non‑repudiation
      - Change management – Supports secure SDLC processes
    - **CISSP Security Considerations**
      - Must enforce: Strong authentication (MFA)
      - Must enforce: Access control (least privilege)
      - Must enforce:Logging and monitoring
    - **CISSP Exam‑Safe Statement**
      - A source code repository supports development integrity and change control but does not guarantee source availability if a vendor becomes insolvent.  
   
-   **API Security (Application Programming Interface):**  
      - Allows an application to communicate with another application, operating systems, databases, networks, SSO...
      - Many applications use API's, this could be to add super sign-on, integrate 2 applications, or many other things,...
      - They are a good example of how we integrate for better usability, but often security is overlooked.
      - API's are the cause of a number of recent high-profile website security breaches including Snap Chat, Pinterest and Instagram.
      - We covered the OWASP top 10 web vulnerabilities in domain 3.
      - OWASP also has an Enterprise Security API Toolkits project, which includes these critical API controls:
      - Authentication, Access control, Input validation, Output encoding/escaping, Cryptography, Error handling and logging, Communication security, HTTP security and Security configuration.

-   **Software Change and Configuration Management:**  
    - Earlier in this domain we covered how software development has a lifecycle, and in Domain 7 we covered configuration and change management.
    - Both change and configuration management are very applicable to our software development process, all the way from investigation/initiation to disposal of the software.
    - As with many of the concepts we cover they are to some extend logical, configuration management tracks changes to a specific piece of software where change management is all changes in the entire software development process.
    - NIST 80-128: Guide for Security-Focused Configuration Management of Information Systems uses these terms:
    - A Configuration Management Plan (CM Plan) is a comprehensive description of the roles, responsibilities, policies, and procedures that apply when managing the configuration of products and systems.

      - CM Plan - **Configuration Control Board (CCB)** – Establishment of and charter for a group of qualified people with responsibility for the process of controlling and approving changes throughout the development and operational lifecycle of products and systems, may also be referred to as a change control board.
      - CM Plan - **Configuration Item Identification** – for selecting and naming configuration items that need to be placed under CM.
      - CM Plan - **Configuration Change Control** – Process for managing updates to the baseline configurations for the configuration items.
      - CM Plan - **Configuration Monitoring** – Process for assessing or testing the level of compliance with the established baseline configuration and mechanisms for reporting on the configuration status of items placed under CM


-   **domain 8 - video 49- DevOps and DevSecOps**

-   **DevOps**
    - Cooperation between different silos (orgiazation barriers where depts work in isolatoins) such as development, operations, and Quality Assurance in an organization
    - Aligned with Agile, code is deployed rapidly, multiple times a day. .... small frequent changes and deployment
    - is a cultural and technical approach that combines software development (Dev) and IT operations (Ops) to deliver applications and infrastructure faster, more reliably, and with greater collaboration through automation, continuous integration, and continuous delivery.
    - **CI/CD (Continuous Integration/Continuous Delivery)**:
      - The D in CD can also be referred to as Deployment or Development.
      - Code rollouts may happen many times per day, with that we need to rely on much more automation
      - Via integrating code repositories, deployment, infrastructure changes, software configuration management
      - Also via moving code between development, testing, production environments, …
      - Continuous Integration - build , test, merge
      - Continuous Delivery - automatic release to repository then triggered continuous Deployment  - automatic deploy to production

-   **DevSecOps**
    - Evolved from DevOps to add security into the process.
    - We want security to beintegrated throughout the development process.
    - Security is not just added on later as an afterthought, it is designed in. 

-   **domain 8 - video 50- Scaled Agile Frameworks - (SAFe)**
-   **Scaled Agile Frameworks - SAFe** 
????
    - Integrating Security Practices into SAFe: 
      - Built-in Quality: Security designed and integrated into the system from the beginning.
      - CI/CD Pipeline: Continuous security testing to identify and remediate issues early.
      - Threat Modeling: Identifying and prioritizing potential security risks and designing appropriate mitigation strategies.
      - Security Champions: Designated team members responsible for advocating security best practices.
      - Security Working Group: Coordinating security efforts across the entire ART at the program level.
      - Portfolio Level Security: Ensuring security considerations are factored into strategic decisions and risk management processes.
    - DevSecOps in SAFe:
      - Combining operations, development, and security.
      - Security configurations and policies defined and managed as code.
      - Continuous monitoring for security events and abnormalities.
      - Developer training in secure coding practices.
      - Security services (e.g., penetration testing, vulnerability scanning, threat intelligence) provided as shared services.
    - Implementing SAFe and Integrating Security Practices:
      - May require a technical and cultural shift.
      - Start with a small pilot project or a single ART and continuously learn and adapt.
      - Requires investment in training and coaching for senior leadership and teams.
      - Teams need resources, tools, and infrastructure for development, automation, monitoring, and rapid feedback loops.


- 8.1.1 Development methodologies (e.g., Agile, Waterfall, DevOps, DevSecOps, Scaled Agile Framework)
  - **Agile methodology**: a project management approach to development that involves breaking the project into phases and emphasizes continuous collaboration and improvement; teams follow a cycle of planning, executing, and evaluating; focus is on iterative development and frequent feedback, collab between small self-organizing cross-functional teams; in a very simplified sense, you can say agile is waterfall done in sprints
    - Agile development emphasizes:
      - the delivery of working software in short iterations, helping to get the software to market faster
      - reduced risk by frequently testing and providing feedback, helping to identify and resolve issues earlier in the development process
    - Agile was started by 17 pioneers in 2001, producing the "Manifesto for Agile Software Development" ([agilemanifesto.org](https://agilemanifesto.org)) that lays out the core philosophy of the Agile approach:
      - **individuals and interactions** over processes and tools
      - **working software** over comprehensive documentation
      - **customer collaboration** over contract negotiation
      - **responding to change** over following a plan
    - Agile Manifesto also defines 12 principles:
      - the highest priority is to satisfy the customer through early and continuous delivery of valuable software
      - welcome changing requirements, even late in development; Agile processes harness change for the customer’s competitive advantage
      - deliver working software frequently, from a couple of weeks to a couple of months, with a preference for the shorter timescale
      - business people and developers must work together daily throughout the project
      - build projects around motivated individuals; give them the environment, support, and tools and trust them to build
      - emphasizing face-to-face conversation
      - working software is the primary measure of progress
      - agile processes promote sustainable development; the them should be able to maintain a constant pace indefinitely
      - continuous attention to technical excellence and good design enhances agility
      - simplicity, or the art of maximizing the amount of work not done, is essential
      - the best architectures, requirements, and designs emerge from self-organizing teams
      - at regular intervals, the team reviews their effective and adjusts for improvement
    - Several methodologies have emerged that take these Agile principles and define specific processes around them:
      - **Scrum**: a management framework that teams use to self-organize and work towards a common goal; it describes a set of meetings, tools, and roles for efficient project delivery, allowing teams to self-manage, learn from experience, and adapt to change; named from the daily team meetings, called scrums; development focuses on short sprints that deliver finished products; integrated product teams (IPTs) were an early effort of this approach
      - **Kanban**: a visual system used to manage and keep track of work as it moves through a process; the word kanban is Japanese for "card you can see"; Kanban teams focus on reducing the time a project (or user story) takes from start to finish, using a kanban board and continuously improving their flow of work
      - **Rapid Application Development (RAD)**: an agile software development approach that focuses more on ongoing software projects and user feedback and less on following a strict plan, emphasizing rapid prototyping over planning; RAD uses four phases: requirements planning, user design, construction, and cutover
      - **Rational Unified Process (RUP)**: an agile software development methodology that splits the project life cycle into four phases:
        - inception: which defines the scope of the project and develop business case
        - elaboration: Plan project, specify features, and baseline the architecture
        - construction: Building the product
        - transition: providing the product to its users
        - during each of the phases, all six core development disciplines take place: business modeling, requirements, analysis and design, implementation, testing, and deployment
      - **Agile Unified Process (AUP)**: a simplified version of the rational unified process, it describes a simple, easy to understand approach to developing business application software using agile techniques and concepts yet still remaining true to the RUP
      - **Dynamic Systems Development Model (DSDM)**: an agile project delivery framework, initially used as a software development method; key principles:
        - focus on the business need: DSDM teams establish a valid business case and ensure organizational support throughout the project
        - deliver on time: work should be time-boxed and predictable, to build confidence in the development team
      - **Extreme Programming (XP)**: an Agile project management methodology that targets speed and simplicity with short development cycles, [using five guiding values, and five rules](http://www.extremeprogramming.org); the goal of the rigid structure, focused sprints and continuous integrations is higher quality product
      - **Scaled Agile Framework® (SAFe)**: a set of org and workflow patterns for implementing agile practices at an enterprise scale; the framework is a body of knowledge that includes structured guidance on roles and responsibilities, how to plan and manage the work, and values to uphold
  - **Scaled Agile Framework**: agile methodology applied to large orgs; allows large organizations with multiple teams to coordinate, collaborate, and deliver products
  - **Waterfall**:
    - A linear approach to development, where each phase needs to be completed fully before the next one begins (e.g. water only flows downhill or in one direction); developed by Winston Royce in 1970, the waterfall model uses a linear sequential life-cycle approach; all project requirements are gathered up front, and there is no formal way to integrate changes as more information becomes available
    - Traditional model has 7 stages, as each stage is completed, the project moves into the next phase; the iterative waterfall model does allow development to return to the previous phase to correct defects
      - System requirements
      - Software requirements
      - Preliminary design
      - Detailed design
      - Code and debug
      - Testing
      - Operations and maintenance
    - A major criticism of this model is that it's very rigid, and not ideal for most complex projects which often contain many variables that affect the scope throughout the project's lifecycle
  - **Spiral model**: improved waterfall dev process providing for a cycle of Plan, Do, Check, Act (PDCA) sub-stages at each phase of the SDLC; a risk-driven development process that follows an iterative model while also including waterfall elements
    - following defined phases to completion and then repeats the process, resembling a spiral
    - the spiral model provides a solution to the major criticism of the waterfall model in that it allows devs to return to planning stages as technical demands and customer requirements iterate
  - **DevOps (Development and Operations)**: an approach to software development, quality assurance, and technology operations that unites siloed staff, and bring the three functions together in a single operational model; DevOps goal is to shorten the systems development lifecycle and provide continuous delivery
    - closely aligned with lean and the Agile development approach, DevOps aims to dramatically decrease the time required to develop, test, and deploy software changes
    - using the DevOps model, and continuous integration/continuous delivery (CI/CD), orgs strive to roll out code dozens or even hundreds of times per day
    - this requires a high degree of automation, including integrating code repositories, the software configuration management process, and the movement of code between development, testing and production environments
    - the tight integration of development and operations also calls for the simultaneous integration of security controls
    - security must be tightly integrated and move with the same agility
  - **DevSecOps**: refers to the integration of development, security, and operations; extends DevOps by integrating security practices
    - provides for a merger of phased review (as in the waterfall SDLC) with the DevOps method, to incorporate the needs for security, safety, resilience or other emerging properties in the final system, at each turn of the cycle of development
    - DevSecOps supports the concept of software-defined security, where security controls are actively managed into the CI/CD pipeline

- 8.1.2 Maturity models (e.g., Capability Maturity Model (CMM), Software Assurance Maturity Model (SAMM))
  - Maturity models help software organizations improve the maturity and quality of their software processes by implementing an evolutionary path from ad hoc, chaotic processes to mature, disciplined processes
  - NOTE: be able to describe the SW-CMM, IDEAL, and SAMM models
  - Software Engineering Institute (SEI) (Carnegie Mellon University) created the Capability Maturity Model for Software (AKA Software Capability Maturity Model, abbreviated SW-CMM, CMM, or SCMM)
    - **SW-CMM**: a management process to foster the ongoing and continuous improvement of an org's processes and workflows for developing, maintaining and using software
    - all software development moves through a set of maturity phases in sequential fashion, and CMM describes the principles and practices underlying software process maturity, intended to help improve the maturity and quality of software processes
    - note that CMM doesn't explicitly address security
    - stages of the CMM:
      - **Level 1: Initial**: process is disorganized; usually little or no defined software development process
        - no KPIs
        - processes are ad-hoc, and immature
        - no basis for predicting project quality, time to completion etc
        - limited project management
        - limited software dev tools or automation
        - highly dependent on individual's skills and knowledge
      - **Level 2: Repeatable**: in this phase, basic lifecycle management processes are introduced
        - focus on establishing basic project management policies
        - project planning
        - configuration management
        - requirements management
        - sub-contract management
        - software quality assurance
      - **Level 3: Defined**: in this phase, software devs operate according to a set of formal, documented software development processes; marked by the presence of basic lifecycle management processes and reuse of code; includes the use of requirements management, software project planning, quality assurance, and configuration management
        - documentation of standard guidelines and procedures takes place
        - peer reviews
        - intergroup coordination
        - org process definition
        - org process focus
        - training programs
      - **Level 4: Managed**: in this phase, there is better management of the software process; characterized by the use of quantitative software development measures
        - quantitative goals are set for software products and process
        - software quality management
        - quantitative management
      - **Level 5: Optimizing**: in this phase continuous improvement occurs
        - process change management
        - technology change management
        - defect prevention
  - **Software Assurance Maturity Model (SAMM)**: an open source project maintained by the Open Web Application Security Project (OWASP)
    - provides a framework for integrating security into the software development and maintenance processes and provides orgs with the ability to assess their maturity
    - SAMM associates software development with 5 business functions:
      - Governance: the activities needed to manage software development processes
        - this function includes practices for:
          - strategy
          - metrics
          - policy
          - compliance
          - education
          - guidance
      - Design: process used to define software requirements and develop software
        - this function includes practices for:
          - threat modeling
          - threat assessment
          - security requirements
          - security architecture
      - Implementation: process of building and deploying software components and managing flaws
        - this function includes:
          - secure build
          - secure deployment
          - defect management practices
      - Verification: activities undertaken to confirm code meets business and security requirements
        - this function includes:
          - architecture assessment
          - requirements-driven testing
          - security testing
      - Operations: actions taken to maintain security throughout the software lifecycle after code is released
        - function includes:
          - incident management
          - environment management
          - operational management
  - **IDEAL Model**: developed by SEI, a model for software development that uses many of the SW-CMM attributes, using 5 phases:
    - Initiating: business reasons for the change are outlined, support is built, and applicable infrastructure is allocated
    - Diagnosing: in this phase, engineers analyze the current state of the org and make general recommendations for change
    - Establishing: development of a specific plan of action based on the diagnosing phase recommendations
    - Acting: in this phase, the org develops solutions and then tests, refines, and implements them
    - Learning: continuously analyze efforts to achieve these goals, and propose new actions as required

  - IDEAL vs SW-CMM:

    | IDEAL | SW-CMM |
    |----------------|---------------|
    | Initiating|Initial|
    | Diagnosing  | Repeatable|
    | Establishing | Defined|
    | Acting  | Managed|
    | Learning| Optimizing|

- 8.1.3 Operations and maintenance
  - Once delivered to the production environment, software devs must make any additional changes to accommodate unexpected bugs, vulnerabilities, or interoperability issues
  - They must also keep pace with changing business processes, and work closely with the operations team (typically IT), to ensure reliable operations
    - together, ops and development transition a new system to production and management of the system's config
  - The dev team must continually provide hotfixes, patches, and new releases to address discovered security issues and identified coding errors

- 8.1.4 Change management
  - Change management (AKA control management) plays an important role when monitoring systems in a controlled environment, and has 3 basic components:
    - **Request Control**: process that provides an organized framework within which users can request modifications, managers can conduct cost/benefit analysis, and developers can prioritize tasks
    - **Change Control**: the process of controlling specific changes that need to take place during the life cycle of a system, serving to document the necessary change-related activities; or the process of providing an organized framework within which multiple devs can create and test a solution prior to rolling it out in a production environment
      - where change management is the project manager’s responsibility for the overarching process, change control is what devs do to ensure the software or environment doesn’t break when changed
      - change control is basically the process used by devs to re-create a situation encountered by a user and analyze the appropriate changes; it provides a framework where multiple devs can create and test a solution prior to rolling it out into a prod environment
    - **Release Control**: once changes are finalized, they must be approved for release through the release control procedure
      - one of the responsibilities of release control is ensuring that the process includes acceptance testing, confirming that any alterations to end-user work tasks are understood and functional prior to code release

- 8.1.5 Integrated Product Team (IPT)
  - **Integrated Product Team (IPT)**: Introduced by the US Department of Defense (DoD) as an approach to bring together multifunctional teams with a single goal of delivering a product or developing a process or policy, and fostering parallel, rather than sequential, decisions
  - Essentially, IPT is used to ensure that all aspects of a product, process, or policy are considered during the development process

## [8.2](#82-identify-and-apply-security-controls-in-development-ecosystems-osg-10-chpts-152021) Identify and apply security controls in development ecosystems (OSG-10 Chpts 15,20,21)

- Applications, including custom systems, can present significant risks and vulnerabilities, and to protect against these it's important to introduce security controls into the entire system’s development lifecycle

- 8.2.1 Programming languages
  - Computers understand 1s and 0s (binary), and each CPU has its own (machine) language
  - **Assembly language**: a way of using mnemonics to represent the basic instruction set of a CPU
  - **Assemblers**: tools that convert assembly language source code into machine code
  - Third-generation programming languages, such as C/C++, Java, and Python, are known as high-level languages
    - high-level languages allow developers to write instructions that better approximate human communication
  - **Compiled language**: converts source code into machine-executable format
    - compiled code is generally less prone to manipulation by a third party, however easier to embed backdoors or other security flaws without detection
  - **Decompilers**: convert binary executable back into source code
  - **Disassemblers**: convert back into machine-readable assembly language (an intermediate step during the compilation process)
  - **Interpreted language**: uses an interpreter to execute; sourcecode is viewable; e.g. Python, R, JavaScript, VBScript
  - **Object-oriented programming (OOP)**: defines an object to be set of a software that offers one or more methods, internal to the object, that software external to that object can request to access; each method may require specific inputs and resources and may produce a specified set of outputs; focuses on the objects involved in an interaction
    - OOP languages include C++, Java, and .NET
    - think of OOP as a group of objects that can be requested to perform certain operations or exhibit certain behaviors, working together to provide a system’s functionality or capabilities
    - OOP has the potential to be more reliable and to reduce the propagation of program change errors, and is better suited to modeling or mimicking the real world
    - each object in the OOP model has methods that correspond to specific actions that can be taken on the object
    - objects can also be subclasses of other objects and inherit methods from their parent class; the subclasses can use all the methods of the parent class and have additional class-specific methods
    - from a security standpoint, object-oriented programming provides a black-box approach to abstraction
    - OOP terms:
      - **message**: a communication to or input of an object
      - **method**: internal code that defines the actions of an object
      - **behavior**: results or output exhibited by an object
        - behaviors are the results of a message being processed through a method
      - **class**: a collection of the common methods, from a set of objects that defines the behavior of those objects
      - **instance**: objects are instances of or examples of classes that contain their methods
      - **inheritance**: occurs when the methods from a class (parent or superclass) are inherited by another subclass (child) or object
      - **delegation**: the forwarding of a request by an object to another object or delegate
      - **polymorphism**: the characteristic of an object that allows it to respond with different behaviors to the same message or method because of changes in external conditions
      - **cohesion**: describes the strength of the relationship between the purposes of the methods within the same class
        - if all methods have similar purposes, there is high cohesion, and a sign of good design
      - **coupling**: the level of interaction between objects
        - lower coupling: means less interaction
        - lower coupling provides better software design because objects are more independent, and code is easier to troubleshoot and update

- 8.2.2 Libraries
  - **Software library**: a pre-written collection of components (classes, procedures, scripts etc) that do specific tasks, useful to other components (e.g. software libraries for encryption algorithms, managing network connections, or displaying graphics)
  - Shared software libraries contain reusable code, improving developer's efficiency, and reducing the need to write well-known algorithms from scratch; often available as open source
    - shared libraries can also include many security issues (e.g. Heartbleed), and devs should be aware of the origins of the shared code that they use, and keep informed about any security vulns that might be discovered in these libraries

- 8.2.3 Tool sets
  - Forcing all devs to use the same toolset can reduce productivity and job satisfaction; however letting every dev choose their own tools and environment widens an organization's attack surface
    - a better approach is to use a change advisory board to validate developer tool requirements, assess associated risks; if approved, the sec team monitors controls
  - Developers use a variety of tools, and one of the most important is the IDE (defined below)

- 8.2.4 Integrated Development Environment
  - **Integrated Development Environment (IDE)**: software applications, their control procedures, supporting databases, libraries and toolsets that provide a programmer or team what they need to specify, code, compile, test, and integrate code; IDEs provide developers with a single environment where they can write their code, test and debug, and compile it

- 8.2.5 Runtime
  - **RunTime Environments (RTE)**: allows the portable execution of code across different operating systems or platforms without recompiling (e.g. Java Virtual Manager (JVM))
    - this is known as portable code, which needs translation between each environment, the role of the RTE

- 8.2.6 Continuous Integration and Continuous Delivery (CI/CD)
  - **Continuous Integration and Continuous Delivery**: workflow automation processes and tools that attempt to reduce, if not eliminate, the need for manual communication and coordination between the steps of a software development process
  - **Continuous integration (CI)**: all new code is integrated into the rest of the system as soon as the developer writes it, merging it into a shared repo
    - this merge triggers a batch of unit tests
    - if it merges without error, it's subjected to integration tests
    - CI improves software development efficiency by identifying errors early and often
    - CI also allows the practice of continuous delivery (CD)
  - **Continuous Delivery (CD)**: incrementally building a software product that can be released at any time; because all processes and tests are automated, code can be released to production daily or more often
  - CI/CD relies on automation and often third-party tools which can have vulnerabilities or be compromised
  - Secure practices such as threat modeling, least privilege, defense in depth, and zero trust can help reduce possible threats to these tools and systems

- 8.2.7 Software Configuration Management
  - **Software Configuration Management (SCM)**: a product that identifies the attributes of software at various points in time and performs methodical change control for the purpose of maintaining software integrity and traceability throughout the SDLC
    - SCM tracks config changes, and verifies that the delivered software includes all approved changes
    - SCM systems manage and track revisions made by multiple people against a single master software repository, providing concurrency management, versioning, and synchronization
    - auditing and logging of software changes mitigates risk to the organization by:
      - providing a detailed record of all modifications made to software applications
      - allowing security teams to identify suspicious activity
      - quickly detect unauthorized changes and investigate potential security breaches
      - and take corrective actions, ultimately protecting the integrity and confidentiality of the org's data and systems

- 8.2.8 Code repositories
  - Software development is a collaborative effort, and larger projects require teams of devs working simultaneously on different parts
  - Code repositories support collaborations, acting as a central storage point for source code
    - github, bitbucket, and sourceforge are examples of systems that provide version control, bug tracking, web hosting, release management, and communications functionality

- 8.2.9 Application security testing (e.g., static application security testing (SAST), dynamic application security testing (DAST), software composition analysis, Interactive Application Security Test (IAST))
  - **Static Application Security Testing (SAST)**: AKA static analysis, tools and technique to help identify software defects (e.g. data type errors, loop/structure bounds violations, unreachable code) or security policy violations and is carried out by examining the code without executing the program (or before the program is compiled)
    - the term SAST is generally reserved for automated tools that assist analysts and developers, whereas manual inspection by humans is generally referred to as code review
    - SAST allows devs to scan source code for flaws and vulns; it also provides a scalable method of security code review and ensuring that devs are following secure coding policies
  - **Dynamic Application Security Testing (DAST)**: AKA dynamic analysis, is the evaluation of a program while running in real time
    - tools that execute the software unit, application or system under test, in ways that attempt to drive it to reveal a potentially exploitable vulnerability
    - DAST is usually performed once a program has cleared SAST and basic code flaws have been fixed
    - DAST enables devs to trace subtle logical errors that are likely to cause security problems, without the need to create artificial error-inducing scenarios
    - dynamic analysis is also effective for compatibility testing, detecting memory leakages, identifying dependencies, and analyzing software without accessing the software’s actual source code
  - **Interactive Application Security Testing (IAST)**: the combination of SAST and DAST such application testing is done on the running system (DAST), with access to source code (SAST)

## [8.3](#83-assess-the-effectiveness-of-software-security-osg-10-chpts-2021) Assess the effectiveness of software security (OSG-10 Chpts 20,21)

- 8.3.1 Auditing and logging of changes
  - Applications should be configured to log details of errors and other security events to a centralized log repository
  - The Open Web Application Security Project (OWASP) Secure Coding Practices suggest logging the following events:
    - input validation failures
    - authentication attempts, especially failures
    - access control failures
    - tampering attempts
    - use of invalid or expired session tokens
    - exceptions raised by the OS or applications
    - use of admin privileges
    - Transport Layer Security (TLS) failures
    - cryptographic errors

- 8.3.2 Risk analysis and mitigation
  - Risk management is at the center of secure software development, in particular regarding the mapping of identified risks and implemented controls
    - this is a difficult part of secure software dev, especially related to auditing
  - Threat modeling is important to dev teams, and particularly in DevSecOps
  - Assessors are also interested in the linkages between the software dev and risk management programs
    - software projects should be tracked in the org’s risk matrix, to ensure the dev team is connected to the broader risk management efforts, and not working in isolation

## [8.4](#84-assess-security-impact-of-acquired-software-osg-10-chpts-1620) Assess security impact of acquired software (OSG-10 Chpts 16,20)

- 8.4.1 Commercial-off-the-shelf (COTS)
  - **Commercial Off-the-Shelf (COTS)**: software elements, usually apps, that are provided as finished products (not intended for alteration by or for the end-user)
  - Most widely used commercial-off-the-shelf (COTS) software products have been security researcher (both benign and malicious) tested
    - researching discovered vulnerabilities and exploits can help us understand how seriously the vendor takes security
    - for niche products, you should research vendor certifications, such as ISO/IEC 27034 Application Security
    - other than secure coding certification, you can look for overall information security management system (ISMS) certifications such as ISO/IEC 27001 and FedRAMP (which are difficult to obtain, and show that the vendor is serious about security)
  - If you can talk with a vendor, look for processes like defensive programming, which is a software development best practice that means as code is developed or reviewed, they are constantly looking for opportunities for things to go badly
    - e.g. treating all input routines as untrusted until proven otherwise

- 8.4.2 Open source
  - Open source is typically released with licensing allowing code access and inspection so devs can look for security issues
    - typically, however, this means that there is no service or support that comes with the software and requires in-house support for configuration, and security testing
    - it also means that both open-source devs as well as adversaries are able to review the code for vulns
    - the greatest risk of open-source software is relying on outdated versions -- especially true of shared libraries
    - an org should develop processes to ensure that all open-source software is periodically updated, likely in a way that differs from the process for updating COTS

- 8.4.3 Third-party
  - **Third-party software**: (AKA outsourced software) is software made specifically for an org by a third party
    - third-party software is not considered COTS, since the software is custom or customized
    - third-party software may rely on open-source software, but since it's customized, it may have different or additional vulns
    - it's best practice to use a third-party to do an external audit and security assessment; this should be built into the vendor's contract, with passing the audit conditional for finalizing software purchase

- 8.4.4 Managed services (e.g., enterprise applications)
  - **Managed services**: can include services and assets that are available from on-premises resources (e.g. within the organization) or cloud-based; as organizations move more functionality to the cloud, they reap cloud-based conveniences (e.g. pay only for on-demand resource use, easy scalability etc.) but lose a degree of control since a portion of cloud-based resources are outside the org's control
  
- 8.4.5 Cloud services (e.g., Software as a Service (SaaS), Infrastructure as a Service (IaaS), Platform as a Service (PaaS))
  - As orgs continue to migrate to the cloud (SaaS, IaaS, PaaS), they should increase the security assessment of those services
  - The top reasons for cloud breaches continues to be misconfigurations, lack of visibility into access settings, and poor access controls
    - cloud service providers have tools to help mitigate these issues, and orgs should consider bringing in third-party experts to help if they don't have the internal expertise
  - **Anything as a Service (XaaS)**: catchall term referring to any type of computing service that provides value to customers via a cloud solution

## [8.5](#85-define-and-apply-secure-coding-guidelines-and-standards-osg-10-chpts-2021) Define and apply secure coding guidelines and standards (OSG-10 Chpts 20,21)

- **Secure Coding Guidelines and Standards**: best practices identified by a variety of software and security professionals, that when used correctly can dramatically reduce the number of exploitable vulnerabilities introduced during development

- 8.5.1 Security weaknesses and vulnerabilities at the source-code level
  - A source code vulnerability is a code defect providing a threat actor with an opportunity to compromise the security of a software system
    - source code vulns are caused by design or implementation flaws
    - **design flaw**: if dev did everything correctly, there would still be a vulnerability
    - **implementation flaw**: dev incorrectly implemented part of a good design
  - the OWASP top 10 vulnerabilities for 2024:
    - Broken access control
    - Cryptographic failures
    - Injection
    - Insecure design
    - Security misconfiguration
    - Vulnerable and outdated components
    - Identification and authentication failures
    - Software and data integrity failures
    - Security logging and monitoring failures
    - Server Side Request Forgery (SSRF)

- 8.5.2 Security of Application Programming Interfaces (APIs)
  - **Application Programming Interface (API)**: specifies the manner in which a software component interacts with other components
    - API's reduce the effort of providing secure component interactions by providing easy implementation for security controls
    - API's reduce code maintenance by encouraging software reuse, and keeping the location of changes in one place
    - **Parameter validation**: ensuring that any API parameter is checked against being malformed, invalid, or malicious helps ensure API secure use; validation confirms that the parameter values being received by an app are within defined limits before they are processed by the system

- 8.5.3 Security coding practices
  - Secure coding practices can be summarized as standards and guidelines
    - **standards**: mandatory activities, actions, or rules
    - **guidelines**: recommended actions or ops guidelines that provide flexibility for unforeseen circumstances
    - orgs greatly reduce source code vulns by enforcing secure coding standards and maintaining coding guidelines that reflect best practices
  - To be considered a standard, coding practice must meet the following:
    - reduces the risk of a particular type of vuln
    - enforceable across all of an org's software development efforts
    - verifiably implemented
  - Note: secure coding standards, rigorously applied, is the best way to reduce source code vulns; coding standards ensures devs always do certain things in a certain way, while avoiding others
  - Secure coding guidelines are recommended practices that tend to be less specific than standards
    - e.g. consistently formatted code comments, or keeping code functions short/tight

- 8.5.4 Software-defined security
  - **Software-defined security (SDS or SDSec)**: a security model in which security functions such as firewalling, IDS/IPS, and network segmentation are implemented in software within an SDN environment
    - one of the advantages of this approach is that sensors (for systems like IDS/IPS) can be dynamically repositioned depending on the threat
    - SDS provides a decoupling from physical devices, because it abstracts security functions into software that can run on any compatible physical or virtual infrastructure, critical for supporting cloud services dynamic scaling and virtualized data centers
  - DevSecOps supports the concept of software-defined security, where security controls are actively managed into the CI/CD pipeline
