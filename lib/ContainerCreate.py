from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
import subprocess
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.Window import Window
from lib.Container import Container
window = Window()
user = User()
Arg = Argument(sys.argv)

class ContainerCreate:
    def __init__(self,listContainers,image,mode,userOptions=None,whichPlace=None):
        self.image = image
        self.userOptions = userOptions
        self.mode = mode
        self.whichPlace = whichPlace
        self.listContainers = listContainers
        self.containerOutputData = {}
        self.command = ["docker","container","create"]
        self.json_file_path = "User/data.json"
        self.CreateContainer = self.createContainer()
        
    def createContainer(self):
        if self.userOptions == None and self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                id = Docker_ID(container).ContainerId()
                # Construct A User
                if user.newUser(container,id,self.json_file_path):
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
        
        elif self.userOptions != None and self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            # print(ContainerOptions)
            # print(self.listContainers)
            for index, container in enumerate(self.listContainers):
                id = Docker_ID(container).ContainerId()
                # Construct A User
                if user.newUser(container,id,self.json_file_path):
                    user.addUser(container,id,self.json_file_path)
                    command = Container().UserContainerOptionCommand(self.command,self.userOptions)
                    command.append(id)
                    print(command)
                    # result = subprocess.run(command, capture_output=True, text=True)
                    # if result.stderr != None:
                    #     data = {}
                    #     data['isalreadyuser'] = 'no'
                    #     data['name'] = container
                    #     data['id'] = id
                    #     data['returncode'] = result.returncode
                    #     data['status'] = 'success'
                    #     data['error'] = result.stderr
                    #     data['stdout'] = result.stdout
                    #     self.containerOutputData[index] = data
                    #     continue
                    # else:
                    #     data = {}
                    #     data['isalreadyuser'] = 'no'
                    #     data['name'] = container
                    #     data['id'] = id
                    #     data['returncode'] = result.returncode
                    #     data['status'] = 'fail'
                    #     data['error'] = result.stderr
                    #     data['stdout'] = result.stdout
                    #     self.containerOutputData[index] = data
                    #     continue
                    
                else:
                    data = {}
                    data['isalreadyuser'] = 'yes'
                    data['name'] = container
                    data['id'] = id
                    self.containerOutputData[index] = data
                    continue
                
            return self.containerOutputData
