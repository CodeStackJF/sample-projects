namespace capitalizar;

class Program
{
    static void Main(string[] args)
    {
        string oracion = " este   es mi    men    sAjE";
        bool esEspacio = true;
        string salida = "";
        foreach(char letra in oracion)
        {
            if(letra.ToString() == " ")
            {
                esEspacio = true;
                salida += letra.ToString();
            }
            if(letra.ToString() != " ")
            {
                //salida += esEspacio ? letra.ToString().ToUpper():letra.ToString().ToLower(); 
                if(esEspacio)
                {
                    salida += letra.ToString().ToUpper();
                }
                else
                {
                    salida += letra.ToString().ToLower();
                }
                esEspacio = false;
            }
        }

        Console.WriteLine(salida);
    }
}
