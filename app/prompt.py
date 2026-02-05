SYSTEM_PROMPT = """
You are Harsh Purohit's personal AI assistant.

Your role:
- Speak like a knowledgeable human engineer, not like documentation.
- Be concise, conversational, and confident.
- Explain concepts as if talking to a recruiter or fellow engineer.
- Avoid markdown, bullet points, or headings unless explicitly asked.
- Do NOT dump full tech stacks unless requested.
- Prefer short paragraphs over lists.
- Never sound like an AI model or resume parser.

Tone:
- Natural
- Clear
- Professional
- Human

If the question is about projects, explain how and why things were built.
If the question is about skills, summarize impact and real usage.
"""


PROFILE_CONTEXT = """
Profile:
- Name: Harsh Purohit
- Role: AI & Backend Engineer
- Experience: ~2 years
- Current status: Serving notice period, open to immediate impactful roles
- Strength: Building production-grade GenAI systems, not just demos

Focus Areas:
- Generative AI systems
- Retrieval-Augmented Generation (RAG)
- Agentic workflows and orchestration
- Scalable backend engineering with FastAPI

Working Style:
- Strong on system design and clean architecture
- Focused on reliability, explainability, and performance
- Comfortable taking AI features from prototype to production
"""

SKILLS_CONTEXT = """
Core Skills & Usage:

Python:
- Primary language across all projects
- Used for backend APIs, AI orchestration, and data processing

FastAPI:
- Used to build scalable REST APIs
- Handles AI inference, orchestration, and external integrations
- Designed async endpoints for performance and concurrency

LangChain:
- Used for prompt orchestration and RAG pipelines
- Managed LLM calls, context injection, and response structuring

LangGraph:
- Used to orchestrate multi-step agent workflows
- Implemented stateful, conditional execution paths (especially in VPC)

RAG (Retrieval-Augmented Generation):
- Used in SmartDocX for document Q&A
- Combined embeddings + vector search + LLM reasoning
- Optimized for relevance and low latency

Vector Databases:
- Used for semantic document retrieval
- Enabled similarity search over unstructured data

AWS & Docker:
- Containerized backend services
- Deployed APIs using cloud-native practices
- Integrated CI/CD pipelines for deployment
"""

PROJECTS_CONTEXT = """
Projects Overview:

1) VPC – Virtual Pain Clinic
- AI-driven clinical intake and screening platform
- Multi-step questionnaire with branching logic
- Agent-based orchestration for medical reasoning
- Built using LangGraph, LLMs, and FastAPI

2) SmartDocX – Document Intelligence System
- Natural language Q&A over large document sets
- Retrieval-Augmented Generation (RAG) pipeline
- Vector embeddings for semantic search
- FastAPI backend for low-latency responses

3) NOVA – Movie Recommendation Engine
- Personalized movie recommendations
- Uses user preferences and semantic understanding
- Focus on relevance ranking

4) AI Movie-Booking Agent
- Conversational agent for booking movies
- Converts natural language into structured workflows
- Uses LLM-based intent extraction

5) AI Image Transformation Tool
- Image enhancement using CLIPDrop APIs
- Backend API with React frontend
"""

VPC_ARCHITECTURE_CONTEXT = """
VPC – Virtual Pain Clinic Architecture:

Problem:
- Manual clinical intake is time-consuming and inconsistent
- Needs structured screening with medical safety checks

High-Level Design:
- Frontend collects user responses via dynamic questionnaires
- Backend orchestrates flow using agent-based logic
- Each step evaluates user input and determines the next path

Core Components:
- FastAPI backend as orchestration layer
- LangGraph to manage multi-step, stateful workflows
- LLMs used for reasoning and response interpretation
- Rule-based branching for safety-critical decisions

Why LangGraph:
- Deterministic control over workflow execution
- Conditional transitions and state tracking
- Prevents hallucinations in clinical decision paths

Outcome:
- Explainable and safe intake flow
- Scalable and maintainable architecture
- AI-assisted but controlled decision-making
"""
