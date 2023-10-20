def es_bisiesto(year):
    if year % 4 != 0: #no divisible entre 4
        return False
    elif year % 4 == 0 and year % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0: #divisible entre 4 y 10 y no entre 400
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0: #divisible entre 4, 100 y 400
        return True

def dias_en_mes(year, month):
    bisiesto = es_bisiesto(year)
    dias_30 = [4,6,9,11]
    dias_31 = [1,3,5,7,8,10,12]
    if bisiesto and month == 2:
        dias_en_mes = 29
        
    elif not bisiesto and month == 2:
        dias_en_mes = 28
        
    elif month in dias_30:
        
        dias_en_mes = 30
    elif month in dias_31:
        
        dias_en_mes = 31
    elif not bisiesto and month not in dias_30 and month not in dias_31:
        return None
    
    return dias_en_mes
    
    
    
def dia_del_anio(year, month, day):
    if day > 31:
        return None
    else:
    
        contador_dias = 0
        
        
        #Bucle que vaya del mes 1 al month y por cada nro de mes acumule la cantidad de dias de cada mes
        meses = 1
        while meses < month:
            dias = dias_en_mes(year, meses) #Devuelve la cantidad de dias que tiene el mes dado
            contador_dias += dias
            meses = meses + 1 
        
        contador_dias += day  
        print(contador_dias)  
    

print(dia_del_anio(2000, 2, 28))
