from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from utils import leer_entero, mostrar_opciones

pila = MiPila(10)
cola = MiCola(10)


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  ✓ Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero = pila.desapilar()
            if pasajero:
                print(f"  ✓ Desapilado: {pasajero}")
            else:
                print("  ⚠ La pila está vacía")
        elif op == "4":
            tope = pila.ver_tope()
            if tope:
                print(f"  Tope: {tope}")
            else:
                print("  ⚠ La pila está vacía")
        elif op == "5":
            num = leer_entero("  Número de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en posición [{pos}]: {pila.datos[pos]}")
            else:
                print("  ✕ Pasajero no encontrado")
        elif op == "6":
            num = leer_entero("  Número de pasajero a modificar: ")
            if pila.buscar(num) != -1:
                destino = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                pila.modificar(num, destino, asiento)
                print("  ✓ Datos modificados correctamente")
            else:
                print("  ✕ Pasajero no encontrado")
        elif op == "7":
            num = leer_entero("  Número de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print(f"  ✓ Pasajero #{num} eliminado correctamente")
            else:
                print("  ✕ Pasajero no encontrado o pila vacía")
        elif op == "8":
            copia = pila.copiar()
            print("  --- Copia realizada ---")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()} | ¿Está vacía?: {'Sí' if pila.esta_vacia() else 'No'}")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if pila.apilar(p):
                    cargados += 1
            print(f"  ✓ {cargados} datos de prueba procesados para la pila")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  ✓ Encolado: está al final")
        elif op == "2":
            cola.listar()
        elif op == "3":
            pasajero = cola.desencolar()
            if pasajero:
                print(f"  ✓ Desencolado: {pasajero}")
            else:
                print("  ⚠ La cola está vacía")
        elif op == "4":
            frente = cola.ver_frente()
            if frente:
                print(f"  Frente: {frente}")
            else:
                print("  ⚠ La cola está vacía")
        elif op == "5":
            num = leer_entero("  Número de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f"  ✓ Encontrado en posición [{pos}]: {cola.datos[pos]}")
            else:
                print("  ✕ Pasajero no encontrado")
        elif op == "6":
            num = leer_entero("  Número de pasajero a modificar: ")
            if cola.buscar(num) != -1:
                destino = input("  Nuevo destino: ").strip()
                asiento = input("  Nuevo asiento: ").strip().upper()
                cola.modificar(num, destino, asiento)
                print("  ✓ Datos modificados correctamente")
            else:
                print("  ✕ Pasajero no encontrado")
        elif op == "7":
            num = leer_entero("  Número de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print(f"  ✓ Pasajero #{num} eliminado correctamente")
            else:
                print("  ✕ Pasajero no encontrado o cola vacía")
        elif op == "8":
            copia = cola.copiar()
            print("  --- Copia realizada ---")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()} | ¿Está vacía?: {'Sí' if cola.esta_vacia() else 'No'}")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if cola.encolar(p):
                    cargados += 1
            print(f"  ✓ {cargados} datos de prueba procesados para la cola")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()