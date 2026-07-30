namespace ejercicios_practicos
{
    public class Ejercicio5
    {
        public void Run()
        {
            Gato gato = new Gato("Miau");
            Perro perro = new Perro("Guau");
            gato.HacerSonido();
            perro.HacerSonido();
        }
    }

    public class Animal
    {
        private readonly string sonido;
        private readonly string animal;

        public Animal(string _sonido, string _animal)
        {
            sonido = _sonido;
            animal = _animal;
        }

        public void HacerSonido()
        {
            Console.WriteLine($"El {animal} hace {sonido}");
        }
    }

    public class Gato : Animal
    {
        public Gato(string sonido):base(sonido, nameof(Gato))
        {
            
        }
    }

    public class Perro : Animal
    {
        public Perro(string sonido):base(sonido, nameof(Perro))
        {
            
        }
    }
}