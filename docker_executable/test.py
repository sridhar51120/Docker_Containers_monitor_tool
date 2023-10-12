import shutil

def find_docker_executable():
    docker_executable = shutil.which('docker')
    return docker_executable

docker_path = find_docker_executable()

if docker_path:
    print(f"Docker executable found at: {docker_path}")
else:
    print("Docker executable not found in the system's PATH.")
