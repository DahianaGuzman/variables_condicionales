📚 Colección de Programas en Python
Este repositorio contiene una colección de programas sencillos escritos en Python, diseñados para realizar diversas tareas útiles. Cada programa está contenido en su propio archivo y es independiente.
🚀 ¿Cómo ejecutar los programas?
Para ejecutar cualquiera de los programas, sigue estos pasos:
Asegúrate de tener Python 3 instalado en tu sistema. Puedes descargarlo desde python.org.
Clona o descarga este repositorio a tu máquina local.
Abre tu terminal o línea de comandos (CMD en Windows, Terminal en macOS/Linux).
Navega hasta el directorio donde guardaste los archivos del programa. Por ejemplo, si los tienes en una carpeta llamada mis_programas_python en tu escritorio:
cd Desktop/mis_programas_python


Una vez en el directorio correcto, ejecuta el programa deseado usando el comando python seguido del nombre del archivo .py. Por ejemplo:
python calculadora_aritmetica.py


o
python conversor_temperatura.py


y así sucesivamente para cada programa.
1. ➕ Calculadora Aritmética
Este programa es una calculadora básica que realiza sumas, restas, multiplicaciones y divisiones entre dos números.
📝 Instrucciones de Uso:
El programa te pedirá que introduzcas el primer número, el símbolo de la operación (+, -, *, /) y el segundo número.
⌨️ Ejemplos de Uso:
Entrada (Primer Valor, Operación, Segundo Valor)
Salida en Consola
10, +, 5
El resultado es 15
20, -, 8
El resultado es 12
4, *, 3
El resultado es 12
15, /, 3
El resultado es 5.0

⚠️ Posibles Errores y Manejo:
Entrada no numérica (ValueError): Si introduces letras o cualquier carácter no numérico en lugar de números, el programa mostrará: Error: Debes ingresar valores numéricos, no letras.
División por Cero: Si intentas dividir entre 0, el programa indicará: Error, ingresa un valor diferente a cero.
Operación No Válida: Si el carácter de la operación no es +, -, * o /, obtendrás: Error, introduce una operación valida.
Errores Inesperados: Se incluye un manejo genérico para cualquier otro error imprevisto.
2. 🌡️ Conversor de Temperatura
Este programa convierte temperaturas entre las escalas Celsius, Fahrenheit y Kelvin.
📝 Instrucciones de Uso:
Introduce el valor numérico de la temperatura, la unidad actual (C, F, K) y la unidad a la que deseas convertir. El programa ahora acepta tanto mayúsculas como minúsculas para las unidades.
⌨️ Ejemplos de Uso:
Entrada (Temperatura, Actual, Final)
Salida en Consola
0, C, F
0 C, es igual a 32.00 F
100, c, K
100 C, es igual a 373.15 K
32, F, c
32 F, es igual a 0.00 C
273.15, k, C
273.15 K, es igual a 0.00 C
23, c, k
23 C, es igual a 296.15 K
23, c, x
Error: Unidad final no válida para la conversión desde Celsius. Usa F o K.

⚠️ Posibles Errores y Manejo:
Entrada no numérica (ValueError): Si introduces letras o cualquier carácter no numérico en lugar de números para la temperatura, el programa mostrará: Error: Debes ingresar un valor numérico para la temperatura, no letras.
Unidad inicial no válida: Si la unidad inicial (actual) no es C, F o K (en mayúsculas o minúsculas), el programa mostrará: Error: Introduce una unidad inicial válida (C, F, K).
Unidad final no válida: Si la unidad final (final) no es válida para la conversión desde la unidad inicial seleccionada (por ejemplo, intentas convertir de Celsius a una unidad que no sea Fahrenheit o Kelvin), el programa mostrará un mensaje específico como Error: Unidad final no válida para la conversión desde Celsius. Usa F o K.
Errores Inesperados: Se incluye un manejo genérico para cualquier otro error imprevisto, mostrando el detalle del error.



3. 🗳️ Verificador de Edad para Votar
Este programa te permite verificar si cumples con la edad mínima para votar en varios países predefinidos. Ha sido mejorado para manejar correctamente las entradas de usuario, incluyendo valores no numéricos.
📝 Instrucciones de Uso:
El programa te presentará un menú numerado de países. Introduce el número correspondiente al país de interés (como una cadena, por ejemplo, "1", "2") y luego introduce tu edad. El programa validará que las entradas sean numéricas donde se esperan números.
⌨️ Ejemplos de Uso:
Entrada (País, Edad)
Salida en Consola
3, 22
actualmente eres acto para votar en Japón
1, 17
No tienes la edad requerida para votar
5, 18
actualmente eres acto para votar en Estados Unidos
2, diecinueve
Error: Debes ingresar un valor numérico para tu edad, no letras.
6, 30
Error, introduce una número valido
abc, 25
Error, introduce una número valido

⚠️ Posibles Errores y Manejo:
Entrada no numérica para la edad (ValueError): Si introduces letras o cualquier carácter no numérico cuando se te pide la edad, el programa mostrará: Error: Debes ingresar un valor numérico para tu edad, no letras.
Número de país no válido: Si introduces un número que no está en el menú ("1" a "5"), o si introduces letras/caracteres al elegir el país, el programa mostrará: Error, introduce una número valido. Esto se debe a que la entrada para el país se compara como una cadena.
Errores Inesperados (Exception): Se incluye un manejo genérico de excepciones para atrapar cualquier otro tipo de error no previsto, mostrando el detalle del error para ayudar en la depuración.


4. 💸 Calculadora de Descuentos
Este programa calcula el precio final de una compra aplicando descuentos basados en el monto total y si el cliente tiene una tarjeta de fidelidad. Ha sido actualizado para manejar mejor las entradas y los escenarios de descuento.
📝 Instrucciones de Uso:
Introduce el valor numérico de tu compra. Luego, indica si tienes tarjeta de fidelidad ingresando "1" para Sí o "2" para No.
⌨️ Ejemplos de Uso:
Entrada (Precio, Tarjeta Fidelidad)
Salida en Consola
120000, 1
EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: 91200.0 (15% + 5% adic.)
75000, 2
EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: 67500.0 (10%)
30000, 1
EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: 28500.0 (5% + 5% adic.)
7000, 2
Error, valor invalido
7000, 1
EL PRECIO FINAL CON NUESTROS SÚPER DESCUENTOS ES: 6650.0 (0% base + 5% adic.)
abc, 1
Error: Debes ingresar un valor numérico para el precio de tu compra, no letras.
0, 2
Error, valor invalido

⚠️ Posibles Errores y Manejo:
Entrada no numérica (ValueError): Si introduces letras o cualquier carácter no numérico cuando se te pide el precio de la compra, el programa mostrará: Error: Debes ingresar un valor numérico para el precio de tu compra, no letras.
Precio Inválido:
Si el precio ingresado es menor o igual a $0, o si está en el rango de $1 a $9,999, el programa considera que no aplica para un descuento base por monto y mostrará: Error, valor invalido.
Nota: En el rango de $1 a $9,999, aunque no hay un descuento base, el descuento por tarjeta de fidelidad sí se aplicará si el usuario lo selecciona, y el precio final reflejará solo ese descuento.
Opción de Tarjeta de Fidelidad no válida: Si introduces un valor diferente a "1" o "2" para la tarjeta de fidelidad, el programa no aplicará el descuento de fidelidad y solo mostrará el precio final calculado con el descuento base (o sin descuento base si no aplicaba). No se muestra un mensaje de error específico para esta entrada.
Errores Inesperados (Exception): Se incluye un manejo genérico de excepciones para atrapar cualquier otro tipo de error no previsto, mostrando el detalle del error para ayudar en la depuración.
