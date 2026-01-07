from baseline.baseline_builder import BaselineBuilder
from signals.rate_deviation_signal import RateDeviationSignal
from scoring_engine.scoring_engine import ScoringEngine


def run_demo():
    # Synthetic baseline events
    baseline_events = [
        {"timestamp": "2026-01-01T10:00:00", "source_id": "A", "event_type": "login"},
        {"timestamp": "2026-01-01T10:01:00", "source_id": "A", "event_type": "login"},
        {"timestamp": "2026-01-01T10:02:00", "source_id": "B", "event_type": "query"},
        {"timestamp": "2026-01-01T10:03:00", "source_id": "A", "event_type": "login"},
    ]

    baseline_builder = BaselineBuilder(baseline_events)
    baseline = baseline_builder.build()

    baseline_rate = baseline["average_events_per_minute"]

    # Simulated current activity
    current_rate = baseline_rate * 2.5

    signal = RateDeviationSignal(baseline_rate)
    signal_result = signal.evaluate(current_rate)

    scoring = ScoringEngine()
    assessment = scoring.evaluate([signal_result])

    print("Baseline:", baseline)
    print("Signal Result:", signal_result)
    print("Final Assessment:", assessment)


if __name__ == "__main__":
    run_demo()
