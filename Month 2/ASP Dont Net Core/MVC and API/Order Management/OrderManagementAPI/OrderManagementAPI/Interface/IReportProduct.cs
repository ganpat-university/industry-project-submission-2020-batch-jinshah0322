using OrderManagementAPI.DataAccess;

namespace OrderManagementAPI.Interface
{
    public interface IReportProduct
    {
        Task<List<Product>> GetProductsByStockQuantityRange(int minStockQuantity, int maxStockQuantity);
    }
}
