from enum import Enum
from pydantic import BaseModel
from datetime import datetime

class UserType(str, Enum):
    ADMIN = "admin"
    USER = "user"

class AssignmentStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class UserCreate(BaseModel):
    username: str
    password: str
    user_type: UserType

class AssignmentCreate(BaseModel):
    task: str
    admin_username: str

class Assignment(BaseModel):
    id: str
    user_id: str
    task: str
    admin_username: str
    status: str
    created_at: datetime