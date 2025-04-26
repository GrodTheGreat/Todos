using System.Security.Cryptography;
using System.Text;

namespace Dotnet.Utils
{
    public static class PasswordHasher
    {
        public static string Hash(string password) =>
            Convert.ToBase64String(SHA256.Create().ComputeHash(Encoding.UTF8.GetBytes(password)));

        public static bool Verify(string hash, string password) => hash == Hash(password);
    }
}
