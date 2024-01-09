import sys
class Vocales:
    def __init__(self):
        pass
    def comparar(self,letra):
        if letra in ('a','e','i','o','u'):
            print("Es vocal")
        elif letra == " " or not letra.isalpha() or letra.isdigit():
            print("No hay un caracter del alfabeto")
        else:
            print("Es consonante")
    def contar(self,letra):
        while len(letra) != 1 or not letra.isalpha():
            letra = input("Tienes que poner una (1) sola letra: ")
        return letra

                
diccionario= Vocales()
letra=input("Pon una letra :D ")
conteo=len(letra)
letra=diccionario.contar(letra)
diccionario.comparar(letra)
sys.exit()

    