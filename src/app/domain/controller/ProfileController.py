from typing import List, Optional
from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse
from domain.dto import ResourceQuotaDTO
from domain.dto.ProfileCreateDTO import ProfileCreateDTO
from domain.dto.ProfileResponseDTO import ProfileResponseDTO
from domain.model.Profile import Profile
from domain.services.ProfileService import profileService
from config.Settings import settings
from domain.model.Status import Status

router = APIRouter(prefix='/profile')
controller = Controller(router,openapi_tag={'name':'Profile'})

@controller.use()
@controller.resource()
class ProfileController:

    @router.get("/", 
                tags=["Profile"], 
                summary='List profiles from Kubeflow',
                response_model=List[Profile])
    def findAll():
        return profileService.findAll()

    @router.post("/", tags=["Profile"], 
                 status_code=status.HTTP_201_CREATED, 
                 summary='Create profile in the Kubeflow', 
                 response_model=Profile)
    async def create(profileCreate: ProfileCreateDTO):
       profile = Profile(
           name=profileCreate.name,
           createdBy=profileCreate.createdBy,
           description=profileCreate.description,
           onwer=settings.OWNER,
           projectManager=profileCreate.projectManager,
           status=Status.active
       )
            
       return profileService.create(profile)
        
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
                status_code=status.HTTP_204_NO_CONTENT,
                summary='Find and update a profile by ID',        
                response_model=None)
    async def findAndUpdateById(id: str, profile: ProfileCreateDTO): 
        profileService.findAndUpdate()
        return 
        
    
