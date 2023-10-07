import subprocess

docker_executable = r'C:\Program Files\Docker\Docker\docker.exe'
command = [docker_executable, 'container', 'create', '--name', '9d4ccc91818ccb11a650', '-d', 'bc:1.0']

result = subprocess.call(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    print("Container created successfully.")
else:
    print("Error creating the container:")
    print(result.stderr)
