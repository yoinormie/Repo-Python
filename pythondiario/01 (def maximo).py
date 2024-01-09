class Maximo:
    def __init__(self):
        pass
    def comparacion(self,n1,n2):
        if(n1>n2):
            print("El 1er nº es mayor")
        elif(n1<n2):
            print("El 2do nº es mayor")
        else:
            print("Son iguales ://")
            
calculadora=Maximo()

num1=int(input("1er nº: "))
num2=int(input("2do nº: "))
calculadora.comparacion(num1,num2)