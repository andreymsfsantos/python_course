larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = round(larg * alt,50)
print('A sua parede tem a dimensão de {}x{} e sua área é de {}m2'.format(larg, alt, area))
tinta = área * 0.15
print('Considerando que a cada 150ml se pinta 1m2 para pintar sua parede, seram necessários {}L de tinta coral rende muito'.format(tinta))