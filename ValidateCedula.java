import java.util.regex.Pattern;
import java.util.regex.Matcher;

    public class ValidateCedula
    {
        public static void main(String[] args)
        {
			
            System.out.println(validate("Coloque una cedula valida aqui")); 
            System.out.println(validate("02601172932")); //False  
            System.out.println(validate("00000000012")); //False
            System.out.println(validate("001-0247021")); //False
        }

        static boolean validate(String cedula)
        {
            boolean isValid = false;

            if (!cedula.isEmpty())
            {
                /*
                  Regex para filtrar cedulas con el formato correcto: 11 digitos 
                  que no empienzan con 000 ni contenga guiones
                 */
        

				Pattern pattern = Pattern.compile("^(?!000)[0-9]{11}$");
				Matcher matcher = pattern.matcher(cedula);
		
                if (matcher.matches())
                {
                    int len = cedula.length();
                    // Digito verificador. Ultimo digito del arreglo
                    int v = Integer.parseInt( cedula.substring( len-1 ) );
                    
                    int sn  = 0; // sumatoria de los n-elementos del arreglo
                    int pos = 0; // Posicion en el arreglo

                    // Procesar arreglo descendentemente: der -> izq
                    for (int n = len - 2; n >= 0; n--)
                    {
                        int e = Integer.parseInt(cedula.substring(n, n+1));
                        //p ++;
						/* Multiplicar por 2 los numeros en posiciones impares
						   en el arreglo. Restarle 9 si el resultado es
						   mayor que 9 
						*/
                        sn += ( ++p % 2 != 0 ? ( ( e * 2 ) > 9 ? e - 9 : e ) : e );
                    }
                    sn = 10 - sn % 10;
                    /*
                       Si la suma es 10 el verificador debe ser cero
                       o el verificador y la suma deben coincidir
                    */

                    if ((sn == 10 && v == 0) || sn == v )
                        isValid = true;
                }

            }//if

            return isValid;

        }//validate

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

    }//ValidateCedula