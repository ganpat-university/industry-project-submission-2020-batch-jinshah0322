using CoreMVCCRUD.Models;

namespace CoreMVCCRUD.Interface
{
    public interface IDepartment
    {
        IEnumerable<Department> Index();
        Department GetDepartmentByID(int id);
        void Create(Department d);
        void Edit(Department d);
        void Delete(Department d);
    }
}