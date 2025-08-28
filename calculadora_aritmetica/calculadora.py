print ('''CALCULADORA ARITMÉRICA 


Ten en cuenta la siguiente información para usar nuestra

calculadora aritmetica:


- para realizar una suma usa: +

- para realizar una resta usa: -

- para realizar una multiplicación usa: * 

- para realizar una división usa: / \n''')

# se dan las pautas de las operaciones validas



""" TAREAS:
#declarar error si introducen una letra
"""

try:

    valor1=int(input("Introduce el primer valor  "))

    operacion=input("Introduce el tipo de operación  ")

    valor2=int(input("Introduce el segundo valor  "))

    # se solicita al usuario los valores a operar y el tipo de operadción que desea realizar



    match operacion:

    #se estableceran los diferentes casos según la operacion a realizar

    #es decir, el valor introducido en la variable operacion

        case "+":

            suma= valor1 + valor2

            print("El resultado es", suma)

            #primer caso: si la operación a realizar es una suma

            #se suman ambos valores y se da al usuario el resultado

        case "-":

            resta= valor1 - valor2

            print("El resultado es", resta)

            #segundo caso: si la operación a realizar es una resta

            # se restan ambos valores y se imprime el resultado

        case "*":

            multiplicacion= valor1 * valor2

            print("El resultado es", multiplicacion)

            #tercer caso: si la operacion deseada es una multiplicación

            # se multiplican ambos valores y se da el resultado

        case "/":

            if valor1== 0 or valor2==0:

                print ("Error, ingresa un valor diferente a cero")

                #se verifica de ambos valores sean diferentes a cero

                #sino se imprimirá un aviso de error


            else:

                division= valor1 / valor2

                print("El resultado es", division)

                #cuarto caso: si se desea realizar una división

                #se divide ambos valores y se imprimirá el resultado


        case _:

            print ("Error, introduce una operación valida")

            #en caso de introducir un operador diferente a +,-,*,/

            #se imprimira un aviso de error al usuario


except ValueError: 
    print("Error: Debes ingresar valores numéricos, no letras.") 

    # Maneja el error si el usuario no introduce un número válido.

except exception as e: 
    print(f"Ocurrió un error inesperado: {e}")

    # Captura cualquier otro error no previsto para evitar que el programa se detenga