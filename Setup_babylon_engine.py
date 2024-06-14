import os

def create_controller_file(name):
    content = f"""
using Microsoft.AspNetCore.Mvc;
using BabylonGameEngine.Services;

namespace BabylonGameEngine.Controllers
{{
    [ApiController]
    [Route("api/[controller]")]
    public class {name}Controller : ControllerBase
    {{
        private readonly I{name}Service _{name.lower()}Service;

        public {name}Controller(I{name}Service {name.lower()}Service)
        {{
            _{name.lower()}Service = {name.lower()}Service;
        }}

        // Define your endpoints here
    }}
}}
"""
    with open(f"Controllers/{name}Controller.cs", "w") as file:
        file.write(content.strip())

def create_service_file(name):
    content = f"""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BabylonGameEngine.Services
{{
    public interface I{name}Service
    {{
        // Define your service interface here
    }}

    public class {name}Service : I{name}Service
    {{
        // Implement your service here
    }}
}}
"""
    with open(f"Services/{name}Service.cs", "w") as file:
        file.write(content.strip())

def main():
    controllers = [
        "Auth",
        "Character",
        "Inventory",
        "Achievement",
        "Quest",
        "Skill",
        "World",
        "NPC",
        "Logging",
        "Notification",
        "Leaderboard",
        "Analytics",
        "Settings",
        "User",
        "Home"
    ]

    for controller in controllers:
        create_controller_file(controller)
        create_service_file(controller)
        print(f"Created {controller}Controller.cs and {controller}Service.cs")

if __name__ == "__main__":
    main()

