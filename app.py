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
from lib.ContainerRestart import ContainerRestart
from lib.ContainerStart import ContainerStart
from lib.ContainerRemove import ContainerRemove
from lib.ContainerPause import ContainerPause
from lib.ContainerUnPause import ContainerUnPause
from lib.ContainerKill import ContainerKill
from lib.ContainerExport import ContainerExport
from lib.ContainerLogs import ContainerLogs
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
                        print(f'The container {name} has been successfully taken away')
                        # window.showInfoMessage(f'The container {name} has been successfully taken away')
                    else:
                        print(f'The container {name} has been failed taken away')
                        # window.showErrorMessage(f'The container {name} has been failed taken away')
                else:
                    print(f'Container {name} is not Available')
                
                    
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerStop(listContainers).containerOutputData
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully taken away')
                        # window.showInfoMessage(f'The container {name} has been successfully taken away')
                    else:
                        print(f'The container {name} has been failed taken away')
                        # window.showErrorMessage(f'The container {name} has been failed taken away')
                else:
                    print(f'Container {name} is not Available')
             
             
    if Arg.hasCommands(['restart']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerRestart(listContainers,userOptions).containerOutputData
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully restarted...')
                        # window.showInfoMessage(f'The container {name} has been successfully restarted...')
                    else:
                        print(f'The container {name} has been failed restarted...')
                        # window.showErrorMessage(f'The container {name} has been failed restarted...')
                else:
                    print(f'Container {name} is not Available')
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerRestart(listContainers).containerOutputData
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully restarted...')
                        # window.showInfoMessage(f'The container {name} has been successfully restarted...')
                    else:
                        print(f'The container {name} has been failed restarted...')
                        # window.showErrorMessage(f'The container {name} has been failed restarted...')
                else:
                    print(f'Container {name} is not Available')
                
    if Arg.hasCommands(['start']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerStart(listContainers,userOptions).containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully started...')
                        # window.showInfoMessage(f'The container {name} has been successfully started...')
                    else:
                        print(f'The container {name} has been failed started...')
                        # window.showErrorMessage(f'The container {name} has been failed started...')
                else:
                    print(f'Container {name} is not Available')
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerStart(listContainers).containerOutputData
            # print(data)
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully started...')
                        # window.showInfoMessage(f'The container {name} has been successfully started...')
                    else:
                        print(f'The container {name} has been failed started...')
                        # window.showErrorMessage(f'The container {name} has been failed started...')
                else:
                    print(f'Container {name} is not Available')
                
    if Arg.hasCommands(['remove']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerRemove(listContainers,userOptions).containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully removed...')
                        # window.showInfoMessage(f'The container {name} has been successfully removed...')
                    else:
                        print(f'The container {name} has been failed removed...')
                        # window.showErrorMessage(f'The container {name} has been failed removed...')
                else:
                    print(f'Container {name} is not Available')
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerRemove(listContainers).containerOutputData
            # print(data)
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully removed...')
                        # window.showInfoMessage(f'The container {name} has been successfully removed...')
                    else:
                        print(f'The container {name} has been failed removed...')
                        # window.showErrorMessage(f'The container {name} has been failed removed...')
                else:
                    print(f'Container {name} is not Available')      
                    
    if Arg.hasCommands(['pause']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerPause(listContainers,userOptions).containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully paused...')
                        # window.showInfoMessage(f'The container {name} has been successfully paused...')
                    else:
                        print(f'The container {name} has been failed paused...')
                        # window.showErrorMessage(f'The container {name} has been failed paused...')
                else:
                    print(f'Container {name} is not Available')
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerPause(listContainers).containerOutputData
            # print(data)
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully paused...')
                        # window.showInfoMessage(f'The container {name} has been successfully paused...')
                    else:
                        print(f'The container {name} has been failed paused...')
                        # window.showErrorMessage(f'The container {name} has been failed paused...')
                else:
                    print(f'Container {name} is not Available')       
                    
    if Arg.hasCommands(['unpause']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerUnPause(listContainers,userOptions).containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully unpaused...')
                        # window.showInfoMessage(f'The container {name} has been successfully unpaused...')
                    else:
                        print(f'The container {name} has been failed unpaused...')
                        # window.showErrorMessage(f'The container {name} has been failed unpaused...')
                else:
                    print(f'Container {name} is not Available')
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerUnPause(listContainers).containerOutputData
            # print(data)
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully unpaused...')
                        # window.showInfoMessage(f'The container {name} has been successfully unpaused...')
                    else:
                        print(f'The container {name} has been failed unpaused...')
                        # window.showErrorMessage(f'The container {name} has been failed unpaused...')
                else:
                    print(f'Container {name} is not Available') 
                    
    if Arg.hasCommands(['export']):
        if Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerExport(listContainers).containerOutputData
            print(data)
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully exported...')
                        # window.showInfoMessage(f'The container {name} has been successfully exported...')
                    else:
                        print(f'The container {name} has been failed exported...')
                        # window.showErrorMessage(f'The container {name} has been failed exported...')
                else:
                    print(f'Container {name} is not Available')   
                    
    if Arg.hasCommands(['logs']):
        if Arg.hasOptionValue('--containers'):
            if Arg.hasOption(['--output']):
                listContainers = Arg.getoptionvalue('--containers')
                data = ContainerLogs(listContainers,userOptions="output").containerOutputData
                # print(data)
                for key, value in data.items():
                    status = value['status']
                    name = value['name']
                    isAvailbleContainer = value['isavailblecontainer']
                    if isAvailbleContainer == 'yes':
                        if status == 'success':
                            print(f"The container {name} and Data ::\n",value['error'])
                        else:
                            print(f'The container {name} has been failed fetched the logs....')
                    else:
                        print(f'Container {name} is not Available')

            elif Arg.hasOption(['--file']):
                listContainers = Arg.getoptionvalue('--containers')
                data = ContainerLogs(listContainers,userOptions="file").containerOutputData
                # print(data)
                for key, value in data.items():
                    status = value['status']
                    name = value['name']
                    isAvailbleContainer = value['isavailblecontainer']
                    if isAvailbleContainer == 'yes':
                        if value['isfilecreated'] :
                            print(f'Log file {value["id"]}_logs_file.txt is Successfully created')
                        else:
                            print(f'Log file {value["id"]}_logs_file.txt is failed to create')
                    else:
                        print(f'Container {name} is not Available')      
                    
    if Arg.hasCommands(['kill']):
        if Arg.hasOptionValue('--options') and Arg.hasOptionValue('--containers'):
            userOptions = Arg.getoptionvalue('--options')
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerKill(listContainers,userOptions).containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully killed....')
                        # window.showInfoMessage(f'The container {name} has been successfully killed....')
                    else:
                        print(f'The container {name} has been failed killed....')
                        # window.showErrorMessage(f'The container {name} has been failed killed....')
                else:
                    print(f'Container {name} is not Available')
            
        elif Arg.hasOptionValue('--containers'):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerKill(listContainers).containerOutputData
            # print(data)
            for key, value in data.items():
                # print(value['isavailblecontainer'])
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f'The container {name} has been successfully killed....')
                        # window.showInfoMessage(f'The container {name} has been successfully killed....')
                    else:
                        print(f'The container {name} has been failed killed....')
                        # window.showErrorMessage(f'The container {name} has been failed killed....')
                else:
                    print(f'Container {name} is not Available')  

    if Arg.hasCommands(['kill']):
        if Arg.hasOptionValue('--containers'):
            if Arg.hasOption(['--stopped']):
                pass
            elif Arg.hasOption(['--all']):
                pass
            elif Arg.hasOption(['--running']):
                pass

