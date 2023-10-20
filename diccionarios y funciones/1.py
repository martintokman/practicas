# Crear una función que reciba una lista de 10 números entre 1 y 10 y 
# devuelva un diccionario con el número como clave y su cuadrado como valor.

def validar_numero(numero):
    if numero > 0 and numero <= 10:
        numero = (numero, "validado")
        return numero
    else: 
        numero = (numero, "novalidado")
        return numero

lista_de_numeros = []
diccionario_de_salida = {}

for i in range(10):
    while True:
        try:
            numero = int(input("Ingresa un número entre 1 y 10: "))
            numero_validado = validar_numero(numero)
            if numero_validado[1] == "validado":
                lista_de_numeros.append(numero_validado[0])
                break
            elif numero_validado[1] == "novalidado":
                print("El número está fuera del rango. Vuelve a intentar.")
                continue
        except ValueError:
            print("Sólo se admiten números entre 1 y 10. Vuelve a intentar")
            continue


for numero in lista_de_numeros:
    diccionario_de_salida.update({numero : numero ** 2})
    
print (diccionario_de_salida)

    
