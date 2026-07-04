"""A standalone integration sample script demonstrating non-interactive execution of the posture engine."""

import sys
import os

# Appending current root module relative pathing variables
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import system_checks
import report_generator
from utils import save_json

def execute_automated_diagnostic() -> None:
    print("Initiating Non-Interactive System Posture Scan...")
    
    os_info = system_checks.get_os_metadata()
    processes = system_checks.audit_running_processes()
    startup = system_checks.inspect_startup_awareness()
    checklist = system_checks.execute_posture_checklist()
    
    # Run an automated sample with a fixed placeholder quiz score
    payload = report_generator.build_report_payload(os_info, processes, startup, checklist, 75.0)
    
    output_target = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports", "automated_sample.json")
    if save_json(output_target, payload):
        print(f"Automated diagnostic snapshot saved directly to: {output_target}")
    else:
        print("Failed to save report.")

if __name__ == "__main__":
    execute_automated_diagnostic()