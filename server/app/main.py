# Entry point for the FastAPI application.
# Registers all routers and configures CORS.
# Keep this file thin — no business logic here.
from fastapi import FastAPI
# from app.routes.auth import router as auth_router
from app.database.base import Base
from app.database.session import engine

app = FastAPI()

# Create tables automatically
Base.metadata.create_all(bind=engine)

# include routes
# app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Mentree AI API Running"}