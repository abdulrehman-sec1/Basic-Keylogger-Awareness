"""Primary execution orchestrator implementing the interactive CLI menu loop."""

import os
import sys
from typing import Dict, Any

from utils import clear_screen, print_banner, colored_print, save_json, export_text, format_table
import awareness
import system_checks
import report_generator
from config import QUIZ_QUESTIONS, REPORTS_DIR

# Global State Container for session-based variables
session_state: Dict[str, Any] = {
    "quiz_completed": False,
    "quiz_score": 0.0,
    "system_checked": False,
    "os_info": {},
    "processes": [],
    "startup_items": [],
    "checklist": []
}

def execute_quiz_workflow() -> None:
    """Executes the interactive awareness quiz module and logs completion state details."""
    print_banner("Security Awareness Interactive Quiz")
    correct_count = 0
    total_questions = len(QUIZ_QUESTIONS)
    
    for idx, q in enumerate(QUIZ_QUESTIONS, 1):
        print(f"\nQuestion {idx} of {total_questions}: {q['question']}")
        for option in q['options']:
            print(option)
            
        choice = input("\nEnter your selection (A/B/C/D): ").strip().upper()
        if choice == q['answer']:
            colored_print("Correct Response.", "SUCCESS")
            correct_count += 1
        else:
            colored_print(f"Incorrect. The correct answer was {q['answer']}.", "FAIL")
        print(f"Context: {q['explanation']}")
        
    score = (correct_count / total_questions) * 100
    session_state["quiz_completed"] = True
    session_state["quiz_score"] = score
    
    print("\n" + "-"*40)
    colored_print(f"Quiz Completed! Final Score: {score:.2f}%", "SUCCESS" if score >= 75 else "WARNING")
    print("-"*40)
    input("\nPress Enter to return to the main operational interface...")

def run_system_audit_workflow() -> None:
    """Executes safe, non-invasive system posture checks and updates session configuration models."""
    print_banner("Running Defensive Architecture Posture Assessment...")
    
    session_state["os_info"] = system_checks.get_os_metadata()
    session_state["processes"] = system_checks.audit_running_processes()
    session_state["startup_items"] = system_checks.inspect_startup_awareness()
    session_state["checklist"] = system_checks.execute_posture_checklist()
    session_state["system_checked"] = True
    
    # Render OS environment variables layout
    print("\n--- Host Environment ---")
    for k, v in session_state["os_info"].items():
        print(f"{k:<20}: {v}")
        
    print("\n--- Defensive Posture Framework Reminders ---")
    table_data = [[item['control'], item['status']] for item in session_state["checklist"]]
    print(format_table(table_data, ["Control Target Validation", "Recommended Action"]))
    
    colored_print("\nPosture check complete. Data staged for report generation.", "SUCCESS")
    input("\nPress Enter to return to the main operational interface...")

def process_report_generation_workflow() -> None:
    """Generates structural compliance reports across both JSON and TXT format variations."""
    if not session_state["system_checked"]:
        colored_print("Warning: System posture scanning has not run yet. Running defaults now...", "WARNING")
        run_system_audit_workflow()
        
    payload = report_generator.build_report_payload(
        session_state["os_info"],
        session_state["processes"],
        session_state["startup_items"],
        session_state["checklist"],
        session_state["quiz_score"]
    )
    
    text_report = report_generator.convert_payload_to_text(payload)
    
    json_path = os.path.join(REPORTS_DIR, "awareness_assessment_report.json")
    txt_path = os.path.join(REPORTS_DIR, "awareness_assessment_report.txt")
    
    if save_json(json_path, payload) and export_text(txt_path, text_report):
        colored_print(f"\nReports generated successfully!", "SUCCESS")
        print(f"JSON Target: {json_path}")
        print(f"Text Target: {txt_path}")
    else:
        colored_print("Error: Failed to write reports to the local file system.", "FAIL")
        
    input("\nPress Enter to return to the main operational interface...")

def rendering_help_system() -> None:
    """Displays project navigational context parameters."""
    print_banner("System Help Documentation")
    print(
        "This terminal environment helps you analyze threat architectures and configuration risks.\n"
        "Options 1 & 2 deliver raw baseline educational components.\n"
        "Option 3 evaluates safe host configurations.\n"
        "Option 4 gauges tracking architectural awareness.\n"
        "Option 5 commits session insights directly into static filesystem artifacts."
    )
    input("\nPress Enter to return to the main operational interface...")

def execution_loop() -> None:
    """Main application interaction loop managing choices and workflow routing."""
    while True:
        clear_screen()
        print("=========================================")
        print(f" {report_generator.report_generator.__color_placeholder if False else 'Basic Keylogger Awareness Report'} ")
        print("=========================================")
        print("1. Learn About Keyloggers")
        print("2. View Common Warning Signs")
        print("3. Run Basic Security Awareness Check")
        print("4. Take Security Awareness Quiz")
        print("5. Generate Awareness Report")
        print("6. Prevention Guide")
        print("7. Help")
        print("8. Exit")
        print("=========================================")
        
        choice = input("Select an option (1-8): ").strip()
        
        clear_screen()
        if choice == "1":
            awareness.explain_keyloggers()
            awareness.hardware_keyloggers()
            awareness.software_keyloggers()
            input("\nPress Enter to return...")
        elif choice == "2":
            awareness.warning_signs()
            awareness.infection_methods()
            input("\nPress Enter to return...")
        elif choice == "3":
            run_system_audit_workflow()
        elif choice == "4":
            execute_quiz_workflow()
        elif choice == "5":
            process_report_generation_workflow()
        elif choice == "6":
            awareness.prevention_methods()
            awareness.security_best_practices()
            input("\nPress Enter to return...")
        elif choice == "7":
            rendering_help_system()
        elif choice == "8":
            colored_print("Exiting awareness framework context. Stay safe.", "SUCCESS")
            sys.exit(0)
        else:
            colored_print("Invalid choice configuration option. Try again.", "FAIL")
            input("\nPress Enter to retry...")

if __name__ == "__main__":
    execution_loop()