from fastapi import APIRouter
from datetime import datetime
from app.models.alert import Alert
from app.services.alert_storage import save_alerts_to_file, load_alerts_from_file
from uuid import uuid4
import logging

logging.basicConfig(level=logging.INFO)

router = APIRouter()

alerts = load_alerts_from_file()

@router.post("/scan")
def simulate_scan():
    alert = Alert(
        id=uuid4(),
        timestamp=datetime.utcnow(),
        source="Field Unit A",
        threat_level="High",
        description="Simulated intrusion detected in perimeter zone 3."
    )

    alerts.append(alert)
    logging.info(f"Saving alert: {alert.dict()}")  # Confirm execution path
    save_alerts_to_file(alerts)
    print("ALERT STRUCTURE >>>", alert.dict())
    return {"status": "alert stored", "alert": alert.dict()}

@router.get("/alerts")
def get_alerts():
    return [a.dict() for a in alerts]
