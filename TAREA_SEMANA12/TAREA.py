# definimos las dimenciones de la matriz
ciudades= 3 # numeros de ciudades
dias= 7     # dias de la semana
semanas =4  # numeros de semana
# creamos una matriz 3D para almacenar datos
temperaturas = [
    [ # ciudad 1
        [27,18,32,25,17,32,32], # semana 1
        [19,33,38,29,23,22,28], # semana 2
        [35,26,28,22,28,37,28],  # semana3
        [38,29,25,36,28,29,37]  # semana 4
    ],
    [ # ciudad 2
        [28,35,37,40,38,40,38],  # semana1
        [35,37,38,39,40,35,36],  # semana2
        [38,38,38,35,36,29,30],  # semana3
        [29,30,32,32,35,29,39]  # semana 4
    ],
    [ # ciudad 3
        [26,27,26,28,30,29,29],  # semana1
        [28,28,26,26,28,24,25],  # semana2
        [29,30,30,28,29,29,27],  # semana3
        [28,28,27,27,26,26,24]  # semana 4
    ]
]

# calculamos y mostramos el promedio de temperaturas para cada ciudad por semana
for ciudad in range (ciudades):
    print(f"ciudad {ciudad + 1}:")
    for semana in range (semanas):
        suma_temperaturas=0
        for dia in range (dias):
            suma_temperaturas+=temperaturas[ciudad][semana][dia]
        promedio=suma_temperaturas/dias
        print(f" semana {semana +1}: promedio de temperatura={promedio:.2f}c")