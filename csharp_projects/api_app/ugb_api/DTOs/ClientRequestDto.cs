using System.ComponentModel.DataAnnotations;

namespace ugb_api.DTOs
{
    public class ClientRequestDto
    {
        [Required]
        public string first_name { get; set; } = string.Empty;

        [Required]
        public string last_name { get; set; } = string.Empty;

        [Required]
        [EmailAddress]
        public string email { get; set; } = string.Empty;
    }
}