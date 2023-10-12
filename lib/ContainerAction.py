import os
import subprocess
import json
from lib.User import User
from lib.RunCommand import RunCommand
run = RunCommand()
user = User()
class ContainerAction:
    def CreateContainer(self,name,image,options,mode,whichPlace):
        if options != None:
            options_str = user.UserContainerOption(options)
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
        if options:
            pass
            # TODO: --options="key1:value1,key2:value2,key3:value3"
            # command = ["docker", "container","stop",f"{id}",dictionary]
            # print(command)
            # result = subprocess.run(command, capture_output=True, text=True)
            # print(result)
            # if result.returncode == 0:
            #     return True
            # else:
            #     return False
        else:
            command = ["docker", "container","stop", f"{id}"]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode == 0:
                return True
            else:
                return False
        
    def ContainerRestart(self,id,options=None):
        if options:
            options_str = user.UserContainerOption(options)
            command = f"docker container restart {id}"
            # TODO:Change it with Subproccess.run Command For Validating the input and output
            # os.system(command)
            return True
           
        else:
            command  = f"docker container restart {id}"
            # TODO:Change it with Subproccess.run Command For Validating the input and output
            # os.system(command)
            return True
    
    def ContainerStart(self):
        pass