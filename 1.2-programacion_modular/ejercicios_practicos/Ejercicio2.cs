namespace ejercicios_practicos
{
    public class Ejercicio2
    {
        public void Intercambiar(ref int a, ref int b)
        {
            //Creamos una variable temporal para guardar uno de los valores
            int temp = b; 
            //realizamos el intercambio
            b = a;
            a = temp;
        }
    }
}