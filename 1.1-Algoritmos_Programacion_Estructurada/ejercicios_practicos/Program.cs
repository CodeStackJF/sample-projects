namespace ejercicios_practicos;

class Program
{
    static void Main(string[] args)
    {
        Ejercicio5();
    }

    public static void Ejercicio1()
    {
        string nombre = string.Empty;
        //Ejecutamos un ciclo infinito hasta que el usuario ingrese un nombre
        while(nombre == string.Empty)
        {
            Console.WriteLine("Escriba su nombre:");
            nombre = Console.ReadLine()!;
        }

        //Declaramos la variable para almacenar las 3 notas
        decimal[] notas = new decimal[3];
        for(int i = 0; i <= 2; i++)
        {
            Console.WriteLine($"Ingrese la nota #{i+1}");
            string sNota = Console.ReadLine()!;
            //esta variable almacenará el valor ingresado por el usuario solamente si es un numero, caso contrario se quedará como seri
            decimal nota = 0;
            //el TryParse permite realizar un intento de conversión, si la cadena no es un decimal entonces devuelve false y no almacena ningun valor en nota
            decimal.TryParse(sNota, out nota);
            //guardamos la nota en la primera posición del arreglo
            notas[i] = nota;
        }

        decimal suma_nota = 0;
        //sumamos las notas
        foreach(decimal nota in notas)
        {
            suma_nota += nota;
        }
        //obtenemos la cantidad de notas
        decimal promedio = suma_nota / notas.Length;
        //mostramos el resultado
        Console.WriteLine($"El estudiante ha {(promedio >= 6? "aprobado":"reprobado")} con una nota de {Math.Round(promedio, 2)}");
    }

    public static void Ejercicio2()
    {
        int numero = 0;
        //ejecutamos mientras el valor ingresado no sea un numero entero
        bool isInteger = false;
        while(!isInteger)
        {
            Console.WriteLine("Ingrese un número entero:");
            string sNumero = Console.ReadLine()!;
            //TryParse intenta convertir la cadena en un numero, si no es compatible devuelve false
            isInteger = int.TryParse(sNumero, out numero);
        }
        Console.WriteLine($"El numero {numero} es {(numero < 0 ? "negativo":"positivo")}");
    }

    public static void Ejercicio3()
    {
        int numero = 0;
        

        bool isInteger = false;
        //ejecutamos mientras el valor ingresado no sea un numero entero
        while(!isInteger)
        {
            Console.WriteLine("Ingrese un número entero:");
            string sNumero = Console.ReadLine()!;
            isInteger = int.TryParse(sNumero, out numero);
        }

        //mostramos la tabla de multiplicar
        for(int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{i} x {numero} = {i*numero}");
        }
    }

    public static void Ejercicio4()
    {
        int edad = 0;
        
        bool isInteger = false;
        //ejecutamos mientras el valor ingresado no sea un numero entero
        while(!isInteger)
        {
            Console.WriteLine("Ingrese su edad:");
            string sNumero = Console.ReadLine()!;
            isInteger = int.TryParse(sNumero, out edad);
        }

        //Determinamos si posee licencia o no por medio de una lista de opciones
        string opcion_licencia = string.Empty;
        //definimos las opciones validas
        string[] opciones = ["S", "N"];
        //ejecutamos mientras sea un valor vacio o un opción no válida
        while(opcion_licencia == string.Empty)
        {
            Console.WriteLine("¿Posee licencia?:");
            Console.WriteLine("S = Si");
            Console.WriteLine("N = No");
            opcion_licencia = Console.ReadLine()!;
            //Si el valor ingresado no corresponde a los de la lista de opciones vaciamos la variable para que siga ejecutandose el while
            if(!opciones.Contains(opcion_licencia))
            {
                opcion_licencia = string.Empty;
            }
        }

        //ejecutamos las condiciones
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
        //almacenamos los estudiantes, los indice servirán como llaves para identificarlos
        string[] estudiantes =
        [
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
        ];

        //declaramos una variable bidimensional para guardar las 3 notas de cada estudiante
        double[,] notas = new double[10, 3];
        Random rand = new Random();
        //generamos valores aleatorios para las notas entre 0 a 10
        for(int i = 0; i <= notas.GetLength(0) - 1; i++)
        {
            notas[i, 0] = rand.NextDouble() * 10;
            notas[i, 1] = rand.NextDouble() * 10;
            notas[i, 2] = rand.NextDouble() * 10;
        }

        //obtenemos el promedio de cada estudiante
        for(int i = 0; i <= notas.GetLength(0) - 1; i++)
        {
            double promedio = (notas[i, 0] + notas[i, 1] + notas[i, 2]) / 3;
            Console.WriteLine($"La nota promedio de {estudiantes[i]} es {promedio}");
        }

        //variable temporal para almacenar el estudiante con la nota mayor en cada iteración
        int idEstudiantePromedioMayor = 0;
        //variable temporal para almacenar la mayor nota encontrada en cada iteración
        double notaMayor = 0;
        for(int i = 0; i <= notas.GetLength(0) - 1; i++)
        {
            double promedio = (notas[i, 0] + notas[i, 1] + notas[i, 2]) / 3;
            if(promedio >= notaMayor)
            {
                notaMayor = promedio;
                idEstudiantePromedioMayor = i;
            }
        }

        Console.WriteLine($"El estudiante con la nota promedio mayor es {estudiantes[idEstudiantePromedioMayor]} con {Math.Round(notaMayor)}");

        int idEstudiantePromedioMenor = 0;
        double notaMenor = notaMayor;
        for(int i = 0; i <= notas.GetLength(0) - 1; i++)
        {
            double promedio = (notas[i, 0] + notas[i, 1] + notas[i, 2]) / 3;
            if(promedio <= notaMenor)
            {
                notaMenor = promedio;
                idEstudiantePromedioMenor = i;
            }
        }

        Console.WriteLine($"El estudiante con la nota promedio menor es {estudiantes[idEstudiantePromedioMenor]} con {Math.Round(notaMenor, 2)}");
    }
}
