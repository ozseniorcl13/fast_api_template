from typing import List, Optional
from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from app.domain.dto import ResourceQuotaDTO
from app.domain.dto.ProfileCreateDTO import ProfileCreateDTO
from app.domain.dto.ProfileResponseDTO import ProfileResponseDTO
from app.domain.model.Profile import Profile
from app.domain.services.ProfileService import profileService
from pydantic.fields import ModelField

router = APIRouter(prefix='/profile')
controller = Controller(router,openapi_tag={'name':'Profile'})

@controller.use()
@controller.resource()
class ProfileController:

    def __init__(self) -> None:
        pass

    @router.get("/", tags=["Profile"], summary='List profiles from Kubeflow')
    def findAll():
        return ProfileResponseDTO(name='Charles')

    @router.post("/", tags=["Profile"], 
                 status_code=status.HTTP_201_CREATED, 
                 summary='Create profile in the Kubeflow', 
                 response_model=ProfileResponseDTO)
    async def create(profile: ProfileCreateDTO):
       return ProfileResponseDTO(name=profile.name, detail='Created profile')
        
    @router.get("/{id}", tags=["Profile"],
                status_code=status.HTTP_200_OK, 
                summary='Get profile by ID', 
                response_model=ProfileResponseDTO)
    async def findById(id: str):
        return ProfileResponseDTO(name='profile-name', detail='Profile sample')
    
    @router.delete("/{id}",tags=["Profile"],
                status_code=status.HTTP_204_NO_CONTENT, 
                summary='Find and delete a profile by ID', 
                response_model=None)
    async def findAndDeleteById(id: str):
        print(f'Delete: {id}')    
        return
    
    @router.patch("/{id}",tags=["Profile"],
                status_code=status.HTTP_200_OK,
                summary='Find and update a profile by ID',        
                response_model=List[Profile])
    async def findAndUpdateById(id: str, profile: ProfileCreateDTO): 
        return profileService.findAll()
        
    
