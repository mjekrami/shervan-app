from pydantic import BaseModel


class UesrSchema(BaseModel):
    id:int
    name:str
    age:int
    is_active:bool
    created_at:str

