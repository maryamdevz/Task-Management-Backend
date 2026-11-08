from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.users.router import user_routes
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(engine)

origins = [
    "http://localhost:5173"
]



app = FastAPI(title = "Task Management App")
app.include_router(task_routes)
app.include_router(user_routes)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)