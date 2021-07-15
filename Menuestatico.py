import sys
import os
class Menu:
    def __init__(self, prompt=">"):
        self.prompt = prompt + " "
        self.elecciones = {
                "1" : self.suma_Estatica,
                "2" : self.Multi_Estatica,
                "3" : self.Resta_Estatica,
                "4" : self.quit
                } 

    def imprimir_menu(self):
        print("""
                Class Menu
                Operaciones simples estaticas
                1 Suma estatica
                2 Multiplicacion estatica
                3 Resta estatica
                4 Salir
                """)
    a=4
    b=3
    def suma_Estatica(self, a, b) :
        return a + b

    def Multi_Estatica(self, a, b) :
        return a * b

    def Resta_Estatica(self, a, b) :
        return a - b

    

    def run(self):
        while True:
            self.imprimir_menu()
            eleccion = input("Ingrese una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} incorrecto intente nuevamente".format(eleccion))

    

    def quit(self):
        print("Gracias por visitarnos.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()