using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace inventario
{

    public class Herencia()
    {
        public void Run()
        {
            var empleado = new Empleado("Juan", 500);
            empleado.MostrarDatos();

            var docente = new Docente("Ana", 600, "Matemáticas");
            docente.MostrarDatos();
            Console.WriteLine(docente.materia);
        }
    }

    public class Empleado
    {
        public string nombre;
        public decimal salario;

        public Empleado(string _nombre, decimal _salario)
        {
            nombre = _nombre;
            salario = _salario;
        }

        public virtual void MostrarDatos()
        {
            Console.WriteLine($"Nombre: {nombre} Salario: {salario}");
        }
    }

    public class Docente : Empleado
    {
        public string materia;
        public Docente(string _nombre, decimal _salario, string _materia) : base(_nombre, _salario)
        {
            materia = _materia;
        }

        public override void MostrarDatos()
        {
            Console.WriteLine($"Nombre: {nombre} Salario: {salario} Materia: {materia}");
        }
    }
}