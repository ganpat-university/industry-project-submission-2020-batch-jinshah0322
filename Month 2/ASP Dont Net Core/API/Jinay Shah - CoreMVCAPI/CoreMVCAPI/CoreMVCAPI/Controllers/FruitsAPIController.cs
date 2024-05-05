using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace CoreMVCAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FruitsAPIController : ControllerBase
    {
        public List<string> fruits = new List<string>()
        {
            "Apple",
            "Grapes",
            "Banana",
            "Mango"
        };

        [HttpGet]
        public List<string> GetAllFruits()
        {
            return fruits;
        }

        [HttpGet("{id}")]
        public string GetFruitByID(int id)
        {
            return fruits[id];
        }
    }
}
