using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace DAL.DataAccess;

public partial class CoreMvcContext : DbContext
{
    public CoreMvcContext()
    {
    }

    public CoreMvcContext(DbContextOptions<CoreMvcContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Department> Departments { get; set; }

    public virtual DbSet<Employee> Employees { get; set; }

    public virtual DbSet<Log> Logs { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    { }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Department>(entity =>
        {
            entity.HasKey(e => e.DepartmentId).HasName("PK__Departme__B2079BCD24FF41B7");

            entity.ToTable("Department");

            entity.Property(e => e.DepartmentId).HasColumnName("DepartmentID");
            entity.Property(e => e.Budget).HasColumnType("decimal(18, 2)");
            entity.Property(e => e.DepartmentHead)
                .HasMaxLength(100)
                .IsUnicode(false);
            entity.Property(e => e.DepartmentName)
                .HasMaxLength(100)
                .IsUnicode(false);
        });

        modelBuilder.Entity<Employee>(entity =>
        {
            entity.HasKey(e => e.EmployeeId).HasName("PK__Employee__7AD04FF19B305084");

            entity.ToTable("Employee");

            entity.Property(e => e.EmployeeId).HasColumnName("EmployeeID");
            entity.Property(e => e.Email)
                .HasMaxLength(100)
                .IsUnicode(false);
            entity.Property(e => e.FirstName)
                .HasMaxLength(50)
                .IsUnicode(false);
            entity.Property(e => e.LastName)
                .HasMaxLength(50)
                .IsUnicode(false);
            entity.Property(e => e.Salary).HasColumnType("decimal(10, 2)");
        });

        modelBuilder.Entity<Log>(entity =>
        {
            entity.HasKey(e => e.LogId).HasName("PK__logs__7839F64D13A42923");

            entity.ToTable("logs");

            entity.Property(e => e.LogId).HasColumnName("logId");
            entity.Property(e => e.LogMessage).HasColumnName("logMessage");
            entity.Property(e => e.LogTimestamp)
                .HasDefaultValueSql("(getdate())")
                .HasColumnType("datetime")
                .HasColumnName("logTimestamp");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
