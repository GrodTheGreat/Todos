using Dotnet.Utils;
using Microsoft.AspNetCore.Mvc;
using TodoApi.Data;
using TodoApi.DTOs.Auth;
using TodoApi.Models;

namespace TodoApi.Controllers
{
    [ApiController]
    [Route("api/")]
    public class AuthController : ControllerBase
    {
        private readonly TodoContext _context;

        public AuthController(TodoContext context)
        {
            _context = context;
        }

        [HttpPost]
        [Route("login")]
        public IActionResult Login([FromBody] LoginDTO loginDTO)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest();
            }

            var user = _context.Users.FirstOrDefault(user => user.Email == loginDTO.Email);
            if (user == null || PasswordHasher.Verify(user.PasswordHash, loginDTO.Password))
            {
                return Unauthorized(new { message = "Invalid email and password combination" });
            }

            HttpContext.Session.SetInt32("UserId", user.Id);
            // HttpContext.Session.SetInt32("UserRole", user.Role);

            return Ok(new { message = "Login successful" });
        }

        [HttpPost]
        [Route("logout")]
        public IActionResult Logout()
        {
            HttpContext.Session.Clear();

            return Ok(new { message = "Logged out" });
        }

        [HttpPost]
        [Route("register")]
        public IActionResult Register([FromBody] RegisterDTO registerDTO)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest();
            }

            if (_context.Users.Any(user => user.Email == registerDTO.Email))
            {
                return BadRequest("User with this email already exists");
            }

            var user = new User
            {
                Email = registerDTO.Email,
                PasswordHash = PasswordHasher.Hash(registerDTO.Password),
            };

            _context.Users.Add(user);
            _context.SaveChanges();

            return Ok(new { message = "Registration successful" });
        }
    }
}
