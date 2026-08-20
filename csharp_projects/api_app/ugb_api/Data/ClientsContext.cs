using Microsoft.EntityFrameworkCore;
using ugb_api.Entities;

namespace ugb_api.Data
{
    public class ClientsContext : DbContext
    {
        public ClientsContext(DbContextOptions<ClientsContext> options)
            : base(options)
        {
        }

        public DbSet<Client> Clients => Set<Client>();

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfigurationsFromAssembly(typeof(ClientsContext).Assembly);
            base.OnModelCreating(modelBuilder);
        }
    }
}