using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Interface
{
    public interface IOrder
    {
        Task<List<Order>> GetAllOrder();
        Task<Order> GetOrderByID(int id);
        Task<OrderModel> AddOrder(OrderModel prder);
        Task<OrderModel> UpdateOrder(int id, OrderModel prder);
        Task<Order> DeleteOrder(int id);
    }
}
