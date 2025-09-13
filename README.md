# 🧠 Smart Timetable Scheduler

A web-based platform for intelligent class scheduling in higher education institutions, designed to handle complex constraints under NEP 2020. This system automates timetable generation using faculty availability, classroom capacity, subject combinations, and student preferences.

## 🚀 Features

- Role-based login for Admins and Department Heads
- Input interface for classrooms, subjects, faculty, and batches
- Constraint-based timetable generation using Python
- Multiple optimized timetable options
- Review and approval workflow
- Suggestions for rearrangements when optimal solutions aren't available
- Multi-department and multi-shift support
- Export timetable as PDF or Excel (coming soon)

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (React upgrade planned)
- **Backend**: Flask (Python)
- **Database**: SQLite (PostgreSQL upgrade planned)
- **Optimization Engine**: Python (OR-Tools or PuLP)
- **Authentication**: Flask sessions (JWT/OAuth2 planned)

## 📦 Installation

```bash
git clone https://github.com/your-username/smart-timetable.git
cd smart-timetable
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
