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

 ```
   # ⚙️ Installation & Prerequisites
Ensure you have Python 3.8+ installed on your host system.

Bash
# Clone the educational repository layout

git clone https://github.com/abdulrehman-sec1/Basic-Keylogger-Awareness-Report.git


cd Basic-Keylogger-Awareness-Report

# Install required presentation and terminal dependencies
```
pip install -r requirements.txt
```
# 🛠️ Usage Instructions
To launch the primary interactive user environment loop, run:

Bash
```
python main.py
```
Running the Test Suite
To run the automated tests and verify compliance logic:

Bash
```
python -m unittest discover tests
```

# 🖥️ Example Terminal Output
Plaintext
============================================================
 Basic Keylogger Awareness Report 
============================================================
1. Learn About Keyloggers
2. View Common Warning Signs
3. Run Basic Security Awareness Check
4. Take Security Awareness Quiz
5. Generate Awareness Report
6. Prevention Guide
7. Help
8. Exit
============================================================
Select an option (1-8): 
# 🛠️ Technologies & Architectural Mapping
 Architecture Overview
main.py: Coordinates workflow routing and manages session states.

awareness.py: Contains static educational content and definition tables.

system_checks.py: Executes non-elevated, read-only environment checks.

report_generator.py: Transforms session metrics into structured JSON schemas and formatted plain text reports.

utils.py: Handles screen formatting, color schemes, and file writes.