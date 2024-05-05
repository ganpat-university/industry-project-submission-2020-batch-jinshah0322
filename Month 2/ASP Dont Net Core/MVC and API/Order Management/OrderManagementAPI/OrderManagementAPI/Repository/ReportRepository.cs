using Microsoft.EntityFrameworkCore;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;

namespace OrderManagementAPI.Repository
{
    public class ReportRepository : IReport
    {
        private readonly OrderManagementContext context;

        public ReportRepository(OrderManagementContext context)
        {
            this.context = context;
        }

        public async Task<List<Order>> GetOrdersByDateRange(DateTime startDate, DateTime endDate)
        {
            return await context.Orders
                .Where(o => o.OrderDate >= startDate && o.OrderDate <= endDate)
                .ToListAsync();
        }
    }
}