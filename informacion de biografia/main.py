# Información de biografía
import datetime
nombre = ""

def validar_nombre(nombre):
    while True:
        if nombre == "*":
            print("Entrada incorrecta")
            nombre = input("Ingresa tu nombre: ")
        else:
            return(nombre)
        


    


nombre = input("Ingresa tu nombre: ")
print(validar_nombre(nombre))  

#fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy:")
#direccion = input("Ingresa tu dirección: ")
#metas_personales = input ("Ingresa tus metas personales: ")




x = datetime.datetime(1976,2,8)

print(x.strftime("%d/%m/%Y"))
