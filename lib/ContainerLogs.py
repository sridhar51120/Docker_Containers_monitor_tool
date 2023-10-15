import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerLogs:
    def __init__(self,listContainers,userOptions):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.userOptions = userOptions
        self.json_file_path = "User/data.json"
        self.ContainerLogs = self.ContainerLogs()

    def ContainerLogs(self):
        if self.userOptions == "output" and self.listContainers:
            command = ["docker", "container","logs"]
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):  
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

        elif self.userOptions == "file" and self.listContainers:
            self.listContainers = ast.literal_eval(self.listContainers)
            for index, container in enumerate(self.listContainers):  
                if not User().newUser(container,self.json_file_path):
                    if Container.ContainerId(container,self.json_file_path):
                        id = Container.ContainerId(container,self.json_file_path)
                        command = ["docker", "container","logs"]
                        command.append(id)
                        # print(command)
                        result = subprocess.run(command, capture_output=True, text=True)
                        if result.stderr != None:
                            if Container.createLogFile(f"{result.stderr}",id):
                                data = {}
                                data['isavailblecontainer'] = 'yes'
                                data['name'] = container
                                data['id'] = id
                                data['returncode'] = result.returncode
                                data['status'] = 'success'
                                data['error'] = result.stderr
                                data['stdout'] = result.stdout
                                data['isfilecreated'] = True
                                self.containerOutputData[index] = data
                                continue
                            else:
                                data = {}
                                data['isavailblecontainer'] = 'yes'
                                data['name'] = container
                                data['id'] = id
                                data['returncode'] = result.returncode
                                data['status'] = 'success'
                                data['error'] = result.stderr
                                data['stdout'] = result.stdout
                                data['isfilecreated'] = False
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
        
       
        
       