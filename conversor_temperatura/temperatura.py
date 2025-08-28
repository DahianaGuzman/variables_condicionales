print ('''CONVERSOR DE TEMPERATURA



Las unidades de temperatura para nuestro conversor de

temperatura son:



- para Celsius usa: C

- Para Fahrenheit usa: F

- para Kelvin usa: k \n''')

# se da al usuario los simbolos para implementar según el tipo de unidad

""" TAREAS:
# unidades en mayuscula y en minuscula
"""

try:

    temp=int(input("Introduce la temperatura  "))

    actual=input("Introduce el tipo de escala actual ")

    final=input("Introduce el tipo de escala a convertir  ")

    # se solicita al usuario el valor de la temperatura, el tipo de unidad actual y la que se desea obtener


    match actual:

    #se estableceran los diferentes casos según la unidad actual

    #se procesan todas las conversiones y se imprime solo la que el usuario solicite

        case "C"| "c":


            if final == "F" or final=="f":

                temp_final=temp * 9/5 + 32

                print(temp, "C, es igual a ", temp_final, "F")

                # Si la unidad actual es C y la unidad final es F.


            elif final == "K" or "k":

                temp_final= temp + 273.15

                print( temp,"C, es igual a ", temp_final, "K")

                # Si la unidad actual es C y la final es K.

        case "F"|"f":


            if final == "C" or "c":

                temp_final=(temp - 32) * 5/9

                print( temp,"F, es igual a ", temp_final, "C")

                #Si la unidad actual es F y la final es C.


            elif final == "K" or final=="k":

                temp_final=(temp - 32) * 5/9 + 273.15

                print( temp,"F, es igual a ", temp_final, "K")

                #Si la unidad actual es F y la final es K.


        case "K"|"k":


            if final == "C" or final=="c":

                temp_final= temp - 273.15

                print( temp,"k, es igual a ", temp_final, "C")

                # Si la unidad actual es K y la final C.


            elif final == "F" or final=="f":

                temp_final=(temp - 273.15) * 9/5 + 32

                print( temp,"K, es igual a ", temp_final, "F")

                # Si la unidad actual es K y la final F.


        case _:

            print ("Error, introduce una unidad valida")

            print("Introduce la unidad en mayúscula")

            #en caso de introducir un unidad diferente a C,K,F 

            #se imprimira un aviso de error al usuario



except ValueError:

    print("Error: Debes ingresar un valor numérico para la temperatura, no letras.")

    # Captura cualquier otro error no previsto para evitar que el programa se detenga.

except Exception as e:

    print(f"Ocurrió un error inesperado: {e}")

    # Este bloque genérico captura cualquier error que no sea un ValueError