namespace TodoApi.DTOs.Todo
{
    public class TodoDTO
    {
        public int Id { get; set; }
        public required string Title { get; set; }
        public string? Description { get; set; } = string.Empty;
        public bool IsCompleted { get; set; } = false;
        public DateTime CreatedAt { get; set; }
    }
}
