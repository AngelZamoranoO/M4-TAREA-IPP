def validaMayuscula(clave:str):
    mayuscula=False
    for valida in clave:
        if valida.isupper():
            mayuscula=True

    return mayuscula

def validaMinuscula(clave:str):
    minuscula=False
    for valida in clave:
        if valida.islower():
            minuscula=True
    return minuscula
    
def validaDigito(clave:str):
    digito=False
    for valida in clave:
        if valida.isdigit():
            digito=True
    return digito
    
if __name__=='__main__':
    ingresoContrasena = input("Ingrese una palabra: ")
    if ingresoContrasena.isalnum():
        if validaMayuscula(ingresoContrasena) and validaMinuscula(ingresoContrasena) and validaDigito(ingresoContrasena):
            response = "Contrasena Segura"
        else: 
            response = "Contrasena insegura"
            
        
    else: 
        response= "La contrasena a verificar no debe tener caracter extranos"   
    
    print(response)