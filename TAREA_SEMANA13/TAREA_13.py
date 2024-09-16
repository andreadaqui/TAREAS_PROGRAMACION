
def promedio_temperaturas (datos_temperaturas):
  """
  En esta oportunidad realizaremos el calculo del promedio
  de la temperatura de 3 ciudades del pais durante 4 semanas

  mediante la utilizaciòn de la funciòn def
  """
  promedios_ciudades = {}
  for ciudad, semanas in datos_temperaturas.items():
    todas_temperaturas=[temperatura for semana in semanas for temperatura in semana]
    promedio=sum(todas_temperaturas)/len(todas_temperaturas)
    promedios_ciudades[ciudad]=promedio
  return promedios_ciudades


# ciudad:
Datos_temperaturas= {
   "Riobamba":[[18,28,26,26,26,27,28],
               [22,23,23,25,28,27,25],
               [22,25,27,29,28,29,27],
               [26,24,24,26,27,26,25]],
   "Quito":[[22,23,28,16,24,18,19],
            [23,23,25,25,26,26,27],
            [19,22,22,25,25,23,24],
            [29,30,30,31,38,35,35]],
   "Imbabura":[[26,26,27,28,28,26,25],
        [28,28,28,26,27,25,30],
        [27,22,30,31,32,28,26],
        [29,25,25,26,27,27,29]]
}
resultado=promedio_temperaturas(Datos_temperaturas)
print(resultado)