trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
"Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

import random
import statistics
import csv

sueldos = []
def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("\nSueldos asignados correctamente:")
    print(sueldos)
    print("Pulse número 2 para clasificar los sueldos")

def clasificar_sueldos():
    if not sueldos:
        print("Primero debe asignar los sueldos.")
        return

    bajo = []
    medio = []
    altos = []
    
    
    contador_b = 0
    contador_m = 0
    contador_a = 0

    for trabajador,sueldo in zip (trabajadores, sueldos) :
        if sueldo < 800000:
            print(f"{trabajador}: Sueldo bajo -> {sueldo}")
            contador_b=contador_b+1
            print(contador_b)
        elif 800000 <= sueldo <= 2000000:
            print(f"{trabajador}: Sueldo medio -> {sueldo}")
            contador_m=contador_m+1
            print(contador_m)
        else:
            print(f"{trabajador}: Sueldo alto -> {sueldo}")
            contador_a=contador_a+1
            print(contador_a)
def ver_estadisticas():
    if not sueldos:
        print("\nPrimero debe asignar el valor de los sueldos. \n Pulse opción 1 para asignar el valor de los sueldos.")
        return
    
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)
    media = statistics.geometric_mean(sueldos)
    
    print(f"Sueldo más alto: {sueldo_max}")
    print(f"Sueldo más bajo: {sueldo_min}")
    print(f"Promedio de sueldos: {promedio_sueldos}")
    print(f"Media geométrica: {media}")


def generar_reporte():
    if not sueldos:
        print("Debe asignar los sueldos \n presione número 1 para asignar los sueldos.")
        return
    
    with open('reporte_sueldos_Trabajadores.csv', 'w') as file:
        writer=csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador,sueldo in zip(trabajadores,sueldos):
            desc_salud=sueldo* 0.07
            desc_afp=sueldo* 0.12
            sueldo_liq=sueldo,desc_salud,desc_afp
            writer.writerow([trabajador,sueldo,desc_salud,desc_afp,sueldo_liq])
            print("\n")
            print(f"\n{trabajador} Sueldo Base: {sueldo},Descuento por Salud: {desc_salud},Descuento por AFP: {desc_afp},Sueldo Líquido: {sueldo_liq}")

def mostrar_menu():
    while True:
        print("\n------------ MENÚ SUELDOS ------------")
        print("1. Asignar sueldos de manera aleatoria")
        print("2. Clasificar los sueldos")
        print("3. Ver estadísticas")
        print("4. Generar Reporte de sueldos")
        print("5. Salir del programa")
        
        
        opcion = input("Seleccione una opción (1,5): ")
        
        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            generar_reporte()
        elif opcion == '5':
            print("FINALIZANDO PROGRAMA...")
            print("Desarrollado por Josefa Calzada")
            print("RUT: 21.502.445-8")
            break
        else:
            print("Opción inválida. Intente con una otra opción (1,5)")
        

if __name__ == "__main__":
    mostrar_menu()