using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace CoreMVCCRUD.Models;

public partial class Department
{
    public int DepartmentId { get; set; }
    [Required]
    public string DepartmentName { get; set; } = null!;
    [Required]
    public string DepartmentHead { get; set; } = null!;
    [Required]
    public decimal Budget { get; set; }
    [Required]
    public DateOnly CreationDate { get; set; }
    [Required]
    public bool IsActive { get; set; }
}
