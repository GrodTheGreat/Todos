using System.ComponentModel.DataAnnotations;

namespace Rosetta.Models;

public class Todo
{
    public int Id { get; set; }

    [Required]
    public string Title { get; set; } = null!;
    public string? Description { get; set; }

    [Display(Name = "Completed")]
    public bool IsComplete { get; set; }
}
