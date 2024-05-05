using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace CoreMVCCRUD.Models;

public partial class Employee
{
    public int EmployeeId { get; set; }

    [Required]
    public string FirstName { get; set; } = null!;
    [Required]
    public string LastName { get; set; } = null!;
    [Required]
    [EmailAddress]
    public string Email { get; set; } = null!;
    [Required]
    public decimal Salary { get; set; }
    [Required]
    public DateOnly HireDate { get; set; }
}
