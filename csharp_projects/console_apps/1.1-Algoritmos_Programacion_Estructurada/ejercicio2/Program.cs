namespace ejercicio2;
//Escribe un programa que reciba un numero entero y calcule la suma de sus dígitos:
//65487 = 6+5+4+8+7 = 30
class Program
{
    static void Main(string[] args)
    {
        int numero = 0;
        Console.WriteLine("Ingrese un número:");
        numero = Convert.ToInt32(Console.ReadLine());
        int total = 0;
        foreach(char n in numero.ToString())
        {
            total = total + Convert.ToInt32(n.ToString());
        }

        Console.WriteLine($"El total es {total}");


        total = 0;
        string numeroString = numero.ToString();
        for(int i = 0; i <= numeroString.Length - 1; i++)
        {
            total = total + Convert.ToInt32(numeroString[i].ToString());
        }

        Console.WriteLine($"El total es {total}");

        total = 0;
        while(numero > 0)
        {
            int digito = numero % 10;
            numero = numero / 10;
            total += digito;
        }
        Console.WriteLine($"El total es {total}");
    }
}
