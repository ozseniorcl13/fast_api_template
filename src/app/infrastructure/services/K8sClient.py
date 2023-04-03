import os
from kubernetes import client, config
from config.Settings import settings
from core.logger import logger

class K8sClient:

    def __init__(self) -> None:
        self.in_cluster = None
    
    def connect(self, context: str, pathFile: str):
        self.in_cluster = None
        if self.__is_running_in_k8s__():
            config.load_incluster_config()
            self.in_cluster = True
            logger.info(f'K8Client connected in cluster.')
        else:
            config.load_kube_config(
                config_file=pathFile,
                context=context,
                client_configuration=None,
                persist_config=None,
            )
            self.in_cluster = False
            logger.info(f'K8Client connected to cluster by: {pathFile}.')

    def __is_running_in_k8s__(self):
        return os.path.isdir("/var/run/secrets/kubernetes.io/")


client = K8sClient()