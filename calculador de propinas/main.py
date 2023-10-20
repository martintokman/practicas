#Calculador de propinas
porc_propina_por_persona = []

def procesar_entrada(monto_factura):
    propina_18 = round(monto_factura * 0.18)
    propina_20 = round(monto_factura * 0.2)
    propina_25 = round(monto_factura * 0.25)
    lista_propinas = [propina_18, propina_20, propina_25]
    return lista_propinas


print("¿Cuál es la factura total de hoy, por favor?")
monto_factura = float(input("Ingresa el monto de la factura: $"))
cant_personas = int(input("¿Cuántas personas involucradas?: "))
i = 1
total_propina = 100 #Uso esta variable para avisar cuanto % resta x pagar
while i <= cant_personas:
    porc_propina = int(input(f"Que % paga la persona {i}? (Resta {total_propina}% por pagar): "))
    porc_propina_por_persona.append(porc_propina)
    total_propina -= porc_propina
    i += 1
    
    
lista_propinas = procesar_entrada(monto_factura)
print(f"La propina en partes iguales divivido en {cant_personas} personas es: ")
print(f"La propina aplicando el 18% es {round(lista_propinas[0] / cant_personas)} por persona.")
print(f"La propina aplicando el 20% es {round(lista_propinas[1] / cant_personas)} por persona.")
print(f"La propina aplicando el 25% es {round(lista_propinas[2] / cant_personas)} por persona.")
print("")
print("------------------------------------------------------------------------------------")
print("")
print("La propina personalizada que debe pagar cada uno es:")
contador = 1
for i in range(len(porc_propina_por_persona)):
    print(f"Persona {i} que paga {porc_propina_por_persona[i]}%: ${round(monto_factura / porc_propina_por_persona[i])}")
