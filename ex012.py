preco = float(input('Qual é o preço do produto? '))
novo = preco - (preco * 5 / 100)
print('O produto que custava {:.2f} vai passar a custar {:.2f}'.format(preco, novo))