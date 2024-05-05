using CoreMVCCRUD.Interface;
using CoreMVCCRUD.Models;
using CoreMVCCRUD.Repository;
using Microsoft.AspNetCore.Mvc;

namespace CoreMVCCRUD.Controllers
{
    public class DepartmentController : Controller
    {
        private readonly IDepartment departmentRepository;
        public DepartmentController(IDepartment departmentRepository)
        {
            this.departmentRepository = departmentRepository;
        }

        public IActionResult Index()
        {
            var employees = departmentRepository.Index();
            return View(employees);
        }

        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Create(Department department)
        {
            if(ModelState.IsValid)
            {
                departmentRepository.Create(department);
                return RedirectToAction("Index");
            }
            return View(department);
        }

        public IActionResult Edit(int id)
        {
            var department = departmentRepository.GetDepartmentByID(id);
            return View(department);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Edit(Department department)
        {
            if (ModelState.IsValid)
            {
                departmentRepository.Edit(department);
                return RedirectToAction("Index");
            }
            return View(department);
        }

        public IActionResult Details(int id)
        {
            var department = departmentRepository.GetDepartmentByID(id);
            return View(department);
        }

        public IActionResult Delete(int id)
        {
            var department = departmentRepository.GetDepartmentByID(id);
            return View(department);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public IActionResult Delete(Department department)
        {
            departmentRepository.Delete(department);
            return RedirectToAction("Index");
        }
    }
}
