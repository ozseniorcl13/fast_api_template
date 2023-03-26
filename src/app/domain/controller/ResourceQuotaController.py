from typing import List
from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.domain.dto.ResourceQuotaDTO import ResourceQuotaDTO

router = APIRouter(prefix='/resourcequota')
controller = Controller(router,openapi_tag={'name':'ResourceQuota'})

@controller.use()
@controller.resource()
class ResourceQuotaController:

    @router.get("/{id}", 
                tags=["ResourceQuota"], 
                summary='Get ResourceQuota by ID from Kubeflow',
                status_code=status.HTTP_200_OK,
                response_model=List[ResourceQuotaDTO])
    def findById(id: str):
        list: List = []
        list.append(ResourceQuotaDTO(name='role1'))
        return list
