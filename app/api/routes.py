from fastapi import APIRouter, Query
from typing import Optional, List
from datetime import datetime, timedelta
from app.services.alert_storage import load_alerts_from_file, save_alert_to_file

from app.models.alert import Alert
from uuid import uuid4


router = APIRouter()

@router.get("/alerts", response_model=List[Alert])
def get_alerts(
    location: Optional[str] = Query(None),
    type: Optional[str] = Query(None),
    minutes: Optional[int] = Query(None)
):
    alerts = load_alerts_from_file()

    # Apply filters
    if location:
        alerts = [a for a in alerts if a.location and a.location.lower() == location.lower()]
    if type:
        alerts = [a for a in alerts if a.type and a.type.lower() == type.lower()]
    if minutes:
        cutoff = datetime.utcnow() - timedelta(minutes=minutes)
        alerts = [a for a in alerts if a.timestamp >= cutoff]

    return alerts
@router.post("/alerts", response_model=Alert)
def create_alert(alert: Alert):
    alert.id = uuid4()
    alert.timestamp = datetime.utcnow()
    save_alert_to_file(alert)
    return alert