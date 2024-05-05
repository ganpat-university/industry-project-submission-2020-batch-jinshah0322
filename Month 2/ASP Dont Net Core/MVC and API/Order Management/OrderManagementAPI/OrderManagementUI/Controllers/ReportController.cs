using Microsoft.AspNetCore.Mvc;
using OrderManagementUI.Models;


namespace OrderManagementUI.Controllers
{
    public class ReportController : Controller
    {
        private readonly HttpClient _httpClient;
        public ReportController()
        {
            _httpClient = new HttpClient();
        }
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Index(DateTime startDate, DateTime endDate)
        {
            // Redirect to action that displays the data
            return RedirectToAction("ReportData", new { startDate, endDate });
        }

        public async Task<IActionResult> ReportData(DateTime startDate, DateTime endDate)
        {
            var apiUrl = $"https://localhost:7274/api/Report?startDate={startDate.ToString("yyyy-MM-dd")}&endDate={endDate.ToString("yyyy-MM-dd")}";

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
