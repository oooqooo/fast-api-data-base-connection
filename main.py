from fastapi import FastAPI
from src.tasks.models import tasks
from src.utils.db import Base,engine
from src.tasks.router import task_router1
from src.users.router import api_router2

Base.metadata.create_all(bind=engine)
app=FastAPI()
app.include_router(task_router1)
app.include_router(api_router2)


