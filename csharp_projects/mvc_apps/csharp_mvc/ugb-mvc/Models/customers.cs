using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace ugb_mvc.Models
{
    public class customers
    {
        [Key]
        public int customerNumber { get; set; }
        public string customerName { get; set; }
    }
}