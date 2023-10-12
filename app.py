from lib.Argument import Argument
from lib.Dashboard import Dashboard
import json
import os
import sys
from lib.User import User
from lib.Docker_ID import Docker_ID
from lib.ContainerAction import ContainerAction

# TODO: Containers Class
container = ContainerAction()
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
      
    # elif Arg.hasOption(['--list']):
    #     print("list")

    # elif Arg.hasOptionValue('--name') and Arg.hasOption(['--info']):
    #     Dashboard = Dashboard(Arg.getoptionvalue('--name'))
    #     info = Dashboard.ContainerInfo()
    #     print(json.dumps(info, indent = 4))

    # elif Arg.hasOption(['--list-all']):
    #     print("List the Containers list")
      
    # TODO: for container stop
    # TODO: if thw User have the Username or Container Id to Do a Container action
    

    try:
        if user.ContainerId(json_file_path): #TODO: if the Container name or id is given or not 
            id = user.ContainerId(json_file_path) # get the Container id in User Input
            # print(f"Container Id ==> {id}")
            name = user.ContainerName(json_file_path) # get the Container Name
            # print(f"Container Name ==> {name}")
            
            '''
            Command Usage ==> "python app.py Container --name="Sridhar" stop"
            Def           ==> for Container Stop 
            '''
            if Arg.hasCommands(['stop']):
                if Arg.hasOptionValue('--options'):
                    if container.ContainerStop(id,Arg.getoptionvalue('--options')):
                        print(f"Container {name} [{id}] stoped Succesfully....")
                else:
                    if container.ContainerStop(id):
                        print(f"Container {name} [{id}] stoped Successfully....")
                        
            if Arg.hasCommands(['restart']):
                if Arg.hasOptionValue('--options'):
                    if container.ContainerRestart(id,Arg.getoptionvalue('--options')):
                        print(f"Container {name} Restarted Succesfully....")
                else:
                    if container.ContainerRestart(id):
                        print(f"Container {name} Restarted Successfully....")
                        
                        
        else:
            raise Exception("Contianer Name or Container Id is not Available...")
    
        
    except Exception as e:
        print(e)
    
    
#     # TODO: for Cotainer Restart
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['restart']):
#         pass
    
    
#     # TODO: for container Remove
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['remove']):
#         pass
    
    
#     # TODO: for Contaienr Exec
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['exec']):
#         pass
    
    
#     # TODO: for Container export
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['export']):
#         pass
    
    
#     # TODO: for container inspect
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['inspect']):
#         pass
    
    
#     # TODO: for container kill
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['kill']):
#         pass
    
    
#     # TODO: for container logs
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['logs']):
#         pass
    
    
#     # TODO: for container ls
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['ls']):
#         pass

#     # TODO: for Container pause
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['pause']):
#         pass
    
#     # TODO: for port mapping
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['port']):
#         pass
    
#     # TODO: for Container Prune
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['prune']):
#         pass
    
#     # TODO: for Container rename
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['rename']):
#         pass
    
#     # TODO: for container restart
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['restart']):
#         pass
    
#     # TODO: for container run
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['run']):
#         pass
    
#     # TODO: for container run
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['run']):
#         pass    
    
#     # TODO: for container stats
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['stats']):
#         pass 
    
#     # TODO: for container Start
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['start']):
#         pass       
    
#     # TODO: for contaienr stop
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['stop']):
#         pass 
    
#     # TODO: for container top
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['top']):
#         pass  
    
#     # TODO: for container unpause
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['unpause']):
#         pass 
    
#     # TODO: for cotainer update
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['update']):
#         pass  
    
#     # TODO: for cotainer wait
#     elif Arg.hasOptionValue('--name') and Arg.hasCommands(['wait']):
#         pass  
    
# # except:
# #     print("Error")


# # Dashboard = Dashboard("sridhar")
# # print(Dashboard.ContainerInfo())

