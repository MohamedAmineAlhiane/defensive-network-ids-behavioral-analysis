from typing import List, Dict, Any

from data_loader.log_loader import LogLoader
from baseline.baseline_builder import BaselineBuilder
from signals.rate_deviation_signal import RateDeviationSignal
from scoring_engine.scoring_engine import ScoringEngine


class BehaviorAnalyzer:
    """
    Orchestrates the full behavioral analysis pipeline:
    - Loads data
    - Builds baseline
    - Evaluates behavioral signals
    - Produces confidence assessment
    """

    def __init__(self, log_path: str):
        self.log_path = log_path

    def run(self) -> Dict[str, Any]:
        # 1. Load events
        events = LogLoader.load_from_json(self.log_path)

        if not events:
            raise ValueError("No events loaded. Check log file or format.")

        # 2. Build baseline
        baseline_builder = BaselineBuilder(events)
        baseline = baseline_builder.build()

        baseline_rate = baseline.get("average_events_per_minute", 0.0)

        # 3. Evaluate behavioral signals
        signal_results = []

        rate_signal = RateDeviationSignal(baseline_rate)

        # demo: simulate higher current activity
        current_rate = baseline_rate * 2.5

        rate_result = rate_signal.evaluate(current_rate)
        signal_results.append(rate_result)

        # 4. Scoring
        scoring_engine = ScoringEngine()
        assessment = scoring_engine.evaluate(signal_results)

        # 5. Final report
        report = {
            "baseline": baseline,
            "signals": signal_results,
            "assessment": assessment
        }

        return report
