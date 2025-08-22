print('''VERIFICADOR DE EDAD PARA VOTAR
Verifica si cumples con la edad estableci para ejercer tu voto
en cualquiera de los siguientes paises:

-Reino Unido
-Corea del sur
-Japón
-Emiratos Árabes Unidos
-Estados Unidos''')
# Se explica la funcionalidad de la aplicación y los paises en los cuales pueden verificar su aptitud para ejercer el voto como ciudadanos

# ---- INICIO DEL BLOQUE TRY-EXCEPT PRINCIPAL ----
try:
    print("introduce el número del país de interes")
    menu=" 1.Reino Unido \n 2.Corea del sur \n 3.Japón \n 4.Emiratos Árabes unidos \n 5.Estados Unidos \n"
    
    # CAMBIO CRUCIAL: 'pais' almacena la entrada como una CADENA.
    # Por ejemplo, si el usuario escribe '3', pais será la cadena "3".
    pais=input(menu) 
    
    # Intenta convertir la edad a entero. Si se introduce una letra (como 'D'),
    # aquí se generará un ValueError y el programa saltará al 'except ValueError'.
    edad=int(input("Introduce tu edad \n"))
    # Se solicita al usuario su edad y el país de interés como datos de entrada mediante un menú

    match pais:
    # Se establecerán los diferentes casos según el país a verificar.
    # Los 'case' ahora comparan con CADENAS DE TEXTO para que coincidan con la entrada de 'pais'.

        case "1": # CAMBIO: Compara con la cadena "1"
            if edad >= 16: # Nota: La edad para votar en RU es 18, si deseas la real, cambia este valor.
                print("Actualmente eres apto para votar en Reino Unido.") # Mejorado el mensaje
            else: # CORRECCIÓN: 'else' siempre lleva dos puntos.
                print("No tienes la edad requerida para votar en Reino Unido.") # Mejorado el mensaje
            # Si la edad es mayor o igual a 16 puede votar en Reino Unido (según tu código).

        case "2": # CAMBIO: Compara con la cadena "2"
            if edad >= 19:
                print("Actualmente eres apto para votar en Corea del Sur.") # Mejorado el mensaje
            else: # CORRECCIÓN: 'else' siempre lleva dos puntos.
                print("No tienes la edad requerida para votar en Corea del Sur.") # Mejorado el mensaje
            # Si la edad es mayor o igual a 19 puede votar en Corea del Sur.
            
        case "3": # CAMBIO: Compara con la cadena "3"
            if edad >= 20:
                print("Actualmente eres apto para votar en Japón.") # Mejorado el mensaje
            else: # CORRECCIÓN: 'else' siempre lleva dos puntos.
                print("No tienes la edad requerida para votar en Japón.") # Mejorado el mensaje
            # Si la edad es mayor o igual a 20 puede votar en Japón.
            
        case "4": # CAMBIO: Compara con la cadena "4"
            if edad >= 21:
                print("Actualmente eres apto para votar en Emiratos Árabes Unidos.") # Mejorado el mensaje
            else: # CORRECCIÓN: 'else' siempre lleva dos puntos.
                print("No tienes la edad requerida para votar en Emiratos Árabes Unidos.") # Mejorado el mensaje
            # Si la edad es mayor o igual a 21 puede votar en Emiratos Árabes Unidos.
            
        case "5": # CAMBIO: Compara con la cadena "5"
            if edad >= 18:
                print("Actualmente eres apto para votar en Estados Unidos.") # CORRECCIÓN: Mensaje a "Estados Unidos".
            else: # CORRECCIÓN: 'else' siempre lleva dos puntos.
                print("No tienes la edad requerida para votar en Estados Unidos.") # Mejorado el mensaje
            # Si la edad es mayor o igual a 18 puede votar en Estados Unidos.

        case _:
            # Este caso se ejecuta si el usuario introduce un valor que no es "1", "2", "3", "4", "5"
            # (por ejemplo, "6" o "abc").
            print ("Error: Introduce un número válido para el país (1-5).") # Mensaje más claro
            # Se imprimirá un aviso de error al usuario.

# ---- MANEJO DE ERRORES ESPECÍFICOS ----
except ValueError:
    # Este bloque se ejecutará si 'int(input("Introduce tu edad"))' falla,
    # es decir, si el usuario introduce algo que no es un número para la edad.
    print("Error: Debes ingresar un valor numérico para tu edad, no letras.")
# Este bloque captura el error si el usuario no introduce un número válido para la edad.

# ---- MANEJO DE ERRORES GENERALES ----
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    # Este bloque genérico captura cualquier otro error no previsto y muestra su detalle,
    # lo cual es crucial para la depuración y para entender por qué falló el programa.
