print ('''VERIFICADOR DE EDAD PARA VOTAR

Verifica si cumples con la edad estableci para ejercer tu voto

en cualquiera de los siguientes paises:



-Reino Unido

-Corea del sur

-Japón

-Emiratos Árabes Unidos

-Estados Unidos''')

# se explica la funcionalida de la aplicación y los paises en los cuales pueden verificar su aptitud para ejercer el voto como ciudadanos



try:

    

    print("introduce el número del país de interes")

    menu=" 1.Reino Unido \n 2.Corea del sur \n 3.Japón \n 4.Emiratos Árabes unidos \n 5.Estados Unidos \n"

    pais=input(menu)

    edad=int(input("Introduce tu edad  \n"))

    # se solicita al usuario su edad y el país de interés como datos de entrada mediante un menú



    match pais:

    #se estableceran los diferentes casos según el país a verificar

        case "1":


            if edad >= 16:

                print("actualmente eres acto para votar en Reino Unido")


            else:

                print("No tienes la edad requerida para votar")
            
                # Si la edad es mayor o igual a 18 puede votar en Reino Unido



        case "2":


            if edad >= 19:

                print("actualmente eres acto para votar en Corea del sur ")


            else:

                print("No tienes la edad requerida para votar")

                # Si la edad es mayor o igual a 18 puede votar en Corea del sur



        case "3":



            if edad >= 20:

                print("actualmente eres acto para votar en Japón ")



            else:

                print("No tienes la edad requerida para votar")

                # Si la edad es mayor o igual a 18 puede votar en Japón


        case "4":


            if edad >= 21:

                print("actualmente eres acto para votar en Emiratos Árabes Unidos ")



            else:

                print("No tienes la edad requerida para votar")

                # Si la edad es mayor o igual a 18 puede votar en Emiratos Árabes Unidos


        case "5":



            if edad >= 18:

                print("actualmente eres acto para votar en Estados Unidos ")



            else:
                
                print("No tienes la edad requerida para votar")

                # Si la edad es mayor o igual a 18 puede votar en Estados Unidos


        case _:

            print ("Error, introduce una número valido")

            #en caso de introducir un número diferente a 1,2,3,4,5

            #se imprimirá un aviso de error al usuario


except ValueError:

    print("Error: Debes ingresar un valor numérico para tu edad, no letras.")

# Este bloque captura el error si el usuario no introduce un número válido para la edad.

except Exception as e:

    print(f"Ocurrió un error inesperado: {e}")

# Este bloque genérico captura cualquier otro error no previsto y muestra su detalle.