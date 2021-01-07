﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using SsdWebApi.Models;
namespace SsdWebApi.Controllers {
    [ApiController]
    [Route ("api/Indici")]
    public class IndiciController : ControllerBase {
        private readonly FinIndiceContext _context;
        IndiciPersistence P;
        public IndiciController (FinIndiceContext context) {
            _context = context;
           P = new IndiciPersistence(context);
        }

        [HttpGet]
        //public ActionResult<List<Indici>> GetAll () =>_context.indici.ToList ();
         public ActionResult<List<Indici>> GetAll () => _context.indici.ToList ();
         
        // GET by ID action
        [HttpGet ("{attribute}", Name="GetSerie")]
           public string GetSerie(string attribute)
        {
            string res = "{";
            Forecast F = new Forecast();
            res += F.forecastSARIMAindex(attribute);
            res += "}";

            Console.WriteLine(res);

            //var index = P.readIndex(attribute);
            return res;
        }

       /*
        // POST action
        // POST: api/Stagione/PostStagioneItem
        [HttpPost]
        [Route ("[action]")]
        public string PostStagioneItem ([FromBody] Indice item) {
            string res = "Data " + item.Data;
            try {
                _context.indici.Add (item);
                _context.SaveChangesAsync ();
            } catch (Exception ex) {
                Console.WriteLine ("[ERROR] " + ex.Message);
                res = "Error";
            }
            Console.WriteLine (res);
            return res;
        }

        // PUT action
        // PUT: api/Stagione/10
        [HttpPut ("{id}")]
        public async Task<IActionResult> PutStagione (int id, [FromBody] Indice item) {
            if (id != item.id) return BadRequest ();
            _context.Entry (item).State = EntityState.Modified;
            try {
                await _context.SaveChangesAsync ();
            } catch (Exception ex) {
                if (!_context.indici.Any (s => s.id == id)) {
                    return NotFound ();
                } else {
                    Console.WriteLine ("[ERROR] " + ex.Message);;
                }
            }
            return Ok ();
        }
        // DELETE action
        // DELETE: api/Stagione/10
        [HttpDelete ("{id}")]
        public async Task<ActionResult<Indice>> DeleteTodoItem (int id) {
            var item = await _context.indici.FindAsync (id);
            if (item == null) {
                return NotFound ();
            }
            _context.indici.Remove (item);
            await _context.SaveChangesAsync ();
            return item;
        }*/
    }
}