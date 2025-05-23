from abc import ABC, abstractmethod

#Creo clase abstracta ya que nunca el usuario va a utilizar directamente esta clase. (O sea, nunca voy a 
# instanciar un objeto cuenta bancaria)

class CuentaBancaria(ABC):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular
        self._dni_titular = dni_titular
        self._fecha_nacimiento = fecha_nacimiento
        self.__saldo = saldo

    def mostrar_nombre(self):
        return self._nombre_titular

    def cambiar_nombre(self, nuevo_nombre):
        self._nombre_titular = nuevo_nombre

    def obtener_saldo(self):
        return self.__saldo

    #Creo metodos abstractos de extraer y depositar ya que quiero que sean modificables
    #segun la clase hija. 

    @abstractmethod
    def extraer(self, monto):
        pass

    @abstractmethod
    def depositar(self, monto):
        pass