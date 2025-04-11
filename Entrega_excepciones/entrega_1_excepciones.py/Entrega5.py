"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError. Si el primer número es un número no válido,
captura la excepción ValueError. En cualquier caso, muestra un mensaje de error al usuario.
"""
"""
try:
    numerador=int(input("ingresar numerador:")) #Numero entero
except Exception as e:
    print(f"error, debe ser un numero entero. Error: {e}")
except Exception as e:
    denominador=int(input("Ingrese denominador:")) #Numero entero
    resultado = numerador/denominador
    print(f"Resultado:{resultado}") 
except Exception as e: 
    print(f"ah ocurrido un error tipo {e}")
"""
try:
    numerador = int(input("Ingresar numerador: "))
    denominador = int(input("Ingresar denominador: "))
    resultado = numerador / denominador

except ZeroDivisionError as e:
    print(f" Error: No se puede dividir entre cero. Error: {e}")

except ValueError as e:
    print(f" Error: Debes ingresar números enteros válidos. Error: {e}")

else:
    print(f" Resultado: {resultado}")