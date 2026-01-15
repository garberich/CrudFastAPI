from fastapi import FastAPI
from shared.infrastructure.health import router as health_router
from shared.domain.item import router as item_router

from shared.infrastructure.db.base import Base
from shared.infrastructure.db.session import engine
from shared.api.users import router as users_router

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