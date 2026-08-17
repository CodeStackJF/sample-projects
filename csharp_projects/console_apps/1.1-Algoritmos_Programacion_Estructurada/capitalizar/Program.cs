namespace capitalizar;

class Program
{
    static void Main(string[] args)
    {
        string oracion = " este   es mi    men    sAjE";
        //Variable de control para determinar que, si es un espacio, la proxima letra debe pasarse a mayuscula
        bool esEspacio = true;

        //variable para almacenar el texto de salida
        string salida = "";

        //Se recorre caracter por caracter
        foreach(char letra in oracion)
        {
            //Si la letra es un espacio en blanco definimos en true la variable de control y concatenamos el caracter
            if(letra.ToString() == " ")
            {
                esEspacio = true;
                salida += letra.ToString();
            }

            //Si no un espacio evaluamos si capitalizar o no
            if(letra.ToString() != " ")
            {
                //salida += esEspacio ? letra.ToString().ToUpper():letra.ToString().ToLower();
                //Si el caracter anterior fue un espacio, la variable esEspacio será igual a true
                //entonces pasamos la letra a mayuscula
                if(esEspacio)
                {
                    salida += letra.ToString().ToUpper();
                }
                //si esEspacio es igual a false, entonces el caracter anterior fue una letra por lo que solo concatenamos en minuscula
                else
                {
                    salida += letra.ToString().ToLower();
                }
                //ya que no fue una letra pasamos a false la variable
                esEspacio = false;
            }
        }

        Console.WriteLine(salida);
    }
}
