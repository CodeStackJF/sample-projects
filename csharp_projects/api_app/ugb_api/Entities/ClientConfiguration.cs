using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace ugb_api.Entities
{
    public class ClientConfiguration : IEntityTypeConfiguration<Client>
    {
        public void Configure(EntityTypeBuilder<Client> builder)
        {
            builder.ToTable("Clients");

            builder.HasKey(client => client.id);

            builder.HasIndex(client => client.email)
                .IsUnique();

            builder.Property(client => client.id)
                .HasColumnName("id")
                .ValueGeneratedOnAdd();

            builder.Property(client => client.first_name)
                .HasColumnName("first_name")
                .IsRequired();

            builder.Property(client => client.last_name)
                .HasColumnName("last_name")
                .IsRequired();

            builder.Property(client => client.email)
                .HasColumnName("email")
                .IsRequired();
        }
    }
}