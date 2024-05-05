using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;
using OrderManagementAPI.Repository;

namespace OrderManagementAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class OrderItemController : ControllerBase
    {
        private readonly IOrderItem orderItemRepository;

        public OrderItemController(IOrderItem orderItemRepository)
        {
            this.orderItemRepository = orderItemRepository;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllOrderItem(int id)
        {
            var orderItems = await orderItemRepository.GetAllOrderItem(id);
            return Ok(orderItems);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetOrderItemByID(int id)
        {
            var orderItem = await orderItemRepository.GetOrderItemByID(id);
            if (orderItem == null)
            {
                return NotFound();
            }
            return Ok(orderItem);
        }

        [HttpGet("orderitem/{id}")]
        public async Task<IActionResult> GetOrderItemByOrderId(int id)
        {
            var orderItems = await orderItemRepository.GetOrderItemByOrderId(id);
            if (orderItems == null)
            {
                return NotFound();
            }
            int totalAmount = Convert.ToInt16(orderItems.Sum(item => item.UnitPrice * item.Quantity));
            return Ok(totalAmount);
        }

        [HttpPost]
        public async Task<IActionResult> AddOrderItem(OrderItemModel order)
        {
            var newOrderItem = await orderItemRepository.AddOrderItem(order);
            return Ok(newOrderItem);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateOrderItem(int id, OrderItemModel order)
        {
            if (id != order.OrderItemId)
            {
                return NotFound();
            }
            var e = await orderItemRepository.UpdateOrderItem(id, order);
            return Ok(e);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteOrderItem(int id)
        {
            var deletedOrderItem = await orderItemRepository.DeleteOrderItem(id);
            if (deletedOrderItem == null)
            {
                return NotFound();
            }
            return Ok(deletedOrderItem);
        }
    }
}
