import os
from kubernetes import client, config
from app.config.Settings import settings
from fastapi.logger import logger

class K8sClient:

    def __init__(self) -> None:
        self.in_cluster = None        

    def connect(self, context: str, pathFile: str):
        self.in_cluster = None
        if self.__is_running_in_k8s__():
            config.load_incluster_config()
            self.in_cluster = True
            print(f'K8Client connected in cluster.')
        else:
            config.load_kube_config(
                config_file=pathFile,
                context=context,
                client_configuration=None,
                persist_config=None,
            )
            self.in_cluster = False
            print(f'K8Client connected to cluster by: {pathFile}.')         
            #logger.logger.info(f'K8Client connected to cluster by: {pathFile}.')
            #logger = logging.getLogger('fastapi')
            
            #gunicorn_logger = logging.getLogger('gunicorn.error')
            #logger.handlers = gunicorn_logger.handlers
            
            #logger.setLevel(logging.INFO)
            #logger.debug(f'K8Client connected to cluster by: {pathFile}.')
            #logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:     %(message)s')
            #logging.info(f'K8Client connected to cluster by: {pathFile}.')
            #print(f'K8Client connected to cluster by: {pathFile}.')
            

    def __is_running_in_k8s__(self):
        return os.path.isdir("/var/run/secrets/kubernetes.io/")


client = K8sClient()