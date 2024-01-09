import sys
class contar:
    def __init__ (self):
        pass
    def contar(self,cadena):
        contador=0
        for caracter in cadena:
            if caracter!=" ":
                contador+=1
        return contador
        
    def __str__(self):
        return f"Objeto contador"
Contador = contar()
cadena=input("Pon un texto que vamos a contar sus letras :D \n")
resultado= Contador.contar(cadena)
print(f"La cadena tiene {resultado} carateres")
sys.exit()