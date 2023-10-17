from lib.Argument import Argument
import sys
from lib.ContainerCreate import ContainerCreate
from lib.Window import Window
Arg = Argument(sys.argv)
from lib.Container import Container
window = Window()
Arg = Argument(sys.argv)

def Create():
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
        print(data)
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
                        print(f'\nERROR {value["error"]}')
                            # window.showErrorMessage(f'The container {name} has been failed created..')
            else:
                # window.showErrorMessage(f'The container {name} has been failed created.. because already a Registered User')
                print(f'The container {name} has been failed created.. because the container is already available...')