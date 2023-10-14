from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerAction import ContainerAction
from lib.Window import Window
from lib.Container import Container
container  = Container()
window = Window()


# TODO: Containers Class
containerAction = ContainerAction()
user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"

# try:
# if Arg.hasCommands(['Container']):
    # Create A container with (name or ID) with image
    # python app.py Container Create --name=sri --image=sjhfd --options="{'-e':'-er','-f':'fr'}"
    # docker container create --ip6 2001:db8::1 -it my-image /bin/bash
    # if Arg.hasCommands(['Create']):
    #     if Arg.hasOptionValue('--name') and Arg.hasOptionValue('--image') or Arg.hasOptionValue('--options'):
    #         name = Arg.getoptionvalue('--name')
    #         user_id = Docker_ID(name).ContainerId()
    #         if user.newUser(name,user_id,json_file_path):
    #             constainer_id = user.addUser(name,user_id,json_file_path)
    #             image = Arg.getoptionvalue('--image')
    #             options = None
    #             if Arg.getoptionvalue('--options') != None:
    #                 options = Arg.getoptionvalue('--options')

    #             if Arg.getoptionvalue('--mode') == "-d":
    #                 mode = Arg.getoptionvalue('--mode')
    #                 whichPlace = None
    #                 container.CreateContainer(constainer_id,image,options,mode,whichPlace)

    #             if Arg.getoptionvalue('--mode') == "-it" and Arg.hasOptionValue('--where'):
    #                 mode = Arg.getoptionvalue('--mode')
    #                 whichPlace = Arg.getoptionvalue('--where')
    #                 container.CreateContainer(constainer_id,image,options,mode,whichPlace)
    #         else:
    #             raise Exception("User Name is Already Registered...")
      
    # elif Arg.hasOption(['--list']):
    #     print("list")

    # elif Arg.hasOptionValue('--name') and Arg.hasOption(['--info']):
    #     Dashboard = Dashboard(Arg.getoptionvalue('--name'))
    #     info = Dashboard.ContainerInfo()
    #     print(json.dumps(info, indent = 4))

    # elif Arg.hasOption(['--list-all']):
    #     print("List the Containers list")
      
    # TODO: for container stop
    # TODO: if thw User have the Username or Container Id to Do a Container action
    

# try:
if container.ContainerId(json_file_path): #TODO: if the Container name or id is given or not 
    id = container.ContainerId(json_file_path) # get the Container id in User Input
    print(f"Container Id ==> {id}")
    name = container.ContainerName(json_file_path) # get the Container Name
    print(f"Container Name ==> {name}")
    
    
    if Arg.hasCommands(['stop']):
        '''
        Command Usage : python app.py Container < {--name=ContainerName/--id=ContainerID} > stop 
        Options       :  
                        --options="{ContainerOptions}"  
                                Options Format ==> < --options="{'s':'1','se':'2'}" >
        '''
        if Arg.hasOptionValue('--options'):
            if containerAction.ContainerStop(id,Arg.getoptionvalue('--options')):
                print(window.showInfoMessage(f"Container {name} [{id}] stoped Succesfully...."))
            else:
                print(window.showErrorMessage(f"User Action ==> Container stoped Failed... --> ID = [{id}] and Name = {name}"))
                
        else:
            if containerAction.ContainerStop(id):
                print(window.showInfoMessage(f"Container {name} [{id}] stoped Successfully...."))
            else:
                print(window.showErrorMessage(f"User Action ==> Container stoped Failed... --> ID = [{id}] and Name = {name}"))
                
    if Arg.hasCommands(['restart']):
        '''
        Command Usage : python app.py Container < {--name=ContainerName/--id=ContainerID} > restart
        Options       :  
                        --options="{ContainerOptions}"  
                                Options Format ==> < --options="{'s':'1','se':'2'}" >
        '''
        if Arg.hasOptionValue('--options'):
            if containerAction.ContainerRestart(id,Arg.getoptionvalue('--options')):
                print(window.showInfoMessage(f"Container {name} [{id}] restart Succesfully...."))
            else:
                print(window.showErrorMessage(f"User Action ==> Container restart Failed... --> ID = [{id}] and Name = {name}"))
        else:
            if containerAction.ContainerRestart(id):
                print(window.showInfoMessage(f"Container {name} [{id}] restart Successfully....")) 
            else:
                print(window.showErrorMessage(f"User Action ==> Container restart Failed... --> ID = [{id}] and Name = {name}"))
                
    if Arg.hasCommands(['start']):
        '''
        Command Usage : python app.py Container < {--name=ContainerName/--id=ContainerID} > start
        Options       :  
                        --options="{ContainerOptions}"  
                                Options Format ==> < --options="{'s':'1','se':'2'}" >
        '''
        if Arg.hasOptionValue('--options'):
            if containerAction.ContainerStart(id,Arg.getoptionvalue('--options')):
                print(window.showInfoMessage(f"Container {name} [{id}] start Succesfully...."))
            else:
                print(window.showErrorMessage(f"User Action ==> Container start Failed... --> ID = [{id}] and Name = {name}"))
        else:
            if containerAction.ContainerStart(id):
                print(window.showInfoMessage(f"Container {name} [{id}] start Successfully...."))   
            else:
                print(window.showErrorMessage(f"User Action ==> Container start Failed... --> ID = [{id}] and Name = {name}")) 
                
    if Arg.hasCommands(['remove']):
        '''
        Command Usage : python app.py Container < {--name=ContainerName/--id=ContainerID} > remove
        Options       :  
                        --options="{ContainerOptions}"  
                                Options Format ==> < --options="{'s':'1','se':'2'}" >
        '''
        if Arg.hasOptionValue('--options'):
            if containerAction.ContainerRemove(id,Arg.getoptionvalue('--options')):
                print(window.showInfoMessage(f"Container {name} [{id}] remove Succesfully...."))
            else:
                print(window.showErrorMessage(f"User Action ==> Container remove Failed... --> ID = [{id}] and Name = {name}"))
        else:
            if containerAction.ContainerRemove(id):
                print(window.showInfoMessage(f"Container {name} [{id}] remove Successfully...."))   
            else:
                print(window.showErrorMessage(f"User Action ==> Container remove Failed... --> ID = [{id}] and Name = {name}"))  

# TODO: python app.py Container pause --name="Sridhar"  or   python app.py Container pause --containers="[]"         
if Arg.hasCommands(['pause']):
        '''
        Command Usage : python app.py Container < {--name=ContainerName/--id=ContainerID} > pause
        Options       :  
                        --containers="['container1','container2'...]"  
                                Options Format ==> < --containers="['container1','container2'...]" >
        '''
        if Arg.hasOptionValue('--containers'):
            if containerAction.ContainerPause(id,Arg.getoptionvalue('--containers')):
                containers = Arg.getoptionvalue('--containers')
                list_containers = ast.literal_eval(containers)
                for container in list_containers:
                    print(window.showInfoMessage(f"Container {container} paused Succesfully...."))
            else:
                print(window.showErrorMessage(f"User Action ==> Container paused Failed... --> ID = [{id}] and Name = {name}"))
        else:
            if containerAction.ContainerPause(id):
                print(window.showInfoMessage(f"Container {name} [{id}] paused Successfully...."))   
            else:
                print(window.showErrorMessage(f"User Action ==> Container paused Failed... --> ID = [{id}] and Name = {name}"))  
     
                          
else:
    print(window.showWarningMessage("Username is Not Registered..Please check your Container Name"))
    # raise Exception("Contianer Name or Container Id is not Available...")
