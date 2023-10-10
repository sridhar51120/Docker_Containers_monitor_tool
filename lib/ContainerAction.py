import os
import subprocess
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
                
    def ContainerStop(self,id,options):
        if options != None:
            options_str = user.UserContainerOption(options)
            command = f"docker container stop {id} {options_str}"
            # TODO:Change it with Subproccess.run Command For Validating the input and output
            os.system(command)
            '''
            if (subprocess.run(command)):
                return True
            else:
                return False
            if the Process is Successfully Executed then it will returns True value otherwise False
            '''
        else:
            command  = f"docker container stop {id}"
            # TODO:Change it with Subproccess.run Command For Validating the input and output
            os.system(command)
        
    def ContainerRestart(self,id,options=None):
        if options != None:
            options_str = user.UserContainerOption(options)
            command = f"docker container restart {id}"
            # TODO:Change it with Subproccess.run Command For Validating the input and output
            os.system(command)
           
        else:
            command  = f"docker container restart {id}"
            # TODO:Change it with Subproccess.run Command For Validating the input and output
            os.system(command)
    
    def ContainerStart(self):
        pass