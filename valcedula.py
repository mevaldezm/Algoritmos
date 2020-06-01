from functools import reduce
from datetime import date, datetime
import re
 
 
def func_odd(n):

    t = n * 2
    if ( t > 9 ): # Numeros mayores o igual a 10
        t -= 9
        return n
    return n

def validate_cedula( value ):

    ok = False

    m = re.search(r'^(?!000|=.*\d)(?=.*[1-9]).{11}$', value)
    ced = m.group(0)

    if m is not None:
    
        v = int( ced[-1] ) # digito verificador enesimo
        z = [ int(n) for n in ced[1:10] ] # numeros de la cedula del 2 al 9
        
        even_pos = z[1:9:2] # numeros en posiciones pares del arreglo del 2 al 8
        odd_pos  = z[0::2]  # numeros en posiciones impares del arreglo del 1 al 9
        
        for n in odd_pos:
            odd_pos = list(map(lambda x: x(n), [func_odd] ))
        
        sn = 10 - reduce((lambda x, y: (x + y) % 10 ), odd_pos + even_pos)       
      
        print ( sn )
        
        if ( (sn == 10 and v == 0) or sn == v):
            ok = True
    return ok

    
print( validate_cedula('00102470812') )
#print( validate_cedula('00000000012') )

