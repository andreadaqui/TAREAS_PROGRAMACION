def promedio_temp_ciudad  (arreglo_temperaturas,ciudad,semana ):
    acumulador = 0
    for i in range(len(arreglo_temperaturas[ciudad][semana])):
        acumulador = acumulador + arreglo_temperaturas[ciudad][semana][i]
    promedio = acumulador / len(arreglo_temperaturas[ciudad][semana])
    return promedio
temperaturas = [
    [#ciudad1
        [28,38,40,38,48,25,26], #semana1
        [32,29,25,45,32,26,22],#semana2
        [38,28,28,26,24,24,29],#semana3
        [28,28,30,32,32,35,35],#semana4
    ],
    [#ciudad2
        [38,38,36,36,35,35,38],#semana1
        [40,32,32,35,35,36,40],#semana2
        [35,35,36,37,37,38,40],#semana3
        [40,28,28,29,35,35,36],#semana4
     ],
    [#ciudad3
        [26,26,27,28,28,26,25],#semana1
        [28,28,28,26,27,25,30],#semana2
        [27,22,30,31,32,28,26],#semana3
        [29,25,25,26,27,27,29],#semana4
     ]

]
#resultado=promedio_temp_ciudad(promedio
#print(resultado)

 #En este modelo de practica ingrese los datos cree la matriz
 #sin embargo al momento de correr el programa no me ejecuta ningun resultado
# pero tampoco me da error
# "
