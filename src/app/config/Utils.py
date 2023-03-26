import os
import importlib.util as util
 
def controllerLoader():
    
    # Root dir application
    rootDir = os.path.abspath(os.curdir)

    # Root dir controllers
    controllerDir = os.path.join(rootDir, 'src', 'app','domain','controller')

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

    
