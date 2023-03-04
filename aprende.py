texto = "hola mundo!"
entero = 151681981981981981981
flotante = 1515165.15461651


"""
    texto = string = str
    decimal = float = flotante
    boleanos:
    True == 1 == 1243124124 ==  1123123.1231 == "aoiwdmaod"
    False == 0
"""

# listas != tupla != diccionario != conjunto
"""
lista -> 1, 2, 3, 4, 5, 6 -> 7
tupla -> 1, 2, 3, 4, 5, 6 
conjunto -> 1, 2, 3, 4, 5, 6, 6 ,7, 8
"""
"""====================================================="""
lista = ["1", "2", 3, [3.1, 3.2, 3.3], 4, (4.1,4.2,4.3)]
lista2 = list(1,2,3,"4") # ¿cómo agregamos más items a la lista???? -> pendiente
"""====================================================="""
tupla = (4.1,4.2,4.3, [3.1, 3.2, 3.3], )
tupla2 = tuple("1","2", "3")
"""====================================================="""
conjunto = {1,2,3,4,5,6,6,7,7}
conjunto2 = set(1,2,3,4,5,6,6,7,7)
"""====================================================="""
cliente1 = {"nombre":"mikel", "apellido":"Aranda", "edad": 5}
cliente2 = {"nombre":"evelin", "apellido":"Aranda", "edad": 6}
cliente3 = {"nombre":"eduardo", "apellido":"mascota", "edad": 2}
lista_clientes = [cliente1, cliente2, cliente3]

"""funciones"""
"""========================================================"""
"""Conjunto de instrucciones agrupadas que pueden ser reutilizadas"""

def calcular_mitad(n1, n2): #toma esta hojita con estas instrucciones
    mitad_1 = n1/2
    mitad_2 = n2/2
    print(mitad_1)
    print(mitad_2)
#fin de hojita con instrucciones

#ok, la guardo

#ahora!
calcular_mitad(n1=50, n2= 30)

import random

"""clase"""
class Robot():
    #atributos
    color = "rojo"
    nombre = "Eduardo"
    num_piezas = 5000
    #métodos
    def correr(self):
        print("estoy corriendo!")
    def truco1(self):
        print(" me di una voltereta!")
    def truco2(self):
        print("di un salto mortal!")
    def combo_trucos(self):
        if self.num_piezas > 3000:
            self.correr()
            self.truco1()
            self.truco2()
            probability = random.randint(1,100)
            if probability < 30:
                print("me caí! :c")
                self.num_piezas = self.num_piezas - random.randint(100,1000)
            else:
                print("aplaudanme!!!!")
        else:
            print("lo siento, no tengo las piezas necesarias :c")
    def autoreparacion(self):
        self.num_piezas = 5000



mi_robot = Robot()


#TODO:
# Crear un objeto cliente con sus caracteríscas y que tenga las acciones de -> actualizar estado de servicio, enviar whatsapp (en pantalla)
# relacion de servicios con estado, obtener servicios de mantenimiento y así con cada tipo de servicio


