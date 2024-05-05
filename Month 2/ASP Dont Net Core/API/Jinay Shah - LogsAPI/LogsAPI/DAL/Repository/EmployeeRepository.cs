using DAL.DataAccess;
using DAL.Interface;
using DAL.Model;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL.Repository
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

        public async Task<EmployeeData> AddEmployee(EmployeeData employee)
        {
            Employee employee1 = new Employee();
            employee1.EmployeeId = employee.EmployeeId;
            employee1.FirstName = employee.FirstName;
            employee1.LastName = employee.LastName;
            employee1.Email = employee.Email;
            employee1.HireDate = employee.HireDate;
            await context.Employees.AddAsync(employee1);
            await context.SaveChangesAsync();
            return employee;
        }

        public async Task<EmployeeData> UpdateEmployee(int id, EmployeeData employee)
        {
            Employee employee1 = new Employee();
            employee1.EmployeeId = employee.EmployeeId;
            employee1.FirstName = employee.FirstName;
            employee1.LastName = employee.LastName;
            employee1.Email = employee.Email;
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
