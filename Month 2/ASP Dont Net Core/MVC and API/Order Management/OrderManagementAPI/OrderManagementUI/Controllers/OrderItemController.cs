using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System.Text;

namespace OrderManagementUI.Controllers
{
    public class OrderItemController : Controller
    {
        private readonly HttpClient _httpClient;
        private readonly string _baseAddress;

        public OrderItemController()
        {
            _httpClient = new HttpClient();
            _baseAddress = "https://localhost:7274/api/OrderItem";
        }

        public async Task<IActionResult> Index(int id)
        {
            var response = await _httpClient.GetAsync(_baseAddress+$"?id={id}");
            if (response.IsSuccessStatusCode)
            {
                var content = await response.Content.ReadAsStringAsync();
                return View("Index", content);
            }
            return NotFound();
        }

        public IActionResult Create(int customerId, int orderId)
        {
            TempData["CustomerId"] = customerId;
            TempData["OrderId"] = orderId;
            return View();
        }


        [HttpPost]
        public async Task<IActionResult> Create(IFormCollection createOrderItemData, int customerId, int orderId)
        {
            var data = new Dictionary<string, string>();
            for (int i = 0; i < createOrderItemData.Count; i++)
            {
                string field = createOrderItemData.Keys.ElementAt(i);
                string value = createOrderItemData[field];
                data.Add(field, value);
            }
            var jsonData = JsonConvert.SerializeObject(data);
            var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
            var response = await _httpClient.PostAsync(_baseAddress, content);
            if (response.IsSuccessStatusCode)
            {
                var responseContent = await response.Content.ReadAsStringAsync();
                var createdOrderItem = JsonConvert.DeserializeObject<dynamic>(responseContent);
                TempData["Item"] = "Item Added Successfully";
                return RedirectToAction("Create", "OrderItem", new { customerId=customerId,orderId=orderId});
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
                var responseContent = await response.Content.ReadAsStringAsync();
                var deletedItem = JsonConvert.DeserializeObject<dynamic>(responseContent);
                int orderId = deletedItem.orderId;
                return RedirectToAction("Index", new {id=orderId});
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
            data.Add("orderItemId", $"{id}");
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
                var responseContent = await response.Content.ReadAsStringAsync();
                var editedItem = JsonConvert.DeserializeObject<dynamic>(responseContent);
                int orderId = editedItem.orderId;
                return RedirectToAction("Index",new { id = orderId });
            }
            TempData["Edit"] = "Update Unsuccessful";
            return RedirectToAction("Edit", id);
        }
    }
}
