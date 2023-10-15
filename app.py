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
    if Arg.hasCommands(['create']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers') and Arg.hasOptionValue('--image'):
            image = Arg.getoptionvalue('--image')
            options = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerCreate(listContainers,image,options).containerOutputData
            # print(data.items())
            for key, value in data.items():
                # print(value)
                status = value['status']
                name = value['name']
                isAlreadyUser =  value['isalreadyuser']
                if isAlreadyUser == 'no':
                    if status == 'success':
                        if value['error'] == None:
                            print(f'The container {name} has been successfully created..')
                            # window.showInfoMessage(f'The container {name} has been successfully created..') 
                        else:
                            print(f'The container {name} has been failed created.. new User is Created but Error Occured. ERROR => {value["error"]}')
                             # window.showErrorMessage(f'The container {name} has been failed created..')
                else:
                    # window.showErrorMessage(f'The container {name} has been failed created.. because already a Registered User')
                    print(f'The container {name} has been failed created.. because the container is already available...')
                
            
        elif Arg.hasOptionValue('--containers') and Arg.hasOptionValue('--image'):
            image = Arg.getoptionvalue('--image')
            listContainers = Arg.getoptionvalue('--containers')
            # print(listContainers)
            data = ContainerCreate(listContainers,image).createContainer()
            # print(data)
            # print(data)
            for key, value in data.items():
                # print(value)
                status = value['status']
                name = value['name']
                isAlreadyUser =  value['isalreadyuser']
                if isAlreadyUser == 'no':
                    if status == 'success':
                        if value['error'] == None:
                            print(f'The container {name} has been successfully created..')
                            # window.showInfoMessage(f'The container {name} has been successfully created..') 
                        else:
                            print(f'The container {name} has been failed created.. new User is Created but Error Occured')
                             # window.showErrorMessage(f'The container {name} has been failed created..')
                else:
                    # window.showErrorMessage(f'The container {name} has been failed created.. because already a Registered User')
                    print(f'The container {name} has been failed created.. because the container is already available...')
          
    if Arg.hasCommands(['stop']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerStop(listContainers,userOptions)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        window.showInfoMessage(f'The container {name} has been successfully taken away')
                    else:
                        window.showErrorMessage(f'The container {name} has been failed taken away')
                else:
                    print(f'Container {name} is not Available')
                
                    
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

    if Arg.hasCommands(['restart']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerRestart(listContainers,userOptions)
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerRestart(listContainers).containerOutputData
            for key, value in data.items():
                status = value['status']
                name = value['name']
                if status == 'success':
                    window.showInfoMessage(f'The container {name} has been successfully taken away')
                else:
                    window.showErrorMessage(f'The container {name} has been failed taken away')
                    
                    
      
                    
                
            