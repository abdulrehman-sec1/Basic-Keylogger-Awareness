"""Educational modules regarding keylogger mechanics, typologies, and attack vectors."""

from utils import print_banner, colored_print

def show_introduction() -> None:
    print_banner("Project Intent & Ethics Blueprint")
    print(
        "Welcome to the Keylogger Awareness & Education Environment.\n\n"
        "CRITICAL DISCLAIMER:\n"
        "This project does NOT record, track, intercept, or handle real keystrokes.\n"
        "It contains zero offensive software components. It functions explicitly to\n"
        "demonstrate how monitoring threats execute conceptually, enabling defensive\n"
        "engineers to configure adequate host controls and mitigations.\n"
    )

def explain_keyloggers() -> None:
    print_banner("Educational Core: What is a Keylogger?")
    print(
        "A keylogger is a targeted tracking mechanism designed to record sequential\n"
        "inputs struck on a keyboard. While legitimate tracking exists for diagnostic\n"
        "optimization or behavioral metrics, malicious actors employ covert variations\n"
        "to extract highly confidential data streams prior to host encryption routines.\n"
    )

def hardware_keyloggers() -> None:
    print_banner("Deep Dive: Hardware Keyloggers")
    print(
        "Characteristics of Hardware-Based Interception:\n"
        "1. Physical Inline Taps: Small modules attached physically between the peripheral\n"
        "   interface wire and the system input board (e.g., USB passthrough modules).\n"
        "2. Keyboard Firmware Flares: Malicious components flashed directly onto the input controller.\n"
        "3. Accidental Over-Air Leaks: Wireless keyboards transmitting unencrypted radio signals\n"
        "   vulnerable to sniffers nearby.\n\n"
        "Defensive Focus: Regular physical asset sweeps and cryptographically signed firmware enforcement."
    )

def software_keyloggers() -> None:
    print_banner("Deep Dive: Software Keyloggers")
    print(
        "Characteristics of Software-Based Interception:\n"
        "1. API Hooking: Intercepting core OS messaging subsystems (e.g., Windows SetWindowsHookEx API)\n"
        "   to track global keyboard updates.\n"
        "2. Kernel/Driver Level: Rootkits installed at the ring 0 level intercepting I/O request packets.\n"
        "3. Hypervisor Layer: Malicious virtual machine managers tracking guest execution maps.\n"
        "4. Form Grabbing: Malicious browser scripts copying input fields before form submission."
    )

def infection_methods() -> None:
    print_banner("Threat Vectors: Infection Methods")
    print(
        "Malicious keyloggers infiltrate architectures via these common vectors:\n"
        "* Phishing Campaign Delivery: Users open weaponized document macros or scripts.\n"
        "* Strategic Supply Chain Poisoning: Legitimate software updates modified by attackers.\n"
        "* Physical Staging: Unauthorized access to an unlocked corporate workstation."
    )

def warning_signs() -> None:
    print_banner("Incident Indicators: Warning Signs")
    print(
        "Potential system red flags include:\n"
        "- Persistent typing lag or occasional input delays.\n"
        "- Unexplained network traffic to unknown external destinations.\n"
        "- Security application processes periodically turning off unexpectedly.\n"
        "- Suspicious unauthorized scripts listed in system startup profiles."
    )

def prevention_methods() -> None:
    print_banner("Defensive Blueprints: Prevention Methods")
    print(
        "- Enforce Multi-Factor Authentication (MFA) widely to devalue stolen passwords.\n"
        "- Use Virtual Keyboards or Password Managers for highly sensitive inputs.\n"
        "- Implement Least Privilege principles to block unauthorized application installations.\n"
        "- Deploy robust Endpoint Detection and Response (EDR) agents across all hosts."
    )

def security_best_practices() -> None:
    print_banner("Enterprise Security Standards")
    print(
        "1. Apply OS security patches quickly and automatically.\n"
        "2. Disable unneeded physical ports and unused expansion protocols.\n"
        "3. Audit active memory tables and look out for signed driver anomalies.\n"
        "4. Train operations teams to lock active displays whenever leaving workstations."
    )