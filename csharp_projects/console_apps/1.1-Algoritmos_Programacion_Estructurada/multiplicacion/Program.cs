namespace multiplicacion;

class Program
{
    static void Main(string[] args)
    {
        //multiplicacion por suma sucesiva
        int a = 43;
        int b = 101;
        int factor = 0;
        for(int i = 0; i <= a - 1; i++)
        {
            factor = factor + b;
        }
        Console.WriteLine(factor);

        //división por resta sucesiva
        int dividendo = 150;
        int divisor = 10;
        int cociente = 0;
        while(dividendo >= divisor)
        {
            cociente++;
            dividendo -= divisor;
        }
        Console.WriteLine($"El resultado es {cociente} y el residuo es {dividendo}");
    }
}