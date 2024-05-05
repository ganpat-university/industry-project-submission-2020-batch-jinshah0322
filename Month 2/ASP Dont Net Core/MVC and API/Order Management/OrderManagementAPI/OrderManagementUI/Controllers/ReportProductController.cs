using Microsoft.AspNetCore.Mvc;

namespace OrderManagementUI.Controllers
{
    public class ReportProductController : Controller
    {
        private readonly HttpClient _httpClient;
        public ReportProductController()
        {
            _httpClient = new HttpClient();
        }
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Index(int minStockQuantity, int maxStockQuantity)
        {
            // Redirect to action that displays the data
            return RedirectToAction("ReportData", new { minStockQuantity, maxStockQuantity});
        }

        public async Task<IActionResult> ReportData(int minStockQuantity, int maxStockQuantity)
        {
            var apiUrl = $"https://localhost:7274/api/Product?minStockQuantity={minStockQuantity}&maxStockQuantity={maxStockQuantity}";

            var response = await _httpClient.GetAsync(apiUrl);

            if (response.IsSuccessStatusCode)
            {
                var reports = await response.Content.ReadAsStringAsync();
                return View("ReportData", reports);
            }
            else
            {
                // Handle error
                return View("Error");
            }
        }
    }
}
