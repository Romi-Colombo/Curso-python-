import CuentaBancaria as cb

#Conceptualmente, creamos un metodo abstracto de la clase padre para que se pueda modificar
#ese metodo en cuenta ahorro y cuenta bancaria, por lo tanto las defino de manera distinta en cada clase hija. 

class CuentaCorriente(cb.CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo = 0, limite_extraccion = 500, limite_deposito = 1000):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._li_extraccion = limite_extraccion #atributo privado. 
        self._li_deposito = limite_deposito #atributo privado. 
    
    def extraer(self, monto):
        if monto <= self.obtener_saldo() and monto <= self._li_extraccion: #A diferencia de C.ahorro, tiene un limite de extraccion.
            self.saldo = self.saldo - monto
            print(f"Se ha extraido {monto} de la cuenta de {self._nombre_titular}, su saldo acutal es de: {self.obtener_saldo()}")

        else:
            if monto > self._li_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")

    def depositar(self, monto): #A diferencia de C.ahorro, tiene un limite de deposito.
        if monto > 0 and monto < self._li_deposito:
            self.saldo = self.saldo + monto
            print(f"Se han depositado {monto} en la cuenta de {self._nombre_titular}. Saldo actual: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser positivo.")

