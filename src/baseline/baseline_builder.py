""

baseline_builder.py
This module is responsible for building a baseline model that represents
normal behavior observed in network or system activity logs.
The baseline is purely descriptive and does NOT perform detection,
classification, or enforcement.

""

from collections import Counter
from datetime import datetime
from statistics import mean, pstdev
from typing import List, Dict, Any


class BaselineBuilder:
    """
    Builds a behavioral baseline from historical event data.
    """

    def __init__(self, events: List[Dict[str, Any]]):
        """
        :param events: A list of event dictionaries.
                       Each event is expected to contain at least:
                       - timestamp (ISO 8601 string)
                       - source_id (e.g., IP, host, session)
                       - event_type (string)
        """
        self.events = events
        self.timestamps = self._parse_timestamps()

    def _parse_timestamps(self) -> List[datetime]:
        """
        Convert timestamp strings into datetime objects.
        """
        parsed = []
        for event in self.events:
            try:
                parsed.append(
                    datetime.fromisoformat(event["timestamp"])
                )
            except (KeyError, ValueError):
                continue
        return sorted(parsed)

    def average_event_rate_per_minute(self) -> float:
        """
        Calculate the average number of events per minute.
        """
        if len(self.timestamps) < 2:
            return 0.0

        duration_seconds = (self.timestamps[-1] - self.timestamps[0]).total_seconds()
        duration_minutes = max(duration_seconds / 60, 1)

        return round(len(self.timestamps) / duration_minutes, 2)

    def timing_variability(self) -> float:
        """
        Calculate the population standard deviation of time gaps between events.
        """
        if len(self.timestamps) < 3:
            return 0.0

        gaps = [
            (self.timestamps[i] - self.timestamps[i - 1]).total_seconds()
            for i in range(1, len(self.timestamps))
        ]

        return round(pstdev(gaps), 2)

    def common_event_types(self) -> Dict[str, int]:
        """
        Identify the most common event types.
        """
        event_types = [
            event.get("event_type", "unknown")
            for event in self.events
        ]

        return dict(Counter(event_types))

    def common_sources(self) -> Dict[str, int]:
        """
        Identify the most common sources generating events.
        """
        sources = [
            event.get("source_id", "unknown")
            for event in self.events
        ]

        return dict(Counter(sources))

    def build(self) -> Dict[str, Any]:
        """
        Build and return the baseline model as a dictionary.
        """
        return {
            "total_events": len(self.events),
            "average_events_per_minute": self.average_event_rate_per_minute(),
            "timing_variability_seconds": self.timing_variability(),
            "common_event_types": self.common_event_types(),
            "common_sources": self.common_sources(),
        }
