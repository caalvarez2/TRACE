from pydantic import BaseModel
from typing import List, Optional

# User and Role models
class User(BaseModel):
    id: int
    name: str
    role: str  # "analyst" or "lead_analyst"
    permissions: List[str] = []

class Analyst(BaseModel):
    id: int
    name: str
    assigned_projects: List[int] = []
    assigned_tasks: List[int] = []

class LeadAnalyst(Analyst):
    # Inherits all fields from Analyst; additional Lead Analyst methods will be implemented in the endpoints.
    pass

class Project(BaseModel):
    id: int
    name: str

class Task(BaseModel):
    id: int
    description: str
    project_id: int

# Web tree node model for the WebTreeView
class TreeNode(BaseModel):
    id: int
    name: str
    children: Optional[List["TreeNode"]] = []

TreeNode.update_forward_refs()
