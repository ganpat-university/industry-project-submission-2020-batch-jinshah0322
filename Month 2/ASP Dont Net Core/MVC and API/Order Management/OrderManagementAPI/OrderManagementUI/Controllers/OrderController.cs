using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System.Text;

namespace OrderManagementUI.Controllers
{
    public class OrderController : Controller
    {
        private readonly HttpClient _httpClient;
        private readonly string _baseAddress;

        public OrderController()
        {
            _httpClient = new HttpClient();
            _baseAddress = "https://localhost:7274/api/Order";
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


        public async Task<IActionResult> Create(int id)
        {
            return View("Create", id);
        }

        [HttpPost]
        public async Task<IActionResult> Create(IFormCollection createOrderData, int customerId)
            {
            var data = new Dictionary<string, string>();
            for (int i = 0; i < createOrderData.Count - 1; i++)
            {
                string field = createOrderData.Keys.ElementAt(i);
                string value = createOrderData[field];
                data.Add(field, value);
            }
            data.Add("totalAmount", "0");
            data.Add("status", "pending");
            var jsonData = JsonConvert.SerializeObject(data);
            var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
            var response = await _httpClient.PostAsync(_baseAddress, content);
            if (response.IsSuccessStatusCode)
            {
                return RedirectToAction("Order", "Customer", new { id = customerId });
            }
            return View();
        }

        public async Task<IActionResult> Details(int id)
        {
            var response = await _httpClient.GetAsync(_baseAddress + $"/{id}");
            if (response.IsSuccessStatusCode)
            {
                var orderItems =  await _httpClient.GetAsync($"https://localhost:7274/api/OrderItem/orderitem/{id}");
                if (orderItems.IsSuccessStatusCode)
                {
                    var totalAmountContent = await orderItems.Content.ReadAsStringAsync();
                    TempData["totalAmount"] = Convert.ToInt32(totalAmountContent);
                }
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
                var responseContent = await response.Content.ReadAsStringAsync();
                var createdOrder = JsonConvert.DeserializeObject<dynamic>(responseContent);
                var customerId = createdOrder.customerId;
                return RedirectToAction("Order", "Customer", new { id = customerId });
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
            data.Add("OrderId", $"{id}");
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
