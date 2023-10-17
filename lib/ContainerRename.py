import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerRename:
    def __init__(self,listContainers):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.json_file_path = "User/data.json"
        self.command = ["docker", "container","rename"]
        self.ContainerRename = self.ContainerRename()

    def ContainerRename(self):
        if self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            # print(self.listContainers)
            for index, container in enumerate(self.listContainers.items()):
                # print(container[1])
                oldName = container[0]
                newName = container[1]
                # print(oldName)
                # print(newName)
                if not User().newUser(oldName,self.json_file_path):
                    id = Container.ContainerId(oldName,self.json_file_path)
                    print(id)
                    oldContainerName = Container.ContainerName(id,self.json_file_path)
                    NewContainerName = User().addUser(newName,id,self.json_file_path)
                    # print(NewContainerName)
                    # print(oldContainerName)
                    if Container.RemoveContainer(oldContainerName,self.json_file_path):
                        data = {}
                        data['isavailblecontainer'] = 'yes'
                        data['oldname'] = oldContainerName
                        data['newname'] = NewContainerName[0]
                        data['id'] = NewContainerName[1]
                        data['status'] = 'success'
                        data['olddata'] = 'deleted'
                        self.containerOutputData[index] = data
                    else:
                        data = {}
                        data['isavailblecontainer'] = 'yes'
                        data['oldname'] = oldContainerName
                        data['newname'] = NewContainerName[0]
                        data['id'] = NewContainerName[1]
                        data['status'] = 'success'
                        data['olddata'] = 'Not deleted'
                        self.containerOutputData[index] = data                           
                    
                else:
                    data = {}
                    data['isavailblecontainer'] = 'no'
                    data['oldname'] = oldName
                    data['newname'] = None
                    data['id'] = None
                    data['status'] = 'fail'
                    self.containerOutputData[index] = data
                    
            return self.containerOutputData
        
       