#valida si tiene mayuscula la clave
def validaMayuscula(clave:str):
    mayuscula=False
    for valida in clave:
        if valida.isupper():
            mayuscula=True

    return mayuscula

#valida si tiene minuscula la clave
def validaMinuscula(clave:str):
    minuscula=False
    for valida in clave:
        if valida.islower():
            minuscula=True
    return minuscula

#valida si tiene numero la clave    
def validaDigito(clave:str):
    digito=False
    for valida in clave:
        if valida.isdigit():
            digito=True
    return digito
    
if __name__=='__main__':
    #ingresa una palabra
    ingresoContrasena = input("Ingrese una palabra: ")
    
    if ingresoContrasena.isalnum():#=> valida si la palabra es alfanumerica.
        if validaMayuscula(ingresoContrasena) and validaMinuscula(ingresoContrasena) and validaDigito(ingresoContrasena):
            response = "Contrasena Segura"
        else: 
            response = "Contrasena insegura"
            
        
    else: 
        response= "La contrasena a verificar no debe tener caracter extranos"   
    #responde la respuesta de la clave
    print(response)