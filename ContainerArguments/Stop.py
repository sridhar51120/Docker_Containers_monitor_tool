from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerStop import ContainerStop
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
container  = Container()
window = Window()
user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"

def Stop():
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