from fastapi import APIRouter
from datetime import datetime
from app.models.alert import Alert
from typing import List

router = APIRouter()

alerts: List[Alert] = []
alert_id_counter = 1

@router.post("/scan")
def simulate_scan():
    global alert_id_counter

    alert = Alert(
        id=alert_id_counter,
        timestamp=datetime.utcnow(),
        source="Field Unit A",
        threat_level="High",
        description="Simulated intrusion detected in perimeter zone 3."
    )

    alerts.append(alert)
    alert_id_counter += 1

    return {"status": "alert stored", "alert": alert.dict()}