using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace ValidateCedulaApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ValidateCedula("Coloque una cedula valida aqui")); 
            Console.WriteLine(ValidateCedula("02601172932")); //False  
            Console.WriteLine(ValidateCedula("00000000012")); //False
            Console.WriteLine(ValidateCedula("001-0247021")); //False
        }

        static bool ValidateCedula(string cedula)
        {
            bool isValid = false;

            if (!string.IsNullOrEmpty(cedula))
            {
                /*
                  Regex para filtrar cedulas con el formato correcto: 11 digitos 
                  que no empienzan con 000 ni contenga guiones
                 */

                if (Regex.IsMatch(cedula, "^(?!000)[0-9]{11}$"))
                {
                    int len = cedula.Length;
                    // Digito verificador. Ultimo digito del arreglo
                    int v = int.Parse(cedula.Substring(len - 1));

                    int sn  = 0; // sumatoria de los n-elementos del arreglo
                    int pos = 0; // Posicion en el arreglo

                    // Procesar arreglo descendentemente: der -> izq
                    for (int n = len - 2; n >= 0; n--)
                    {
                        int e = int.Parse(cedula.Substring(n, 1));
                        pos++;
                        sn += EvalPos(e, pos);
                    }
                    sn = 10 - sn % 10;
                    /*
                       Si la suma es 10 el verificador debe ser cero
                       o el verificador y la suma deben coincidir
                    */

                    if ((sn == 10 && v == 0) || sn == v)
                        isValid = true;
                }

            }//if

            return isValid;

        }//ValidateCedula

        /* Multiplicar por 2 los numeros en posiciones impares
           en el arreglo. Restarle 9 si el resultado es
           mayor que 9 
        */
        static int EvalPos(int n, int pos)
        {
            if (pos % 2 != 0)
            {
                int t = n * 2;
                if (t > 9)
                    t -= 9;
                return t;
            }
            return n;
        }//EvalPos

    }//Program
}//Namespace
