import json
import ast
from lib.RunCommand import RunCommand
run = RunCommand()
class DockerContainer:
    def CreateContainer(self,name,image,options,mode,whichPlace):
        user_options = options.replace("'", "\"")
        user_options = options.replace("'", "\"")
        user_options_dict = ast.literal_eval(user_options)
        options_str = ''
        for i in user_options_dict.items():
            options_str = options_str + f"'{i[0]}','{i[1]}',"
        if whichPlace == None and mode == None:
                # docker container create --ip6 2001:db8::1 -it my-image /bin/bash
                # ['docker', 'build', '-t', 'my_image:latest', '.']
            command = f"['docker','container','create', {options_str[:-1]},'-d','{image}']"
            print(command)
            # run.Run_Command(command)
        if mode == '-d' and whichPlace == None:
            command = f"['docker','container','create', {options_str[:-1]},'-d','{image}']"
            print(command)
        if mode == '-it' and whichPlace != None:
            command = f"['docker','container','create', {options_str[:-1]},'{mode}','{image}','{whichPlace}']"
            print(command)
