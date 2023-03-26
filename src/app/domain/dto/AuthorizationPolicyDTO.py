from pydantic import BaseModel

class AuthorizationPolicyDTO(BaseModel):
    name: str