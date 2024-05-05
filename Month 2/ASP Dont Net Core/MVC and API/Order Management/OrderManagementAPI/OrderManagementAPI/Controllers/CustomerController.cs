using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CustomerController : ControllerBase
    {
        private readonly ICustomer customerRepository;

        public CustomerController(ICustomer customerRepository)
        {
            this.customerRepository = customerRepository;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllCustomer()
        {
            var customers = await customerRepository.GetAllCustomer();
            return Ok(customers);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetCustomerByID(int id)
        {
            var customer = await customerRepository.GetCustomerByID(id);
            if (customer == null)
            {
                return NotFound();
            }
            return Ok(customer);
        }

        [HttpGet]
        [Route("orders/{customerId}")]
        public async Task<IActionResult> GetOrdersByCustomerId(int customerId)
        {
            var orders = await customerRepository.GetOrdersByCustomerId(customerId);
            if (orders == null)
            {
                return NotFound();
            }
            return Ok(orders);
        }

        [HttpPost]
        public async Task<IActionResult> AddCustomer(CustomerModel customer)
        {
            var newCustomer = await customerRepository.AddCustomer(customer);
            return Ok(newCustomer);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateCustomer(int id, CustomerModel customer)
        {
            if (id != customer.CustomerId)
            {
                return NotFound();
            }
            var e = await customerRepository.UpdateCustomer(id, customer);
            return Ok(e);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteCustomer(int id)
        {
            var deletedCustomer = await customerRepository.DeleteCustomer(id);
            if (deletedCustomer == null)
            {
                return NotFound();
            }
            return Ok(deletedCustomer);
        }
    }
}
