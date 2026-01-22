from infrastructure.db.session import get_engine, get_sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = get_engine(DATABASE_URL)
SessionLocal = get_sessionmaker(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
