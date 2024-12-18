## 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario 
## con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

def frecuencias(cadena):

    # Creo un diccionario para almacenar las frecuencias
    frecuencias = {}

    # Cadena ignorando los espacios
    for letra in cadena.replace(" ", ""):
        frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias

cadena_texto = "Katas Python"
print(frecuencias(cadena_texto))


## 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()

lista_numeros = [1, 2, 3, 4, 5]

lista_duplicados = list(map(lambda x: x * 2, lista_numeros))
print(f'Lista duplicada: {lista_duplicados}')


## 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. 
## La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

palabras = ["puerta", "pueril", "purga", "puerto", "pulga"]
objetivo = "pue"

print(f'Palabras que contienen {objetivo}: {filtrar_palabras(palabras, objetivo)}')


## 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencia(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

lista_a = [10, 20, 30, 40]
lista_b = [7, 14, 21, 28]
print(f'Diferencia entre listas: {calcular_diferencia(lista_a, lista_b)}')


## 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. 
# La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. 
# Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.

def calcular_media(lista_numeros, nota_aprobado=5):

    suma_notas = 0
    for numero in lista_numeros:
        suma_notas += numero
    
    media = round(suma_notas / len(lista_numeros), 2)

    if media >= nota_aprobado:
        return media, "aprobado"
    else:
        return media, "suspenso"

numeros = [ 7, 5, 8, 4, 10, 9]
print(f'La media y el estado son: {calcular_media(numeros, 5)}')


## 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
   
    if numero == 0 or numero == 1:  
        return 1
    return numero * factorial(numero - 1)  # Llamada recursiva

numero = 7
print(f'El factorial de {numero} es: {factorial(numero)}')


## 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: str(tupla), lista_tuplas))

tuplas = [(1, 2), (3, 4), (5, 6)]
print(tuplas_a_strings(tuplas))


## 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor 
# no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. 
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_numeros():

    num1 = input("Ingresa el primer número: ")

    # Verificar si el primer número es numérico
    if not num1.replace('.', '', 1).isdigit():
        print("Error: Por favor, ingresa un número válido.")
        return  

    num2 = input("Ingresa el segundo número: ")

    # Verificar si el segundo número es numérico
    if not num2.replace('.', '', 1).isdigit():
        print("Error: Por favor, ingresa un número válido.")
        return  

    # Convertir los valores a float
    num1 = float(num1)
    num2 = float(num2)

    if num2 == 0:
        print("Error: No se puede dividir por cero. Anota otro número.")
    else:
        resultado = num1 / num2
        print(f"La división fue exitosa. El resultado es: {resultado}")

dividir_numeros()


## 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una 
# nueva lista excluyendo ciertas mascotas prohibidas en España. 
# La lista de mascotas a excluir es ["Mapache","Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter() 

def mascotas(lista_mascotas):
    
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    
    mascotas_permitidas = filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas)
 
    return list(mascotas_permitidas)

animales = ["Pantera", "Oso", "Mapache", "Tigre", "Alpaca", "Cocodrilo", "Serpiente Pitón"]

print(mascotas(animales))


## 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, 
# lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(numeros):
   
    if len(numeros) == 0:
        print('Error: La lista está vacía. No se puede calcular el promedio.')
        return None  
    
    # Calcular el promedio
    promedio = sum(numeros) / len(numeros)
    return promedio

lista = [7, 22, 94, 48, 12] 
promedio = calcular_promedio(lista)

if promedio is not None: 
    print(f'El promedio es: {promedio}')


## 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico
#  o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def Anotar_edad():
    # Pedir al usuario que introduzca su edad
    edad = input('Introduce tu edad: ')

    # Verificar si el valor anotado es numérico
    if not edad.isdigit():
        print('Error: Por favor, introduce un número válido.')
        return  

    edad = int(edad)

    if edad < 0 or edad > 120:
        print('Error: La edad debe estar entre 0 y 120.')
        
    else:
        print(f'Edad válida: {edad} años.')

Anotar_edad()


## 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitud_palabra(frase):

    # Se divide la frase en palabras
    palabras = frase.split()
    
    longitud = map(len, palabras)
    return list(longitud)

frase = 'Resolución de las katas de Python'
print(longitud_palabra(frase))


## 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
#  mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()

def lista_tuplas(conjunto_caracteres):

    conjunto_unico = set(conjunto_caracteres)  

    resultado = list(map(lambda c: (c.upper(), c.lower()), conjunto_unico))
    return resultado

conjunto = 'MurCIelaGo'
print(lista_tuplas(conjunto))


## 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()

def filtro_palabras(palabras, letra):
  
    palabras_filtradas = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))
    
    return (palabras_filtradas)

lista_palabras = ['fútbol', 'tenis', 'golf', 'badminton', 'baloncesto', 'voleyball']
letra_especifica = 'b'

print(filtro_palabras(lista_palabras, letra_especifica))


## 15. Crea una función lambda que sume 3 a cada número de una lista dada.

def sumar_tres(lista):
   
    return list(map(lambda x: x + 3, lista))

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sumar_tres(lista_numeros))


## 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista 
# de todas las palabras que sean más largas que n. Usa la función filter()

def palabras_largas(texto, entero):

    palabras = texto.split()
    
    palabras_filtradas = list(filter(lambda palabra: len(palabra) > entero, palabras))
    return (palabras_filtradas)

cadena_texto = 'Resolución de las katas de Python'
numero = 7

print(palabras_largas(cadena_texto, numero))


## 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] 
# corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_digitos(digitos):
    
    numero = reduce(lambda x, y: x * 10 + y, digitos)
    return numero

lista_numeros = [5, 7, 2, 8, 0]
print(lista_digitos(lista_numeros))


## 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor
# o igual a 90. Usa la función filter()

def estudiantes_aprobados(estudiantes):
 
    aprobados = list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))
    return (aprobados)

estudiantes = [ {'nombre': 'Jorge', 'edad': 24, 'calificacion': 85},
                {'nombre': 'Anabel', 'edad': 22, 'calificacion': 87},
                {'nombre': 'Carlos', 'edad': 20, 'calificacion': 92},
                {'nombre': 'Mercedes', 'edad': 23, 'calificacion': 80},
                {'nombre': 'Isabel', 'edad': 21, 'calificacion': 93}]

print(estudiantes_aprobados(estudiantes))


## 19. Crea una función lambda que filtre los números impares de una lista dada.

def impares(lista):
  
    return list(filter(lambda x: x % 2 != 0, lista))

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(impares(lista_numeros))


## 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

def valores_enteros(lista):
   
    return list(filter(lambda x: isinstance(x, int), lista))

elementos = [1, 'perro', 14, 235, 'leopardo', 77]
print(valores_enteros(elementos))


## 21. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor
# o igual a 90. Usa la función filter()

def estudiantes_aprobados(estudiantes):
 
    aprobados = list(filter(lambda estudiante: estudiante['calificacion'] >= 90, estudiantes))
    return (aprobados)

estudiantes = [ {'nombre': 'Jorge', 'edad': 24, 'calificacion': 85},
                {'nombre': 'Anabel', 'edad': 22, 'calificacion': 87},
                {'nombre': 'Carlos', 'edad': 20, 'calificacion': 92},
                {'nombre': 'Mercedes', 'edad': 23, 'calificacion': 80},
                {'nombre': 'Isabel', 'edad': 21, 'calificacion': 93}]

print(estudiantes_aprobados(estudiantes))


## 22. Crea una función que calcule el cubo de un número dado mediante una función lambda.

def calcular_cubo(x):
  
    cubo = lambda x: x ** 3
    return cubo(x)

numero = 5
print (calcular_cubo(numero))


## 23. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce() 

from functools import reduce

def producto_total(lista):

    return reduce(lambda x, y: x * y, lista)

numeros = [2, 3, 5, 9]
print(producto_total(numeros))


## 24. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce

def concatenar_palabras(lista):
    
    return reduce(lambda x, y: x + y, lista)

palabras = ['Solución', ' ', 'katas',' ', 'Python']
print(concatenar_palabras(palabras))

## 25. Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

def diferencia_total(lista):

    return reduce(lambda x, y: x - y, lista)

valores = [90, 10, 13, 17]
print(diferencia_total(valores))


## 26. Crea una función que cuente el número de caracteres en una cadena de texto dada.

def numero_caracteres(texto):
    return len(texto)

cadena_texto = 'Resolución de katas de Python'
print(numero_caracteres(cadena_texto))


## 27. Crea una función lambda que calcule el resto de la división entre dos números dados.

def resto_division (x, y):
    return (lambda a, b: a % b)(x, y)

numero1 = 27
numero2 = 5

print(resto_division(numero1, numero2))


## 28. Crea una función que calcule el promedio de una lista de números.

def promedio(lista):
    
    return sum(lista) / len(lista)

lista_numeros = [10, 7, 48, 97, 102]
print(promedio(lista_numeros))


## 29. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
  
  vistos = set()

  for elemento in lista:
    if elemento in vistos:
      return elemento
    vistos.add(elemento)
  return None

lista_numeros = [1, 12, 8, 57, 514, 12, 1457, 4583]
print(primer_duplicado(lista_numeros))


## 30. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el 
# carácter '#', excepto los últimos cuatro.

def enmascarar(variable):

    # Convertir la variable a texto
    texto = str(variable)  

    if len(texto) <= 4:
        return texto  
    return "#" * (len(texto) - 4) + texto[-4:]

variable = "katas python"
print(enmascarar(variable))


## 31. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las
#  mismas letras pero en diferente orden.

def anagramas(palabra1, palabra2):
  
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

palabra1 = "Roma"
palabra2 = "Amor"

if anagramas(palabra1, palabra2):
  print("Las palabras son anagramas")
  
else:
  print("Las palabras no son anagramas")


## 32. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar
#  en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, 
# de lo contrario, se lanza una excepción.

def buscar_nombre():

  nombres = input("Ingrese una lista de nombres: ").split(',')
  nombre_a_buscar = input("Ingrese el nombre a buscar: ")

  if nombre_a_buscar in nombres:
    print(f"El nombre {nombre_a_buscar} fue encontrado.")

  else:
    print(f"El nombre {nombre_a_buscar} no se encuentra en la lista.")

buscar_nombre()


## 33. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve
#  el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre_completo, empleados):
 
    for empleado in empleados:
        if empleado['nombre'] == nombre_completo:
            return f"{nombre_completo} trabaja aquí como {empleado['puesto']}."
    
    return f"{nombre_completo} no trabaja aquí."

empleados = [{'nombre': 'David Albares', 'puesto': 'Economista'},
            {'nombre': 'Lucía Sanz', 'puesto': 'Analista'},
            {'nombre': 'Alfredo Corleone', 'puesto': 'Director Ejecutivo'}]

nombre_completo = input("Ingrese el nombre completo del empleado: ")
print(buscar_empleado(nombre_completo, empleados))


## 34. Crea una función lambda que sume elementos correspondientes de dos listas dadas.

def sumar_listas(lista1, lista2):

    return list(map(lambda x, y: x + y, lista1, lista2))

lista1 = [10, 21, 84, 154]
lista2 = [15, 154, 41, 81]

print (sumar_listas(lista1, lista2))


## 35. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
# crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol . El objetivo es implementar estos
# métodos para manipular la estructura del árbol.

# Código a seguir:
#1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
#6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.

#Caso de uso:
#1. Crear un árbol.
#2. Hacer crecer el tronco del árbol una unidad.
#3. Añadir una nueva rama al árbol.
#4. Hacer crecer todas las ramas del árbol una unidad.
#5. Añadir dos nuevas ramas al árbol.
#6. Retirar la rama situada en la posición 2.
#7. Obtener información sobre el árbol.

class Arbol:
    def __init__(self):
        self.tronco = 1  # El tronco tiene una longitud inicial de 1.
        self.ramas = []  # Lista vacía de ramas.
    
    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1
    
    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1 a la lista de ramas."""
        self.ramas.append(1)
    
    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas existentes."""
        self.ramas = [rama + 1 for rama in self.ramas]
    
    def quitar_rama(self, posicion):
        """Elimina una rama en una posición específica."""
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("Posición de rama inválida.")
    
    def info_arbol(self):
        """Devuelve información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas."""
        print(f'Longitud del tronco: {self.tronco}')
        print(f'Número de ramas: {len(self.ramas)}')
        print(f'Longitudes de las ramas: {self.ramas}')

mi_arbol = Arbol()          # Crear un árbol
mi_arbol.crecer_tronco()    # Hacer crecer el tronco una unidad
mi_arbol.nueva_rama()       # Añadir una nueva rama
mi_arbol.crecer_ramas()     # Hacer crecer todas las ramas una unidad
mi_arbol.nueva_rama()       # Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)     # Retirar la rama en la posición 2
mi_arbol.info_arbol()       # Información sobre el árbol


## 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.

#Código a seguir:
#1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
#2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
#3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
    # Lanzará un error en caso de no poder hacerse.
#4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.

# Caso de uso:
#1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#2. Agregar 20 unidades de saldo de "Alicia".
#3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
#4. Retirar 50 unidades de saldo a "Alicia".

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
      
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
      
        if cantidad > self.saldo:
            return (f'{self.nombre} no tiene suficiente saldo para retirar {cantidad}.')
        self.saldo -= cantidad
        return (f'{self.nombre} retiró {cantidad} unidades. Saldo actual: {self.saldo}.')

    def transferir_dinero(self, otro_usuario, cantidad):
      
        if cantidad > otro_usuario.saldo:
            return(f'{otro_usuario.nombre} no tiene suficiente saldo para transferir {cantidad}.')
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        return(f'{self.nombre} recibió {cantidad} unidades de {otro_usuario.nombre}. Saldo actual: {self.saldo}.')

    def agregar_dinero(self, cantidad):
       
        self.saldo += cantidad
        return(f'{self.nombre} agregó {cantidad} unidades. Saldo actual: {self.saldo}.')

cliente1 = UsuarioBanco("Alicia", 100, True)
cliente2 = UsuarioBanco("Bob", 50, True)

print(cliente1.agregar_dinero(20))               # Agregar 20 unidades al saldo de Alicia
print(cliente1.transferir_dinero(cliente2, 80))  # Hacer una transferencia de 80 unidades desde Bob a Alicia
print(cliente1.retirar_dinero(50))               # Retirar 50 unidades del saldo de Alicia


## 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras, 
# eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .

# Código a seguir:
#1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
#2. Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva . 
   # Tiene que devolver el texto con el reemplazo de palabras.
#3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#4. Crear la función procesar_texto que tome un texto, una opción(entre"contar", "reemplazar", "eliminar") y un número de argumentos
   # variable según la opción indicada.

# Caso de uso:
# Comprueba el funcionamiento completo de la función procesar_texto.

def contar_palabras(texto):

    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        contador[palabra] = contador.get(palabra, 0) + 1
    return contador

def reemplazar_palabras(texto, palabra_inicial, palabra_nueva):
    return texto.replace(palabra_inicial, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    
    palabras = texto.split()
    resultado = ' '.join([palabra for palabra in palabras if palabra.strip(".,!?") != palabra_a_eliminar])
    return resultado

def procesar_texto(texto, opcion, *args):

    if opcion == 'contar':
        return contar_palabras(texto)
    elif opcion == 'reemplazar':
        if len(args) != 2:
            raise ValueError('La opción reemplazar requiere dos argumentos adicionales.')
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == 'eliminar':
        if len(args) != 1:
            raise ValueError('Se necesita un argumento para la opción eliminar: palabra_a_eliminar.')
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError('Opción inválida. Las opciones válidas son: contar, reemplazar y eliminar.')

texto = 'En todo caso había un solo túnel, oscuro y solitario: el mío, el túnel en el que había transcurrido mi infancia, mi juventud, toda mi vida'

print('Conteo de palabras:')
print(procesar_texto(texto, 'contar'))

print('\nReemplazar palabras:')
print(procesar_texto(texto, 'reemplazar', 'túnel', 'abismo'))

print('\nEliminar palabra:')
print(procesar_texto(texto, 'eliminar', 'túnel'))


## 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario. 

def momento_del_dia(hora):
  
    if hora < 0 or hora > 23:
        return 'La hora ingresada no es válida. Por favor, ingresa una hora entre 0 y 23.'
    if 6 <= hora < 12:
        return 'Es de día.'
    elif 12 <= hora < 18:
        return 'Es de tarde.'
    elif (18 <= hora <= 23) or (0 <= hora < 6):
        return 'Es de noche.'

hora = int(input('Ingrese la hora (en formato 24 horas): '))
print(momento_del_dia(hora))


## 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
# Las reglas de calificación son:
# 0 - 69 insuficiente
# 70 - 79 bien
# 80 - 89 muy bien
# 90 - 100 excelente

def obtener_calificacion(calificacion):

  if calificacion < 0 or calificacion > 100:
    return 'Error: La calificación debe estar entre 0 y 100'
  elif calificacion < 70:
    return 'Insuficiente'
  elif calificacion < 80:
    return 'Bien'
  elif calificacion < 90:
    return 'Muy bien'
  else:
    return 'Excelente'

nota = int(input("Ingrese la calificación: "))
print(obtener_calificacion(nota))


## 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" )
#  y datos (una tupla con los datos necesarios para calcular el área de la figura).

import math

def calcular_area(figura, datos):
   
    if figura == 'rectangulo':
        if len(datos) == 2:
            base, altura = datos
            return base * altura
    
    elif figura == 'circulo':
        if len(datos) == 1:
            radio = datos [0]
            return math.pi * radio**2
    
    elif figura == 'triangulo':
        if len(datos) == 2:
            base, altura = datos
            return (base * altura) / 2
       
    else:
        return "Error: Figura no reconocida. Usa 'rectangulo', 'circulo' o 'triangulo'."

print(f'El área del rectángulo es: {calcular_area('rectangulo', (5, 10))}')  
print(f'El área del círculo es: {round(calcular_area('circulo', (7,)),2)}')       
print(f'El área del triángulo es: {calcular_area('triangulo', (8, 4))}')  


## 41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto
#  final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:

#1. Solicita al usuario que ingrese el precio original de un artículo.
#2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
#3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
#4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). 
   # Por ejemplo, descuento de 15€.
#5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
#6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.

def compra_final(precio_original, tiene_cupon, valor_cupon=0):

  precio_final = precio_original

  if tiene_cupon and valor_cupon > 0:
    precio_final -= valor_cupon

  return precio_final

precio_original = float(input('Ingrese el precio del artículo: '))
tiene_cupon = input('¿Tiene un cupón de descuento? (si/no): ').lower() == 'si'

if tiene_cupon:
  valor_cupon = float(input('Ingrese el valor del cupón de descuento: '))

  precio_final = compra_final(precio_original, tiene_cupon, valor_cupon)    # Calcular el precio final
  print('El precio final a pagar es:', precio_final)

else:
  precio_final = compra_final(precio_original, tiene_cupon)    # Si no tiene cupón, se calcula el precio final sin descuento
  print('El precio final a pagar es:', precio_final)