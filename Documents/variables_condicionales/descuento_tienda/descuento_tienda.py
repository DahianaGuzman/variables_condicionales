print('''CONVERSOR DE TEMPERATURA

Las unidades de temperatura para nuestro conversor de
temperatura son:

- para Celsius usa: C
- Para Fahrenheit usa: F
- para Kelvin usa: K \n''')
# Se dan al usuario los símbolos para implementar según el tipo de unidad

# TAREAS:
# - unidades en mayúscula y en minúscula (RESUELTO con comparaciones explícitas)
# - declarar error si introducen una letra (RESUELTO con try-except)

try:
    # Se solicita al usuario el valor de la temperatura, convirtiéndolo a entero.
    # Se usa un bloque try-except para manejar entradas no numéricas.
    temp = int(input("Introduce la temperatura "))

    # Se solicita el tipo de unidad actual y la que se desea obtener.
    # NO usamos .upper() o .lower() para que podamos verificar ambas versiones (mayúscula/minúscula)
    # explícitamente en los 'if/elif' anidados.
    actual = input("Introduce el tipo de escala actual ")
    final = input("Introduce el tipo de escala a convertir ")

    # Se establecerán los diferentes casos según la unidad actual.
    # Cada 'case' ahora verifica tanto la versión mayúscula como minúscula de la unidad.
    match actual:
        case "C" | "c": # Acepta 'C' o 'c' como unidad actual
            # La condición anterior 'final == "F" or "f"' siempre era True.
            # Ahora, verificamos explícitamente si 'final' es "F" o si 'final' es "f".
            if final == "F" or final == "f": # Acepta 'F' o 'f' como unidad final
                temp_final = temp * 9/5 + 32
                # Formato de salida con f-string y dos decimales
                print(f"{temp} C, es igual a {temp_final:.2f} F")
            # Similar a la anterior, corregida para verificar explícitamente "K" o "k".
            elif final == "K" or final == "k": # Acepta 'K' o 'k' como unidad final
                temp_final = temp + 273.15
                # Formato de salida con f-string y dos decimales
                print(f"{temp} C, es igual a {temp_final:.2f} K")
            # Manejo para unidad final inválida para Celsius
            else:
                print("Error: Unidad final no válida para la conversión desde Celsius. Usa F o K.")
        
        case "F" | "f": # Acepta 'F' o 'f' como unidad actual
            # Corregida para verificar explícitamente "C" o "c".
            if final == "C" or final == "c": # Acepta 'C' o 'c' como unidad final
                temp_final = (temp - 32) * 5/9
                # Formato de salida con f-string y dos decimales
                print(f"{temp} F, es igual a {temp_final:.2f} C")
            # Ya estaba bien en tu código, pero la incluyo para consistencia.
            elif final == "K" or final == "k": # Acepta 'K' o 'k' como unidad final
                temp_final = (temp - 32) * 5/9 + 273.15
                # Formato de salida con f-string y dos decimales
                print(f"{temp} F, es igual a {temp_final:.2f} K")
            # Manejo para unidad final inválida para Fahrenheit
            else:
                print("Error: Unidad final no válida para la conversión desde Fahrenheit. Usa C o K.")
        
        case "K" | "k": # Acepta 'K' o 'k' como unidad actual
            # Ya estaba bien en tu código, pero la incluyo para consistencia.
            if final == "C" or final == "c": # Acepta 'C' o 'c' como unidad final
                temp_final = temp - 273.15
                # Formato de salida con f-string y dos decimales
                print(f"{temp} K, es igual a {temp_final:.2f} C")
            # Ya estaba bien en tu código, pero la incluyo para consistencia.
            elif final == "F" or final == "f": # Acepta 'F' o 'f' como unidad final
                temp_final = (temp - 273.15) * 9/5 + 32
                # Formato de salida con f-string y dos decimales
                print(f"{temp} K, es igual a {temp_final:.2f} F")
            # Manejo para unidad final inválida para Kelvin
            else:
                print("Error: Unidad final no válida para la conversión desde Kelvin. Usa C o F.")
        
        case _:
            # Mensaje de error para unidad inicial inválida
            print("Error: Introduce una unidad inicial válida (C, F, K).")
            # Este mensaje se muestra cuando la unidad inicial (`actual`) ingresada
            # por el usuario no coincide con ninguna de las opciones válidas (C, F, K),
            # sin importar si está en mayúscula o minúscula.

except ValueError:
    print("Error: Debes ingresar un valor numérico para la temperatura, no letras.")
# Maneja el error si el usuario no introduce un número válido para la temperatura.
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    # Este bloque genérico captura cualquier error que no sea un ValueError,
    # como errores de lógica imprevistos o problemas del sistema.
    # Imprime el mensaje de error específico que Python genera (guardado en 'e'),
    # lo cual es crucial para la depuración y para entender por qué falló el programa.
