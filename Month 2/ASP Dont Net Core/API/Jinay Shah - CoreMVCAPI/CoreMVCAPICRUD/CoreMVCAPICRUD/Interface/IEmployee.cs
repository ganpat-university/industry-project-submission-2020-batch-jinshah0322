using CoreMVCAPICRUD.Models;
using CoreMVCAPICRUD.DataAccess;

namespace CoreMVCAPICRUD.Interface
{
    public interface IEmployee
    {
        Task<List<Employee>> GetAllEmployee();
        Task<Employee> GetEmployeeByID(int id);
        Task<EmployeeModel> AddEmployee(EmployeeModel employee);
        Task<EmployeeModel> UpdateEmployee(int id , EmployeeModel employee);
        Task<Employee> DeleteEmployee(int id);
    }
}