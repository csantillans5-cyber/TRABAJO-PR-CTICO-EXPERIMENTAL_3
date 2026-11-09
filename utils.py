def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


def menu(titulo, opciones):
    print(f"\n========== {titulo} ==========")
    for opcion in opciones:
        print(f" {opcion}")
    lon = len(opciones) - 1
    op = input(f"Opción[0...{lon}]: ").strip().upper()
    return op