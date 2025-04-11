"""
Escribe un programa que intente dividir dos números. Si el segundo número es cero,
captura la excepción ZeroDivisionError y muestra un mensaje de error al usuario.
"""
try:
    numerador=int(input("ingresar numerador:"))
    denominador=int(input("Ingrese denominador:"))
    resultado = numerador/denominador
    print(f"Resultado:{resultado}")

except Exception as e: 
    print(f"ah ocurrido un error tipo {e}")
