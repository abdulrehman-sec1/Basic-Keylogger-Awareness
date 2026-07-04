"""Transforms operational telemetry and quiz metrics into JSON data layers and TXT formats."""

import datetime
from typing import Dict, Any, List
from config import SCORE_EXCELLENT, SCORE_GOOD

def evaluate_awareness_rating(score: float) -> str:
    """Computes an overarching security posture assessment from quiz metrics."""
    if score >= SCORE_EXCELLENT:
        return "EXCELLENT (Strong Defensive Foundations)"
    elif score >= SCORE_GOOD:
        return "GOOD (Proficient Core Understanding - Needs Fine Tuning)"
    return "WARNING (Defensive Knowledge Gaps Identified - Review Recommended)"

def generate_recommendations(score: float, platform_name: str) -> List[str]:
    """Assembles programmatic mitigation checklists tailored to the environment context."""
    recommendations = [
        "Enforce strict multi-factor authentication across all active systems to decouple compromised inputs from authentication states."
    ]
    if score < SCORE_EXCELLENT:
        print("Appending structural education protocols...")
        recommendations.append("Dedicate operational time to reviewing the core 'Prevention and Detection' architecture frameworks.")
    
    if platform_name == "Windows":
        recommendations.append("Regularly check low-level execution logs and review AppLocker or Software Restriction Policies.")
    else:
        recommendations.append("Ensure auditd policies log unusual terminal execve calls or strange unsigned tasks.")
        
    return recommendations

def build_report_payload(os_info: Dict[str, str], processes: List[str], startup_items: List[str], 
                         checklist: List[Dict[str, Any]], quiz_score: float) -> Dict[str, Any]:
    """Aggregates all application assessment telemetry into a single comprehensive data schema."""
    rating = evaluate_awareness_rating(quiz_score)
    recs = generate_recommendations(quiz_score, os_info.get("OS", "Unknown"))
    
    return {
        "report_metadata": {
            "generated_at": datetime.datetime.now().isoformat(),
            "framework_version": "1.0.0",
            "compliance_intent": "Cybersecurity Educational Awareness & Self Assessment Only"
        },
        "system_posture_telemetry": {
            "os_metadata": os_info,
            "monitored_process_count": len(processes),
            "startup_hooks_detected": startup_items,
            "host_controls_checklist": checklist
        },
        "educational_metrics": {
            "quiz_percentage_score": quiz_score,
            "overall_awareness_rating": rating
        },
        "tailored_defensive_recommendations": recs
    }

def convert_payload_to_text(payload: Dict[str, Any]) -> str:
    """Converts a structured JSON report payload into a highly readable, human-facing plain text report."""
    meta = payload["report_metadata"]
    sys_tel = payload["system_posture_telemetry"]
    metrics = payload["educational_metrics"]
    recs = payload["tailored_defensive_recommendations"]
    
    lines = [
        "============================================================",
        "          SECURITY AWARENESS COMPLIANCE REPORT              ",
        "============================================================",
        f"Generated At          : {meta['generated_at']}",
        f"Intent Statement      : {meta['compliance_intent']}",
        "------------------------------------------------------------",
        "1. ENVIRONMENT METADATA",
        "------------------------------------------------------------"
    ]
    for k, v in sys_tel["os_metadata"].items():
        lines.append(f"  {k:<20}: {v}")
        
    lines.extend([
        f"  Active Monitored Processes Snapshotted: {sys_tel['monitored_process_count']}",
        "------------------------------------------------------------",
        "2. AWARENESS METRICS & EVALUATION",
        "------------------------------------------------------------",
        f"  Quiz Correctness Metric  : {metrics['quiz_percentage_score']}%",
        f"  Evaluated Threat Rating  : {metrics['overall_awareness_rating']}",
        "------------------------------------------------------------",
        "3. PROACTIVE SYSTEM COMPLIANCE POSTURE CHECKLIST",
        "------------------------------------------------------------"
    ])
    
    for idx, item in enumerate(sys_tel["host_controls_checklist"], 1):
        lines.append(f"  [{idx}] Control: {item['control']}")
        lines.append(f"      Status:  {item['status']}")
        lines.append(f"      Context: {item['guidance']}")
        
    lines.extend([
        "------------------------------------------------------------",
        "4. REMEDIATION & DEFENSIVE ACTION STRATEGIES",
        "------------------------------------------------------------"
    ])
    for idx, rec in enumerate(recs, 1):
        lines.append(f"  * {rec}")
        
    lines.append("============================================================")
    return "\n".join(lines)