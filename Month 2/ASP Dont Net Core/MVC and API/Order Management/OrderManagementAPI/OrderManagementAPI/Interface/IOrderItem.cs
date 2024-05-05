using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Interface
{
    public interface IOrderItem
    {
        Task<List<OrderItem>> GetAllOrderItem(int id);
        Task<OrderItem> GetOrderItemByID(int id);
        Task<List<OrderItem>> GetOrderItemByOrderId(int id);
        Task<OrderItemModel> AddOrderItem(OrderItemModel prder);
        Task<OrderItemModel> UpdateOrderItem(int id, OrderItemModel prder);
        Task<OrderItem> DeleteOrderItem(int id);
    }
}