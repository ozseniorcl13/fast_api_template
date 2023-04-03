import uvicorn
from fastapi_router_controller import ControllersTags
from fastapi import FastAPI
from config.Settings import settings
from config.Utils import controllerLoader, load_routes
from infrastructure.services.K8sClient import client

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

for route in load_routes():
    api.include_router(route)

# Register routes by Controller
# for controller in controllerLoader():
#    api.include_router(controller.router)

if __name__ == "__main__":
    uvicorn.run("main:api", host='0.0.0.0', port=settings.PORT)