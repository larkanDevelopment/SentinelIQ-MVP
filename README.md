# SentinelIQ

SentinelIQ is a real-time alert intelligence system designed to simulate high-risk field operations for military contractors, intelligence teams, and tactical response units. The system enables fast ingestion, filtering, and triage of mission-critical alerts with future-facing support for scan-based enrichments like facial recognition and object detection.

This project serves as a backend-focused showcase for modular architecture, structured data modeling, and system planning under high-stakes use cases.

## Features

- Alert creation via API with support for:
  - Timestamp
  - Source
  - Threat level
  - Description
  - Location
  - Type
- Query-based filtering of alerts by:
  - Location
  - Type
  - Time range (last X minutes)
- Data persistence to JSON for lightweight offline use
- Swagger UI for self-documenting endpoints
- Clean codebase with separation of concerns (models, routes, services)

## Tech Stack

- FastAPI (web framework)
- Pydantic (data validation and serialization)
- Python 3.10+
- JSON file storage (for MVP)
- Uvicorn (ASGI server)

## Example Alert (Enriched)

```json
{
  "id": "11111111-1111-1111-1111-111111111111",
  "timestamp": "2025-04-23T20:02:11.125045",
  "source": "Drone Patrol Bravo",
  "threat_level": "High",
  "description": "Thermal signature detected near ammo depot. Possible hostile.",
  "location": "Baghdad",
  "type": "thermal_intrusion"
}
