using CoreMVCCRUD.Interface;
using CoreMVCCRUD.Models;
using Microsoft.EntityFrameworkCore;

namespace CoreMVCCRUD.Repository
{
    public class EmployeeRepository : IEmployee
    {
        private readonly CoreMvcContext context;
        public EmployeeRepository(CoreMvcContext context)
        {
            this.context = context;
        }
        public IEnumerable<Employee> GetAllEmployees()
        {
            return context.Employees.ToList();
        }

        public Employee GetEmployeeById(int id)
        {
            return context.Employees.Where(model => model.EmployeeId == id).FirstOrDefault();
        }

        public void Create(Employee employee)
        {
            context.Employees.Add(employee);
            context.SaveChanges();
        }

        public void Edit(Employee employee)
        {
            context.Attach(employee);
            context.Entry(employee).State = EntityState.Modified;
            context.SaveChanges();
        }

        public void Delete(Employee employee)
        {
            context.Employees.Remove(employee);
            context.SaveChanges();
        }
    }
}
