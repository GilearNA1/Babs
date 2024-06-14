using Microsoft.AspNetCore.Mvc;
using BabylonGameEngine.Services;

namespace BabylonGameEngine.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class HomeController : ControllerBase
    {
        private readonly IHomeService _homeService;

        public HomeController(IHomeService homeService)
        {
            _homeService = homeService;
        }

        // Define your endpoints here
    }
}