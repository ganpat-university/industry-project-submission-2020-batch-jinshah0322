using System;
using System.Collections.Generic;

namespace OrderManagementAPI.DataAccess;

public partial class Order
{
    public int OrderId { get; set; }

    public int? CustomerId { get; set; }

    public DateTime? OrderDate { get; set; }

    public decimal? TotalAmount { get; set; }

    public string? Status { get; set; }

    public bool? IsDeleted { get; set; }

    public virtual Customer? Customer { get; set; }

    public virtual ICollection<OrderItem> OrderItems { get; set; } = new List<OrderItem>();
}
