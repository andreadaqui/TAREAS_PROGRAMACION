#Crear una matriz de donde analizaremos las temperaturas de 4 ciudades
#durante los 7 días de la semana, durante un mes
#creamos una matriz con 3 ciudades, durante 1 mes se analizará


tem_quito = [[27,18,32,25,17,32,32], #semana1
           [19,33,38,29,23,22,28],  #semana2
           [35,26,28,22.28,37,28],#semana3
           [38,29,25,36,28,29,37], #semana4
         ]

tem_guayaquil = [[28,35,37,40,38,40,38], #semana1
              [35,37,38,39,40,35,36], #semana2
             [38,38,38,35.36,29,30], #semana3
              [29,30,32,32,35,29,39], #semana
            ]
tem_imbabura =[[26,27,26,28,30,29,29],#semana1
             [28,28,26,26,28,24,25],#semana2
             [29,30,30,28,29,29,27],#semana3
              [28,28,27,27,26,26,24],#semana4
             ]
#tem_ciudades=[ tem_quito, tem_guayaquil, tem_imbabura]

#print(tem_ciudades)

#print("tem_quito")
print("Temperatura ciudad de Quito")
suma_filas1 = []
for f in tem_quito:
    suma_filas1.append(sum(f)/7)
print(suma_filas1)

print("Temperatura ciudad de Guayaquil")

suma_filas2 = []
for f in tem_guayaquil:
    suma_filas2.append(sum(f)/7)
print(suma_filas2)

print("Temperaturas ciudad de Imbabura")
suma_filas3 = []
for f in tem_imbabura:
    suma_filas3.append(sum(f)/7)
print(suma_filas3)