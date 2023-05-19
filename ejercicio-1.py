def validadorClave(clave:str):
   
    
    
    if bool(clave.isalpha()):
        return True
    else:
        return False
    
    

        
    
    
    

ingreso = input("Ingrese una palabra: ")
response = validadorClave(ingreso)
print(response)