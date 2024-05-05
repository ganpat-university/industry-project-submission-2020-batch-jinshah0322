using Microsoft.EntityFrameworkCore;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;

namespace OrderManagementAPI.Repository
{
    public class ReportProductRepository : IReportProduct
    {
        private readonly OrderManagementContext context;

        public ReportProductRepository(OrderManagementContext context)
        {
            this.context = context;
        }

        public async Task<List<Product>> GetProductsByStockQuantityRange(int minStockQuantity, int maxStockQuantity)
        {
            return await context.Products
                .Where(p => p.StockQuantity >= minStockQuantity && p.StockQuantity <= maxStockQuantity)
                .ToListAsync();
        }
    }
}
