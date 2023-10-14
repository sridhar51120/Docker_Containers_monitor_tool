import os
import subprocess
import json
import ast
from lib.User import User
from lib.RunCommand import RunCommand
from lib.Container import Container
container  = Container()
run = RunCommand()
user = User()
class ContainerAction:
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
                
    def ContainerStop(self,id,options=None):
        # TODO: python app.py Container stop --name="Sridhar" --options="{'s':'1','se':'2'}"
        command = ["docker", "container","stop"]
        if options:
            # for constructing a docker container stop command
            stopContainerCommand = container.UserContainerOptionCommand(command,id,options)
            result = subprocess.run(stopContainerCommand, capture_output=True, text=True)
            # print(result)
            if result.returncode == 0:
                print(stopContainerCommand)
                return True
            else:
                return False
        else:
            # for constructing a docker container stop command
            stopContainerCommand = container.UserContainerOptionCommand(command,id)
            result = subprocess.run(stopContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(stopContainerCommand)
                return True
            else:
                return False
        
    def ContainerRestart(self,id,options=None):
        # for constructing a docker container restart command
        # TODO: python app.py Container restart --name="Sridhar" --options="{'s':'1','se':'2'}"
        command = ["docker", "container","restart"]
        if options:
            restartContainerCommand = container.UserContainerOptionCommand(command,id,options)
            result = subprocess.run(restartContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(restartContainerCommand)
                return True
            else:
                return False
        else:
            restartContainerCommand = container.UserContainerOptionCommand(command,id)
            result = subprocess.run(restartContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(restartContainerCommand)
                return True
            else:
                return False
    
    def ContainerStart(self,id,options=None):
        # for constructing a docker container start command
        # TODO: python app.py Container start --name="Sridhar" --options="{'s':'1','se':'2'}"
        command = ["docker", "container","start"]
        if options:
            startContainerCommand = container.UserContainerOptionCommand(command,id,options)
            result = subprocess.run(startContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(startContainerCommand)
                return True
            else:
                return False
        else:
            startContainerCommand = container.UserContainerOptionCommand(command,id)
            result = subprocess.run(startContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(startContainerCommand)
                return True
            else:
                return False
        
    def ContainerRemove(self,id,options=None):
        # for constructing a docker container remove command
        # TODO: python app.py Container remove --name="Sridhar" --options="{'s':'1','se':'2'}"
        command = ["docker", "container","rm"]
        if options:
            removeContainerCommand = container.UserContainerOptionCommand(command,id,options)
            result = subprocess.run(removeContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(removeContainerCommand)
                return True
            else:
                return False
        else:
            removeContainerCommand = container.UserContainerOptionCommand(command,id)
            result = subprocess.run(removeContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(removeContainerCommand)
                return True
            else:
                return False


    def ContainerPause(self,id,containers=None):
        command = ["docker", "container","pause"]
        if containers:
            listContainers = container.listContainers(command,containers)
            result = subprocess.run(listContainers, capture_output=True, text=True)
            if result.returncode == 0:
                print(listContainers)
                return True
            else:
                return False
        else:
            pauseContainerCommand = container.UserContainerOptionCommand(command,id)
            result = subprocess.run(pauseContainerCommand, capture_output=True, text=True)
            if result.returncode == 0:
                print(pauseContainerCommand)
                return True
            else:
                return False