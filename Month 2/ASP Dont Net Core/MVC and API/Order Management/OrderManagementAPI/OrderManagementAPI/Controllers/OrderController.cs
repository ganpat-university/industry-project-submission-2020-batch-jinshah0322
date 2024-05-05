using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;
using OrderManagementAPI.Repository;

namespace OrderManagementAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class OrderController : ControllerBase
    {
        private readonly IOrder orderRepository;

        public OrderController(IOrder orderRepository)
        {
            this.orderRepository = orderRepository;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllOrder()
        {
            var orders = await orderRepository.GetAllOrder();
            return Ok(orders);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetOrderByID(int id)
        {
            var order = await orderRepository.GetOrderByID(id);
            if (order == null)
            {
                return NotFound();
            }
            return Ok(order);
        }

        [HttpPost]
        public async Task<IActionResult> AddOrder(OrderModel order)
        {
            var newOrder = await orderRepository.AddOrder(order);
            return Ok(newOrder);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateOrder(int id, OrderModel order)
        {
            if (id != order.OrderId)
            {
                return NotFound();
            }
            var e = await orderRepository.UpdateOrder(id, order);
            return Ok(e);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteOrder(int id)
        {
            var deletedOrder = await orderRepository.DeleteOrder(id);
            if (deletedOrder == null)
            {
                return NotFound();
            }
            return Ok(deletedOrder);
        }
    }
}
