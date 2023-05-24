
def numero(): #funcion recursiva
    #ingresa el numero
    ingresarNumero = input('Ingrese un numero, (ingresar espacio se sale del programa)')
    
    #si ingresa un espacio entra al if y retorna un 0
    if ingresarNumero == ' ':

       return 0
    
    #se transforma el numero que ingresa y la funcion en enteros
    numeroEntero = int(ingresarNumero)
    sumaNumero = int(numero())
    #al ingresar un numero entra en la funcion recursiva y realiza la misma consulta para escribir un numero
    # si escribe espacio, retorna toda la sumatoria en la funcionalidad recursiva.
    return numeroEntero + sumaNumero
    
#funcion main
if __name__=='__main__':
    
    #imprime el resultado de la funcion recursiva
    print(numero())
    
   
        