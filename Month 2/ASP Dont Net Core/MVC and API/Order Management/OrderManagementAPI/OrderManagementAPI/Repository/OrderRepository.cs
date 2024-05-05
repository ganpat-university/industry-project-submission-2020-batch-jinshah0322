    using Microsoft.EntityFrameworkCore;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Repository
{
    public class OrderRepository : IOrder
    {
        private readonly OrderManagementContext context;

        public OrderRepository(OrderManagementContext context)
        {
            this.context = context;
        }

        public async Task<OrderModel> AddOrder(OrderModel order)
        {
            Order order1 = new Order();
            order1.CustomerId = order.CustomerId;
            order1.OrderDate = order.OrderDate;
            order1.TotalAmount = order.TotalAmount;
            order1.Status = order.Status;
            await context.Orders.AddAsync(order1);
            await context.SaveChangesAsync();
            return order;
        }

        public async Task<Order> DeleteOrder(int id)
        {
            var order = await context.Orders.FindAsync(id);
            if (order == null)
            {
                return null;
            }
            order.IsDeleted = true;
            await context.SaveChangesAsync();
            return order;
        }

        public async Task<List<Order>> GetAllOrder()
        {
            return await context.Orders.Where(o => o.IsDeleted == false).ToListAsync();
        }

        public async Task<Order> GetOrderByID(int id)
        {
            return await context.Orders.FirstOrDefaultAsync(o => o.OrderId == id && o.IsDeleted == false);
        }

        public async Task<OrderModel> UpdateOrder(int id, OrderModel order)
        {
            var existingOrder = await context.Orders.FindAsync(id);

            if (existingOrder == null)
            {
                return null;
            }

            existingOrder.OrderDate = order.OrderDate;
            existingOrder.TotalAmount = order.TotalAmount;
            existingOrder.Status = order.Status;

            await context.SaveChangesAsync();

            return order;
        }
    }
}
