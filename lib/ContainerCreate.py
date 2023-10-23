import json
import ast
import subprocess
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.Container import Container
Container = Container()
user = User()


class ContainerCreate:
    def __init__(self,listContainers,image,userOptions=None):
        self.image = image
        self.listContainers = listContainers
        self.userOptions = userOptions
        self.containerOutputData = {}
        self.command = ["docker","container","create"]
        self.json_file_path = "User/data.json"
        self.CreateContainer = self.createContainer()
        
    def createContainer(self):
        if self.userOptions == None and self.listContainers:
            listContainers = ast.literal_eval(self.listContainers)
            # print(listContainers)
            for index, container in enumerate(listContainers):
                id = Docker_ID(container).ContainerId()
                # Construct A User
                if user.newUser(container,self.json_file_path):
                    user.addUser(container,id,self.json_file_path)
                    command = ["docker","container","create"]
                    command.append(id)
                    result = subprocess.run(command, capture_output=True, text=True)
                    if result.stderr != None:
                        data = {}
                        data['isalreadyuser'] = 'no'
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
                        data['isalreadyuser'] = 'no'
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
                    data['isalreadyuser'] = 'yes'
                    data['name'] = container
                    data['id'] = id
                    self.containerOutputData[index] = data
                    continue
                
            return self.containerOutputData
        
        if self.userOptions != None and self.listContainers :
            self.listContainers = ast.literal_eval(self.listContainers)
            # print(self.listContainers)
            for index, container in enumerate(self.listContainers):
                id = Docker_ID(container).ContainerId()
                # Construct A User
                if user.newUser(container,id,self.json_file_path):
                    user.addUser(container,id,self.json_file_path)
                    dockercommand = ["docker","container","create"]
                    # print(dockercommand)
                    command = Container.UserContainerOptionCommand(dockercommand,self.userOptions)
                    # print(self.userOptions)
                    command.append(id)
                    # print(command)
                    result = subprocess.run(command, capture_output=True, text=True)
                    if result.stderr != None:
                        data = {}
                        data['isalreadyuser'] = 'no'
                        data['name'] = container
                        data['id'] = id
                        data['returncode'] = result.returncode
                        data['status'] = 'success'
                        data['error'] = result.stderr
                        data['stdout'] = result.stdout
                        # print(data)
                        self.containerOutputData[index] = data
                        # print(self.containerOutputData)
                        continue
                    else:
                        data = {}
                        data['isalreadyuser'] = 'no'
                        data['name'] = container
                        data['id'] = id
                        data['returncode'] = result.returncode
                        data['status'] = 'fail'
                        data['error'] = result.stderr
                        data['stdout'] = result.stdout
                        # print(data)
                        self.containerOutputData[index] = data
                        # print(self.containerOutputData)
                        continue
                    
                else:
                    data = {}
                    data['isalreadyuser'] = 'yes'
                    data['name'] = container
                    data['id'] = id
                    # print(data)
                    self.containerOutputData[index] = data
                    # print(self.containerOutputData)
                    continue
                
            return self.containerOutputData
