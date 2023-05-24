from os import system
import time
class Cuenta():
    #atributos de la clase
    number_account:int
    headline_name:str
    initial_balance:int
    account_type:str
    
    #como valor agregado se creo tambien un constructor
    def constructor(self, number_account:int, headline_name:str, initial_balance:int, account_type:str):
        self.number_account=number_account
        self.headline_name=headline_name
        self.initial_balance=initial_balance
        self.account_type=account_type
        
    
    def deposit(self,abono:int):
        self.initial_balance=self.initial_balance+abono
        new_balance=self.initial_balance
        return f'Se abono: {abono} \n El nuevo saldo es => {new_balance}'
        
    
    def withdraw(self, retiro:int):
        if self.initial_balance<=retiro:
            return f'Saldo maximo a retirar => {self.initial_balance}'
        else:
            self.initial_balance=self.initial_balance-retiro
            new_balance=self.initial_balance
            return f'Se retiro: {retiro} \n El nuevo saldo es => {new_balance}'
        
    
    def balance(self):
        return f'Saldo actual: {self.initial_balance}'
        


if __name__=='__main__':
    
    try:
        print('*************** CUENTA BANCARIA ***************')
        cuenta =  Cuenta()
        
        cuenta.number_account=int(input('Ingrese numero de cuenta: \n'))
        cuenta.headline_name=str(input('Ingrese nombre del titular: \n'))
        cuenta.initial_balance=int(input('Ingrese el monto inicial: \n'))
        cuenta.account_type=str(input('Ingrese el tipo de cuenta: \n'))
        
        system('cls')
        
        while True:
            
            print('Opcion 1 => DEPOSITAR')
            print('Opcion 2 => RETIRAR')
            print('Opcion 3 => BALANCE')
            print('Opcion 4 => Salir')
            opcion=int(input('Numero Opcion => '))
            
            if opcion==1:
                deposito=int(input('1) Ingrese el monto a depositar => $'))
                print(cuenta.deposit(deposito))
                time.sleep(5)
                system('cls')
            elif opcion==2:
                retiro=int(input('1) Ingrese el monto a retiro => $'))
                print(cuenta.withdraw(retiro))
                time.sleep(5)
                system('cls')
            elif opcion==3:
                print(cuenta.balance())
                time.sleep(5)
                system('cls')
            elif opcion==4:
                break
                
            else:
                print('La opcion ingresar no existe, vuelve a intentarlo')
                time.sleep(5)
                system('cls')
            
        print('FIN DEL PROGRAMA')         
    except ValueError as e:
        print('El valor ingresaro no exite, ValueError =>',e)
        