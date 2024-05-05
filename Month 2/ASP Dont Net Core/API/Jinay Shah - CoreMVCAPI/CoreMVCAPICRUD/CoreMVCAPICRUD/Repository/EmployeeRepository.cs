using CoreMVCAPICRUD.DataAccess;
using CoreMVCAPICRUD.Models;
using CoreMVCAPICRUD.Interface;
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.EntityFrameworkCore;

namespace CoreMVCAPICRUD.Repository
{
    public class EmployeeRepository : IEmployee
    {
        private readonly CoreMvcContext context;

        public EmployeeRepository(CoreMvcContext context)
        {
            this.context = context;
        }

        public async Task<List<Employee>> GetAllEmployee()
        {
            return await context.Employees.ToListAsync();
        }

        public async Task<Employee> GetEmployeeByID(int id)
        {
            return await context.Employees.FindAsync(id);
        }

        public async Task<EmployeeModel> AddEmployee(EmployeeModel employee)
        {
            Employee employee1 = new Employee();
            employee1.EmployeeId = employee.EmployeeId;
            employee1.FirstName = employee.FirstName;
            employee1.LastName = employee.LastName;
            employee1.Email = employee.Email;
            employee1.Salary = employee.Salary;
            employee1.HireDate = employee.HireDate;
            await context.Employees.AddAsync(employee1);
            await context.SaveChangesAsync();
            return employee;
        }

        public async Task<EmployeeModel> UpdateEmployee(int id, EmployeeModel employee)
        {
            Employee employee1 = new Employee();
            employee1.EmployeeId = employee.EmployeeId;
            employee1.FirstName = employee.FirstName;
            employee1.LastName = employee.LastName;
            employee1.Email = employee.Email;
            employee1.Salary= employee.Salary;
            employee1.HireDate = employee.HireDate;
            context.Entry(employee1).State = EntityState.Modified;
            await context.SaveChangesAsync();
            return employee;
        }

        public async Task<Employee> DeleteEmployee(int id)
        {
            var employee = await context.Employees.FindAsync(id);
            if (employee == null)
            {
                return null;
            }
            context.Employees.Remove(employee);
            await context.SaveChangesAsync();
            return employee;
        }
    }
}
