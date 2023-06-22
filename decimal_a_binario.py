#convertir decimal a binario


numero= int(input("Ingrese el valor decimal: "))
divisor = numero
cociente= 0
resto= 0
binario = []



while divisor > 1:

    cociente = divisor // 2
    resto = divisor % 2
    binario.append(resto)
    divisor = cociente
    
else: 
    
    binario.append(cociente)
    
    
binario.reverse()
print("El binaro de", numero, "es: ", end="")
for item in binario:
    print(item, end="")
