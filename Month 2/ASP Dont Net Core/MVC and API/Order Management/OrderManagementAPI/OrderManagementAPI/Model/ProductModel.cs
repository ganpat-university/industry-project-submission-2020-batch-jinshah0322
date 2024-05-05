using System.ComponentModel.DataAnnotations;

namespace OrderManagementAPI.Model
{
    public class ProductModel
    {
        public int ProductId { get; set; }

        [Required(ErrorMessage = "Name is required")]
        [StringLength(100, ErrorMessage = "Name cannot exceed 100 characters")]
        public string? Name { get; set; }

        [Required(ErrorMessage = "Description is required")]
        [StringLength(250, ErrorMessage = "Description cannot exceed 100 characters")]
        public string? Description { get; set; }

        [Required(ErrorMessage = "Price is required")]
        public decimal? Price { get; set; }

        [Required(ErrorMessage = "Quantity is required")]
        public int? StockQuantity { get; set; }

        public bool? IsDeleted { get; set; } = false;
    }
}
