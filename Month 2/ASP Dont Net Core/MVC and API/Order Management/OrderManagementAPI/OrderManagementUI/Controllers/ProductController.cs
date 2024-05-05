using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System.Text;

namespace OrderManagementUI.Controllers
{
    public class ProductController : Controller
    {
        private readonly HttpClient _httpClient;
        private readonly string _baseAddress;

        public ProductController()
        {
            _httpClient = new HttpClient();
            _baseAddress = "https://localhost:7274/api/Product";
        }

        public async Task<IActionResult> Index()
        {
            var response = await _httpClient.GetAsync(_baseAddress);
            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                return View("Index", content);
            }
            return NotFound();
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Create(IFormCollection createProductData)
        {
            var data = new Dictionary<string, string>();
            for (int i = 0; i < createProductData.Count - 1; i++)
            {
                string field = createProductData.Keys.ElementAt(i);
                string value = createProductData[field];
                data.Add(field, value);
            }
            var jsonData = JsonConvert.SerializeObject(data);
            var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
            var response = await _httpClient.PostAsync(_baseAddress, content);
            if (response.IsSuccessStatusCode)
            {
                return RedirectToAction("Index");
            }
            else
            {
                TempData["Create"] = "All Fields are mandatory";
                return RedirectToAction("Create");
            }
        }

        public async Task<IActionResult> Details(int id)
        {
            var response = await _httpClient.GetAsync(_baseAddress + $"/{id}");
            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                return View("Details", content);
            }
            return NotFound();
        }

        public async Task<IActionResult> Delete(int id)
        {
            var response = await _httpClient.DeleteAsync(_baseAddress + $"/{id}");
            if (response.IsSuccessStatusCode)
            {
                return RedirectToAction("Index");
            }
            return NotFound();
        }

        public async Task<IActionResult> Edit(int id)
        {
            var response = await _httpClient.GetAsync(_baseAddress + $"/{id}");
            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                return View("Edit", content);
            }
            return NotFound();
        }

        [HttpPost]
        public async Task<IActionResult> Edit(int id, IFormCollection form)
        {
            var data = new Dictionary<string, string>();
            data.Add("productId", $"{id}");
            for (int i = 0; i < form.Count - 1; i++)
            {
                string field = form.Keys.ElementAt(i);
                string value = form[field];
                data.Add(field, value);
            }
            var jsonData = JsonConvert.SerializeObject(data);
            var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
            var response = await _httpClient.PutAsync(_baseAddress + $"/{id}", content);
            if (response.IsSuccessStatusCode)
            {
                return RedirectToAction("Index");
            }
            TempData["Edit"] = "Update Unsuccessful";
            return RedirectToAction("Edit", id);
        }
    }
}
