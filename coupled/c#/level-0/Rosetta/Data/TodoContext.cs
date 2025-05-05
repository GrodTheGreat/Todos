using Microsoft.EntityFrameworkCore;
using Rosetta.Models;

namespace Rosetta.Data;

public class TodoContext : DbContext
{
    public DbSet<Todo> Todos { get; set; }

    public TodoContext(DbContextOptions<TodoContext> options)
        : base(options) { }
}
