using System.ComponentModel.DataAnnotations;

namespace OrderManagementAPI.Model
{
    public class OrderModel
    {
        public int OrderId { get; set; }

        public int? CustomerId { get; set; }

        [Required(ErrorMessage = "Order date is required")]
        public DateTime? OrderDate { get; set; }

        [Required(ErrorMessage = "Total amount is required")]
        [Range(0, double.MaxValue, ErrorMessage = "Total amount must be greater than or equal to 0")]
        public decimal? TotalAmount { get; set; }

        public string? Status { get; set; } = "Pending";

        public bool? IsDeleted { get; set; } = false;
    }
}
