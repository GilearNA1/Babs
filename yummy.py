import os

# Base directory
base_dir = "C:\\Users\\ian\\Babylon\\BabylonGameEngine\\"

# Directories to be created
directories = [
    "Controllers",
    "Services",
    "Models",
    "Data"
]

# Create directories
for directory in directories:
    os.makedirs(os.path.join(base_dir, directory), exist_ok=True)

# Controller template
controller_template = """using Microsoft.AspNetCore.Mvc;
using {namespace}.Services;
using System.Threading.Tasks;

namespace {namespace}.Controllers
{{
    [ApiController]
    [Route("api/[controller]")]
    public class {controller}Controller : ControllerBase
    {{
        private readonly I{controller}Service _{controller}Service;

        public {controller}Controller(I{controller}Service {controller}Service)
        {{
            _{controller}Service = {controller}Service;
        }}

        // Add your actions here
    }}
}}
"""

# Service template
service_template = """using System.Threading.Tasks;

namespace {namespace}.Services
{{
    public interface I{service}Service
    {{
        // Define your methods here
    }}

    public class {service}Service : I{service}Service
    {{
        // Implement your methods here
    }}
}}
"""

# Services to be created
services = [
    "Auth",
    "Character",
    "Inventory",
    "Achievement",
    "Quest",
    "Skill",
    "World"
]

namespace = "BabylonGameEngine"

# Create service files
for service in services:
    service_file = service + "Service.cs"
    service_path = os.path.join(base_dir, "Services", service_file)
    with open(service_path, "w") as f:
        f.write(service_template.format(namespace=namespace, service=service))

# Create controller files
for service in services:
    controller_file = service + "Controller.cs"
    controller_path = os.path.join(base_dir, "Controllers", controller_file)
    with open(controller_path, "w") as f:
        f.write(controller_template.format(namespace=namespace, controller=service))

# Add services to Startup.cs
startup_file = os.path.join(base_dir, "Startup.cs")
startup_code = """
public void ConfigureServices(IServiceCollection services)
{
    services.AddControllers();

    // Register services
"""

for service in services:
    startup_code += f"    services.AddScoped<I{service}Service, {service}Service>();\n"

startup_code += "}"

# Update Startup.cs with dependency injection configuration
with open(startup_file, "r") as f:
    lines = f.readlines()

with open(startup_file, "w") as f:
    for line in lines:
        if "public void ConfigureServices(IServiceCollection services)" in line:
            f.write(startup_code)
        else:
            f.write(line)

# Create models (example for Character model)
models = {
    "Character": """
namespace {namespace}.Models
{{
    public class Character
    {{
        public int Id { get; set; }
        public string Name { get; set; }
        public string Class { get; set; }
        public int Level { get; set; }
        // Other properties
    }}
}}
""".format(namespace=namespace)
}

# Create model files
for model, code in models.items():
    model_file = model + ".cs"
