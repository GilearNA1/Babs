using Microsoft.AspNetCore.Mvc;
using BabylonGameEngine.Services;

namespace BabylonGameEngine.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SettingsController : ControllerBase
    {
        private readonly ISettingsService _settingsService;

        public SettingsController(ISettingsService settingsService)
        {
            _settingsService = settingsService;
        }

        // Define your endpoints here
    }
}