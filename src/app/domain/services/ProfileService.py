
from typing import List
from app.domain.model.Profile import Profile
from app.domain.model.Status import Status
from kubernetes import client
from kubernetes.client import exceptions
from app.core.logger import logger

class ProfileService():

    def __init__(self) -> None:
        self.group = "kubeflow.org"
        self.version = "v1beta1"
        self.plural="profiles"
        self.api = client.CustomObjectsApi()

    def findAll(self) -> list[Profile]:
        profilesObjects = self.api.get_cluster_custom_object(
             group=self.group, 
             version=self.version, 
             plural=self.plural, 
             name="")
         
        profiles: List = []
        for profile in profilesObjects["items"]: 
            metadata = profile['metadata'] 
            if metadata.get('annotations') is not None: 
                annotations = metadata.get('annotations') 
                profile = Profile(
                    name=metadata["name"],
                    createdBy=annotations['createdby'],
                    projectManager=annotations['projectmanager'],
                    status=Status(annotations['status']),
                    description=annotations['description'],
                    onwer=metadata["spec"]["owner"]["name"]
                )
                profiles.append(profile)
         
        return profiles
    
    def create(self, profile: Profile):
        body = {
            'apiVersion': 'kubeflow.org/v1',
            'kind': 'Profile',
            'metadata': {
                'name': profile.name,
                'labels': {
                    'app.kubernetes.io/managed-by': 'dpmp'
                },
                'annotations': {           
                    'status': profile.status.value,
                    'createdby': profile.createdBy,
                    'description': profile.description,
                    'projectmanager': profile.projectManager
                }
            },
            'spec': {
                'owner': {
                    'kind': 'User',
                    'name': profile.onwer
                }
            }
        }
        thread = self.api.create_cluster_custom_object(
            group=self.group, 
            version='v1', 
            plural=self.plural,
            body=body,
            async_req=True)
        
        result = thread.get()
        logger.info(result)
        return profile

    def findByProfileId(self, profileName: str):
        pass

    def findAndUpdate(self):
        '''Update'''
        return

profileService = ProfileService()