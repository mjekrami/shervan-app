from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime,String,Boolean,Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(255),nullable=False)
    age = Column(Integer,nullable=False,default="18")
    is_active = Column(Boolean,default=False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    
    def __repr__(self) -> str:
        return "<{}> {}".format(self.id,self.name)
