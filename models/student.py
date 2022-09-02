from pydantic import BaseModel


class Student(BaseModel):
    name: str
    age: int
    email: str

    class Config:
        orm_mode = True
