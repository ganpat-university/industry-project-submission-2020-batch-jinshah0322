using System;
using System.Collections.Generic;

namespace OrderManagementAPI.DataAccess;

public partial class Customer
{
    public int CustomerId { get; set; }

    public string? Name { get; set; }

    public string? Email { get; set; }

    public string? Address { get; set; }

    public bool? IsDeleted { get; set; }

    public virtual ICollection<Order> Orders { get; set; } = new List<Order>();
}
