# import subprocess

# command = "docker images"

# output = subprocess.check_output(command, shell=True, text=True)
# lines = output.strip().split('\n')[1:]

# for i in lines:
#     if (str(i.split()[0]) == 'sridhardscv/simple_calculater'):
#         print(i.split()[6])
#     # print(i.split())


test = {'-e':'-er','-f':'fr'}
dict_str = ', '.join([f'{key}: {value}' for key, value in test.items()])
re = dict_str.replace(',','')
print(re.replace(':',''))
