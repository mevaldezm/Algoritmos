import re
 
# Multiplicar por 2 los numeros en posiciones impares
# en el arreglo. Restarle 9 si el resultado es
# mayor que 9

def eval_pos(n, pos):
 
    if ( pos % 2 != 0 ):
        t = n * 2
        if ( t > 9 ): 
            t -= 9
        return t
    return n

def validate_cedula( value ):
    
    # Regex para filtrar cedulas con el formato correcto: 11 digitos 
    # que no empienzan con 000 ni contenga guiones
    p = re.compile(r'^(?!000)[0-9]{11}$')
    m = p.match( value )
    
    is_valid = False
    
    if m:
        ced = m.group(0)
        v = int( ced[-1] ) # Digito verificador. Ultimo digito del arreglo
        z = [ int(n) for n in ced[:10] ] #Los primeros 10 digitos
        
        sn  = 0 # sumatoria de los n-elementos del arreglo
        pos = 0 # Posicion en el arreglo
        
        for n in z[::-1]: # Procesar arreglo descendentemente: der -> izq
            pos += 1
            sn  += eval_pos(n, pos)
            
        sn = 10 - sn % 10
        
        # Si la suma es 10 el verificador debe ser cero
        # o el verificador y la suma deben coincidir
        if ( (sn == 10 and v == 0) or sn == v):
            is_valid = True
            
    return is_valid
   
print( validate_cedula('00104464664'))
print( validate_cedula('01800475863'))
print( validate_cedula('02601172932'))
print( validate_cedula('00000000012') )
print( validate_cedula('001-0247021') )

