using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ugb_mvc.Models;

namespace ugb_mvc.Controllers
{
    public class UsersController : Controller
    {
        public ActionResult Index()
        {
            IEnumerable<Users> users = new List<Users>()
            {
                new Users()
                {
                    id = 1,
                    name = "Jose",
                    address = "San Miguel",
                    phone_number = "787879"
                },
                new Users()
                {
                    id = 2,
                    name = "Juan",
                    address = "Santa Ana",
                    phone_number = "8989778"
                }
            };
            ViewBag.Users = users;
            return View();
        }

       /*  public FileResult File()
        {
            if(no existe)
            {
                return Json("archivo no existe");
            }
            return new System.IO.File.Open();
            el
        }

        public ContentResult Content()
        {
            return Content("Hola mundo");
        }

        public JsonResult Json()
        {
            return Json(new
            {
                id = 1,
                nombre = "jose"
            });
        } */
    }
}