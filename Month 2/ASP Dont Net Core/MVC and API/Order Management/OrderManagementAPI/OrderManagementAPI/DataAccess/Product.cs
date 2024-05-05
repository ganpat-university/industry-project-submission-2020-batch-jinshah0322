using System;
using System.Collections.Generic;

namespace OrderManagementAPI.DataAccess;

public partial class Product
{
    public int ProductId { get; set; }

    public string? Name { get; set; }

    public string? Description { get; set; }

    public decimal? Price { get; set; }

    public int? StockQuantity { get; set; }

    public bool? IsDeleted { get; set; }

    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
}
