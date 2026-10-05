# ==========================================
# 1. Variables 
# Nahum Flores NC 0065
# ==========================================
# Ejemplo 1: Crear una variable de texto (string)
nombre = "Carlos"

# Ejemplo 2: Crear una variable numérica (integer)
edad = 25

# Ejemplo 3: Reasignar el valor y cambiar el tipo de dato de una variable
precio = 19.99
precio = "Oferta: $19.99"


# ==========================================
# 2. Múltiples Variables (python_variables_multiple.asp)
# ==========================================
# Ejemplo 1: Asignar múltiples valores a múltiples variables en una sola línea
x, y, z = "Manzana", "Banana", "Cereza"

# Ejemplo 2: Asignar el mismo valor a múltiples variables
a = b = c = "Python"

# Ejemplo 3: Desempaquetar una lista en variables
frutas = ["Naranja", "Mango", "Uva"]
fruta1, fruta2, fruta3 = frutas


# ==========================================
# 3. Tipos de Datos (python_datatypes.asp)
# ==========================================
# Ejemplo 1: Tipos numéricos (int, float, complex)
numero_entero = 10
numero_decimal = 3.14
numero_complejo = 1j

# Ejemplo 2: Tipos de secuencia (str, list, tuple)
texto = "Hola Mundo"
lista_compras = ["pan", "leche", "huevos"]
coordenadas_tupla = (10.0, 20.0)

# Ejemplo 3: Otros tipos de datos comunes (dict, set, bool)
diccionario_usuario = {"nombre": "Ana", "edad": 30}
conjunto_numeros = {1, 2, 3, 3}  # Elimina duplicados automáticamente
es_mayor_de_edad = True


# ==========================================
# 4. Operadores Aritméticos (python_operators_arithmetic.asp)
# ==========================================
# Ejemplo 1: Suma (+), Resta (-) y Multiplicación (*)
suma = 15 + 5
resta = 20 - 8
multiplicacion = 4 * 3

# Ejemplo 2: División (/), División entera (//) y Módulo (%)
division_decimal = 10 / 3       # Resultado: 3.3333...
division_entera = 10 // 3       # Resultado: 3
modulo_residuo = 10 % 3         # Resultado: 1

# Ejemplo 3: Exponenciación (**)
potencia = 2 ** 3               # Resultado: 8


# ==========================================
# 5. Operadores de Comparación (python_operators_comparison.asp)
# ==========================================
# Ejemplo 1: Igual a (==) y Diferente de (!=)
es_igual = (5 == 5)             # True
es_diferente = (5 != 3)         # True

# Ejemplo 2: Mayor que (>) y Menor que (<)
es_mayor = (10 > 20)            # False
es_menor = (10 < 20)            # True

# Ejemplo 3: Mayor o igual que (>=) y Menor o igual que (<=)
mayor_o_igual = (15 >= 15)      # True
menor_o_igual = (8 <= 5)        # False


# ==========================================
# 6. Operadores Lógicos (python_operators_logical.asp)
# ==========================================
# Ejemplo 1: Operador AND (devuelve True si ambas condiciones son verdaderas)
resultado_and = (10 > 5) and (5 < 8)     # True

# Ejemplo 2: Operador OR (devuelve True si al menos una condición es verdadera)
resultado_or = (10 < 5) or (5 == 5)      # True

# Ejemplo 3: Operador NOT (invierte el resultado lógico)
resultado_not = not(10 > 5)              # False (ya que 10 > 5 es True)


# ==========================================
# Imprimir algunos resultados para verificar
# ==========================================
print("--- Datos de Usuario ---")
print(f"Nombre: {nombre}, Edad: {edad}")

print("\n--- Múltiples Variables ---")
print(f"Frutas: {x}, {y}, {z}")
print("\n--- Operaciones ---")
print(f"Potencia (2^3): {potencia}")
print(f"Resultado AND: {resultado_and}")
print(f"Resultado NOT: {resultado_not}")
print("Nahum Flores NC 0065")