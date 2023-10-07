from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import sys
from lib.DockerContainer import DockerContainer

# TODO: Containers Class
container = DockerContainer()
Arg = Argument(sys.argv)
       
def addUser(data, json_file_path="data.json"):
    try:
        if json_file_path and json_file_path.strip() and len(json_file_path.strip()) > 0:
            with open(json_file_path, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []
        existing_data.append(data)

        with open(json_file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
        return True

    except json.JSONDecodeError as e:
        print(f"Invalid JSON format in the JSON file: {json_file_path}")
        return False

    except Exception as e:
        print("An error occurred:", str(e))
        return False

# try:
if Arg.hasCommands(['Container']):
    # Create A container with (name or ID) with image
    # python app.py Container Create --name=sri --image=sjhfd --options="{'-e':'-er','-f':'fr'}"
    # docker container create --ip6 2001:db8::1 -it my-image /bin/bash
    if Arg.hasCommands(['Create']):
        if Arg.hasOptionValue('--name') and Arg.hasOptionValue('--image') or Arg.hasOptionValue('--options'):
            name = Arg.getoptionvalue('--name')
            image = Arg.getoptionvalue('--image')
            
            if Arg.getoptionvalue('--options') != None:
                options = Arg.getoptionvalue('--options')

            if Arg.getoptionvalue('--mode') == "-d":
                mode = Arg.getoptionvalue('--mode')
                whichPlace = None
                print(mode)
                print(whichPlace)
                container.CreateContainer(name,image,options,mode,whichPlace)
    
            if Arg.getoptionvalue('--mode') == "-it" and Arg.hasOptionValue('--where'):
                mode = Arg.getoptionvalue('--mode')
                whichPlace = Arg.getoptionvalue('--where')
                # print(mode)
                # print(whichPlace)
                container.CreateContainer(name,image,options,mode,whichPlace)
            mode = None
            whichPlace = None
            container.CreateContainer(name,image,options,mode,whichPlace)
            

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

