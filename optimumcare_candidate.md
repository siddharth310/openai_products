. Overview
Goal:
Build a modern recruitment platform for CareHome staffing.
Candidate journey: registration, compliance, job matching, application, shift management, timesheets, alerts, and communication.

2. Main Entities
plaintext
Copy
Edit
Candidate
- id
- email
- phone
- password (hashed)
- full_name
- dob
- address
- emergency_contact
- skills
- experience
- bio
- documents: [CV, RightToWork, DBS, TrainingCerts]
- compliance_status
- availability
- timesheets: []
- notifications: []
3. Core User Flows
3.1 Registration & Authentication
markdown
Copy
Edit
#### Registration
- Input: email, phone, password
- Validates: unique email/phone, password rules
- Sends: verification email/SMS
- Next: On verification, prompt profile setup

#### Login
- Input: email/phone, password
- Validates: correct password, account status
- Option: forgot/reset password
3.2 Profile Setup
markdown
Copy
Edit
#### Profile Completion
- Input: name, DOB, address, skills, experience, emergency contact
- Action: upload documents (CV, RightToWork, DBS, certs)
- Validates: required fields, file type/size, document expiry

#### Document Management
- Stores: uploads with expiry dates
- Checks: completeness for compliance
- Blocks: job application if incomplete
3.3 Job Search & Application
markdown
Copy
Edit
#### Job Search
- Filters: role, location, shift, pay, employer
- Auto-matches: recommends jobs based on profile

#### Apply for Job
- Action: click “Apply”, attach notes
- Prevent: duplicate application
- Allows: withdraw (if before interview)

#### Application Status
- Stages: Applied → Shortlisted → Interview → Hired/Rejected
- Receives: notifications at each stage
3.4 Shift & Timesheet Management
markdown
Copy
Edit
#### Shift Booking
- Views: available shifts (calendar/list)
- Books: shift (must meet eligibility/compliance)
- Cancels: with warning, checks for penalties

#### Timesheet
- Action: logs hours per shift, submits for approval
- Status: Pending → Approved/Rejected
- Prevents: duplicate submissions
- Allows: resubmission if rejected
3.5 Compliance & Notifications
markdown
Copy
Edit
#### Compliance
- Daily/weekly cron: checks for expired/expiring docs
- Triggers: alerts 30, 15, 7, 1 days before expiry
- Locks: job app/shift booking if expired

#### Notifications
- Events: job match, interview, document expiry, timesheet
- Modes: in-app, email, SMS, push (mobile)
3.6 Communication
markdown
Copy
Edit
#### Messaging
- Inbox: recruiter/admin/candidate
- Unread badge, reply, block/report

#### Alerts
- New job, interview scheduled, feedback, timesheet
4. API Suggestions
markdown
Copy
Edit
POST   /api/auth/register
POST   /api/auth/verify
POST   /api/auth/login
POST   /api/candidate/profile
POST   /api/candidate/documents
GET    /api/candidate/compliance-status
GET    /api/candidate/dashboard
GET    /api/jobs
POST   /api/applications
GET    /api/applications
POST   /api/shifts/book
GET    /api/shifts
POST   /api/timesheets
GET    /api/timesheets
POST   /api/messages
GET    /api/messages
5. Acceptance Criteria
markdown
Copy
Edit
- Candidate cannot apply or book shifts if compliance is incomplete/expired
- Duplicate job applications are blocked
- Timesheet can be submitted only once per shift
- Notifications are triggered at every journey milestone
- All user data is stored securely and compliant with data regulations
6. Example Use Case – End-to-End
markdown
Copy
Edit
1. Candidate registers with email/phone, gets OTP, and verifies account.
2. Completes profile (personal info, uploads documents).
3. System checks compliance; if incomplete, shows warning and prevents job application.
4. Once complete, candidate sees matched jobs on dashboard, applies to one.
5. Application status updates trigger notifications at each step.
6. Candidate books a shift; after working, logs hours in timesheet and submits.
7. System sends expiry reminders for documents; candidate uploads new docs when needed.
8. Messaging enabled with recruiter/admin for support and scheduling.
7. Tech Stack Suggestion
markdown
Copy
Edit
Frontend: React.js / Next.js (Web), React Native / Flutter (Mobile)
Backend: Node.js/Express or Python/FastAPI
Database: PostgreSQL or MongoDB
File Storage: AWS S3 or equivalent
Notifications: Twilio (SMS), SendGrid (Email), Firebase Cloud Messaging (push)
8. Security & Compliance
markdown
Copy
Edit
- Passwords hashed (bcrypt/argon2)
- JWT for session auth
- Role-based access control
- File storage with restricted access
- GDPR/UK DPA compliance
9. Wireframe Screens (Outline)
markdown
Copy
Edit
- Registration/Login
- Profile Setup
- Document Upload
- Candidate Dashboard
- Job Search/Matched Jobs
- Job Application Details
- Shift Booking/Calendar
- Timesheet Submission
- Compliance Alerts/Reminders
- Messaging/Inbox
- Settings/Logout
