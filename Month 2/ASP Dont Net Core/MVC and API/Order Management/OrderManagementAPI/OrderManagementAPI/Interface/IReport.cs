using OrderManagementAPI.DataAccess;

namespace OrderManagementAPI.Interface
{
    public interface IReport
    {
        Task<List<Order>> GetOrdersByDateRange(DateTime startDate, DateTime endDate);
    }
}
