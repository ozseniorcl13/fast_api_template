from pydantic import BaseModel
from domain.model.Status import Status

class Profile(BaseModel):
    name: str
    status: Status
    createdBy: str
    description: str
    projectManager: str
    onwer: str