using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ugb_api.Data;

namespace ugb_api.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ClientsController : ControllerBase
    {
        private readonly ClientsContext _ctx;

        public ClientsController(ClientsContext ctx)
        {
            _ctx = ctx;
        }

        public async Task<IActionResult> GetClients()
        {
            return Ok(await _ctx.Clients.ToListAsync());
        }
    }
}