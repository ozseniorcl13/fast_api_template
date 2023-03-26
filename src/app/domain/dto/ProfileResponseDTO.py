from pydantic import BaseModel

class ProfileResponseDTO(BaseModel):
    name: str
    detail: str