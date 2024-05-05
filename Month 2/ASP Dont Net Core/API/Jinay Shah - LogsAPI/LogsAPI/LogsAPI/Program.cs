using BAL;
using DAL.DataAccess;
using DAL.Interface;
using DAL.Repository;
using Microsoft.EntityFrameworkCore;
using NLog;
using NLog.Web;

var logger = NLog.LogManager.Setup().LoadConfigurationFromAppSettings().GetCurrentClassLogger();
try
{



    var builder = WebApplication.CreateBuilder(args);

    // Add services to the container.

    builder.Services.AddControllers();
    // Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
    builder.Services.AddEndpointsApiExplorer();
    builder.Services.AddSwaggerGen();

    builder.Logging.ClearProviders();
    builder.Host.UseNLog();

    var provider = builder.Services.BuildServiceProvider();
    var config = provider.GetRequiredService<IConfiguration>();
    builder.Services.AddDbContext<CoreMvcContext>(item => item.UseSqlServer(config.GetConnectionString("dbcs")));

    builder.Services.AddScoped<IEmployeeService, EmployeeRepositoryService>();
    builder.Services.AddScoped<IEmployee, EmployeeRepository>();

    var app = builder.Build();

    // Configure the HTTP request pipeline.
    if (app.Environment.IsDevelopment())
    {
        app.UseSwagger();
        app.UseSwaggerUI();
    }

    app.UseHttpsRedirection();

    app.UseAuthorization();

    app.MapControllers();

    app.Run();
}
catch (Exception ex)
{
    logger.Error(ex);
    throw (ex);
}
finally
{
    NLog.LogManager.Shutdown(); 
}