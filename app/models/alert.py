from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Alert(BaseModel):
    id: int
    timestamp: datetime
    source: str
    threat_level: str  # "Low", "Medium", "High", "Critical"
    description: Optional[str] = None
