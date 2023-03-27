import uvicorn
from fastapi_router_controller import ControllersTags
from fastapi import FastAPI
from app.config.Settings import settings
from app.config.Utils import controllerLoader
from app.infrastructure.services.K8sClient import client

api = FastAPI(
    title="Application FastAPI",
    version="0.1.0",
    openapi_tags=ControllersTags    
)

# Load K8sClient
client.connect(
    context=settings.KUBE_CONFIG_DEFAULT_CONTEXT,
    pathFile=settings.KUBE_CONFIG_DEFAULT_LOCATION
)

# Register routes by Controller
for controller in controllerLoader():
    api.include_router(controller.router)

if __name__ == "__main__":
    uvicorn.run("main:api", host='0.0.0.0', port=settings.PORT, log_level="info")