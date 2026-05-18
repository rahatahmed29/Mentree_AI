# AI Project Rules

Project:
AI Smart Learning Roadmap & Accountability System

Goal:
Build a recruiter-impressive MVP 

Audience:
Absolute beginner developer.

Always optimize for:
- simplicity
- readability
- maintainability
- beginner understanding

--------------------------------------------------
GENERAL RULES
--------------------------------------------------

Use beginner-friendly code.

Explain generated code before or after implementation.

Define technical terms before using them.

Prefer readability over clever code.

Avoid unnecessary abstractions.

Avoid overly advanced patterns.

Keep files small and focused.

Add comments for important logic.

Do not generate huge files.

Generate one feature at a time.

Do not implement multiple systems in one request.

Follow clean code practices.

Use meaningful variable and function names.

Avoid duplicate code.

Always explain where generated files belong.

When modifying code:
Explain what changed and why.

--------------------------------------------------
FRONTEND RULES
--------------------------------------------------

Frontend Stack:

React
Vite
Axios
React Router
Tailwind CSS
Recharts

Use functional React components only.

Use React Hooks only.

Avoid class components.

Keep components small.

One component = one responsibility.

Create reusable UI components.

Separate:

pages/
components/
services/
hooks/
context/
utils/

Use Axios for API calls.

Do not call APIs directly inside UI components if avoidable.

Create service files:

authService.js
roadmapService.js
taskService.js

Use React Context for authentication.

Use protected routes.

Add loading states.

Add error handling.

Show user-friendly messages.

Prefer clean responsive layouts.

Avoid unnecessary animation libraries.

Use charts only with Recharts.

--------------------------------------------------
BACKEND RULES
--------------------------------------------------

Backend Stack:

FastAPI
SQLAlchemy ORM
PostgreSQL

Use MVC/service structure.

Separate:

models/
schemas/
routes/
services/
database/
utils/

Do not place all code in main.py

Keep business logic inside services.

Keep routes thin.

Use SQLAlchemy ORM.

Use PostgreSQL.

Use environment variables.

Never hardcode secrets.

Use JWT authentication.

Hash passwords.

Create Pydantic schemas.

Use dependency injection when needed.

Explain API flow.

Comment difficult logic.

--------------------------------------------------
DATABASE RULES
--------------------------------------------------

Use proper relationships.

Use foreign keys.

Explain One-to-Many relationships.

Avoid duplicate tables.

Use created_at fields.

Use clear naming.

Table names:

users
roadmaps
tasks
progress
streaks

--------------------------------------------------
AI INTEGRATION RULES
--------------------------------------------------

Do NOT integrate OpenAI immediately.

First generate mock data.

Example:

Week1:
Task1
Task2

Only after APIs work:
Integrate AI.

Explain prompt structure.

Explain request and response flow.

Validate AI responses before saving.

--------------------------------------------------
PROJECT WORKFLOW RULES
--------------------------------------------------

Build in this order:

1. Database
2. Models
3. Authentication
4. Roadmaps
5. Tasks
6. Dashboard
7. Streaks
8. AI integration
9. Deployment

Never skip steps.

Commit after milestones.

Suggested commit format:

feat:
fix:
refactor:

--------------------------------------------------
WHEN GENERATING CODE
--------------------------------------------------

After generating code:

1. Explain purpose
2. Explain file location
3. Explain flow
4. Explain beginner mistakes