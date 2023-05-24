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
        
        cuenta.
        while True:
            
        
    except ValueError as e:
        print('El valor ingresaro no exite, ValueError =>',e)
        