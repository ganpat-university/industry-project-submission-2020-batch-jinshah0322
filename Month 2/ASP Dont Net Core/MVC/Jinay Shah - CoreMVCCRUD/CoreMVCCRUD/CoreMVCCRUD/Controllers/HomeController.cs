using CoreMVCCRUD.Interface;
using CoreMVCCRUD.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace CoreMVCCRUD.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IEmployee employeeRepository;

        public HomeController(ILogger<HomeController> logger, IEmployee employeeRepository)
        {
            _logger = logger;
            this.employeeRepository = employeeRepository;
        }

        public IActionResult GetAllEmployees()
        {
            var employees = employeeRepository.GetAllEmployees();
            return View(employees);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(Employee employee)
        {
            if (ModelState.IsValid)
            {
                employeeRepository.Create(employee);
                return RedirectToAction("GetAllEmployees");
            }
            return View(employee);
        }

        public IActionResult Edit(int id)
        {
            var row = employeeRepository.GetEmployeeById(id);
            return View(row);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(Employee employee)
        {
            if (ModelState.IsValid)
            {
                employeeRepository.Edit(employee);
                return RedirectToAction("GetAllEmployees");
            }
            return View(employee);
        }

        public IActionResult Details(int id)
        {
            var row = employeeRepository.GetEmployeeById(id);
            return View(row);
        }

        public IActionResult Delete(int id)
        {
            var row = employeeRepository.GetEmployeeById(id);
            return View(row);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Delete(Employee employee)
        {
            employeeRepository.Delete(employee);
            return RedirectToAction("GetAllEmployees");
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
