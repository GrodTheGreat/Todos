namespace TodoApi.Models
{
    public class User
    {
        public int Id { get; set; }
        public required string Email { get; set; }
        public required string PasswordHash { get; set; }

        // public DateTime CreatedAt { get; set; }
        // public DateTime UpdatedAt { get; set; }
        // public DateTime DeletedAt { get; set; }
        public List<Todo> Todos { get; set; } = new List<Todo>();
    }
}
