"""
scoring_engine.py

This module aggregates behavioral signal outputs and produces
a high-level confidence assessment of observed activity.

The scoring engine does NOT label activity as malicious.
It classifies confidence levels based on deviation from baseline behavior.
"""

from typing import List, Dict


class ScoringEngine:
    """
    Aggregates signal evaluations and determines a confidence level.
    """

    def __init__(self):
        self.levels = {
            "NORMAL": 0,
            "SUSPICIOUS": 1,
            "ANOMALOUS": 2
        }

    def evaluate(self, signal_results: List[Dict]) -> Dict[str, str | List[str]]:
        """
        Evaluate aggregated signals and return a confidence assessment.

        :param signal_results: List of signal evaluation dictionaries
        :return: Assessment result with confidence level and explanations
        """
        confidence_level = "NORMAL"
        explanations = []

        for result in signal_results:
            ratio = result.get("deviation_ratio", 1)
            explanation = result.get("explanation", "")

            explanations.append(explanation)

            level = self._classify_ratio(ratio)

            if self.levels[level] > self.levels[confidence_level]:
                confidence_level = level

        return {
            "confidence_level": confidence_level,
            "explanations": explanations
        }

    def _classify_ratio(self, ratio: float) -> str:
        """
        Classify deviation ratio into a confidence level.
        """
        if ratio < 1.5:
            return "NORMAL"
        elif 1.5 <= ratio < 3:
            return "SUSPICIOUS"
        else:
            return "ANOMALOUS"
