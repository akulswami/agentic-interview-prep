# Agentic Interview Prep

An AI-assisted interview preparation platform and structured knowledge base for Embedded Systems, Linux, Edge AI, DSA, system design, and behavioral interviews.

This repository is being developed as both:

1. A practical system for improving technical interview performance
2. A portfolio project demonstrating applied agentic AI engineering

The project is currently in its initial development phase. The knowledge-management structure is being established first, followed by retrieval, evaluation, mock-interview, and progress-tracking capabilities.

## Objectives

The platform is intended to support:

- Structured interview-preparation notes
- Retrieval-augmented generation over technical content
- Interactive mock interviews
- Response evaluation using explicit rubrics
- Weakness and mistake identification
- Progress tracking
- Spaced review
- Design-review workflows
- Behavioral STAR story coaching

The system is not intended to replace actual interview preparation. AI tooling must remain subordinate to deliberate technical practice.

## Current Status

**Phase: Repository and knowledge-base initialization**

Currently available:

- Public repository structure
- Domain-specific knowledge directories
- Initial DSA preparation structure
- Space for evaluation datasets and reports
- Architecture and experiment documentation directories
- Separation between public content and local private data

Not yet implemented:

- Document ingestion pipeline
- Embedding generation
- Vector retrieval
- Mock-interview agent
- Automated response evaluation
- Weakness analytics
- Spaced-repetition scheduler
- LangGraph orchestration
- Model-provider integrations

See the project roadmap for planned development.

## Repository Structure

\`\`\`text
agentic-interview-prep/
├── knowledge/
│   ├── dsa/
│   ├── embedded/
│   ├── linux/
│   ├── linux-kernel/
│   ├── system-design/
│   └── behavioral/
│
├── src/
│   └── interview_prep_ai/
│
├── evals/
│   ├── datasets/
│   └── reports/
│
├── tests/
├── configs/
├── scripts/
│
├── docs/
│   ├── architecture/
│   ├── decisions/
│   └── experiments/
│
└── private/
\`\`\`

The \`private/\` directory is excluded from version control and is intended for sensitive or personally identifiable preparation material.

## Knowledge Domains

### DSA

The DSA knowledge base contains:

- Learning roadmap
- Algorithm-pattern notes
- Individual problem records
- Mistake analysis
- Review tracking
- Confidence and mastery metadata

DSA content is stored under:

\`\`\`text
knowledge/dsa/
\`\`\`

### Embedded Systems

Planned content includes:

- Embedded C and C++
- Memory layout and pointers
- Interrupts and DMA
- UART, SPI, I2C, and CAN
- RTOS concepts
- Concurrency and synchronization
- Bootloaders
- Watchdogs
- Power management
- Firmware debugging

### Linux and Linux Kernel

Planned content includes:

- Processes and threads
- Scheduling
- Virtual memory
- Synchronization
- IPC
- Networking
- Interrupt handling
- Bottom halves
- Device drivers
- Device Tree
- DMA-BUF and buffer sharing
- Kernel debugging

### System Design

Planned content includes:

- Embedded platform architecture
- Edge AI systems
- Telemetry
- OTA updates
- Reliability
- Fault tolerance
- Safety mechanisms
- Diagnostics
- Distributed embedded systems

### Behavioral Interviews

Planned content includes:

- STAR story bank
- Leadership examples
- Conflict resolution
- Technical disagreements
- Project ownership
- Failures and lessons learned
- Influence without authority
- Stakeholder management

Sensitive personal stories should remain in the ignored \`private/\` directory unless they are explicitly sanitized for publication.

## Planned AI Architecture

The initial architecture will focus on four capabilities.

### Knowledge Retrieval

- Parse Markdown documents
- Preserve document metadata
- Generate embeddings
- Retrieve relevant passages
- Return source-grounded responses with citations
- Detect insufficient evidence

### Interview Session Engine

- Select questions by domain and difficulty
- Ask adaptive follow-up questions
- Maintain session state
- Avoid revealing answers prematurely
- Produce structured interview summaries

### Response Evaluation

- Evaluate factual correctness
- Assess reasoning quality
- Identify omissions and misconceptions
- Evaluate communication clarity
- Apply domain-specific rubrics
- Produce actionable feedback

### Learning Tracker

- Record attempts
- Track recurring mistakes
- Estimate topic confidence
- Schedule reviews
- Generate progress summaries

Deterministic code will remain authoritative for persistent state, scheduling, scoring calculations, and analytics. LLMs will be used only where language reasoning provides clear value.

## Development Principles

1. **Interview preparation comes first**

   AI development must directly support preparation rather than compete with it.

2. **Build the smallest useful system**

   Features should be introduced only after a concrete preparation need is established.

3. **Do not call every component an agent**

   Retrieval services, evaluators, schedulers, and deterministic utilities should be described accurately.

4. **Use explicit evaluation**

   Retrieval quality, groundedness, scoring consistency, latency, and cost should be measured.

5. **Preserve human control**

   The learner should approve conclusions, weakness classifications, and public knowledge-base content.

6. **Keep public and private data separate**

   Employer-confidential, personally sensitive, and proprietary material must never be committed.

7. **Prefer reproducibility over demos**

   Architecture decisions, experiments, failures, and evaluation results should be documented.

## Six-Month Roadmap

### Phase 1 — Knowledge Base and Baseline Retrieval

- Define Markdown schemas
- Add structured technical notes
- Implement document ingestion
- Implement chunking and metadata extraction
- Generate embeddings
- Add local vector retrieval
- Build a retrieval evaluation dataset

### Phase 2 — Mock Interview Workflow

- Add interview-session state
- Implement question selection
- Add adaptive follow-ups
- Store structured transcripts
- Introduce domain-specific rubrics

### Phase 3 — Weakness and Progress Tracking

- Define attempt records
- Build topic-level analytics
- Track recurring mistakes
- Add review scheduling
- Generate weekly progress reports

### Phase 4 — Agentic Orchestration

- Model workflows as explicit state machines
- Add tool interfaces
- Introduce retry and failure handling
- Add human approval points
- Evaluate LangGraph where justified

### Phase 5 — Evaluation and Reliability

- Measure retrieval quality
- Evaluate answer groundedness
- Test rubric consistency
- Add prompt-regression tests
- Track cost and latency
- Create a failure taxonomy

### Phase 6 — Portfolio Hardening

- Finalize architecture documentation
- Publish benchmark results
- Add reproducible demos
- Document design tradeoffs
- Improve installation and usage instructions
- Produce a portfolio-ready project walkthrough

## Intended Technology Areas

Technologies will be introduced incrementally based on actual requirements.

Potential areas include:

- Python
- OpenAI and Anthropic APIs
- Embedding models
- Vector databases
- Retrieval-augmented generation
- Structured LLM outputs
- Tool calling
- LangGraph
- Model Context Protocol
- Evaluation frameworks
- Prompt and workflow testing
- Memory and state-management systems

The repository will not adopt a technology merely to increase the number of tools listed in the stack.

## Evaluation Strategy

The project will evaluate more than whether an LLM response appears plausible.

Planned evaluation areas include:

- Retrieval Recall@K
- Retrieval precision
- Citation correctness
- Answer groundedness
- Unsupported-claim rate
- Interview-rubric consistency
- Weakness-classification accuracy
- Prompt-regression behavior
- Cost per interview session
- End-to-end latency

Human-reviewed datasets will be used where automated evaluation is insufficient.

## Privacy and Publication Rules

Do not commit:

- API keys or credentials
- Employer-confidential information
- Proprietary code or architecture
- Confidential interview questions
- Immigration or legal documents
- Personally identifiable information
- Unredacted behavioral stories
- Raw private interview transcripts
- Paid or copyrighted solution material

Use environment variables for secrets and the ignored \`private/\` directory for sensitive preparation data.

## Project Constraints

The project follows a preparation-to-tooling ratio of approximately:

\`\`\`text
4 hours of interview preparation
for every
1 hour of AI tooling
\`\`\`

A proposed feature should be rejected or deferred unless it solves a real preparation problem, has measurable value, and can be implemented without disrupting the primary interview-preparation plan.

## License

This project is licensed under the MIT License.

## Disclaimer

This repository is an independent learning and portfolio project. It is not affiliated with any employer, interview platform, model provider, or educational service.
