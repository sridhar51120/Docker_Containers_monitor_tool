import subprocess

# docker_executable = r'C:\Program Files\Docker\Docker\docker.exe'
command = ["docker","images"]

result = subprocess.run(command,capture_output=True, text=True)

# if result.returncode == 0:
#     print("Container created successfully.")
# else:
#     print("Error creating the container:")
#     print(result.stderr)
print(result)
