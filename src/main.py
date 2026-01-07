from baseline.baseline_builder import BaselineBuilder
from signals.rate_deviation_signal import RateDeviationSignal
from signals.timing_variability_signal import TimingVariabilitySignal
from scoring_engine.scoring_engine import ScoringEngine
from datetime import datetime


def run_demo():
    # Synthetic baseline events
    baseline_events = [
        {"timestamp": "2026-01-01T10:00:00", "source_id": "A", "event_type": "login"},
        {"timestamp": "2026-01-01T10:01:00", "source_id": "A", "event_type": "login"},
        {"timestamp": "2026-01-01T10:02:00", "source_id": "B", "event_type": "query"},
        {"timestamp": "2026-01-01T10:03:00", "source_id": "A", "event_type": "login"},
    ]

    # ---- Baseline Phase ----
    baseline_builder = BaselineBuilder(baseline_events)
    baseline = baseline_builder.build()

    baseline_rate = baseline["average_events_per_minute"]
    baseline_variability = baseline["timing_variability_seconds"]

    # ---- Simulated Current Activity ----
    current_rate = baseline_rate * 2.5  # frequency deviation

    current_events = [
        "2026-01-01T11:00:00",
        "2026-01-01T11:00:05",
        "2026-01-01T11:00:07",
        "2026-01-01T11:01:30",
        "2026-01-01T11:01:32",
    ]

    # convert to relative seconds
    parsed = [datetime.fromisoformat(t) for t in current_events]
    base_time = parsed[0]
    current_timestamps = [
        (t - base_time).total_seconds() for t in parsed
    ]

    # ---- Signals ----
    rate_signal = RateDeviationSignal(baseline_rate)
    rate_result = rate_signal.evaluate(current_rate)

    timing_signal = TimingVariabilitySignal(baseline_variability)
    timing_result = timing_signal.evaluate(current_timestamps)

    # ---- Scoring ----
    scoring = ScoringEngine()
    assessment = scoring.evaluate([rate_result, timing_result])

    # ---- Output ----
    print("Baseline:", baseline)
    print("Rate Signal:", rate_result)
    print("Timing Signal:", timing_result)
    print("Final Assessment:", assessment)


if __name__ == "__main__":
    run_demo()
