from fastapi import FastAPI

from database import Base, engine
from app.models.user import User
from app.routers.user import router as user_router


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)


@app.get("/")
def home():
    return {"message": "Hello Backend"}