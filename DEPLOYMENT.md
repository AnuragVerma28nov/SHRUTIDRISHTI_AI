# 🚀 Deployment Guide

This guide explains how to deploy and run **ShrutiDrishti AI** locally.

---

## Prerequisites

- Python 3.11+
- Git
- Supabase Account
- Streamlit

---

## 1. Clone the Repository

```bash
git clone https://github.com/AnuragVerma28nov/ShrutiDrishti-AI.git

cd ShrutiDrishti-AI
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Supabase

Create:

```
.streamlit/secrets.toml
```

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"
SUPABASE_KEY="YOUR_SUPABASE_ANON_KEY"
```

---

## 5. Create Storage Buckets

Create the following buckets in **Supabase Storage**:

- `assignments`
- `assignment-submissions`
- `student-faces`
- `student-voices`

Set appropriate **Row Level Security (RLS)** policies for each bucket.

---

## 6. Database

Run the SQL scripts to create the required tables:

- teachers
- students
- subjects
- subject_students
- attendance_logs
- assignments
- assignment_submissions

---

## 7. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# Common Issues

| Error | Solution |
|--------|----------|
| Bucket not found | Create the required storage bucket in Supabase. |
| RLS Policy Error | Add or update Row Level Security policies. |
| Schema Cache Error | Refresh the Supabase schema cache after altering tables. |
| Module Not Found | Run `pip install -r requirements.txt`. |

---

# Deployment Checklist

- Python installed
- Dependencies installed
- Supabase project created
- Database initialized
- Storage buckets created
- `secrets.toml` configured
- Application starts successfully

---

Happy Coding! 🚀