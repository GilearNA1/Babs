# controller_service.py

import os

controller_template = """using System;
using Microsoft.AspNetCore.Mvc;

namespace BabylonGameEngine.Controllers
{{
    [Route("api/[controller]")]
    [ApiController]
    public class {controller_name}Controller : ControllerBase
    {{
        // Your code here
    }}
}}
"""

service_template = """using System;
using Microsoft.Extensions.Logging;

namespace BabylonGameEngine.Services
{{
    public class {service_name}Service
    {{
        private readonly ILogger<{service_name}Service> _logger;

        public {service_name}Service(ILogger<{service_name}Service> logger)
        {{
            _logger = logger;
        }}

        // Your code here
    }}
}}
"""

def create_controller_service_files(controller_name, service_name):
    controller_file_content = controller_template.format(controller_name=controller_name)
    service_file_content = service_template.format(service_name=service_name)

    controller_file_path = os.path.join("Controllers", f"{controller_name}Controller.cs")
    service_file_path = os.path.join("Services", f"{service_name}Service.cs")

    with open(controller_file_path, "w") as controller_file:
        controller_file.write(controller_file_content)
    
    with open(service_file_path, "w") as service_file:
        service_file.write(service_file_content)

if __name__ == "__main__":
    controllers_and_services = [
        ("Auth", "Auth"),
        ("Character", "Character"),
        ("Inventory", "Inventory"),
        ("Achievement", "Achievement"),
        ("Quest", "Quest"),
        ("Skill", "Skill"),
        ("World", "World"),
        ("NPC", "NPC"),
        ("Logging", "Logging"),
        ("Notification", "Notification"),
        ("Leaderboard", "Leaderboard"),
        ("Analytics", "Analytics"),
        ("Settings", "Settings"),
        ("User", "User"),
        ("Home", "Home")
    ]

    for controller_name, service_name in controllers_and_services:
        create_controller_service_files(controller_name, service_name)
