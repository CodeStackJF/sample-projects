namespace ejercicios_practicos;

class Program
{
    static void Main(string[] args)
    {
        Ejercicio4();
    }

    public static void Ejercicio1()
    {
        string nombre = string.Empty;
        while(nombre == string.Empty)
        {
            Console.WriteLine("Escriba su nombre:");
            nombre = Console.ReadLine()!;
        }

        decimal[] notas = new decimal[3];
        for(int i = 0; i <= 2; i++)
        {
            Console.WriteLine($"Ingrese la nota #{i+1}");
            string sNota = Console.ReadLine()!;
            decimal nota = 0;
            decimal.TryParse(sNota, out nota);
            notas[i] = nota;
        }

        decimal suma_nota = 0;
        foreach(decimal nota in notas)
        {
            suma_nota += nota;
        }
        decimal promedio = suma_nota / notas.Length;
        Console.WriteLine($"El estudiante ha {(promedio >= 6? "aprobado":"reprobado")} con una nota de {Math.Round(promedio, 2)}");
    }

    public static void Ejercicio2()
    {
        int numero = 0;
        
        bool isInteger = false;
        while(!isInteger)
        {
            Console.WriteLine("Ingrese un número entero:");
            string sNumero = Console.ReadLine()!;
            isInteger = int.TryParse(sNumero, out numero);
        }
        Console.WriteLine($"El numero {numero} es {(numero < 0 ? "negativo":"positivo")}");
    }

    public static void Ejercicio3()
    {
        int numero = 0;
        
        bool isInteger = false;
        while(!isInteger)
        {
            Console.WriteLine("Ingrese un número entero:");
            string sNumero = Console.ReadLine()!;
            isInteger = int.TryParse(sNumero, out numero);
        }
        for(int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{i} x {numero} = {i*numero}");
        }
    }

    public static void Ejercicio4()
    {
        int edad = 0;
        
        bool isInteger = false;
        while(!isInteger)
        {
            Console.WriteLine("Ingrese su edad:");
            string sNumero = Console.ReadLine()!;
            isInteger = int.TryParse(sNumero, out edad);
        }

        string opcion_licencia = string.Empty;
        string[] opciones = ["S", "N"];
        while(opcion_licencia == string.Empty)
        {
            Console.WriteLine("¿Posee licencia?:");
            Console.WriteLine("S = Si");
            Console.WriteLine("N = No");
            opcion_licencia = Console.ReadLine()!;
            if(!opciones.Contains(opcion_licencia))
            {
                opcion_licencia = string.Empty;
            }
        }

        if(edad >= 18)
        {
            if(opcion_licencia == "S")
                Console.WriteLine("Puede conducir con licencia para adultos.");
            else
                Console.WriteLine("Es un adulto pero no tiene licencia.");
        }
        else        
        if(edad >= 15 && edad < 18)
        {
            if(opcion_licencia == "S")
                Console.WriteLine("Puede conducir con licencia juvenil.");
            else
                Console.WriteLine("No posee licencia, pero puede aplicar a la licencia juvenil.");
        }
        else
        {
            Console.WriteLine("No cumple con el requisito minimo de edad para poder conducir.");
        }
    }

    public static void Ejercicio5()
    {
        string[] estudiantes = new string[]
        {
            "Juan",
            "María",
            "Roxana",
            "Carlos",
            "Felipe",
            "Karla",
            "Marta",
            "Pedro",
            "Sofía",
            "Roxana"
        };

        double[,] notas = new double[10, 3];
        Random rand = new Random();
        for(int i = 0; i <= notas.GetLength(0) - 1; i++)
        {
            notas[i, 0] = rand.NextDouble() * 10;
            notas[i, 0] = rand.NextDouble() * 10;
            notas[i, 0] = rand.NextDouble() * 10;
        }
    }
}
