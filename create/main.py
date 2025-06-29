from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI(title="OptimumCare Recruitment")

class RegisterRequest(BaseModel):
    email: EmailStr
    phone: str
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class CandidateProfile(BaseModel):
    full_name: str
    dob: str
    address: str
    skills: List[str] = []
    experience: Optional[str] = None
    emergency_contact: Optional[str] = None

registered_users = {}
profiles = {}

@app.post("/api/auth/register")
def register(req: RegisterRequest):
    if req.email in registered_users:
        raise HTTPException(status_code=400, detail="Email already registered")
    registered_users[req.email] = {"phone": req.phone, "password": req.password}
    return {"message": "Registered"}

@app.post("/api/auth/login")
def login(req: LoginRequest):
    user = registered_users.get(req.email)
    if not user or user["password"] != req.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Logged in"}

@app.post("/api/candidate/profile")
def update_profile(profile: CandidateProfile, email: EmailStr):
    if email not in registered_users:
        raise HTTPException(status_code=404, detail="User not found")
    profiles[email] = profile
    return {"message": "Profile saved"}

@app.get("/api/candidate/profile")
def get_profile(email: EmailStr):
    profile = profiles.get(email)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
