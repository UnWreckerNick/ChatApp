from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth import hash_password, verify_password, create_access_token, get_current_user
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse
from sqlalchemy import select
from typing import cast
from sqlalchemy.sql import ColumnElement

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        UserCreate(**user.model_dump())

        result = await db.execute(select(User).where(cast(ColumnElement[bool], User.username == user.username)))
        existing_user = result.scalar_one_or_none()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        hashed_password = hash_password(user.password)
        new_user = User(username=user.username, hashed_password=hashed_password)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

        return UserResponse(id=new_user.id, username=new_user.username)
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

@router.post("/login/")
async def login(user_login: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(cast(ColumnElement[bool], User.username == user_login.username)))
    user = result.scalar_one_or_none()
    if not user or not verify_password(user_login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me/")
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(cast(ColumnElement[bool], User.id == user_id)))
    user_to_delete = result.scalar_one_or_none()
    if not user_to_delete:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user_to_delete)
    await db.commit()
    return {"message": "User successfully deleted"}