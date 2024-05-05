using System;
using System.Collections.Generic;

namespace DAL.DataAccess;

public partial class Log
{
    public int LogId { get; set; }

    public DateTime? LogTimestamp { get; set; }

    public string? LogMessage { get; set; }
}
