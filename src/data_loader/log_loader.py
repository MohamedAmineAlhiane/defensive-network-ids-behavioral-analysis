import json
from typing import List, Dict, Any


class LogLoader:
    """
    Loads synthetic or pre-collected log events from JSON files.
    """

    @staticmethod
    def load_from_json(path: str) -> List[Dict[str, Any]]:
        with open(path, "r") as f:
            return json.load(f)
