using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using ugb_mvc.Models;

namespace ugb_mvc.Controllers;

public class HomeController : Controller
{
    private readonly IConfiguration _config;

    public HomeController(IConfiguration config)
    {
        _config = config;   
    }
    public IActionResult Index()
    {
        ViewBag.Nombre = "Jose";
        ViewData["Nombre"] = "Jose";
        return View();
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
