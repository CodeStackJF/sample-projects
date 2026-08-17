namespace ejercicios_practicos
{
    public class Ejercicio1
    {
        public void MostrarBienvenida(string nombre)
        {
            Console.WriteLine($"Bienvenido {nombre}");
        }

        //se usa _base porque base es una palabra reservada
        public decimal CalcularAreaRectangulo(decimal _base, decimal altura)
        {
            return _base * altura;
        }
    }
}