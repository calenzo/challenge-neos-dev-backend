from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.database.settings import create_tables
from app.interactors.response_api_interactor import ResponseError
from app.routes import (
    user_routes,
    link_routes,
)


create_tables()

app = FastAPI()


@app.exception_handler(ResponseError)
async def unicorn_exception_handler(request: Request, exc: ResponseError):
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.error(),
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router)
app.include_router(link_routes.router)
