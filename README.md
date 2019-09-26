# Complejidad Algorítmica

## Trabajo Parcial

### Sección CC41

### Tema: Problema de corte y empaquetamiento 

###      Integrantes:

- Zevallos Ccorahua, Arthur Antoni F.
- Guadalpe Carrillo, Luis Enrique

### INTRODUCCIÓN:

Este proyecto trata de solucionar un problema sobre la optimización de uso de espacio, ya que se  cuenta  con  diversas  aplicacaciones  en diferentes  industrias.  Hace  referencia al ahorro de espacio que se podria aplicar en los almazenes, empaquetamiento o realizar cortes en planchas de cualquier material para poder minimizar el desperdicio de recursos o activo (el costo y espacio) y maximizar algún otro. Para este proyecto se podrian aplicar varios algorítmos, pero estaremos implementando y aplicando los algoritmos de Fuerza bruta y Divide y vencerás. Luego se compararan los algoritmos implementados y analizar las eficiencias con la que buscan una respuesta al problema comparando uno con el otro y determinar cuál seria la mejor solución.

### OBJETIVOS:

##### Objetivo General:

Al finalizar el curso,el estudiante implemente distintos algoritmos para resolver problemas en contecto real sobre cortes y empaquetamiento basándose en técnicas tales como Fuerza Bruta, Divide-y-Vencerás y BackTracking.

##### Objetivos Específicos:

- Crear algoritmos que solucione el problema de cortes y empaquetamientode con distintos métodos por integrante.
- Implementar una interfaz que le permita al usuario ingresar los datos necesarios y que el programa sea capaz de mostrar los distintos resultados o implementar la posibilidad de ueasr archivos para la carga y escritura de estos.
- Hallar la complejidad de los algoritmos propuestos.
- Generar archivos de entrada, siguiendo el formato establecido
- Analizar la eficiencia de las soluciones mediante:
- Porcentaje de desperdicio para el empaquetamiento y número de cortes (para los recortes)
- Tablas de comparación: tiempo de ejecución de algoritmo vs entrada de datos, memoria consumida por algoritmo vs entrada de datos
- Presentar conclusiones finales en función de los datos levantados en el punto anterior.

### MARCO TEORICO:

Para el trabajo, la implementación de los algoritmos que usaremos estará en base al lenguaje de programación Phyton. Dichos algoritmos son los siguientes:
1.	Backtracking
Este algoritmo es una técnica de programación para realizar búsquedas sistemáticas de todas las configuraciones posibles dentro de un espacio de búsqueda. Busca encontrar la mejor combinación en la búsqueda. Si se encuentra con una opción incorrecta, la búsqueda retrocede hasta el paso anterior y elige la siguiente opción.

2.	Fuerza Bruta
Es el algoritmo más simple. Consiste en probar todas las posibles posiciones de forma exhaustiva. Ya que la fuerza bruta atravesará todas las combinaciones posibles, no toma en cuenta nada. Entonces, al considerar todo, el problema se puede salir de control, por lo que solo es lo suficientemente buena para problemas de pequeñas instancias.


# Analisis de complejidad de Backtratring

Backtraking  = n^3

# Análisis de complejidad de Fuerza Bruta
Fuerza bruta= n^3
