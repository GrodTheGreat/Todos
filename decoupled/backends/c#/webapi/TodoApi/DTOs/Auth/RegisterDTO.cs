namespace TodoApi.DTOs.Auth
{
    public class RegisterDTO
    {
        public required string Email { get; set; }
        public required string Password { get; set; }
    }
}
