using DAL.DataAccess;
using DAL.Model;

namespace DAL.Interface
{
    public interface IEmployee
    {
        Task<List<Employee>> GetAllEmployee();
        Task<Employee> GetEmployeeByID(int id);
        Task<EmployeeData> AddEmployee(EmployeeData employee);
        Task<EmployeeData> UpdateEmployee(int id, EmployeeData employee);
        Task<Employee> DeleteEmployee(int id);
    }
}