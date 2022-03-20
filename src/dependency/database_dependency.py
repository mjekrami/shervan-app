from src.database import session

# Database Dependency
def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()
