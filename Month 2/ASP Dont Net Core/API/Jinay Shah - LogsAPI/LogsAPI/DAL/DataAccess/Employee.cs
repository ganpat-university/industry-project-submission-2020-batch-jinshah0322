using System;
using System.Collections.Generic;

namespace DAL.DataAccess;

public partial class Employee
{
    public int EmployeeId { get; set; }

    public string FirstName { get; set; } = null!;

    public string LastName { get; set; } = null!;

    public string Email { get; set; } = null!;

    public decimal Salary { get; set; }

    public DateOnly HireDate { get; set; }
}
