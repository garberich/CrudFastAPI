import sys
from pathlib import Path

# Add the src directory to the path for absolute imports
sys.path.insert(0, str(Path(__file__).parent))

from fastapi import FastAPI
from users.infrastructure.health import router as health_router
from item import router as item_router

from users.infrastructure.db.base import Base
from users.infrastructure.db.session import engine
from users.api.users import router as users_router

# from fastapi.middleware.cors import CORSMiddleware

'''
Add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
'''

'''
@app.middleware("http")
async def add_process_time_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Process-Time"] = "0.123"
    return response
'''

app = FastAPI(title="DDD FastAPI Example")

Base.metadata.create_all(bind=engine)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(item_router, prefix="/item", tags=["item"])
app.include_router(users_router, prefix="/user", tags=["user"])