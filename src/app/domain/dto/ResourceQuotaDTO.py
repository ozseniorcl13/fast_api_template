from pydantic import BaseModel

class ResourceQuotaDTO(BaseModel):
    name: str