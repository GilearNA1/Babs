import os

def run_migrations():
    os.system('dotnet ef migrations add InitialCreate')
    os.system('dotnet ef database update')

run_migrations()
