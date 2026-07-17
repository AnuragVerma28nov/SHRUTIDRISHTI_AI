# 🏗️ Architecture

## Overview

ShrutiDrishti AI follows a modular architecture built with Streamlit, Supabase, and AI pipelines for Face Recognition, Voice Recognition, and Assignment Management.

## System Architecture

```
User
 │
 ▼
Streamlit UI
 │
 ▼
Business Logic
 │
 ├── Face Pipeline
 ├── Voice Pipeline
 └── Assignment Pipeline
 │
 ▼
Supabase Database
 │
 ▼
Supabase Storage
```

## Project Structure

```
src/
├── components/
├── database/
├── pipelines/
├── screens/
├── ui/
└── utils/
```

## AI Modules

- 👁 Face Recognition
- 🎤 Voice Recognition
- 📄 Assignment Analysis (Upcoming)

## Database

- teachers
- students
- subjects
- subject_students
- attendance_logs
- assignments
- assignment_submissions

## Workflow

Teacher → Create Subject → Student Joins → AI Attendance → Assignment → Submission → Marks

## Future Improvements

- Live Camera Attendance
- AI Assignment Evaluation
- OCR
- Plagiarism Detection
- Mobile App