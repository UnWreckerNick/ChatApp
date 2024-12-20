from fastapi import FastAPI
from app.database import init_db
from app.routes import chats, messages, users, websocket
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(application: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan, title="Chat App with WebSocket")

app.include_router(chats.router, prefix="/chats", tags=["Chats"])
app.include_router(messages.router, prefix="/messages", tags=["Messages"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(websocket.router, prefix="/ws", tags=["WebSocket"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Chat App!"}