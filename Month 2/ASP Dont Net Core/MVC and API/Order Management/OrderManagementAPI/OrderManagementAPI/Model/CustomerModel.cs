using OrderManagementAPI.Model;
using System.ComponentModel.DataAnnotations;

namespace OrderManagementAPI.Model
{
    public class CustomerModel
    {
        [Required]  
        public int CustomerId { get; set; }

        [Required(ErrorMessage = "Name is required")]
        [StringLength(100, ErrorMessage = "Name cannot exceed 100 characters")]
        public string Name { get; set; }

        [Required(ErrorMessage = "Email is required")]
        [EmailAddress(ErrorMessage = "Invalid Email Address")]
        [StringLength(100, ErrorMessage = "Email cannot exceed 100 characters")]
        public string Email { get; set; }

        [Required(ErrorMessage = "Email is required")]
        [StringLength(255, ErrorMessage = "Address cannot exceed 255 characters")]
        public string Address { get; set; }

        public bool isDeleted { get; set; } = false;
    }
}
