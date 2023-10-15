import subprocess
import ast
from lib.Container import Container
Container = Container()

class ContainerRestart:
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
                # TODO: this command is costucted only Id but if the user Use's Container Name
                # TODO: Construct with username and id
                # TODO: if the Container is Available or not
                # TODO: if not Append thd id to => self.containerOutputData[index] = data
                stopContainer.append(container)
                result = subprocess.run(stopContainer, capture_output=True, text=True)
                if result.stderr != None:
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
                # print(command)
                result = subprocess.run(command, capture_output=True, text=True)
                if result.stderr != None:
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