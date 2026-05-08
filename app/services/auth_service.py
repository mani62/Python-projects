from datetime import datetime, timezone
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.schemas.user import UserUpdate
from fastapi import HTTPException
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

class AuthService:

    def register(self, db: Session, data: UserCreate):
        existing_user = db.query(User).filter(User.email == data.email).first()

        if(existing_user):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password=hash_password(data.password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    def login(self, db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()

        if not user:
            raise HTTPException(status_code=400, detail="Invalid email or password")
        
        if not verify_password(password, user.password):
            raise HTTPException(status_code=400, detail="Invalid email or password")
        
        token = create_access_token(
            {"sub": str(user.uuid)}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }
