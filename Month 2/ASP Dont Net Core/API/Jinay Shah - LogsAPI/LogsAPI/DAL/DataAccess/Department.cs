using System;
using System.Collections.Generic;

namespace DAL.DataAccess;

public partial class Department
{
    public int DepartmentId { get; set; }

    public string DepartmentName { get; set; } = null!;

    public string DepartmentHead { get; set; } = null!;

    public decimal Budget { get; set; }

    public DateOnly CreationDate { get; set; }

    public bool IsActive { get; set; }
}
