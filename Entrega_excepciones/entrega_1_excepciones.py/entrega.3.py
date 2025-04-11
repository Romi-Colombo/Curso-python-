"""
Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra.
"""

try:
    diccionario = {
  "Nombre": "Romina",
  "Edad": 23,
  "Documento": 1003882
}
    llave1 = input("Ingrese llave que quiera buscar en diccionario: ")
    llave2 = diccionario[llave1]
    print(f"Valor de llave: {llave2}")
except KeyError as e: 
    print(f"ah ocurrido un error tipo {type(e)}, no existe esa llave en el diccionario")