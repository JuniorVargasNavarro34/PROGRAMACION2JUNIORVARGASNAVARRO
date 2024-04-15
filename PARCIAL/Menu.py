class MenuPrincipal:
    def __init__(self):
        self.opciones = {
            '1': SubMenu('PERSONAS'),
            '2': SubMenu('UNIVERSIDADES'),
            '3': SubMenu('NOTAS'),
            '4': SubMenu('ASIGNATURA'),
            '5': self.salir
        }

    def mostrar_menu(self):
        print("\nMENU PRINCIPAL\n")
        print("1. PERSONAS")
        print("2. UNIVERSIDADES")
        print("3. NOTAS")
        print("4. ASIGNATURA")
        print("5. SALIR")

    def salir(self):
        print("Saliendo del programa...")
        exit()

class SubMenu:
    def __init__(self, categoria):
        self.categoria = categoria
        self.opciones = {
            '1': self.crear_elemento,
            '2': self.listar_elementos,
            '3': self.eliminar_elemento,
            '4': self.atras
        }
        self.elementos = []

    def mostrar_submenu(self):
        print(f"\nSUBMENU {self.categoria}\n")
        print("1. CREAR")
        print("2. LISTAR")
        print("3. ELIMINAR")
        print("4. ATRAS")

    def crear_elemento(self):
        if self.categoria == 'PERSONAS':
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = input("Ingrese la edad: ")
            correo = input("Ingrese el correo electrónico: ")
            identificacion = input("Ingrese la identificación: ")
            raza = input("escriba si es negro o blanco:")
            persona = {'Nombre': nombre, 'Apellido': apellido, 'Edad': edad, 'Correo': correo, 'Identificación': identificacion, 'raza': raza,}
            self.elementos.append(persona)
            print("Persona creada exitosamente.")
        elif self.categoria == 'UNIVERSIDADES':
            nombre = input("Ingrese el nombre de la universidad: ")
            direccion = input("Ingrese la dirección de la universidad: ")
            universidad = {'Nombre': nombre, 'Dirección': direccion}
            self.elementos.append(universidad)
            print("Universidad creada exitosamente.")
        elif self.categoria == 'NOTAS':
            notas = []
            for i in range(5):
                nota = float(input(f"Ingrese la nota {i + 1}: "))
                notas.append(nota)
            self.elementos.append(notas)
            print("Notas ingresadas exitosamente.")
        elif self.categoria == 'ASIGNATURA':
            asignaturas = []
            for i in range(5):
                asignatura = input(f"Ingrese la asignatura {i + 1}: ")
                asignaturas.append(asignatura)
            self.elementos.append(asignaturas)
            print("Asignaturas ingresadas exitosamente.")

    def listar_elementos(self):
        if self.elementos:
            print(f"\nListado de {self.categoria.lower()}s:")
            for elemento in self.elementos:
                print(elemento)
        else:
            print(f"No hay {self.categoria.lower()}s para mostrar.")

    def eliminar_elemento(self):
        if self.elementos:
            print(f"\nListado de {self.categoria.lower()}s:")
            for i, elemento in enumerate(self.elementos):
                print(f"{i + 1}. {elemento}")
            opcion = input("Seleccione el número del elemento a eliminar: ")
            try:
                indice = int(opcion) - 1
                if 0 <= indice < len(self.elementos):
                    del self.elementos[indice]
                    print(f"{self.categoria[:-1]} eliminado exitosamente.")
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Opción inválida.")
        else:
            print(f"No hay {self.categoria.lower()}s para eliminar.")

    def atras(self):
        menu_principal = MenuPrincipal()
        menu_principal.mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        menu_principal.opciones[opcion]()

def main():
    menu_principal = MenuPrincipal()
    while True:
        menu_principal.mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion in menu_principal.opciones:
            if opcion == '5':
                menu_principal.opciones[opcion]()
            else:
                submenu = menu_principal.opciones[opcion]
                submenu.mostrar_submenu()
                opcion_submenu = input("\nSeleccione una opción del submenu: ")
                submenu.opciones[opcion_submenu]()

if __name__ == "__main__":
    main()



#JUNIOR VARGAS NAVARRO Y CARLOS MARTINEZ TOBINSON