"""Defensive, non-intrusive host diagnostics and posture configuration assessment."""

import os
import sys
import platform
from typing import Dict, Any, List
from utils import colored_print

def get_os_metadata() -> Dict[str, str]:
    """Compiles basic operating system identifiers safely without administrative elevation."""
    return {
        "OS": platform.system(),
        "OS_Release": platform.release(),
        "OS_Version": platform.version(),
        "Architecture": platform.machine(),
        "Python_Version": sys.version.split()[0]
    }

def audit_running_processes() -> List[str]:
    """Collects current execution spaces (process names only) cleanly using lightweight OS hooks."""
    processes = []
    try:
        if platform.system() == "Windows":
            # Native fallback using tasks allocation listing
            with os.popen('tasklist /nh /fo csv') as f:
                for line in f:
                    if line.strip():
                        name = line.split(',')[0].strip('"')
                        if name not in processes:
                            processes.append(name)
        else:
            # Unix-like process evaluation abstraction
            with os.popen('ps -e -o comm=') as f:
                processes = list(set(line.strip() for line in f if line.strip()))
    except Exception as e:
        colored_print(f"Could not retrieve process space tracking: {e}", "WARNING")
        processes = ["Unavailable or insufficient access permissions"]
    
    return sorted(processes)[:40]  # Return an abbreviated snapshot for defensive readability

def inspect_startup_awareness() -> List[str]:
    """Identifies potential structural runtime entry points configured for auto-execution."""
    entries = []
    try:
        if platform.system() == "Windows":
            # Read-only evaluation of general user registry hives via query calls
            with os.popen('reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run') as f:
                for line in f:
                    if "REG_SZ" in line or "REG_EXPAND_SZ" in line:
                        entries.append(line.strip())
        else:
            # POSIX compliance mapping for system configuration directories
            paths = ['/etc/rc.local', '/etc/init.d', os.path.expanduser('~/.config/autostart')]
            for path in paths:
                if os.path.exists(path):
                    entries.append(f"Checked Path Active: {path}")
    except Exception:
        pass
    
    return entries if entries else ["No explicit custom configurations queried or permission denied."]

def execute_posture_checklist() -> List[Dict[str, Any]]:
    """Evaluates global system host settings for proactive endpoint defensive baseline validation."""
    posture = []
    
    # 1. Antivirus / EDR Active Reminder Verification
    posture.append({
        "control": "Endpoint Detection / Anti-Malware Suite running",
        "status": "Verification Recommended",
        "guidance": "Ensure Windows Defender or enterprise-grade EDR agents are actively monitoring process memory flags."
    })
    
    # 2. Host Firewall Status
    posture.append({
        "control": "Stateful Host Firewall Enabled",
        "status": "Verification Recommended",
        "guidance": "Confirm that Windows Advanced Firewall, ufw, or iptables blocks unauthorized inbound/outbound packets."
    })
    
    # 3. Automatic Software Updates Configuration
    posture.append({
        "control": "System Modernity & Patch Cycle Management",
        "status": "Verification Recommended",
        "guidance": "Verify updates are set to automatic to patch core driver structures against API exploitation vectors."
    })
    
    return posture