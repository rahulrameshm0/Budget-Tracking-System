# 💰 Budget Tracking System

A full-stack personal finance tracker built with **Django**, allowing users to efficiently manage their income and expenses. The system provides transaction-level insights, balance summaries, and soon, user profile customization.

---

## 📌 Table of Contents

- [📸 Screenshots](#-screenshots)
- [✨ Features](#-features)
- [🛠️ Tech Stack](#-tech-stack)
- [🚀 Getting Started](#-getting-started)
- [📂 Project Structure](#-project-structure)
- [👤 User Profile (Upcoming)](#-user-profile-upcoming)
- [🎯 Roadmap](#-roadmap)
- [🙌 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📸 Screenshots

> *(Add screenshots inside a `screenshots/` folder and update the paths below)*

| Home Page             | Transaction Summary        | Add Transaction Form       |
|-----------------------|----------------------------|----------------------------|
| ![](screenshots/home.png) | ![](screenshots/summary.png) | ![](screenshots/add_form.png) |

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
| Database         | SQLite (Django default)|
| Styling (Optional)| TailwindCSS / Bootstrap |
| Templates        | Django Template Engine |
| Version Control  | Git & GitHub           |

---

## 🚀 Getting Started

### 🔧 Prerequisites

Ensure you have Python 3.8+ installed.

```bash
python --version
