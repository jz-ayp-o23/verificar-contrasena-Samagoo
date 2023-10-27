"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
CONSTANTE = valor

# Entradas
contrasena = input()

# Proceso
longitud = False
    if len(contrasena)>=10:
        longitud = True
    mayusculas = 0
    for caracter in contrasena: 
        if caracter.isupper() == True:
            mayuscula += 1
    numero = False 
    if contrasena[0].isdigit():
        numero = True
    if longitud and mayusculas>=2 and numero == False:
        resultado = 'La contraseña sí cumple con los requisitos'
    else: 
        resultado = 'La contraseña no cumple con los requisitos'

# Salidas
print(resultado)
