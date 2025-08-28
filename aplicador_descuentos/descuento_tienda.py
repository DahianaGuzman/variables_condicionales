print ('''CALCULADORA DE DESCUENTOS\n

Conoce aquí los increibles descuestos de tu compra según nuestra promociones\n''')

# se da al usuario los simbolos para implementar según el tipo de unidad


try:

    precio=int(input("Ingresa el valor de tu compra:"))

    print("¿Tienes tarjeta de fidelidad con nosotros?")

    menu=" 1.Si \n 2.No \n"

    print("Ingresa 1 o 2 ")

    tarjeta_fidelidad=input(menu)

    # se solicita al usuario el valor de su compra y se confirma si cuenta con tarjeta de fidelidad

    descuento = 0.0

    # se incia descuento, para evitar un error si el precio de la compra es menor que 10.000 ( se le aplicará un 0% de descuento)

    #se estableceran los diferentes casos según el total

    if precio > 100000:

        descuento= 0.15

    #Si el precio es mayor a $100,000, aplicar 15% de descuento

    elif precio >= 50000 and precio <= 100000:

        descuento= 0.10

        #Si el precio está entre $50,000 y $100,000, aplicar 10% de descuento

    elif precio >= 10000 and precio <=49999:

        descuento= 0.05

        #Si el precio está entre $10,000 y $49,999, aplicar 5% de descuento

    else:

        print("Error, valor invalido")

        #Si el usuario establece un valor de entrada invalido

    precio_final = precio - (precio * descuento)

    #se calcula el precio final con el descuento valido

    if tarjeta_fidelidad == "1":

        descuento_fidelidad= 0.05

        precio_final_fidelidad= precio_final - (precio_final * descuento_fidelidad)

        print(" EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES:", precio_final_fidelidad)

        #Se agraga el descuento adicional de tarjeta de fidelidad si aplica         



    elif tarjeta_fidelidad == "2":

        print(" EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES:", precio_final)

        #Si no aplica el descuento por tarjeta de fidelidad, solo se imprime el precio_final (solo con el primer descuento)  

except ValueError:

    print("Error: Debes ingresar un valor numérico para el precio de tu compra, no letras.")
    
    # Este bloque captura el error si el usuario no introduce un número válido para el precio.

except Exception as e:

    print(f"Ocurrió un error inesperado: {e}")
    #captura otros errores