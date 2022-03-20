import sys
import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from src.database import session
from src.routers.user_route import user
from src.dependency.database_dependency import get_db


app = FastAPI()


app.include_router(user,prefix="/api/v1")




if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8000)
