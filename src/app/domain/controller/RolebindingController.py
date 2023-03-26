from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.domain.dto.RolebindingDTO import RolebindingDTO

router = APIRouter(prefix='/rolebinding')
controller = Controller(router,openapi_tag={'name':'Rolebinding'})

@controller.use()
@controller.resource()
class RolebindingController:

    @router.get("/", 
                tags=["Rolebinding"], 
                summary='List Rolebinding by Profile from Kubeflow',
                response_model=RolebindingDTO)
    def findAllByProfileId():
        return RolebindingDTO(name='role1')
