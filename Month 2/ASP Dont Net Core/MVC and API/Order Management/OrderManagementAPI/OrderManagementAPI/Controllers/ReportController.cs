using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Repository;

namespace OrderManagementAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ReportController : ControllerBase
    {
        private readonly IReport reportRepository;

        public ReportController(IReport reportRepository)
        {
            this.reportRepository = reportRepository;
        }

        [HttpGet]
        public async Task<IActionResult> GetOrdersByDateRange([FromQuery] DateTime startDate, [FromQuery] DateTime endDate)
        {
            var orders = await reportRepository.GetOrdersByDateRange(startDate, endDate);
            return Ok(orders);
        }
    }
}
