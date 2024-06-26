from claims.config.config import get_config
from fastapi import FastAPI, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.exception_handlers import http_exception_handler
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from asgi_correlation_id import (
    CorrelationIdMiddleware,
    correlation_id,
)
from database import Database
from claims.controllers.claims import router as claims_router


# Initialize FastAPI
app = FastAPI()

# Load environment variables
DB_USER = get_config("DB_USER")
DB_PASS = get_config("DB_PASS")
DB_HOST = get_config("DB_HOST")
DB_NAME = get_config("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

engine_args = {
    "pool_size": 20,  # Maximum number of database connections in the pool
    "max_overflow": 50,  # Maximum number of connections that can be created beyond the pool_size
    "pool_timeout": 30,  # Timeout value in seconds for acquiring a connection from the pool
    "pool_recycle": 1800,  # Recycle connections after this number of seconds (optional)
    "pool_pre_ping": False,  # Enable connection health checks (optional)
}

app.add_middleware(DBSessionMiddleware, db_url=DB_URL, engine_args=engine_args)
app.add_middleware(CorrelationIdMiddleware)

app.include_router(claims_router, prefix="/api/claim")


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return await http_exception_handler(
        request,
        HTTPException(
            500,
            "Internal server error",
            headers={"X-Request-ID": correlation_id.get() or ""},
        ),
    )


# Configure CORS middleware
origins = [
    "*",  # Allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Request-ID"],
)

database = Database(DB_URL)
engine = database.get_engine()

@app.get("/api/health")
def health_check():
    return {"status": "ok"}


