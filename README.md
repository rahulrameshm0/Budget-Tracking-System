# 💰 Budget Tracking System

A full-stack personal finance tracker built with **Django**, allowing users to efficiently manage their income and expenses. The system provides transaction-level insights, balance summaries, and soon, user profile customization.

---

## 📌 Table of Contents


- [✨ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [📂 Project Structure](#-project-structure)
- [👤 User Profile (Upcoming)](#-user-profile-upcoming)
- [🎯 Roadmap](#-roadmap)
- [🙌 Contributing](#-contributing)

---

## ✨ Features

### 🔐 Authentication
- Secure registration and login system.
- Session-based authentication using Django’s built-in `User` model.
- CSRF protection for all forms.

### 📊 Dashboard
- Real-time view of current balance, total income, and total expenses.
- Pie or bar charts (optional) to visualize spending patterns.

### 🧾 Transactions
- Create, read, update, and delete income/expense entries.
- Categorize transactions (e.g., Food, Bills, Salary).
- Automatically updates totals upon new entries or edits.

### 🔍 Filters
- Filter transactions by:
  - Date range
  - Category
  - Type (Income/Expense)

### 📱 Responsive UI
- Fully responsive layout using media queries.
- Works on mobile, tablet, and desktop devices.

### 👤 User Profile (Coming Soon)
- View personal details (username, email, etc.)
- Upload/change profile picture.
- Update password and personal info.
- Option to delete account.

---

## 🛠️ Tech Stack

| Layer            | Technology             |
|------------------|------------------------|
| Backend          | Python, Django         |
| Frontend         | HTML5, CSS3, JavaScript |
| Database         | PostgreSQL|
| Styling (Optional)| TailwindCSS / Bootstrap |
| Templates        | Django Template Engine |
| Version Control  | Git & GitHub           |

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have Python 3.8+ installed.

```bash
python --version
```

## 📥 Installation Steps

```bash
  git clone https://github.com/your-username/Budget-Tracking-System.git
  cd Budget-Tracking-System
```

## Install Dependencies

```bash
  pip install -r requirements.txt
  Apply Migrations
```
## Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser (for admin access)

```bash
  python manage.py createsuperuser
  Run the Development Server
```
## Run the Development Server
```bash
  python manage.py runserver
  Visit the App
  Go to: http://127.0.0.1:8000
```

## 📂 Project Structure

```bash
budget-tracking-system/
│
├── budgetapp/               
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── forms.py
│
├── budgetproject/           
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```
## 👤 User Profile (Upcoming)
Planned Features:
A dedicated profile page accessible via the navbar.

Display current user details (email, username).

Option to:

Change username/password

Upload/change profile picture

Set monthly budget goals

View historical spending stats

Profile view and edit forms will use Django’s UserChangeForm and UserProfile model (custom extension).

## 🎯 Roadmap
 Income/Expense CRUD

 Summary dashboard

 User authentication

 User profile page

 Budget goal tracking

 Graphical reports (chart.js or Plotly)

 Export to CSV/PDF

## 🙌 Contributing
Want to make this better?

Fork the repo

Create your branch: git checkout -b feature-name

Commit changes: git commit -m 'Added feature'

Push to your branch: git push origin feature-name

Submit a Pull Request

## 📬 Contact
If you have any questions or feedback, feel free to reach out.

Email: rahulramesh98@gmail.com
---

