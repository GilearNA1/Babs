namespace BabylonGameEngine.Models
{
    public class User
    {
        public int Id { get; set; }
        public string Name { get; set; } = string.Empty; // Non-nullable
        public string Email { get; set; } = string.Empty; // Non-nullable
    }
}
