# 🛡️ SentinelShield

### A Flask-Based Web Application Firewall (WAF) with Real-Time Intrusion Detection and Security Dashboard

> **Securing Web Applications Through Intelligent Request Inspection, Threat Detection, and Real-Time Security Monitoring.**

---

## 📌 Overview

SentinelShield is a lightweight Web Application Firewall (WAF) developed using **Python** and **Flask** that inspects every incoming HTTP request before it reaches the web application. The system detects multiple categories of web attacks, blocks malicious requests, applies rate limiting, logs security events, and visualizes attack analytics through a real-time dashboard.

The project demonstrates practical web security concepts including request inspection, rule-based attack detection, request logging, dashboard visualization, and web application protection.

---

## ✨ Features

- HTTP Request Inspection
- SQL Injection Detection
- Cross-Site Scripting (XSS) Detection
- Command Injection Detection
- Directory Traversal Detection
- Local File Inclusion (LFI) Detection
- IP-Based Rate Limiting
- Request Logging
- Security Dashboard
- Attack Distribution Analytics
- Threat Level Monitoring
- Blocked Request Page
- Responsive User Interface

---

## 🛠️ Technologies Used

| Category | Technology |
|-----------|------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Visualization | Plotly |
| Data Processing | Pandas |
| Security | Regular Expressions (Regex) |
| Logging | Custom Logger |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
SentinelShield/
│
├── logs/
│   └── requests.log
├── reports/
│   ├── Architecture_Diagram.png
│   ├── Project_Summary.md
│   ├── Request_Worflow.png
│   ├── SentinelShield_Presentation.pptx
│   └── SentineShield_Report.pdf
├── screenshots/
│   ├── command_injection/
│   ├── cross_site_scripting(xss)/
│   ├── dashboard/
│   ├── directoty_traversal/
│   ├── home/
│   ├── inspect/
│   ├── kali_linux_testing/
│   ├── local_file_inclusion/
│   ├── rate_limit_exceeding/
│   └── sql_injection/
├── src/
│   ├── detector.py
│   ├── dashboard.py
│   ├── logger.py
│   ├── rate_limiter.py
│   ├── rules.py
│   └── utils.py
│
├── static/
│   └── css/
│       └── common.css
├── templates/
│   ├── blocked.html
│   ├── dashboard.html
│   ├── home.html
│   └── inspect.html
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🏗️ System Architecture

The SentinelShield application follows a modular architecture where every HTTP request is inspected before reaching the application.

```
                    Client Request
                           │
                           ▼
                  Flask Application
                           │
                           ▼
                  Request Inspector
                           │
                           ▼
                Threat Detection Engine
       ┌────────────┼────────────┬─────────────┐
       │            │            │             │
       ▼            ▼            ▼             ▼
 SQL Injection    XSS      Command Injection   LFI /
   Detection    Detection      Detection    Directory Traversal
                           │
                           ▼
                    Rate Limiter
                           │
                           ▼
                    Security Logger
                           │
                           ▼
                  Security Dashboard
```

The application uses a rule-based detection engine to identify malicious requests. Every incoming request is inspected, classified, logged, and visualized through the dashboard for security monitoring.

---

# 🔄 Request Processing Workflow

Every incoming HTTP request follows the workflow below:

```
Incoming Request
        │
        ▼
Request Inspection
        │
        ▼
Threat Detection
        │
   ┌────┴────┐
   │         │
Safe      Malicious
   │         │
   ▼         ▼
Home      Blocked Page
   │
   ▼
Logging
   │
   ▼
Dashboard Analytics
```

### Workflow Explanation

1. Client sends an HTTP request.
2. Flask captures and inspects the request.
3. Request parameters, URL, and form data are analyzed.
4. Detection engine checks for supported attack signatures.
5. Rate limiter validates request frequency.
6. Safe requests proceed to the application.
7. Malicious requests are blocked immediately.
8. Every processed request is recorded in the log file.
9. Dashboard updates attack statistics and recent security events.

---

# 🛡️ Supported Attack Detection

| Attack | Status |
|---------|--------|
| SQL Injection | ✅ |
| Cross Site Scripting (XSS) | ✅ |
| Command Injection | ✅ |
| Directory Traversal | ✅ |
| Local File Inclusion (LFI) | ✅ |
| Rate Limiting | ✅ |

---

# 📊 Dashboard Features

The dashboard provides real-time visibility into application security.

It includes:

- Total Requests
- Blocked Requests
- Threat Level Indicator
- Attack Distribution Chart
- Recent Security Events
- Request Statistics
- Interactive Analytics

---

# 🧪 Testing

The application has been tested against multiple attack scenarios.

| Test | Result |
|------|--------|
| Normal Request | ✅ Passed |
| SQL Injection | ✅ Blocked |
| XSS Attack | ✅ Blocked |
| Command Injection | ✅ Blocked |
| Directory Traversal | ✅ Blocked |
| Local File Inclusion | ✅ Blocked |
| Rate Limiting | ✅ Blocked |

Testing was performed using:

- Web Browser
- Kali Linux
- Manual Payload Injection

---

# 📸 Screenshots

Example screenshots are available inside the **screenshots/** directory.

- Home Page
- Request Inspection
- Dashboard
- SQL Injection Detection
- XSS Detection
- Command Injection Detection
- Directory Traversal Detection
- Local File Inclusion Detection
- Rate Limiting
- Kali Linux Testing

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SentinelShield.git
```

Navigate to the project

```bash
cd SentinelShield
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🔮 Future Improvements

- Machine Learning Based Attack Detection
- Authentication & Role-Based Access Control
- Email Alerts
- Geo-IP Tracking
- Threat Intelligence Integration
- Docker Deployment
- REST API Support
- Cloud Deployment

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Aarav Shah**

Cybersecurity & AI Enthusiast

---

⭐ If you found this project useful, consider giving it a star on GitHub.