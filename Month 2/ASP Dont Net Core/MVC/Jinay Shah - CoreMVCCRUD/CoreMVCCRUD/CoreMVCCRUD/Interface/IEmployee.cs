using CoreMVCCRUD.Models;

namespace CoreMVCCRUD.Interface
{
    public interface IEmployee
    {
        IEnumerable<Employee> GetAllEmployees();
        Employee GetEmployeeById(int id);
        void Create(Employee e);
        void Edit(Employee e);
        void Delete(Employee e);
    }
}