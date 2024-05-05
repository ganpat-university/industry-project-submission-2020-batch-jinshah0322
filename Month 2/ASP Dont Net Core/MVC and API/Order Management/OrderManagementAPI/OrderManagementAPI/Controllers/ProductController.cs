using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;
using OrderManagementAPI.Repository;

namespace OrderManagementAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductController : ControllerBase
    {
        private readonly IProduct productRepository;

        public ProductController(IProduct productRepository)
        {
            this.productRepository = productRepository;
        }

        [HttpGet]
        public async Task<IActionResult> GetAllProduct()
        {
            var products = await productRepository.GetAllProduct();
            return Ok(products);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetProductByID(int id)
        {
            var product = await productRepository.GetProductByID(id);
            if (product == null)
            {
                return NotFound();
            }
            return Ok(product);
        }

        [HttpPost]
        public async Task<IActionResult> AddProduct(ProductModel product)
        {
            var newProduct = await productRepository.AddProduct(product);
            return Ok(newProduct);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateProduct(int id, ProductModel product)
        {
            if (id != product.ProductId)
            {
                return NotFound();
            }
            var e = await productRepository.UpdateProduct(id, product);
            return Ok(e);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteProduct(int id)
        {
            var deletedProduct = await productRepository.DeleteProduct(id);
            if (deletedProduct == null)
            {
                return NotFound();
            }
            return Ok(deletedProduct);
        }
    }
}
