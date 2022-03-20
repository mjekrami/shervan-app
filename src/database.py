from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
engine = create_engine("postgresql://mjekrami:mamali75@database:5432/mjekrami")
session = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)
