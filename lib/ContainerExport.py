import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerExport:
    def __init__(self,listContainers):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.json_file_path = "User/data.json"
        self.command = ["docker", "container","export","--output"]
        self.ContainerExport = self.ContainerExport()

    def ContainerExport(self):
        if self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):
                command = ["docker", "container","export","--output"]
                if not User().newUser(container,self.json_file_path):
                    if Container.ContainerId(container,self.json_file_path):
                        id = Container.ContainerId(container,self.json_file_path)
                        command.append(id) 
                        exportFileName = id
                        command.append(exportFileName)    
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