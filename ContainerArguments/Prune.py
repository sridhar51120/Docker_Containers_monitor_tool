from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import ast
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerPrune import ContainerPrune
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
container  = Container()
window = Window()

user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"

def Prune():
    if Arg.hasOption(['--all']):
        print("hello")
        data = ContainerPrune().containerOutputData
        print(data)