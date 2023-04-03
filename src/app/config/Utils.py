import os
import importlib.util as util

from fastapi import APIRouter

from domain.controller.AuthorizationPolicyController import controller as AuthorizationPolicyController
from domain.controller.ProfileController import controller as ProfileController
from domain.controller.ResourceQuotaController import controller as ResourceQuotaController
from domain.controller.RolebindingController import controller as RolebindingController



def load_routes() -> list[APIRouter]:
    routes = []
    routes.append(AuthorizationPolicyController.router)
    routes.append(ProfileController.router)
    routes.append(ResourceQuotaController.router)
    routes.append(RolebindingController.router)
    
    return routes
 
def controllerLoader():
    
    # Root dir application
    rootDir = os.path.abspath(os.curdir)

    # Root dir controllers
    controllerDir = os.path.join(rootDir, 'src', 'app', 'domain','controller')

    controllers = []
    for module in os.listdir(controllerDir):
        subDir = controllerDir + "/" + module
        if os.path.isdir(subDir):
            continue
        if module == "__init__.py" or module[-3:] != ".py":
            continue
        else:
            controler = moduleFromFile(moduleName=module, filePath=subDir)
            controllers.append(controler)

    return controllers

def moduleFromFile(moduleName, filePath):
    spec = util.spec_from_file_location(moduleName, filePath)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module  
