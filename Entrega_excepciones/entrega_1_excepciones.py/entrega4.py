"""
Escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe.
"""

try:
    archivo=input("ingresar nombre de archivo:")
    open(archivo, mode="r")

except FileNotFoundError as e: 
    print(f"ah ocurrido un error tipo {type(e)}, el archivo no existe")
    print("Se creara un archivo automaticamente")
    with open(archivo, "w") as archivo1:
        archivo1.write("Archivo creado con Python recientemente.\n")
    print(f"archivo {archivo} creado")    
