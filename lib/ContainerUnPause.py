import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerUnPause:
    def __init__(self,listContainers,userOptions=None):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.userOptions = userOptions
        self.json_file_path = "User/data.json"
        self.command = ["docker", "container","unpause"]
        self.ContainerUnPause = self.ContainerUnPause()

    def ContainerUnPause(self):
        if self.userOptions != None and self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                containerUnPauseCommand = Container.UserContainerOptionCommand(self.command,self.userOptions)
                
                if not User().newUser(container,self.json_file_path):
                    if Container.ContainerId(container,self.json_file_path):
                        id = Container.ContainerId(container,self.json_file_path)
                        containerUnPauseCommand.append(id)
                        result = subprocess.run(containerUnPauseCommand, capture_output=True, text=True)
                        if result.stderr != None:
                            data = {}
                            data['isavailblecontainer'] = 'yes'
                            data['name'] = container
                            data['id'] = id
                            data['returncode'] = result.returncode
                            data['status'] = 'success'
                            data['error'] = result.stderr
                            data['stdout'] = result.stdout
                            self.containerOutputData[index] = data
                            continue
                        else:
                            data = {}
                            data['isavailblecontainer'] = 'yes'
                            data['name'] = container
                            data['id'] = id
                            data['returncode'] = result.returncode
                            data['status'] = 'fail'
                            data['error'] = result.stderr
                            data['stdout'] = result.stdout
                            self.containerOutputData[index] = data
                            continue
                    else:
                        data = {}
                        data['isavailblecontainer'] = 'no'
                        data['name'] = container
                        data['id'] = None
                        data['status'] = 'fail'
                        self.containerOutputData[index] = data
                        continue
                else:
                    data = {}
                    data['isavailblecontainer'] = 'no'
                    data['name'] = container
                    data['id'] = None
                    data['status'] = 'fail'
                    self.containerOutputData[index] = data
                    continue
                    
            return self.containerOutputData
        
        else:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                command = ["docker", "container","unpause"]
                if not User().newUser(container,self.json_file_path):
                    if Container.ContainerId(container,self.json_file_path):
                        id = Container.ContainerId(container,self.json_file_path)
                        command.append(id)    
                        # print(command)
                        result = subprocess.run(command, capture_output=True, text=True)                    
                        if result.stderr != None:
                            data = {}
                            data['isavailblecontainer'] = 'yes'
                            data['name'] = container
                            data['id'] = Container.ContainerId(container,self.json_file_path)
                            data['returncode'] = result.returncode
                            data['status'] = 'success'
                            data['error'] = result.stderr
                            data['stdout'] = result.stdout
                            self.containerOutputData[index] = data
                            continue
                        
                        else:
                            data = {}
                            data['isavailblecontainer'] = 'yes'
                            data['name'] = container
                            data['id'] = Container.ContainerId(container,self.json_file_path)
                            data['returncode'] = result.returncode
                            data['status'] = 'fail'
                            data['error'] = result.stderr
                            data['stdout'] = result.stdout
                            self.containerOutputData[index] = data
                            continue
                    else:
                        data = {}
                        data['isavailblecontainer'] = 'no'
                        data['name'] = container
                        data['id'] = None
                        data['status'] = 'fail'
                        self.containerOutputData[index] = data
                        continue
                else:
                    data = {}
                    data['isavailblecontainer'] = 'no'
                    data['name'] = container
                    data['id'] = None
                    data['status'] = 'fail'
                    self.containerOutputData[index] = data
                    continue
                    
            return self.containerOutputData