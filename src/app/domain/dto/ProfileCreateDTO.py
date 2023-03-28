from pydantic import BaseModel

class ProfileCreateDTO(BaseModel):
    name: str
    createdBy: str
    description: str
    projectManager: str