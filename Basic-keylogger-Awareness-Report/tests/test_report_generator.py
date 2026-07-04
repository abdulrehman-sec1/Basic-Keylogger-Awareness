"""Unit tests confirming structural report transformation accuracy."""

import unittest
from report_generator import build_report_payload, convert_payload_to_text

class TestReportGenerationEngine(unittest.TestCase):

    def setUp(self) -> None:
        self.os_info = {"OS": "TestOS", "OS_Release": "1.0", "OS_Version": "1.0", "Architecture": "x86", "Python_Version": "3"}
        self.processes = ["init_proc", "system_task"]
        self.startup = ["test_hook"]
        self.checklist = [{"control": "Test Control", "status": "Good", "guidance": "None"}]

    def test_payload_generation_schema(self) -> None:
        """Confirms built JSON report structures match the specified schema layout fields."""
        payload = build_report_payload(self.os_info, self.processes, self.startup, self.checklist, 100.0)
        
        self.assertIn("report_metadata", payload)
        self.assertIn("system_posture_telemetry", payload)
        self.assertEqual(payload["educational_metrics"]["quiz_percentage_score"], 100.0)

    def test_plain_text_serialization_output(self) -> None:
        """Verifies that generated reports transform into human-readable plain text without formatting loss."""
        payload = build_report_payload(self.os_info, self.processes, self.startup, self.checklist, 80.0)
        text_out = convert_payload_to_text(payload)
        
        self.assertIn("SECURITY AWARENESS COMPLIANCE REPORT", text_out)
        self.assertIn("TestOS", text_out)

if __name__ == "__main__":
    unittest.main()