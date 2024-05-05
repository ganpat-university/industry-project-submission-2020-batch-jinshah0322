using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Repository;

namespace OrderManagementUI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ReportProductController : ControllerBase
    {
        private readonly IReportProduct reportProductRepository;

        public ReportProductController(IReportProduct reportProductRepository)
        {
            this.reportProductRepository = reportProductRepository;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Product>>> GetProductsByStockQuantityRange(int minStockQuantity, int maxStockQuantity)
        {
            var products = await reportProductRepository.GetProductsByStockQuantityRange(minStockQuantity, maxStockQuantity);
            return Ok(products);
        }
    }
}
