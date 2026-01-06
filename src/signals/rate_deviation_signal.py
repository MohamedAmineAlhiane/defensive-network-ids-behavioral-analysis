"""
rate_deviation_signal.py

This signal evaluates how much the current event rate deviates
from an established baseline rate.

It does NOT determine whether an activity is malicious.
It only quantifies deviation from expected behavior.
"""

from typing import Dict


class RateDeviationSignal:
    """
    Computes deviation score between current activity rate
    and baseline event rate.
    """

    def __init__(self, baseline_rate: float):
        """
        :param baseline_rate: Average events per minute from baseline
        """
        self.baseline_rate = max(baseline_rate, 0.01)

    def evaluate(self, current_rate: float) -> Dict[str, float | str]:
        """
        Evaluate deviation between current rate and baseline.

        :param current_rate: Current observed events per minute
        :return: Dictionary containing deviation ratio and explanation
        """
        deviation_ratio = round(current_rate / self.baseline_rate, 2)

        explanation = self._explain(deviation_ratio)

        return {
            "baseline_rate": self.baseline_rate,
            "current_rate": current_rate,
            "deviation_ratio": deviation_ratio,
            "explanation": explanation
        }

    def _explain(self, ratio: float) -> str:
        """
        Provide a human-readable explanation of the deviation.
        """
        if ratio < 1.5:
            return "Activity rate is consistent with baseline behavior."
        elif 1.5 <= ratio < 3:
            return "Activity rate shows moderate deviation from baseline."
        else:
            return "Activity rate shows significant deviation from baseline."
