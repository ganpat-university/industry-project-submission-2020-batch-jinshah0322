using OrderManagementAPI.DataAccess;
using OrderManagementAPI.Model;

namespace OrderManagementAPI.Interface
{
    public interface IProduct
    {
        Task<List<Product>> GetAllProduct();
        Task<Product> GetProductByID(int id);
        Task<ProductModel> AddProduct(ProductModel product);
        Task<ProductModel> UpdateProduct(int id, ProductModel product);
        Task<Product> DeleteProduct(int id);
    }
}