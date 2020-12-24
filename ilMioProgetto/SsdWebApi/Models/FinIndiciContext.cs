using Microsoft.EntityFrameworkCore;


namespace SsdWebApi.Models 

{ public class FinIndiciContext : DbContext 
    { 
         public FinIndiciContext(DbContextOptions <FinIndiciContext> options) : base(options) 
         {

         }
        public DbSet<Indici> indici { get; set; }
    }       
}