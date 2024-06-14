import os

def install_nuget_packages():
    packages = [
        "Microsoft.EntityFrameworkCore",
        "Microsoft.EntityFrameworkCore.SqlServer",
        "Microsoft.AspNetCore.Authentication.JwtBearer",
        "Swashbuckle.AspNetCore"
    ]
    for package in packages:
        os.system(f'dotnet add package {package} --version 8.0.0-preview.5.23280.1')

install_nuget_packages()
