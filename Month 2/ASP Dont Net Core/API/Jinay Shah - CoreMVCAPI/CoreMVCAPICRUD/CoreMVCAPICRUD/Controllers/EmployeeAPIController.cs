using CoreMVCAPICRUD.DataAccess;
using CoreMVCAPICRUD.Models;
using CoreMVCAPICRUD.Interface;
using CoreMVCAPICRUD.Repository;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace CoreMVCAPICRUD.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EmployeeAPIController : ControllerBase
    {
        private readonly IEmployee employeeRepository;

        public EmployeeAPIController(IEmployee employeeRepository)
        {
            this.employeeRepository = employeeRepository;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllEmployees()
        {
            var employees = await employeeRepository.GetAllEmployee();
            return Ok(employees);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetEmployeeByID(int id)
        {
            var employee = await employeeRepository.GetEmployeeByID(id);
            if(employee == null)
            {
                return NotFound();
            }
            return Ok(employee);
        }

        [HttpPost]
        public async Task<IActionResult> AddEmployee(EmployeeModel employee)
        {
            var newEmployee = await employeeRepository.AddEmployee(employee);
            return Ok(newEmployee);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateEmployee(int id, EmployeeModel employee)
        {
            if (id != employee.EmployeeId)
            {
                return NotFound();
            }
            var e = await employeeRepository.UpdateEmployee(id, employee);
            return Ok(e);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteEmployee(int id)
        {
            var deletedEmployee = await employeeRepository.DeleteEmployee(id);
            if (deletedEmployee == null)
            {
                return NotFound();
            }
            return Ok(deletedEmployee);
        }
    }
}
