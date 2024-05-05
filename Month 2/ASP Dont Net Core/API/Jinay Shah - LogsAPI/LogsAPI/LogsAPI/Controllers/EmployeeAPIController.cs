using BAL;
using DAL.Model;
using DAL.Repository;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using System.Runtime.CompilerServices;

namespace LogsAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EmployeeAPIController : ControllerBase
    {
        private readonly ILogger<EmployeeAPIController> _logger;
        private readonly IEmployeeService employeeRepositoryService;

        public EmployeeAPIController(ILogger<EmployeeAPIController> logger,IEmployeeService employeeRepositoryService)
        {
            _logger = logger;
            this.employeeRepositoryService = employeeRepositoryService;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllEmployees()
        {
            _logger.LogInformation("All employee are logged.");
            var employees = await employeeRepositoryService.GetAllEmployee();
            return Ok(employees);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetEmployeeByID(int id)
        {
            var employee = await employeeRepositoryService.GetEmployeeByID(id);
            if (employee == null)
            {
                return NotFound();
            }
            return Ok(employee);
        }

        [HttpPost]
        public async Task<IActionResult> AddEmployee(EmployeeData employee)
        {
            var newEmployee = await employeeRepositoryService.AddEmployee(employee);
            return Ok(newEmployee);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateEmployee(int id, EmployeeData employee)
        {
            if (id != employee.EmployeeId)
            {
                return NotFound();
            }
            var e = await employeeRepositoryService.UpdateEmployee(id, employee);
            return Ok(e);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteEmployee(int id)
        {
            var deletedEmployee = await employeeRepositoryService.DeleteEmployee(id);
            if (deletedEmployee == null)
            {
                return NotFound();
            }
            return Ok(deletedEmployee);
        }
    }
}
