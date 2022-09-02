from fastapi import FastAPI

from routes import student_router, hello_router

app = FastAPI()
app.include_router(hello_router)
app.include_router(student_router)
