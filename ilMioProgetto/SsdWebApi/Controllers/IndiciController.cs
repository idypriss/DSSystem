using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc; 
using Microsoft.EntityFrameworkCore; 
using SsdWebApi.Models;

namespace SsdWebApi.Controllers 
{
    [ApiController] 
    [Route("api/Indici")]
     public class IndiciController : ControllerBase 
     {
        private readonly FinIndiciContext _context;
        IndiciPersistence p;
        public IndiciController(FinIndiciContext context) 
        {  
            _context = context;
             p = new IndiciPersistence(context);
         }
        
         [HttpGet]
        public ActionResult<List<Indici>> GetAll () => _context.indici.ToList ();

         // GET by serie
        [HttpGet ("{id}", Name="GetSerie")]
        
           public  String GetSerie (int id) {
            String res = "{";
            
            if (id>0) id=8;
            
                string[] indices = new string []{"id","Data","SP_500","FTSE_MIB","GOLD_SPOT","MSCI_EM","MSCI_EURO","All_Bonds","US_Treasury"};
                string myid= id.ToString();
                string attribute =indices[id];
                Forecast fore = new Forecast();
                res = fore.forecastSARIMAindex(attribute);
                res ="}";

                var index = p.readIndex(attribute);

            return res;
        }
     }

}
       
     