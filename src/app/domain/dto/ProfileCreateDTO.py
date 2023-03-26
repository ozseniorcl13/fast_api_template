from pydantic import BaseModel

class ProfileCreateDTO(BaseModel):
    name: str