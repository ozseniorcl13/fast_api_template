from fastapi_router_controller import Controller
from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from domain.dto.AuthorizationPolicyDTO import AuthorizationPolicyDTO

router = APIRouter(prefix='/authorizationpolicy')
controller = Controller(router,openapi_tag={'name':'AuthorizationPolicy'})

@controller.use()
@controller.resource()
class AuthorizationPolicyController:

    @router.get("/", 
                tags=["AuthorizationPolicy"], 
                summary='List AuthorizationPolicy by Profile from Kubeflow',
                response_model=AuthorizationPolicyDTO)
    def findAllByProfileId():
        return AuthorizationPolicyDTO(name='policy1')
