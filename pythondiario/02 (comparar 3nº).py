class Tres:
    def __init__(self):
        pass
    def comparar(self,n1,n2,n3):
        if(n1>n2 and n1>n3):
            print(n1)
        elif(n2>n1 and n2>n3):
            print(n2)
        else:
            print(n3)

calk=Tres()
n1=int(input("1er nº: "))
n2=int(input("2do nº: "))
n3=int(input("3er nº: "))

calk.comparar(n1,n2,n3)