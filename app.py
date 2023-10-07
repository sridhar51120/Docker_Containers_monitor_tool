from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.DockerContainer import DockerContainer

# TODO: Containers Class
container = DockerContainer()
user = User()
Arg = Argument(sys.argv)
json_file_path = "User/data.json"

# try:
if Arg.hasCommands(['Container']):
    # Create A container with (name or ID) with image
    # python app.py Container Create --name=sri --image=sjhfd --options="{'-e':'-er','-f':'fr'}"
    # docker container create --ip6 2001:db8::1 -it my-image /bin/bash
    if Arg.hasCommands(['Create']):
        if Arg.hasOptionValue('--name') and Arg.hasOptionValue('--image') or Arg.hasOptionValue('--options'):
            name = Arg.getoptionvalue('--name')
            user_id = Docker_ID(name).ContainerId()
            if user.newUser(name,user_id,json_file_path):
                constainer_id = user.addUser(name,user_id,json_file_path)
                image = Arg.getoptionvalue('--image')
                options = None
                if Arg.getoptionvalue('--options') != None:
                    options = Arg.getoptionvalue('--options')

                if Arg.getoptionvalue('--mode') == "-d":
                    mode = Arg.getoptionvalue('--mode')
                    whichPlace = None
                    container.CreateContainer(constainer_id,image,options,mode,whichPlace)

                if Arg.getoptionvalue('--mode') == "-it" and Arg.hasOptionValue('--where'):
                    mode = Arg.getoptionvalue('--mode')
                    whichPlace = Arg.getoptionvalue('--where')
                    container.CreateContainer(constainer_id,image,options,mode,whichPlace)
            else:
                raise Exception("User Name is Already Registered...")
      

    elif Arg.hasOption(['--list']):
        print("list")

    elif Arg.hasOptionValue('--name') and Arg.hasOption(['--info']):
        Dashboard = Dashboard(Arg.getoptionvalue('--name'))
        info = Dashboard.ContainerInfo()
        print(json.dumps(info, indent = 4))

    elif Arg.hasOption(['--list-all']):
        print("List the Containers list")
            

# except:
#     print("Error")


# Dashboard = Dashboard("sridhar")
# print(Dashboard.ContainerInfo())

