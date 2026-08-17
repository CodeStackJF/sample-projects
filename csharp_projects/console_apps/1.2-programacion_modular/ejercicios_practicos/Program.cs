namespace ejercicios_practicos;

class Program
{
    static void Main(string[] args)
    {
       Ejercicio1 ejercicio1 = new Ejercicio1();
       ejercicio1.MostrarBienvenida("José");
       ejercicio1.CalcularAreaRectangulo(3, 4);

       Ejercicio2 ejercicio2 = new Ejercicio2();

       int a = 10;
       int b = 5;
       Console.WriteLine($"El valor de a es {a} y el valor de b es {b}");
       ejercicio2.Intercambiar(ref a, ref b);
       Console.WriteLine($"El valor de a es {a} y el valor de b es {b}");

       Ejercicio3_4 ejercicio3_4 = new Ejercicio3_4(1, "José");
       ejercicio3_4.DefinirSalario(-10);
       ejercicio3_4.DefinirSalario(100);
       ejercicio3_4.MostrarInformacion();
       
       Ejercicio5 ejercicio5 = new Ejercicio5();
       ejercicio5.Run();
    }
}
