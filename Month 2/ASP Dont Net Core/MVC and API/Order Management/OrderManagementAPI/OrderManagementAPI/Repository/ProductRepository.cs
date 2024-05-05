using Microsoft.EntityFrameworkCore;
using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Interface;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Repository
{
    public class ProductRepository : IProduct
    {
        private readonly OrderManagementContext context;

        public ProductRepository(OrderManagementContext context)
        {
            this.context = context;
        }

        public async Task<ProductModel> AddProduct(ProductModel product)
        {
            Product product1 = new Product();
            product1.Name = product.Name;
            product1.Description = product.Description;
            product1.Price = product.Price;
            product1.StockQuantity = product.StockQuantity;
            await context.Products.AddAsync(product1);
            await context.SaveChangesAsync();
            return product;
        }

        public async Task<Product> DeleteProduct(int id)
        {
            var product = await context.Products.FindAsync(id);
            if (product == null)
            {
                return null;
            }
            product.IsDeleted = true;
            await context.SaveChangesAsync();
            return product;
        }

        public async Task<List<Product>> GetAllProduct()
        {
            return await context.Products.Where(p => p.IsDeleted == false).ToListAsync();
        }

        public async Task<Product> GetProductByID(int id)
        {
            return await context.Products.FirstOrDefaultAsync(p => p.ProductId == id && p.IsDeleted == false);
        }

        public async Task<ProductModel> UpdateProduct(int id, ProductModel product)
        {
            var existingProduct = await context.Products.FindAsync(id);

            if (existingProduct == null)
            {
                return null;
            }

            existingProduct.Name = product.Name;
            existingProduct.Description = product.Description;
            existingProduct.Price = product.Price;
            existingProduct.StockQuantity = product.StockQuantity;

            await context.SaveChangesAsync();

            return product;
        }
    }
}
