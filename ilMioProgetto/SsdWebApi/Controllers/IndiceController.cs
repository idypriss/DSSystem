using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SsdWebApi.Models;
using System.IO;

namespace SsdWebApi.Controllers {
    [ApiController]
    [Route ("api/Indici")]
    public class IndiceController : ControllerBase {
        private readonly FinIndiceContext _context;
           IndicePersistence P;
        public IndiceController (FinIndiceContext context) {
            _context = context;
           P = new IndicePersistence(context);
        }
         
        // GET by ID action
        [HttpGet ("{attribute}", Name="GetSerie")]
           public string GetSerie(string attribute)
        {
            string res = "{";
            Forecast F = new Forecast();
            res += F.forecastSARIMAindex(attribute);
            res += "}";

            Console.WriteLine(res);
            
            return res;
        }  
    }
}