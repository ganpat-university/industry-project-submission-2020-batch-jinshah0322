using OrderManagementAPI.Model;
using OrderManagementAPI.DataAccess;

namespace OrderManagementAPI.Interface
{
    public interface ICustomer
    {
        Task<List<Customer>> GetAllCustomer();
        Task<Customer> GetCustomerByID(int id);
        Task<List<Order>> GetOrdersByCustomerId(int customerId);
        Task<CustomerModel> AddCustomer(CustomerModel employee);
        Task<CustomerModel> UpdateCustomer(int id, CustomerModel employee);
        Task<Customer> DeleteCustomer(int id);
    }
}
