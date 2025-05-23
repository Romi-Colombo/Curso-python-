import CuentaBancaria as cb

class CuentaAhorro(cb.CuentaBancaria): 
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo) #Heredamos los atributos de la clase madre.
        self.__tasa_interes = 0.001  # Tasa fija por defecto, atributo privado. 

    def calcular_interes(self): #le agregamos un metodo nuevo, que nos calcule el interes.
        interes = self.obtener_saldo() * self.__tasa_interes
        return interes

    def extraer(self, monto):
        if monto <= self.obtener_saldo():
            self.saldo = self.saldo - monto
            print(f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}. Saldo actual: {self.obtener_saldo()}")
        else:
            print("No posee saldo suficiente para esta operación.")

    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto
            print(f"Se han depositado {monto} en la cuenta de {self._nombre_titular}. Saldo actual: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser positivo.")