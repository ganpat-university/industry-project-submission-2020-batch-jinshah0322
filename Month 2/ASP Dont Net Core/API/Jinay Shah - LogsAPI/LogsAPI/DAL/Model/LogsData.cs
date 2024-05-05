using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DAL.Model
{
    public class LogsData
    {
        public int LogId { get; set; }

        public DateTime? LogTimestamp { get; set; } = DateTime.Now;
        [Required]
        public string? LogMessage { get; set; }
    }
}