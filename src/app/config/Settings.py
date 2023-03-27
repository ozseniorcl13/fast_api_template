import os
from typing import List
from pydantic import AnyHttpUrl, BaseSettings

class Settings(BaseSettings):
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    USE_DEBUG: bool = os.environ.get('USE_DEBUG', default=False)
    PORT: int = int(os.environ.get('PORT', default="5000"))
    KUBE_CONFIG_DEFAULT_LOCATION: str = os.environ.get('KUBE_CONFIG_DEFAULT_LOCATION', '~/.kube/config')
    KUBE_CONFIG_DEFAULT_CONTEXT: str = os.environ.get('KUBE_CONFIG_DEFAULT_CONTEXT', 'minikube')

settings = Settings()