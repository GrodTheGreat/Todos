using TodoApi.DTOs.Todo;
using TodoApi.Models;

namespace TodoApi.Mappers
{
    public static class TodoMappers
    {
        public static TodoDTO ToTodoDTO(this Todo todo)
        {
            return new TodoDTO()
            {
                Id = todo.Id,
                Title = todo.Title,
                Description = todo.Description,
                IsCompleted = todo.IsCompleted,
                CreatedAt = todo.CreatedAt,
            };
        }

        public static Todo ToTodoFromCreateDTO(this CreateTodoDTO todoDTO)
        {
            return new Todo()
            {
                Title = todoDTO.Title,
                Description = todoDTO.Description,
                IsCompleted = todoDTO.IsCompleted,
            };
        }
    }
}
