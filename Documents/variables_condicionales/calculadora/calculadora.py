print('''CALCULADORA DE DESCUENTOS

Conoce aquí los increíbles descuentos de tu compra según nuestras promociones\n''')
# Se explica la funcionalidad de la aplicación.

try:
    precio = int(input("Ingresa el valor de tu compra:"))
    print("¿Tienes tarjeta de fidelidad con nosotros?")

    menu = " 1.Si \n 2.No \n"
    print("Ingresa 1 o 2 ")
    tarjeta_fidelidad = input(menu)
# Se solicita al usuario el valor de su compra y se confirma si cuenta con tarjeta de fidelidad

    descuento = 0.0
# Se inicializa el descuento. Esto es clave para evitar errores si no se cumple ninguna condición de descuento.

# Se establecerán los diferentes casos según el total de la compra para el descuento base.
    if precio > 100000:
        descuento = 0.15
# Si el precio es mayor a $100,000, aplicar 15% de descuento.
        
    elif precio >= 50000 and precio <= 100000:
        descuento = 0.10
# Si el precio está entre $50,000 y $100,000, aplicar 10% de descuento.
        
    elif precio >= 10000 and precio <= 49999:
        descuento = 0.05
# Si el precio está entre $10,000 y $49,999, aplicar 5% de descuento.

    elif precio > 0 and precio < 10000:
        descuento = 0.0
        # Eliminamos el mensaje "Tu valor de compra no aplica para el descuento" de aquí.
        # Esto evita la confusión si luego aplica el descuento de fidelidad.
# Si el precio es mayor que 0 y menor que 10000, se aplica el 0% de descuento base por monto.

    else:
        # Este 'else' ahora solo se activa si el precio es 0 o negativo, que son valores inválidos.
        print("Error: El valor de tu compra es inválido (debe ser mayor a 0).")
        descuento = 0.0 # Aseguramos que descuento tenga un valor.
        precio = 0 # Forzamos el precio a 0 para que no se intente calcular el precio final si es inválido.
# Si el usuario establece un valor de entrada inválido (0 o negativo).


    # Solo calcula el precio final y aplica descuentos adicionales si el precio inicial fue válido (mayor que 0).
    if precio > 0:
        precio_final = precio - (precio * descuento)
    # Se calcula el precio final con el descuento base.

        if tarjeta_fidelidad == "1":
            descuento_fidelidad = 0.05
            precio_final_fidelidad = precio_final - (precio_final * descuento_fidelidad)
            # Este print está AHORA CORRECTAMENTE INDENTADO dentro del 'if'.
            print(f"EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: ${precio_final_fidelidad:,.2f}")
    # Se agrega el descuento adicional de tarjeta de fidelidad si aplica.
            
        elif tarjeta_fidelidad == "2":
            # Este 'elif' ahora es válido y su 'print' está correctamente indentado.
            print(f"EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: ${precio_final:,.2f}")
    # Si no aplica el descuento por tarjeta de fidelidad, solo se imprime el precio_final (solo con el primer descuento).
        else:
            # Este 'else' maneja entradas de tarjeta de fidelidad que no son "1" ni "2".
            print("Error: Opción de tarjeta de fidelidad no válida. Se aplicará solo el descuento base.")
            print(f"EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: ${precio_final:,.2f}")
    else:
        # Este mensaje se mostrará si el precio inicial fue 0 o negativo.
        print("No se pudo calcular el precio final debido a un valor de compra no válido (menor o igual a cero).")


except ValueError:
    print("Error: Debes ingresar un valor numérico para el precio de tu compra, no letras.")
# Este bloque captura el error si el usuario no introduce un número válido para el precio.


except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
# Captura otros errores inesperados.
