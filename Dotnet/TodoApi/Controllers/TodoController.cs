using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using TodoApi.Data;
using TodoApi.DTOs.Todo;
using TodoApi.Mappers;
using TodoApi.Models;

namespace TodoApi.Controllers
{
    [ApiController]
    [Route("api/todos")]
    public class TodoController : ControllerBase
    {
        private UserManager<User> _userManager { get; set; }
        private TodoContext _context { get; set; }

        public TodoController(UserManager<User> userManager, TodoContext context)
        {
            _userManager = userManager;
            _context = context;

            if (_context.Todos.Count() == 0)
            {
                _context.Todos.Add(
                    new Todo
                    {
                        Title = "Todo 1",
                        Description = "Description 1",
                        IsCompleted = false,
                    }
                );
                _context.Todos.Add(
                    new Todo
                    {
                        Title = "Todo 2",
                        Description = "Description 2",
                        IsCompleted = false,
                    }
                );
                _context.Todos.Add(
                    new Todo
                    {
                        Title = "Todo 3",
                        Description = "Description 3",
                        IsCompleted = false,
                    }
                );
                _context.SaveChanges();
            }
        }

        [HttpPost]
        public IActionResult Create([FromBody] CreateTodoDTO todoDTO)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest();
            }

            var todo = todoDTO.ToTodoFromCreateDTO();

            _context.Todos.Add(todo);
            _context.SaveChanges();

            return CreatedAtAction(nameof(GetById), new { id = todo.Id }, todo.ToTodoDTO());
        }

        [HttpDelete]
        [Route("{id:int}")]
        public IActionResult Delete([FromRoute] int id)
        {
            var todo = _context
                .Todos.Where(todo => todo.Id == id && todo.DeletedAt == null)
                .FirstOrDefault();

            if (todo == null)
            {
                return NotFound();
            }

            todo.DeletedAt = DateTime.UtcNow;
            // _context.Remove(todo); //Only for hard deletes
            _context.SaveChanges();

            return NoContent();
        }

        [HttpGet]
        public IActionResult Get()
        {
            var todos = _context.Todos.Where(todo => todo.DeletedAt == null).ToList();

            return Ok(todos.Select(todo => todo.ToTodoDTO()));
        }

        [HttpGet]
        [Route("{id:int}")]
        public IActionResult GetById([FromRoute] int id)
        {
            var todo = _context
                .Todos.Where(todo => todo.Id == id && todo.DeletedAt == null)
                .SingleOrDefault();

            if (todo == null)
            {
                return NotFound();
            }

            return Ok(todo.ToTodoDTO());
        }

        [HttpPut]
        [Route("{id:int}")]
        public IActionResult Update([FromRoute] int id, UpdateTodoDTO todoDTO)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest();
            }

            var todo = _context
                .Todos.Where(todo => todo.Id == id && todo.DeletedAt == null)
                .SingleOrDefault();

            if (todo == null)
            {
                return NotFound();
            }

            todo.Title = todoDTO.Title;
            todo.Description = todoDTO.Description;
            todo.IsCompleted = todoDTO.IsCompleted;
            todo.UpdatedAt = DateTime.UtcNow;

            _context.SaveChanges();

            Console.WriteLine(todo.UpdatedAt);

            return Ok(todo.ToTodoDTO());
        }
    }
}
