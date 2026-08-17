namespace ejercicios_practicos
{
    public class Ejercicio3_4
    {
        private int id { get; set; }
        private string nombre { get; set; }
        private double salario {get; set;} = 0;

        public Ejercicio3_4(int _id, string _nombre)
        {
            id = _id;
            nombre = _nombre;
        }

        public void MostrarInformacion()
        {
            Console.WriteLine($"El id del empleado es {id} y su nombre {nombre}. Salario: {salario}");
        }

        //parte de ejercicio 4
        public void DefinirSalario(double _salario)
        {
            if(salario < 0)
            {
                Console.WriteLine("El salario no puede ser menor a cero.");
            }
            else
            {
                salario = _salario;
            }
        }
    }
}