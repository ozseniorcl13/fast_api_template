import uvicorn
from fastapi_router_controller import ControllersTags
from fastapi import FastAPI
from app.config.Settings import settings
from app.config.Utils import controllerLoader

api = FastAPI(
    title="Application FastAPI",
    version="0.1.0",
    openapi_tags=ControllersTags
)

# Register routes by Controller
for controller in controllerLoader():
    api.include_router(controller.router)

if __name__ == "__main__":
    uvicorn.run("main:api", host='0.0.0.0', port=settings.PORT, log_level="info")