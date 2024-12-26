from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    messages = relationship("Message", back_populates="user")
    chats = relationship("ChatUser", back_populates="user")
    refresh_token = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")

class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    messages = relationship("Message", back_populates="chat")
    participants = relationship("ChatUser", back_populates="chat")

class ChatUser(Base):
    __tablename__ = "chat_users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))
    chat = relationship("Chat", back_populates="participants")
    user = relationship("User", back_populates="chats")

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    chat = relationship("Chat", back_populates="messages")
    user = relationship("User", back_populates="messages")

class RefreshToken(Base):
    __tablename__ = "refresh_token"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="refresh_token")