from pydantic import BaseModel, Field

class ProfilePatchDTO(BaseModel):
    name: str