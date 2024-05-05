using Microsoft.EntityFrameworkCore;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Repository
{
    public class CustomerRepository : ICustomer
    {
        private readonly OrderManagementContext context;

        public CustomerRepository(OrderManagementContext context)
        {
            this.context = context;
        }

        public async Task<CustomerModel> AddCustomer(CustomerModel customer)
        {
            Customer customer1 = new Customer();
            customer1.Name = customer.Name;
            customer1.Email = customer.Email;
            customer1.Address = customer.Address;
            await context.Customers.AddAsync(customer1);
            await context.SaveChangesAsync();
            customer.CustomerId = customer1.CustomerId;
            return customer;
        }

        public async Task<Customer> DeleteCustomer(int id)
        {
            var customer = await context.Customers.FindAsync(id);
            if (customer == null)
            {
                return null;
            }
            customer.IsDeleted = true;
            await context.SaveChangesAsync();
            return customer;
        }

        public async Task<List<Customer>> GetAllCustomer()
        {
            return await context.Customers.Where(c=>c.IsDeleted == false).ToListAsync();
        }

        public async Task<Customer> GetCustomerByID(int id)
        {
            return await context.Customers.FirstOrDefaultAsync(c => c.CustomerId == id && c.IsDeleted == false);
        }

        public async Task<List<Order>> GetOrdersByCustomerId(int customerId)
        {
            return await context.Orders.Where(o => o.CustomerId == customerId && o.IsDeleted == false).ToListAsync();
        }

        public async Task<CustomerModel> UpdateCustomer(int id, CustomerModel customer)
        {
            var existingCustomer = await context.Customers.FindAsync(id);

            if (existingCustomer == null)
            {
                return null;
            }

            existingCustomer.Name = customer.Name;
            existingCustomer.Email = customer.Email;
            existingCustomer.Address = customer.Address;

            await context.SaveChangesAsync();

            return customer;
        }
    }
}
