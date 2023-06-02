#Información de biografía

#Importación de módulos
import datetime



#Definición de funciones
def validar_nombre(nombre):
    while True:
        nombre = nombre.capitalize()
        if nombre == "*":
            print("Entrada inválida.")
            nombre = input("Ingresa tu nombre: ")
        else:
            return(nombre)
            break
        
def validar_fecha(fecha_nac):
    while True:
        if len(fecha_nac) > 10 or len(fecha_nac) < 10:
            print("Formato de fecha inválido.")
            fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
        else:
            if fecha_nac[2] == "/" and fecha_nac[5] == "/":
                dia_nac = fecha_nac[:2]
                mes_nac = fecha_nac[3:5] 
                anio_nac = fecha_nac[6:]
                
                try:
                    if int(dia_nac) > 31:
                        print("El día de nacimiento no puede ser mayor a 31")
                        fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
                        continue
                except ValueError:
                        print("Error en día.")
                        fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
                try:
                    if int(mes_nac) > 12:
                        print("El mes de nacimiento no puede ser mayor a 12")
                        fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
                        continue
                except ValueError:
                    print("Error en mes.")
                    fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
                try:
                    if int(anio_nac) > 2023:
                        print("El año de nacimiento no puede ser mayor al año actual.")
                        fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
                        continue
                except ValueError:
                    print("Error en año.")
                    fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
                else:
                    return(fecha_nac)
                    break
            else:
                print("Formato de fecha inválido.")
                fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
    


nombre = input("Ingresa tu nombre: ")
validar_nombre(nombre)
fecha_nac = input("Ingresa tu fecha de nacimiento en formato dd/mm/yyyy: ")
validar_fecha(fecha_nac)
direccion = input("Ingresa tu dirección: ")
metas = input("Ingresa tus metas: ")

print(f"""Te paso el resumen:\n
      - Nombre: {nombre}
      - Fecha de nacimiento: {fecha_nac}
      - Dirección: {direccion}
      - Metas: {metas}
      """)


