# Mentree AI — Product Requirements Document (Revised)

## Vision
Help users turn any learning goal into a structured plan — and actually complete it
through AI planning, daily tasks, and accountability.

## Problem
- No clear learning roadmap for self-learners
- Poor consistency and execution
- Lack of accountability and progress visibility

## Solution
An AI-powered platform that generates personalized learning roadmaps, breaks them
into daily tasks, and keeps users on track through streaks and a progress dashboard.

## Target Users
- Developers, AI/ML Engineers, Data Scientists
- Self-learners in any technical field

---

## MVP Scope (Build This First)

### 1. Authentication
- User registration and login
- JWT-based authentication (access token + session token)
- Secure password hashing with bcrypt
- Protected routes on both frontend and backend
- role-based access (admin)

> Refresh tokens and role-based access (admin) are deferred.
> They add complexity without adding MVP value.

---

### 2. Roadmap Generator
Onboarding quiz collects:
- Topic (e.g., "Machine Learning")
- Duration (e.g., 4 weeks)
- Daily available time (e.g., 1.5 hours)
- Preferred study time (morning / afternoon / night)
- Level (beginner / intermediate)
- Content preference (videos / reading)
- Learning approach (theory-first / project-first)

AI (or mock AI in early development) generates:
- A structured weekly and daily task plan
- Industry-relevant skills for the chosen field

Free tier: 1 roadmap
Pro tier: unlimited roadmaps (gated by `is_pro` flag in DB — billing built later)

---

### 3. Daily Task System
- View today's tasks as a checklist
- Mark tasks as complete or incomplete
- Each task has: title, description, estimated duration, scheduled date

---

### 4. Streak Tracking
- Completing all daily tasks increases the streak by 1
- Missing a day resets the streak
- Freeze count stored (freeze logic can be added later without schema change)
- Show current streak and longest streak

---

### 5. Progress Dashboard
- Daily completion percentage
- Weekly completion percentage
- List of missed tasks for the current week
- Simple bar/line chart using Recharts
- Motivational message based on weekly percentage

---

## Deferred Features (Post-MVP)

| Feature | Reason Deferred |
|---|---|
| Google Calendar integration | Requires OAuth2 + Google Cloud setup. High complexity for MVP. |
| Browser push notifications | Requires service worker + HTTPS + Web Push API. Replace with in-app alerts for now. |
| Billing / bKash payment | Payment gateway is a separate project. `is_pro` flag in DB is enough to gate features. |
| Admin role & access control | No admin features defined yet. Don't build infrastructure for unused features. |
| Weekly reschedule notification | Reschedule + calendar sync is complex. Show missed tasks on dashboard instead. |
| Refresh tokens | Adds session management complexity. Single access token is fine for MVP. |
| AI improvement suggestions (Pro) | Core AI roadmap generation is enough. Suggestions layer added post-MVP. |

---

## Build Order

```
Phase 1 — Foundation
  1. Database schema + SQLAlchemy models
  2. Auth API (register, login, get current user)
  3. React shell (routing, auth context, protected routes)

Phase 2 — Core Feature
  4. Roadmap onboarding quiz (frontend form)
  5. Mock AI roadmap generation (backend returns hardcoded structure)
  6. Task system (list tasks, mark complete)

Phase 3 — Tracking
  7. Streak logic (calculate on task completion)
  8. Progress calculation (daily %, weekly %)
  9. Dashboard page (charts + missed tasks)

Phase 4 — Real AI
  10. Replace mock with OpenAI / Gemini API call
  11. Validate and save AI response properly

Phase 5 — Post-MVP Enhancements
  12. In-app notifications
  13. Google Calendar integration
  14. Billing and Pro tier
```

---

## Database Entities

### users
| Column | Type | Notes |
|---|---|---|
| id | UUID / int | Primary key |
| name | string | |
| email | string | Unique |
| password_hash | string | bcrypt hashed |
| is_pro | boolean | Default false. Gates pro features. |
| created_at | datetime | |

### roadmaps
| Column | Type | Notes |
|---|---|---|
| id | int | Primary key |
| user_id | int | FK → users |
| title | string | e.g. "ML Roadmap" |
| topic | string | |
| duration_weeks | int | |
| daily_hours | float | |
| preferred_time | string | morning/afternoon/night |
| level | string | beginner/intermediate |
| content_preference | string | videos/reading |
| approach | string | theory-first/project-first |
| status | string | active / completed |
| created_at | datetime | |

### tasks
| Column | Type | Notes |
|---|---|---|
| id | int | Primary key |
| roadmap_id | int | FK → roadmaps |
| user_id | int | FK → users |
| title | string | |
| description | text | |
| week_number | int | |
| day_number | int | |
| scheduled_date | date | |
| estimated_duration | int | minutes |
| is_completed | boolean | Default false |
| completed_at | datetime | Nullable |
| created_at | datetime | |

### streaks
| Column | Type | Notes |
|---|---|---|
| id | int | Primary key |
| user_id | int | FK → users, unique |
| current_streak | int | Default 0 |
| longest_streak | int | Default 0 |
| last_active_date | date | Last day tasks were completed |
| freeze_count | int | Default 0. Reserved for later. |
| updated_at | datetime | |

### progress
| Column | Type | Notes |
|---|---|---|
| id | int | Primary key |
| user_id | int | FK → users |
| roadmap_id | int | FK → roadmaps |
| date | date | One row per user per day |
| tasks_total | int | |
| tasks_completed | int | |
| completion_percentage | float | Calculated server-side |
| created_at | datetime | |

---

## API Modules

### /auth
- POST /auth/register
- POST /auth/login
- GET  /auth/me

### /roadmaps
- POST /roadmaps/generate
- GET  /roadmaps
- GET  /roadmaps/{id}
- DELETE /roadmaps/{id}

### /tasks
- GET  /tasks/today
- GET  /tasks?roadmap_id=&week=
- PATCH /tasks/{id}/complete
- PATCH /tasks/{id}/uncomplete

### /progress
- GET /progress/daily?date=
- GET /progress/weekly?week=

### /streaks
- GET /streaks/me

---

## Frontend Pages

| Page | Route | Purpose |
|---|---|---|
| Landing | / | Intro, login/signup CTA |
| Register | /register | Sign up form |
| Login | /login | Login form |
| Onboarding Quiz | /onboarding | Roadmap generation form |
| Today's Tasks | /tasks/today | Daily checklist (home after login) |
| Roadmap Detail | /roadmaps/:id | Full weekly task breakdown |
| My Roadmaps | /roadmaps | List of all user roadmaps |
| Dashboard | /dashboard | Charts, streak, missed tasks |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite + Tailwind CSS + Recharts |
| HTTP Client | Axios |
| Routing | React Router |
| Backend | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL |
| Auth | JWT (python-jose) + bcrypt |
| AI (Phase 4) | OpenAI or Gemini API |
