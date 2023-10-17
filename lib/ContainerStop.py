import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerStop:
    def __init__(self,listContainers,userOptions=None):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.userOptions = userOptions
        self.json_file_path = "User/data.json"
        self.command = ["docker", "container","stop"]
        self.ContainerStop = self.ContainerStop()

    def ContainerStop(self):
        if self.userOptions != None and self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                containerStopCommand = Container.UserContainerOptionCommand(self.command,self.userOptions)
                
                if not User().newUser(container,self.json_file_path):
                    if Container.ContainerId(container,self.json_file_path):
                        id = Container.ContainerId(container,self.json_file_path)
                        containerStopCommand.append(id)
                        result = subprocess.run(containerStopCommand, capture_output=True, text=True)
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
                        data['id'] = id
                        data['status'] = 'fail'
                        self.containerOutputData[index] = data
                        continue
                else:
                    data = {}
                    data['isavailblecontainer'] = 'no'
                    data['name'] = container
                    data['id'] = id
                    data['status'] = 'fail'
                    self.containerOutputData[index] = data
                    continue
                    
            return self.containerOutputData
        
        else:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                command = ["docker", "container","stop"]
                if not User().newUser(container,self.json_file_path):
                    if Container.ContainerId(container,self.json_file_path):
                        id = Container.ContainerId(container,self.json_file_path)
                        command.append(id)
                        result = subprocess.run(command, capture_output=True, text=True)                        
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
                        data['id'] = id
                        data['status'] = 'fail'
                        self.containerOutputData[index] = data
                        continue
                else:
                    data = {}
                    data['isavailblecontainer'] = 'no'
                    data['name'] = container
                    data['id'] = id
                    data['status'] = 'fail'
                    self.containerOutputData[index] = data
                    continue
                    
            return self.containerOutputData