# import subprocess
from lib.User import User
usr = User()

# command = "docker images"

# output = subprocess.check_output(command, shell=True, text=True)
# lines = output.strip().split('\n')[1:]

# for i in lines:
#     if (str(i.split()[0]) == 'sridhardscv/simple_calculater'):
#         print(i.split()[6])
#     # print(i.split())


# test = "{'-e':'-er','-f':'fr'}"
# val = usr.UserContainerOption(test)
# print(val)


# import json

# # Open and read the JSON file
# with open('User/data.json', 'r') as json_file:
#     datas = json.load(json_file)

# value = 'b9fa87a5a0fa56dd9e48'
# for data in datas.items():
#     if data[1] == value:
#         print(data[0])

# import ast

# input_str = "['container1', 'container2']"
# container_list = ast.literal_eval(input_str)

# print(container_list)
# for i in container_list:
#     print(i)

text_to_save = "This is the text that will be saved in the text file."
file_name = "output.txt"
with open(file_name, "w") as text_file:
    text_file.write(text_to_save)

print(f'Text has been saved to {file_name}')





