"""
Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario.
"""
def buscar_palabra (palabra, *args):
    print("Palabra encontrada" if palabra in args else "Palabra no encontrada")

lista = input ("ingrese las palabras de la lista separadas por comas: ")
lista = lista.split(",") #Return a list of the substrings in the string. Separa por comas. 
palabra_buscada = input("Ingrese palabra que quisiera verificar en lista: ")

buscar_palabra(palabra_buscada, *lista)