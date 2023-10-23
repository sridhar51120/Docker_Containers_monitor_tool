import subprocess
import ast
from lib.User import User
from lib.Container import Container
Container = Container()

class ContainerTop:
    def __init__(self,listContainers,userOptions):
        self.containerOutputData = {}
        self.listContainers = listContainers
        self.userOptions = userOptions
        self.json_file_path = "User/data.json"
        self.ContainerTop = self.ContainerTop()

    def ContainerTop(self):
        if self.userOptions == "output" and self.listContainers:
            command = ["docker", "container","top"]
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
                        command = ["docker", "container","top"]
                        command.append(id)
                        # print(command)
                        result = subprocess.run(command, capture_output=True, text=True)
                        if result.stderr != None:
                            file = Container.CovertOutputTextFile(f"{result.stdout}",id,'process')
                            if file:
                                data = {}
                                data['isavailblecontainer'] = 'yes'
                                data['name'] = container
                                data['id'] = id
                                data['returncode'] = result.returncode
                                data['status'] = 'success'
                                data['error'] = result.stderr
                                data['stdout'] = result.stdout
                                data['isfilecreated'] = True
                                data['filename'] = id + "_process_file.txt"
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
        
       
        
       