# update_configs.py

import os
import subprocess

def get_current_localhost():
    result = subprocess.run(['dotnet', 'run'], capture_output=True, text=True)
    for line in result.stdout.split('\n'):
        if 'Now listening on:' in line:
            return line.split(' ')[-1].strip()
    return None

def update_config_files(localhost_url):
    files_to_update = [
        "launchSettings.json",
        "BabylonGameEngine.csproj"
    ]

    for file_name in files_to_update:
        with open(file_name, "r") as file:
            content = file.read()
        
        updated_content = content.replace("https://localhost:7072", localhost_url)
        
        with open(file_name, "w") as file:
            file.write(updated_content)

if __name__ == "__main__":
    localhost_url = get_current_localhost()
    if localhost_url:
        update_config_files(localhost_url)
    else:
        print("Failed to detect localhost URL.")
