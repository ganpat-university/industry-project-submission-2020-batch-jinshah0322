using System;
using System.ComponentModel.DataAnnotations;

namespace OrderManagementAPI.Model
{
    public class OrderItemModel
    {
        public int OrderItemId { get; set; }

        public int? OrderId { get; set; }

        public int? ProductId { get; set; }

        [Required(ErrorMessage = "Quantity is required")]
        [Range(1, int.MaxValue, ErrorMessage = "Quantity must be greater than 0")]
        public int? Quantity { get; set; }

        [Required(ErrorMessage = "Unit price is required")]
        [Range(0, double.MaxValue, ErrorMessage = "Unit price must be greater than or equal to 0")]
        public decimal? UnitPrice { get; set; }

        public bool? IsDeleted { get; set; } = false;
    }
}