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
            
        if mode == '-d' and whichPlace == None:
            command = f"['docker','container','create', {options_str[:-1]},'--name',{name},'-d','{image}']"
            run.Run_Command(command)
        if mode == '-it' and whichPlace != None:
            command = f"['docker','container','create', {options_str[:-1]},'--name',{name},'{mode}','{image}','{whichPlace}']"
            run.Run_Command(command)
