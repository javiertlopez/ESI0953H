
meses = {'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 
        'MAY': 5, 'JUN': 6, 'JUL': 7, 'AUG': 8, 
        'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12}

date = input("Ingresa la fecha deseada de forma dd-MMM-yy:")
date_list = date.split('-')
#mostramos fecha original
print(date_list)

#quitamos "-" y guardamos los 3 elementos de la fecha
mes_upper = date_list[1].upper()

#asignamos los numeros de la fecha correspondiente
mes_numero = meses[mes_upper]
dia_numero = int(date_list[0])
year_numero = int(date_list[2])

tupla = (year_numero, mes_numero, dia_numero)
print(tupla)