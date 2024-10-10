from pymongo import MongoClient
from decouple import config
from bson import ObjectId

# MongoDB Connection
client = MongoClient(config('MONGODB_URL', default='mongodb://localhost:27017'))
db = client[config('DB_NAME', default='assignmentPortal')]

# Collections
users_collection = db["users"]
assignments_collection = db["assignments"]

class Database:
    def create_user(self, user_data):
        return users_collection.insert_one(user_data)
    
    def get_user(self, username):
        return users_collection.find_one({"username": username})
    
    def create_assignment(self, assignment_data):
        return assignments_collection.insert_one(assignment_data)
    
    def get_assignments(self, admin_username):
        return list(assignments_collection.find({"admin_username": admin_username}))
    
    def update_assignment(self, assignment_id, update_data):
        if isinstance(assignment_id, str):
            try:
                assignment_id = ObjectId(assignment_id)
            except:
                return None
        return assignments_collection.update_one(
            {"_id": assignment_id},
            {"$set": update_data}
        )
    
    def get_admins(self):
        return list(users_collection.find({"user_type": "admin"}, {"username": 1, "_id": 0}))
    
    def get_assignment_by_id(self, assignment_id):
        if isinstance(assignment_id, str):
            try:
                assignment_id = ObjectId(assignment_id)
            except:
                return None
        return assignments_collection.find_one({"_id": assignment_id})