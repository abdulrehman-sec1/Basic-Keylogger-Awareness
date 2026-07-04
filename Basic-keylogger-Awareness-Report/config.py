"""Configuration settings, quiz questions, and educational text assets."""

import os

# Application Metadata
APP_NAME = "Basic Keylogger Awareness Report"
VERSION = "1.0.0"

# Score Thresholds
SCORE_EXCELLENT = 80
SCORE_GOOD = 60

# Terminal Color Codes (Fallback if colorama isn't used)
COLORS = {
    "HEADER": "\033[95m",
    "INFO": "\033[94m",
    "SUCCESS": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "ENDC": "\033[0m",
    "BOLD": "\033[1m",
}

# Directories
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "reports")

# Quiz Configuration
QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "What is the primary function of an offensive keylogger?",
        "options": [
            "A) To speed up keyboard typing rates",
            "B) To covertly record and steal user keystrokes",
            "C) To encrypt data stored on the hard drive",
            "D) To clean up duplicate system processes"
        ],
        "answer": "B",
        "explanation": "Keyloggers are designed to record keystrokes covertly to steal sensitive data."
    },
    {
        "id": 2,
        "question": "Which of the following describes a hardware keylogger?",
        "options": [
            "A) A malicious script embedded in a phishing email attachment",
            "B) A physical device plugged between the keyboard cable and the PC port",
            "C) A driver module loaded into the operating system kernel",
            "D) A browser extension tracking web form inputs"
        ],
        "answer": "B",
        "explanation": "Hardware keyloggers are physical components placed inline with input peripherals."
    },
    {
        "id": 3,
        "question": "What is an effective defensive control against software keyloggers?",
        "options": [
            "A) Disconnecting your monitor from the power supply",
            "B) Keeping Operating Systems, EDR/Antivirus, and browsers fully updated",
            "C) Typing passwords using only the Caps Lock key",
            "D) Disabling the system firewall permanently"
        ],
        "answer": "B",
        "explanation": "Updated security software and OS patches mitigate the execution vulnerabilities utilized by keyloggers."
    },
    {
        "id": 4,
        "question": "Why is using a Multi-Factor Authentication (MFA) app helpful against credential theft via keylogging?",
        "options": [
            "A) It stops the keylogger from capturing your initial password entry",
            "B) It generates time-sensitive, single-use tokens that expire rapidly",
            "C) It automatically uninstalls malicious background drivers",
            "D) It prevents physical access to your hardware devices"
        ],
        "answer": "B",
        "explanation": "Even if a static password is stolen via a keylogger, the one-time MFA token will expire before attackers can exploit it."
    }
]