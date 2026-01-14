from fastapi import FastAPI
from shared.infrastructure.health import router as health_router
from shared.domain.api import router as item_router
# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(item_router, prefix="/item", tags=["item"])