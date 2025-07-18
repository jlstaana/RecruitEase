# RecruitEase Backend API

## Applicant Actions

- **Upload Resume/Cover Letter**
  - `POST /api/files/` (multipart/form-data, field: file, file_type)
  - List uploaded files: `GET /api/files/`

- **View Jobs**
  - `GET /api/jobs/`
  - `GET /api/jobs/<id>/`

- **Apply to Job**
  - `POST /api/applications/` (fields: job, resume, cover_letter)
  - List applications: `GET /api/applications/`
  - View application status: `GET /api/applications/<id>/`

## Recruiter/Admin Actions

- **Manage Jobs**
  - `POST /api/jobs/`, `PUT/PATCH/DELETE /api/jobs/<id>/`
- **Manage Applications**
  - `GET /api/applications/`, `PATCH /api/applications/<id>/` (update status)
- **View Applicant Files**
  - `GET /api/files/?user=<user_id>` (if permissions allow)
# RecruitEase Backend

This is the Django REST API backend for RecruitEase, a recruitment management system.

## Features
- User registration and login (JWT authentication)
- Role-based dashboards for applicants, employees, recruiters, and admins
- User profile management
- RESTful API endpoints

## Setup
1. Create and activate a Python virtual environment:
   ```powershell
   py -m venv venv
   .\venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install django djangorestframework djangorestframework-simplejwt
   ```
3. Run migrations:
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser:
   ```powershell
   python manage.py createsuperuser
   ```
5. Start the development server:
   ```powershell
   python manage.py runserver
   ```

## API Endpoints
- `POST /api/users/register/` — Register a new user
- `POST /api/users/login/` — Obtain JWT token
- `POST /api/users/token/refresh/` — Refresh JWT token
- `GET/PUT /api/users/profile/` — Get or update user profile
- `POST /api/users/logout/` — Logout (blacklist refresh token)
- `GET /api/dashboard/` — Get role-based dashboard data

### AI, Resume Extraction & Notification Endpoints
- `POST /api/upload/pdf/` — Upload a PDF resume and extract text (input: `file`)
- `POST /api/upload/image/` — Upload a resume image (photo/scan) and extract text using OCR (input: `file`)
- `POST /api/ai/bert-screen/` — Extracts skills, experience, education, and job match from resume text using BERT (input: `resume_text`, optional: `job_description`)
- `POST /api/ai/rf-screen/` — Uses RandomForest to evaluate candidate-job match (input: `features` as dict with `skills`, `experience_years`, `education`, `job_skills`)
- `POST /api/it/ticket/` — IT Admin submits a ticket; sends notification email to IT admin

## Notes
- The backend uses a custom user model (`users.User`).
- All endpoints (except registration and login) require authentication.
- Email notifications (console backend by default) are supported for IT admin ticketing and can be extended for user/HR notifications, OTP, and security alerts.
