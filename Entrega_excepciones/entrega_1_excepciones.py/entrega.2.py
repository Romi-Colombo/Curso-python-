"""
Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.
"""
try:
    numero=int(input("ingresar numero:"))
    texto=input("Ingrese texto:")
    resultado = numero+texto
except Exception as e: 
    print(f"ah ocurrido un error tipo {e}")

