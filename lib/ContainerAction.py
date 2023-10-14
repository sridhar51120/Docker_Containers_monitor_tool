import os
import subprocess
import json
import ast
from lib.User import User
from lib.RunCommand import RunCommand
from lib.Container import Container
Container  = Container()
run = RunCommand()
user = User()

class ContainerAction:
    def __init__(self,containerOutputData=None):
        self.containerOutputData = {}
        
        
    def CreateContainer(self,name,image,options,mode,whichPlace):
        if options != None:
            options_str = container.UserContainerOption(options)
            if mode == '-d' and whichPlace == None:
                command = f"docker container create {options_str[:-1]} --name {name} {image}"
                # command = f"['docker','container','create', {options_str[:-1]},'--name','{name}','-d','{image}']"
                run.Run_Command(command)
            if mode == '-it' and whichPlace != None:
                command = f"docker container create {options_str[:-1]} --name {name} {image}"
                # command = f"['docker','container','create', {options_str[:-1]},'--name','{name}','{mode}','{image}','{whichPlace}']"
                run.Run_Command(command)
        else:
            if mode == '-d' and whichPlace == None:
                command = f"docker container create --name {name} {image}"
                # command = f"['docker','container','create','--name','{name}','-d','{image}']"
                run.Run_Command(command)
            if mode == '-it' and whichPlace != None:
                command = f"docker container create --name {name} {image}"
                # command = f"['docker','container','create','--name','{name}','{mode}','{image}','{whichPlace}']"
                run.Run_Command(command)
    
    #   TODO: python app.py Container stop  --containers="['b9fa87a5a0fa56dd9e48','agitated_cartwright']"      
    def ContainerStop(self,listContainers,userOptions=None):
        if userOptions != None and listContainers:
            listContainers = ast.literal_eval(listContainers)
            for index, container in enumerate(listContainers):
                command = ["docker", "container","stop"]
                stopContainer = Container.UserContainerOptionCommand(command,userOptions)
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
            listContainers = ast.literal_eval(listContainers)
            for index, container in enumerate(listContainers):
                command = ["docker", "container","stop"]
                command.append(container)
                result = subprocess.run(command, capture_output=True, text=True)
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
        
    