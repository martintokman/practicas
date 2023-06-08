#Extractor de información del correo electrónico
'''
Recopile una dirección de correo electrónico del usuario y luego averigüe si el usuario tiene un nombre de dominio personalizado o un nombre de dominio popular. Por ejemplo

Recopilamos una dirección de correo electrónico del usuario y luego vamos a averiguar si ese email tiene nombre de dominio personalizado o un nombre de un dominio popular. Por ejemplo:

Entrada: mary.jane@gmail.com
Salida: Hola Mary, estoy viendo que tu email está registrado con Google. ¡Eso es genial!.
Entrada: peter.pan@myfantasy.com
Salida: Hola Peter, estoy observando que estás utilizando un dominio personalizado de myfantasy. ¡Impresionante!.
'''
direccion_correo = ""
nombre_usuario = ""
dominio = ""
tipo_de_dominio = ""
lista_dominios_populares = {
                            "Google" : "gmail.com",
                            "Microsoft" : "microsoft.com",
                            "Microsoft" : "hotmail.com",
                            "Amazon" : "amazon.com"
                            }


def validar_correo(direccion_correo):
    direccion_correo = direccion_correo.split("@")
    return direccion_correo

def verificar_dominio(dominio):
    
    if dominio in lista_dominios_populares:
    
        for items in lista_dominios_populares.items():
            
            if dominio == items[1]:
                dominio = ["popular", items[1]]
    
    else: 
        dominio = dominio.split(".")
        dominio = dominio[0]
        dominio = ("personalizado", dominio)
                 
    return dominio

def devolver_mensaje(dominio):
    
    if dominio[0] == "personalizado":
        
        dominio = f"Hola {nombre_usuario}, estoy viendo que tu email está registrado con {dominio[1]}. ¡Eso es genial!."
        return dominio
    
    else:
        
        dominio = f"""Hola {nombre_usuario}, estoy observando que estás utilizando un dominio 
        personalizado de {dominio[0]}. ¡Impresionante!."""
        
        return dominio
    
direccion_correo = input("Ingresa tu dirección de correo: ")
correo_validado = validar_correo(direccion_correo)

#Busco nombre de usuario y dominio
nombre_usuario = correo_validado[0]

dominio = correo_validado[1]

dominio = verificar_dominio(dominio)

dominio = devolver_mensaje(dominio)

print(dominio)


