namespace TodoApi.DTOs.Todo
{
    public class UpdateTodoDTO
    {
        public required string Title { get; set; }
        public string? Description { get; set; } = string.Empty;
        public bool IsCompleted { get; set; } = false;
    }
}
