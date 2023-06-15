from ClaseManejaSabores import ManejaSabores
from ClaseManejadorHelados import ManejaHelados

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    maneja_sabores = ManejaSabores()
    maneja_helados = ManejaHelados()

    maneja_helados.cargar_datos_sabores(maneja_sabores)

    while True:
        print("\nMENU DE OPCIONES")
        print("1. Registrar un helado vendido")
        print("2. Mostrar los 5 sabores de helado más pedidos")
        print("3. Estimar total de gramos vendidos de un sabor")
        print("4. Mostrar sabores vendidos en un tipo de helado")
        print("5. Mostrar importe total recaudado")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_helado_vendido(maneja_helados, maneja_sabores)
    elif opcion == '2':
        mostrar_sabores_mas_pedidos(maneja_helados)
    elif opcion == '3':
        estimar_gramos_vendidos(maneja_helados)
    elif opcion == '4':
        mostrar_sabores_por_tipo_helado(maneja_helados)
    elif opcion == '5':
        mostrar_importe_total_recaudado(maneja_helados)
    elif opcion == '6':
            break
    else:
        print("Opción inválida. Intente nuevamente.")
