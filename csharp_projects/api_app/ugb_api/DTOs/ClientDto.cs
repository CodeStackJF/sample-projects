namespace ugb_api.DTOs
{
    public class ClientDto
    {
        public int id { get; set; }
        public string first_name { get; set; } = string.Empty;
        public string last_name { get; set; } = string.Empty;
        public string email { get; set; } = string.Empty;
    }
}