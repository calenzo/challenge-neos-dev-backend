from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.settings import create_tables
from app.routes import (
    user_routes,
    link_routes,
)

create_tables()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)
app.include_router(link_routes.router)
