"""
Calcular el promedio de una lista de números usando args y un operador ternario.
Imprimir un mensaje de error si no se pasan suficientes argumentos.
"""
def promedio(*args):
   
   print( f"promedio: {sum(args)/len(args)}" if len(args)>0 else "Error. Lista vacía.")

promedio(2,3,4.2)