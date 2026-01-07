"""
timing_variability_signal.py

This signal evaluates how much the timing variability of current events
deviates from the baseline variability.

It does NOT determine malicious behavior.
It only measures behavioral instability.
"""

from statistics import pstdev
from typing import List, Dict


class TimingVariabilitySignal:
    """
    Computes deviation in timing variability between
    baseline and current activity.
    """

    def __init__(self, baseline_variability: float):
        """
        :param baseline_variability: Std deviation of time gaps in baseline
        """
        self.baseline_variability = max(baseline_variability, 0.01)

    def evaluate(self, current_timestamps: List[float]) -> Dict[str, float | str]:
        """
        :param current_timestamps: List of event timestamps in seconds (relative)
        :return: deviation ratio and explanation
        """
        if len(current_timestamps) < 3:
            return {
                "baseline_variability": self.baseline_variability,
                "current_variability": 0.0,
                "deviation_ratio": 1.0,
                "explanation": "Not enough data to assess timing variability."
            }

        gaps = [
            current_timestamps[i] - current_timestamps[i - 1]
            for i in range(1, len(current_timestamps))
        ]

        current_variability = pstdev(gaps)

        deviation_ratio = round(current_variability / self.baseline_variability, 2)

        explanation = self._explain(deviation_ratio)

        return {
            "baseline_variability": self.baseline_variability,
            "current_variability": round(current_variability, 2),
            "deviation_ratio": deviation_ratio,
            "explanation": explanation
        }

    def _explain(self, ratio: float) -> str:
        if ratio < 1.5:
            return "Timing patterns are consistent with baseline behavior."
        elif 1.5 <= ratio < 3:
            return "Timing patterns show moderate instability compared to baseline."
        else:
            return "Timing patterns show significant instability compared to baseline."
