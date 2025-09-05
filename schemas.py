from pydantic import BaseModel
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
# ---- User Schemas ----
class UserBase(BaseModel):
    username: str
    role: str

class UserCreate(UserBase):
    password: str   # plain text password (will be hashed)

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
# ---- Lead Schemas ----
class LeadBase(BaseModel):
    customer_id: int
    status: str
    notes: str

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
# ---- Campaign Schemas ----
class CampaignBase(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int

    class Config:
        orm_mode = True

# ---- Ticket Schemas ----
class TicketBase(BaseModel):
    customer_id: int
    issue: str
    status: str

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str
