using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Newtonsoft.Json;
using System.ComponentModel.DataAnnotations;
using System.Net.Http;
using System.Reflection.Metadata.Ecma335;
using System.Text;

namespace ConsumeAPI.Controllers
{
    public class EmployeeController : Controller
    {

        private readonly HttpClient _httpClient;
        private readonly string _baseAddress;

        public EmployeeController()
        {
            _httpClient = new HttpClient();
            _baseAddress = "http://192.168.11.57:8082/api/EmployeeAPI";
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

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        public async Task<IActionResult> Create(IFormCollection createEmployeeData)
        {
            var data = new Dictionary<string, string>();
            for (int i = 0; i < createEmployeeData.Count-1; i++)
            {
                string field = createEmployeeData.Keys.ElementAt(i);
                string value = createEmployeeData[field];
                data.Add(field, value);
            }
            var jsonData = JsonConvert.SerializeObject(data);
            var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
            var response = await _httpClient.PostAsync(_baseAddress, content);
            if (response.IsSuccessStatusCode)
            {
                return RedirectToAction("Index");
            }
            return RedirectToAction("Create");
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
            data.Add("employeeId", $"{id}");
            for (int i = 0; i < form.Count-1; i++)
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
            return RedirectToAction("Create");
        }

    }
}