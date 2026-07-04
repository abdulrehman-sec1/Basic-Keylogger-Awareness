"""Unit tests confirming compliance scoring and rating mechanics."""

import unittest
from report_generator import evaluate_awareness_rating, generate_recommendations

class TestAwarenessLogic(unittest.TestCase):

    def test_excellent_rating_boundary(self) -> None:
        """Verifies that an excellent score maps to the correct structural text level."""
        result = evaluate_awareness_rating(90.0)
        self.assertIn("EXCELLENT", result)

    def test_warning_rating_boundary(self) -> None:
        """Verifies that low performance triggers a security alert categorization status."""
        result = evaluate_awareness_rating(40.0)
        self.assertIn("WARNING", result)

    def test_recommendation_generation_logic(self) -> None:
        """Verifies that defensive recommendations change appropriately based on host environments."""
        recs_windows = generate_recommendations(100.0, "Windows")
        recs_linux = generate_recommendations(50.0, "Linux")
        
        self.assertTrue(any("Windows" in r or "AppLocker" in r for r in recs_windows))
        self.assertTrue(any("auditd" in r for r in recs_linux))

if __name__ == "__main__":
    unittest.main()