using Microsoft.AspNetCore.Identity;

namespace TodoApi.Models
{
    public class User : IdentityUser
    {
        // public int Id { get; set; }
        // public DateTime CreatedAt { get; set; }
        // public DateTime UpdatedAt { get; set; }
        // public DateTime DeletedAt { get; set; }
        public List<Todo> Todos { get; set; } = new List<Todo>();
    }
}
