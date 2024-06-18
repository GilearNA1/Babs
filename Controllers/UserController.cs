using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using YourNamespace.Models; // Add this line to include the namespace for the User class

namespace YourNamespace.Controllers // Ensure this matches the namespace of your project
{
    [Route("api/[controller]")]
    [ApiController]
    public class UserController : ControllerBase
    {
        // GET: api/User
        [HttpGet]
        public IEnumerable<User> Get()
        {
            return new List<User>
            {
                new User { Id = 1, Name = "John Doe", Email = "john.doe@example.com" },
                new User { Id = 2, Name = "Jane Smith", Email = "jane.smith@example.com" }
            };
        }

        // GET: api/User/5
        [HttpGet("{id}", Name = "GetUser")]
        public User Get(int id)
        {
            return new User { Id = id, Name = "John Doe", Email = "john.doe@example.com" };
        }

        // POST: api/User
        [HttpPost]
        public void Post([FromBody] User user)
        {
            // Add user to database or collection
        }

        // PUT: api/User/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] User user)
        {
            // Update user in database or collection
        }

        // DELETE: api/User/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
            // Delete user from database or collection
        }
    }
}
