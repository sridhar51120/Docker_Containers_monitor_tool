from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerKill import ContainerKill
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
container  = Container()
window = Window()

user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"


def Kill():
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
