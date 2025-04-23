import json
from typing import List
from app.models.alert import Alert
import logging
import os

ALERTS_FILE = "alerts.json"

def save_alerts_to_file(alerts: List[Alert]) -> None:
    try:
        with open(ALERTS_FILE, "w") as f:
            json.dump(
                [alert.model_dump(mode="json") for alert in alerts],
                f,
                indent=4
            )
        logging.info("✅ Alerts successfully saved.")
    except Exception as e:
        logging.error(f"❌ Failed to save alerts: {e}")


def load_alerts_from_file() -> List[Alert]:
    if not os.path.exists(ALERTS_FILE):
        logging.warning("⚠️ No alerts.json file found. Starting with an empty list.")
        return []

    try:
        with open(ALERTS_FILE, "r") as f:
            raw_alerts = json.load(f)
            return [Alert(**alert) for alert in raw_alerts]
    except Exception as e:
        logging.error(f"Failed to load alerts from file: {e}")
        return []
