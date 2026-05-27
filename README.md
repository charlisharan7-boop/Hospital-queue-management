# Hospital-queue-management
# 🏥 Smart Healthcare & Priority Management System

A hospital queue management and doctor availability system built using Streamlit, SQLite, and Pandas.

This project was created as a healthcare hackathon solution to simplify patient registration, automate emergency prioritization, and improve doctor-patient workflow inside hospitals and clinics.

---

# 📌 Project Overview

The Smart Healthcare & Priority Management System is a web-based application that allows:

* Patients to register digitally
* Hospitals to manage waiting queues efficiently
* Emergency patients to receive priority automatically
* Doctors to update their availability status
* Admin staff to manage the current queue in real time

The application provides a clean hospital dashboard with live queue tracking and specialist availability information.

---

# 🚀 Key Features

## ✅ Patient Registration System

Patients can:

* Enter their name
* Enter mobile number
* Select severity level
* Choose a consulting doctor

The system instantly generates a booking entry.

---

## 🚨 Smart Priority Queue Management

The queue is automatically sorted based on medical severity:

| Priority | Severity Level |
| -------- | -------------- |
| 1        | Emergency      |
| 2        | Urgent         |
| 3        | Routine        |

Emergency patients are automatically moved to the front of the waiting list.

---

## 👨‍⚕️ Doctor Discovery System

Patients can:

* View specialist profiles
* Check doctor availability
* View educational qualifications
* See years of experience
* Check room numbers
* Check working hours

---

## 🛡️ Admin Portal

The admin section allows hospital staff to:

* View next patient in queue
* Serve patients
* Remove completed appointments
* Send simulated SMS alerts
* Update doctor availability status

---

## 📊 Real-Time Queue Dashboard

The public queue board displays:

* Patient names
* Severity level
* Assigned doctor
* Arrival time

All data updates live without page refresh complexity.

---

# 🧠 Technologies Used

## 🐍 Python

The entire backend logic and application functionality are built using Python.

Used for:

* Database operations
* Queue management
* Validation logic
* Backend processing

---

## 🎨 Streamlit

Streamlit is used to build the web application UI.

Features used:

* Sidebar forms
* Tabs
* Dataframes
* Expanders
* Buttons
* Status messages
* Dynamic rerendering

Why Streamlit?

* Fast development
* Beginner friendly
* Easy deployment
* Interactive dashboards

---

## 🗄️ SQLite Database

SQLite is used as the database system.

Database tables:

* `doctors`
* `queue`

Why SQLite?

* Lightweight
* No separate server required
* Built directly into Python
* Perfect for hackathons and prototypes

---

## 📈 Pandas

Pandas is used for:

* Reading SQL query data
* Converting database data into tables
* Displaying structured queue dashboards

---

# 🏗️ System Architecture

## 1️⃣ Frontend Layer

Built using Streamlit components:

* Sidebar inputs
* Interactive tabs
* Queue dashboard
* Doctor cards
* Admin controls

---

## 2️⃣ Backend Logic

Python handles:

* Queue sorting
* Database communication
* Input validation
* Appointment handling
* Doctor status updates

---

## 3️⃣ Database Layer

SQLite stores:

* Doctor information
* Patient queue records
* Priority levels
* Arrival timestamps

---

# 🗂️ Database Schema

## Doctors Table

| Column        | Description         |
| ------------- | ------------------- |
| id            | Doctor ID           |
| name          | Doctor Name         |
| specialty     | Medical Specialty   |
| education     | Qualifications      |
| experience    | Years of Experience |
| working_hours | Availability Timing |
| status        | Available/Busy      |
| room_no       | Room Number         |

---

## Queue Table

| Column       | Description          |
| ------------ | -------------------- |
| id           | Queue ID             |
| patient_name | Patient Name         |
| phone        | Mobile Number        |
| priority     | Severity Level       |
| doctor_id    | Assigned Doctor      |
| arrival_time | Time of Registration |

---

# ⚙️ How Priority Logic Works

The system sorts patients using:

```sql id="q7qexg"
ORDER BY priority ASC, id ASC
```

This means:

1. Emergency patients are served first
2. If priority is same, earlier arrivals are served first

This creates a fair and optimized hospital queue system.

---

# 📱 Simulated SMS Notification System

When a patient is served:

* The system triggers a simulated SMS notification
* A toast message appears confirming the alert

This simulates real-world hospital patient calling systems.

---

# 🔒 Input Validation

The application validates:

* Empty patient names
* Invalid mobile numbers
* Missing booking details

This improves reliability and reduces incorrect entries.

---

# 📌 Why This Project Matters

Traditional hospital queues often suffer from:

* Long waiting times
* No emergency prioritization
* Poor patient communication
* Manual record handling

This system helps solve these problems using:

* Digital registration
* Automated queue sorting
* Real-time tracking
* Doctor availability management

---

# 🌟 Future Improvements

Possible future enhancements:

* Real SMS integration using Twilio
* Login authentication
* Online appointment booking
* AI-based patient severity prediction
* QR code patient tickets
* Cloud database integration
* Voice announcements
* Multi-hospital support
* Analytics dashboard

---

# ▶️ Installation Guide

## Step 1 — Clone Repository

```bash id="prj4xy"
git clone <your-repository-link>
```

---

## Step 2 — Install Dependencies

```bash id="0l9q9h"
pip install streamlit pandas
```

---

## Step 3 — Run Application

```bash id="jlwmqe"
streamlit run app.py
```

---

# 📂 Project Structure

```text id="2l0n1n"
project-folder/
│
├── app.py
├── hospital_hackathon.db
├── requirements.txt
└── README.md
```

---

# 📦 Requirements

```text id="b8ce2l"
streamlit
pandas
sqlite3
```

Note:
`sqlite3` is included with Python by default.

---

# 🎯 Use Cases

This project can be used in:

* Hospitals
* Clinics
* Emergency centers
* Healthcare startups
* Medical hackathons
* Queue automation systems

---

# 👨‍💻 Developer Notes

This project was designed as:

* A beginner-friendly healthcare management solution
* A hackathon-ready prototype
* A demonstration of real-time queue prioritization using Python and Streamlit

---

# 📜 License

This project is open-source and free to use for educational and hackathon purposes.

