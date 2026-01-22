import sys
from pathlib import Path
from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware

# Add the src directory to the path for absolute imports
sys.path.insert(0, str(Path(__file__).parent))

# Comun infrastructure
from infrastructure.db.base import Base
from infrastructure.db.dependencies import engine

# Models - Used for creating tables by SQLAlchemy
import users.infrastructure.db.models
import customers.infrastructure.db.models

# Routes
from infrastructure.health import router as health_router
from item import router as item_router
from users.api.users import router as users_router
from customers.api.customers import router as customers_router

app = FastAPI(title="DDD FastAPI Example")
Base.metadata.create_all(bind=engine)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(item_router, prefix="/item", tags=["item"])
app.include_router(users_router, prefix="/user", tags=["user"])
app.include_router(customers_router, prefix="/customer", tags=["customer"])
