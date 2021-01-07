using Microsoft.EntityFrameworkCore;
namespace SsdWebApi.Models
{
    public class FinIndiceContext : DbContext
    {
        public FinIndiceContext(DbContextOptions<FinIndiceContext> options)
        : base(options)
        {
        }
        public DbSet<Indici> indici { get; set; }
    }
}
