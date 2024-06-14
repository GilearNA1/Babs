using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using BabylonGameEngine.Models;

namespace BabylonGameEngine.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UserController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetUsers()
        {
            var users = new List<User>
            {
                new User { Id = 1, Name = "John Doe", Email = "john@example.com" },
                new User { Id = 2, Name = "Jane Doe", Email = "jane@example.com" }
            };
            return Ok(users);
        }
    }
}
