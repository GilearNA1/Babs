using Microsoft.AspNetCore.Mvc;
using BabylonGameEngine.Services;

namespace BabylonGameEngine.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class NPCController : ControllerBase
    {
        private readonly INPCService _npcService;

        public NPCController(INPCService npcService)
        {
            _npcService = npcService;
        }

        // Define your endpoints here
    }
}