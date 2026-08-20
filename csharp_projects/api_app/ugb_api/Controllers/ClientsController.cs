using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ugb_api.Data;
using ugb_api.DTOs;
using ugb_api.Entities;

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

        [HttpGet]
        public async Task<IActionResult> GetClients()
        {
            var clients = await _ctx.Clients
                .Select(client => new ClientDto
                {
                    id = client.id,
                    first_name = client.first_name,
                    last_name = client.last_name,
                    email = client.email
                })
                .ToListAsync();

            return Ok(clients);
        }

        [HttpGet("{id:int}")]
        public async Task<IActionResult> GetClient(int id)
        {
            var client = await _ctx.Clients.FindAsync(id);

            if (client is null)
            {
                return NotFound();
            }

            return Ok(ToDto(client));
        }

        [HttpPost]
        public async Task<IActionResult> CreateClient(ClientRequestDto request)
        {
            if (await _ctx.Clients.AnyAsync(client => client.email == request.email))
            {
                return Conflict(new { message = "The email is already registered." });
            }

            var client = new Client
            {
                first_name = request.first_name,
                last_name = request.last_name,
                email = request.email
            };

            _ctx.Clients.Add(client);
            await _ctx.SaveChangesAsync();

            return CreatedAtAction(nameof(GetClient), new { id = client.id }, ToDto(client));
        }

        [HttpPut("{id:int}")]
        public async Task<IActionResult> UpdateClient(int id, ClientRequestDto request)
        {
            var client = await _ctx.Clients.FindAsync(id);

            if (client is null)
            {
                return NotFound();
            }

            if (await _ctx.Clients.AnyAsync(existing =>
                existing.id != id && existing.email == request.email))
            {
                return Conflict(new { message = "The email is already registered." });
            }

            client.first_name = request.first_name;
            client.last_name = request.last_name;
            client.email = request.email;

            await _ctx.SaveChangesAsync();

            return Ok(ToDto(client));
        }

        [HttpDelete("{id:int}")]
        public async Task<IActionResult> DeleteClient(int id)
        {
            var client = await _ctx.Clients.FindAsync(id);

            if (client is null)
            {
                return NotFound();
            }

            _ctx.Clients.Remove(client);
            await _ctx.SaveChangesAsync();

            return NoContent();
        }

        private static ClientDto ToDto(Client client)
        {
            return new ClientDto
            {
                id = client.id,
                first_name = client.first_name,
                last_name = client.last_name,
                email = client.email
            };
        }
    }
}