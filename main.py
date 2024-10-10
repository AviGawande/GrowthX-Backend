
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import bcrypt
from datetime import datetime
from bson import ObjectId
import uvicorn

from models import UserCreate, AssignmentCreate, UserType, AssignmentStatus, Assignment
from database import Database

app = FastAPI(title="Assignment Submission Portal")
security = HTTPBasic()
db = Database()

# Helper functions
def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Authentication dependency
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = db.get_user(credentials.username)
    if not user or not verify_password(credentials.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user

# User Routes
@app.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate):
    """Register a new user or admin"""
    existing_user = db.get_user(user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    user_data = {
        "username": user.username,
        "password": hash_password(user.password),
        "user_type": user.user_type,
        "created_at": datetime.utcnow()
    }
    
    result = db.create_user(user_data)
    return {"message": "Registration successful", "id": str(result.inserted_id)}

@app.post("/login")
async def login(current_user: dict = Depends(get_current_user)):
    """Login for both users and admins"""
    return {
        "message": "Login successful",
        "username": current_user["username"],
        "user_type": current_user["user_type"]
    }

@app.post("/upload")
async def upload_assignment(
    assignment: AssignmentCreate,
    current_user: dict = Depends(get_current_user)
):
    """Upload a new assignment (User only)"""
    if current_user["user_type"] != UserType.USER:
        raise HTTPException(status_code=403, detail="Only users can upload assignments")

    admin = db.get_user(assignment.admin_username)
    if not admin or admin["user_type"] != UserType.ADMIN:
        raise HTTPException(status_code=404, detail="Admin not found")

    assignment_data = {
        "user_id": current_user["username"],
        "task": assignment.task,
        "admin_username": assignment.admin_username,
        "status": AssignmentStatus.PENDING,
        "created_at": datetime.utcnow()
    }
    
    result = db.create_assignment(assignment_data)
    return {"message": "Assignment uploaded successfully", "id": str(result.inserted_id)}

@app.get("/admins")
async def get_admins():
    """Get list of all admin usernames"""
    admins = db.get_admins()
    return admins

@app.get("/assignments")
async def get_assignments(current_user: dict = Depends(get_current_user)):
    """Get all assignments assigned to the admin (Admin only)"""
    if current_user["user_type"] != UserType.ADMIN:
        raise HTTPException(status_code=403, detail="Only admins can view assignments")

    assignments = db.get_assignments(current_user["username"])
    return [Assignment(id=str(a["_id"]), **a) for a in assignments]

@app.post("/assignments/{assignment_id}/{action}")
async def update_assignment_status(
    assignment_id: str,
    action: str,
    current_user: dict = Depends(get_current_user)
):
    """Accept or reject an assignment (Admin only)"""
    try:
        # Verify admin status
        if current_user.get("user_type") != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Only admins can update assignments"
            )

        # Validate action
        if action not in ["accept", "reject"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid action"
            )

        # Convert string ID to ObjectId
        try:
            assignment_id_obj = ObjectId(assignment_id)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid assignment ID format"
            )

        # Get assignment
        assignment = db.get_assignment_by_id(assignment_id_obj)
        if not assignment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assignment not found"
            )

        # Verify admin ownership
        if assignment["admin_username"] != current_user["username"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You can only update assignments assigned to you"
            )

        # Update assignment
        status_value = "accepted" if action == "accept" else "rejected"
        update_data = {
            "status": status_value,
            "updated_at": datetime.utcnow()
        }
        
        result = db.update_assignment(assignment_id_obj, update_data)
        if not result or result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update assignment"
            )

        return {"message": f"Assignment {action}ed successfully"}
        
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)