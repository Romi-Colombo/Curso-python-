"""
Calcular el mayor de dos números ingresados por teclado usando un operador
ternario
"""
n1 = input("Ingrese primer numero: ")
n2 = input("Ingrese segundo numero: ")
print(f"El primer numero ingresado es mayor o igual, {n1}>{n2}." if n1>=n2 else f"El segundo numero ingresado es mayor que el primero, {n2}>{n1}.")