using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ugb_mvc.Models;

namespace ugb_mvc.Controllers
{
    public class CustomersController : Controller
    {
        private readonly MySQLCTX _ctx;

        public CustomersController(MySQLCTX ctx)
        {
            _ctx = ctx;
        }

        public ActionResult Index()
        {
            List<customers> customers = _ctx.customers.ToList();
            customers.ForEach(x=>x.customerName = "jose");
            _ctx.SaveChangesAsync();

            customers customer = _ctx.customers.Where(x=>x.customerNumber == 124).FirstOrDefault();

            _ctx.Database.SqlQueryRaw<int>("select 1 from clientes where id = {0}", 2);

            ViewBag.Customers = customers;
            ViewBag.Customer = customer;
            return View();
        }
    }
}