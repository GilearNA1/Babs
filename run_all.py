# run_all.py

import os
import subprocess
from update_configs import get_current_localhost, update_config_files

def main():
    current_localhost = get_current_localhost()
    if not current_localhost:
        print("Failed to detect the current localhost URL.")
        return
    
    update_config_files(current_localhost)
    
    os.system("python controller_service.py")
    os.system("python migrate.py")
    os.system("python Nug.py")
    os.system("python postman_python.py")
    os.system("python CI_CD.py")

if __name__ == "__main__":
    main()
