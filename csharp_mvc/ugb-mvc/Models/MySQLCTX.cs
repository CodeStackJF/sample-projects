using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace ugb_mvc.Models
{
    public class MySQLCTX : DbContext
    {
        public MySQLCTX(DbContextOptions options) : base(options)
        {
  
        }

        public virtual DbSet<customers> customers {get; set;}
    }
}