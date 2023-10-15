from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerAction import ContainerAction
from lib.ContainerStop import ContainerStop
from lib.ContainerCreate import ContainerCreate
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
container  = Container()
window = Window()
containerAction = ContainerAction()
user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"

if Arg.hasCommands(['Container']):
    '''
    Command Usage : python app.py Container <containerAction> <{--name=ContainerName/--id=ContainerID}> 
    Options       :  
                    --options="{ContainerOptions}"  
                            Options Format ==> < --options="{'s':'1','se':'2'}" >
                            
                    --containers="['container1','container2'...]"  
                            Options Format ==> < --containers="['container1','container2'...]" >
    '''
    if Arg.hasCommands(['stop']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerStop(listContainers,userOptions)
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerStop(listContainers).containerOutputData
            for key, value in data.items():
                status = value['status']
                name = value['name']
                if status == 'success':
                    window.showInfoMessage(f'The container {name} has been successfully taken away')
                else:
                    window.showErrorMessage(f'The container {name} has been failed taken away')
                    
                    
    if Arg.hasCommands(['create']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers') and Arg.hasOptionValue('--image') and Arg.hasOptionValue('--mode'):
            image = Arg.getoptionvalue('--image')
            mode = Arg.getoptionvalue('--mode')
            options = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerCreate(listContainers,image,mode,options).containerOutputData
            print(data)
            # for key, value in data.items():
            #     status = value['status']
            #     name = value['name']
            #     isAlreadyUser = value['isalreadyuser']
            #     if isAlreadyUser == 'no':
            #         if status == 'success' and value['error'] == None:
            #             window.showInfoMessage(f'The container {name} has been successfully created..')  
            #         else:
            #             window.showErrorMessage(f'The container {name} has been failed created..')
            #     else:
            #         window.showErrorMessage(f'The container {name} has been failed created.. because already a Registered User')
                
        
        elif Arg.hasOptionValue('--containers') and Arg.hasOptionValue('--image') and Arg.hasOptionValue('--mode'):
            image = Arg.getoptionvalue('--image')
            mode = Arg.getoptionvalue('--mode')
            listContainers = Arg.getoptionvalue('--containers')
            # print(listContainers)
            data = ContainerCreate(listContainers,image,mode).containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAlreadyUser = value['isalreadyuser']
                if isAlreadyUser == 'no':
                    if status == 'success' and value['error'] == None:
                        window.showInfoMessage(f'The container {name} has been successfully created..')  
                    else:
                        window.showErrorMessage(f'The container {name} has been failed created..')
                else:
                    window.showErrorMessage(f'The container {name} has been failed created.. because already a Registered User')
                
                    
                
            