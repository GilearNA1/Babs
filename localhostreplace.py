import os
import re
import socket

# Define the directory where your project files are located
project_directory = "C:/Users/ian/Babylon/BabylonGameEngine/scripts/BabylonGameEngine"

# Get the current hostname
hostname = socket.gethostname()

# Define the regex pattern to find localhost URLs
pattern = r"localhost:\d+"

# Function to replace old_url with new_url in a file
def update_file(file_path, pattern, new_url):
    with open(file_path, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub(pattern, new_url, filedata)

    # Write the file out again
    with open(file_path, 'w') as file:
        file.write(filedata)
    print(f"Updated {file_path}")

# Walk through all files in the project directory
for root, dirs, files in os.walk(project_directory):
    for file in files:
        if file.endswith('.cs') or file.endswith('.json') or file.endswith('.py'):
            file_path = os.path.join(root, file)
            update_file(file_path, pattern, hostname + ":5299")

print("All files have been updated.")
