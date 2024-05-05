using System;
using System.Collections.Generic;

namespace CoreMVCAPICRUD.DataAccess;

public partial class Log
{
    public int LogId { get; set; }

    public string? MachineName { get; set; }

    public DateTime? Logged { get; set; }

    public string? Level { get; set; }

    public string? Message { get; set; }

    public string? Logger { get; set; }

    public string? Callsite { get; set; }

    public string? Exception { get; set; }
}
