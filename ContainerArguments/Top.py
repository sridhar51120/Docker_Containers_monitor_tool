from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerTop import ContainerTop
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
container  = Container()
window = Window()
user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"

def Top():
    if Arg.hasOptionValue('--containers'):
        if Arg.hasOption(['--output']):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerTop(listContainers,userOptions="output").containerOutputData
            # print(data)
            # TODO: Validate the stdin and stdout and stderror
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if status == 'success':
                        print(f"The container {name} and Data ::\n",value['stdout'])
                    else:
                        print(f'The container {name} has been failed fetched the process logs....')
                else:
                    print(f'Container {name} is not Available')

        elif Arg.hasOption(['--file']):
            listContainers = Arg.getoptionvalue('--containers')
            data = ContainerTop(listContainers,userOptions="file").containerOutputData
            # print(data)
            for key, value in data.items():
                status = value['status']
                name = value['name']
                isAvailbleContainer = value['isavailblecontainer']
                if isAvailbleContainer == 'yes':
                    if value['isfilecreated'] == True :
                        # print(value['filename'])
                        print(f'The container {name} has been successfully fetched the process logs.... anf FILENAME : {value["filename"]}')
                    else:
                        print(f'Log file {value["filename"]} is failed to create')
                else:
                    print(f'Container {name} is not Available')
                        