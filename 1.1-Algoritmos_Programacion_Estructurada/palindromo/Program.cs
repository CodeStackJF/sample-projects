namespace palindromo;

class Program
{
    static void Main(string[] args)
    {
        string palabra = Console.ReadLine();
        palabra = RemoveWhiteSpaces(palabra);
        string reversa = string.Empty;
        foreach(char letra in palabra)
        {
            reversa = letra.ToString() + reversa;
        }
        Console.WriteLine(reversa);

        if(palabra == reversa)
        {
            Console.WriteLine("Es un palíndromo.");
        }
        else
        {
            Console.WriteLine("No es un palíndromo.");
        }

    }

    public static string RemoveWhiteSpaces(string word)
    {
        string newWord = "";
        foreach(char letter in word)
        {
            if(letter.ToString() == " ")
             continue;
             newWord += letter.ToString();
        }
        return newWord;
    }
}
