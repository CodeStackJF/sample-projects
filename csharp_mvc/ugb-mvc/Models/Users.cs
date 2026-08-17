using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ugb_mvc.Models
{
    public class Users
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public string address { get; set; } = string.Empty;
        public string phone_number { get; set; } = string.Empty;
    }
}