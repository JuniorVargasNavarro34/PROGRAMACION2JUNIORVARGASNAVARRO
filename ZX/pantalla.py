while True:
    print("Menu de opciones:")
    print("1. Personas")
    print("2. Vehiculos")
    print("3. Universidades")
    print("4. Notas")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        print("Hola, has presionado la opción Personas")
    elif opcion == '2':
        print("Hola, has presionado la opción Vehiculos")
    elif opcion == '3':
        print("Hola, has presionado la opción Universidades")
    elif opcion == '4':
        print("Hola, has presionado la opción Notas")
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción válida.")
