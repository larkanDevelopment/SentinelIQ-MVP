from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from uuid import UUID

class Alert(BaseModel):
    id: UUID
    timestamp: datetime
    source: str
    threat_level: str
    description: Optional[str] = None
    location: Optional[str] = None       
    type: Optional[str] = None            
