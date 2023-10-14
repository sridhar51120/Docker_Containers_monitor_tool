import subprocess
import ast
from lib.Container import Container
Container = Container()

class ContainerStop:
    def __init__(self,listContainers,userOptions=None,containerOutputData=None,command=None):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.userOptions = userOptions
        self.command = ["docker", "container","stop"]
        self.ContainerStop = self.ContainerStop()

    def ContainerStop(self):
        if self.userOptions != None and self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                stopContainer = Container.UserContainerOptionCommand(self.command,self.userOptions)
                stopContainer.append(container)
                result = subprocess.run(stopContainer, capture_output=True, text=True)
                if result.returncode == 0:
                    data = {}
                    data['name'] = container
                    data['returncode'] = result.returncode
                    data['status'] = 'success'
                    data['error'] = result.stderr
                    data['stdout'] = result.stdout
                    self.containerOutputData[index] = data
                    continue
                else:
                    data = {}
                    data['name'] = container
                    data['returncode'] = result.returncode
                    data['status'] = 'fail'
                    data['error'] = result.stderr
                    data['stdout'] = result.stdout
                    self.containerOutputData[index] = data
                    continue
                
            return self.containerOutputData
        
        else:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                command = ["docker", "container","stop"]
                command.append(container)
                result = subprocess.run(self.command, capture_output=True, text=True)
                if result.returncode == 0:
                    data = {}
                    data['name'] = container
                    data['returncode'] = result.returncode
                    data['status'] = 'success'
                    data['error'] = result.stderr
                    data['stdout'] = result.stdout
                    self.containerOutputData[index] = data
                    continue
                else:
                    data = {}
                    data['name'] = container
                    data['returncode'] = result.returncode
                    data['status'] = 'fail'
                    data['error'] = result.stderr
                    data['stdout'] = result.stdout
                    self.containerOutputData[index] = data
                    continue
                
            return self.containerOutputData