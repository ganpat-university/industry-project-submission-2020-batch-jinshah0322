using DAL.DataAccess;
using DAL.Interface;
using DAL.Model;

namespace BAL
{
    public class EmployeeRepositoryService : IEmployeeService
    {
        private readonly IEmployee employeeRepository;

        public EmployeeRepositoryService(IEmployee employeeRepository)
        {
            this.employeeRepository = employeeRepository;
        }

        async Task<EmployeeData> IEmployeeService.AddEmployee(EmployeeData employee)
        {
            return await employeeRepository.AddEmployee(employee);
        }

        async Task<Employee> IEmployeeService.DeleteEmployee(int id)
        {
            return await employeeRepository.DeleteEmployee(id);
        }

        async Task<List<Employee>> IEmployeeService.GetAllEmployee()
        {
            return await employeeRepository.GetAllEmployee();
        }

        async Task<Employee> IEmployeeService.GetEmployeeByID(int id)
        {
            return await employeeRepository.GetEmployeeByID(id);
        }

        async Task<EmployeeData> IEmployeeService.UpdateEmployee(int id, EmployeeData employee)
        {
            return await employeeRepository.UpdateEmployee(id, employee);
        }
    }
}
