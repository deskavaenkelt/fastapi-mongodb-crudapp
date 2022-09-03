from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import student_router, hello_router

client_apps = ['http://localhost:3000']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello_router)
app.include_router(student_router)
