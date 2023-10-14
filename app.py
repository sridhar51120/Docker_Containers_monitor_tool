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
            print(data)
            # for index,i in enumerate(data.items()):
                # print((index))
                # print(i)
                
            