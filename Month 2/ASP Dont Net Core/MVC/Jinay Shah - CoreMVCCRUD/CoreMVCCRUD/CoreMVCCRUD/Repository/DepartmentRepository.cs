using CoreMVCCRUD.Interface;
using CoreMVCCRUD.Models;
using Microsoft.EntityFrameworkCore;

namespace CoreMVCCRUD.Repository
{
    public class DepartmentRepository : IDepartment
    {
        private readonly CoreMvcContext context;
        public DepartmentRepository(CoreMvcContext context)
        {
            this.context = context;
        }

        public IEnumerable<Department> Index()
        {
            return context.Departments.ToList();
        }

        public Department GetDepartmentByID(int id)
        {
            return context.Departments.Where(model=>model.DepartmentId== id).FirstOrDefault();
        }

        public void Create(Department department)
        {
            context.Departments.Add(department);
            context.SaveChanges();
        }

        public void Edit(Department department)
        {
            context.Attach(department);
            context.Entry(department).State = EntityState.Modified;
            context.SaveChanges();
        }

        public void Delete(Department department)
        {
            context.Departments.Remove(department);
            context.SaveChanges();
        }
    }
}
