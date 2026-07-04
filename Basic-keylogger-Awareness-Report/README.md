# Basic Keylogger Awareness Report

A modular, highly structured Python project designed for cybersecurity education, corporate threat awareness compliance, and defensive system audits.

## ⚠️ Important Security Disclaimer
This project is intended solely for cybersecurity awareness and defensive education. It does not contain any functionality for recording keystrokes, monitoring user activity, or performing offensive actions. It contains no keystroke hooking, data sniffing, or telemetry collection logic.

---

## 🚀 Key Features
* **Interactive CLI Interface**: A clean terminal UI using Colorama for structured navigation.
* **Deep Awareness Learning Subsystems**: Informative guides explaining API Hooking, Driver Rootkits, and Hardware Keyloggers.
* **Non-Invasive System Assessment**: Safe, read-only checks covering platform metadata, running processes, and configuration reminders.
* **Interactive Threat Verification Quiz**: Tests user understanding and calculates a localized risk score.
* **Multi-Format Report Export**: Generates defensive reports in both human-readable plain text (`.txt`) and programmatic (`.json`) formats.

---

## 📂 Folder Structure
```text
Basic-Keylogger-Awareness-Report/
│
├── main.py
├── awareness.py
├── report_generator.py
├── system_checks.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── reports/
│   └── sample_report.json
│
├── docs/
│   ├── project_overview.md
│   ├── keylogger_basics.md
│   ├── prevention_guide.md
│   └── detection_tips.md
│
├── examples/
│   └── sample_scan.py
│
└── tests/
    ├── test_awareness.py
    ├── test_report_generator.py
    └── __init__.py