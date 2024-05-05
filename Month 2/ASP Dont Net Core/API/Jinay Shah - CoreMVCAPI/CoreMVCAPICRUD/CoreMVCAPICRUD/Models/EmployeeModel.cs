using System.ComponentModel.DataAnnotations;

namespace CoreMVCAPICRUD.Models
{
    public class EmployeeModel
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
}
