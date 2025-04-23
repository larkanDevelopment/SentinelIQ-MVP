from fastapi import FastAPI
from app.api.routes import router as main_router
from app.api.status import router as status_router
from app.api.users import router as users_router
from app.api import scan


app = FastAPI()

app.include_router(main_router)
app.include_router(status_router)
app.include_router(users_router)
app.include_router(scan.router)