from os import system
import random
system("cls")

trabajadores = ["Juan Pérez",
                "María García",
                "Carlos López",
                "Ana Martínez",
                "Pedro Rodríguez",
                "Laura Hernández",
                "Miguel Sánchez",
                "Isabel Gómez",
                "Francisco Díaz",
                "Elena Fernández"
                ]

sueldos = {}

def asignar_sueldos_aleatorios():
    for trabajador in trabajadores:
        sueldos[trabajador] = random.randint(300000, 2500000)
    print("\nSueldos asignados aleatoriamente\n")

def clasificar_sueldos():
    bajos = {k: v for k, v in sueldos.items() if v < 800000}
    medios = {k: v for k, v in sueldos.items() if v >= 800000 and v <= 2000000}
    altos = {k: v for k, v in sueldos.items() if v > 2000000}
    total_bajos = 0
    total_medios = 0
    total_altos = 0
    contador_bajos = 0
    contador_medios = 0
    contador_altos = 0
    print("********* Clasificación de sueldos *********\n")
    
    print("\nSueldos menores a $800.000\n")
    for trabajador, sueldo in bajos.items():
        print(f"{trabajador:20} $ {sueldo}")
        total_bajos = total_bajos + sueldo

    print("\nSueldos entre $800.000 y $2.000.000\n")
    for trabajador, sueldo in medios.items():
        print(f"{trabajador:20} $ {sueldo}")
        total_medios = total_medios + sueldo
        contador_bajos = contador_bajos + 1

    print("\nSueldos superiores a $2.000.000\n")
    for trabajador, sueldo in altos.items():
        print(f"{trabajador:20} $ {sueldo}")
        total_altos = total_altos + sueldo

    total_sueldos = total_bajos + total_medios + total_altos
    print(f"\nTOTAL SUELDOS: $ {total_sueldos}")

def ver_estadistica():
    if not sueldos.items:
        input("Primero asigne los sueldos\nPresione ENTER para continuar")

def main():
    system("cls")
    print("MENÚ\n")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("5. Salir")
    while True:
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            asignar_sueldos_aleatorios()
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadistica()
        elif opcion == "5":
            print("Saliendo del programa... ")
            break
        else:
            print("debe ingresar una opción válida")
main()



















