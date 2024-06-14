using Microsoft.AspNetCore.Mvc;
using BabylonGameEngine.Services;

namespace BabylonGameEngine.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AnalyticsController : ControllerBase
    {
        private readonly IAnalyticsService _analyticsService;

        public AnalyticsController(IAnalyticsService analyticsService)
        {
            _analyticsService = analyticsService;
        }

        // Define your endpoints here
    }
}