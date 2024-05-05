using Microsoft.EntityFrameworkCore;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Repository
{
    public class OrderItemRepository : IOrderItem
    {
        private readonly OrderManagementContext context;

        public OrderItemRepository(OrderManagementContext context)
        {
            this.context = context;
        }

        public async Task<OrderItemModel> AddOrderItem(OrderItemModel orderItem)
        {
            OrderItem orderItem1 = new OrderItem();
            orderItem1.OrderId = orderItem.OrderId;
            orderItem1.ProductId = orderItem.ProductId;
            orderItem1.Quantity = orderItem.Quantity;
            orderItem1.UnitPrice = orderItem.UnitPrice;
            await context.OrderItems.AddAsync(orderItem1);
            var order = await context.Orders.FindAsync(orderItem1.OrderId);
            order.TotalAmount += (orderItem1.Quantity * orderItem1.UnitPrice);
            await context.SaveChangesAsync();
            return orderItem;
        }

        public async Task<OrderItem> DeleteOrderItem(int id)
        {
            var orderItem = await context.OrderItems.FindAsync(id);
            var order = await context.Orders.FindAsync(orderItem.OrderId);
            order.TotalAmount -= orderItem.UnitPrice * orderItem.Quantity;
            if (orderItem == null)
            {
                return null;
            }
            orderItem.IsDeleted = true;
            await context.SaveChangesAsync();
            return orderItem;
        }

        public async Task<List<OrderItem>> GetAllOrderItem(int id)
        {
            return await context.OrderItems.Where(oi => oi.OrderId == id && oi.IsDeleted == false).ToListAsync();
        }

        public async Task<List<OrderItem>> GetOrderItemByOrderId(int id)
        {
            return await context.OrderItems.Where(oi => oi.OrderId == id && oi.IsDeleted == false).ToListAsync();
        }

        public async Task<OrderItem> GetOrderItemByID(int id)
        {
            return await context.OrderItems.FirstOrDefaultAsync(oi => oi.OrderItemId == id && oi.IsDeleted == false);
        }

        public async Task<OrderItemModel> UpdateOrderItem(int id, OrderItemModel orderItem)
        {
            var existingOrderItem = await context.OrderItems.FindAsync(id);
            var order = await context.Orders.FindAsync(orderItem.OrderId);
            order.TotalAmount -= orderItem.UnitPrice * orderItem.Quantity;
            if (existingOrderItem == null)
            {
                return null;
            }

            existingOrderItem.Quantity = orderItem.Quantity;
            existingOrderItem.UnitPrice = orderItem.UnitPrice;
            order.TotalAmount = existingOrderItem.Quantity * existingOrderItem.UnitPrice;

            await context.SaveChangesAsync();

            return orderItem;
        }
    }
}
