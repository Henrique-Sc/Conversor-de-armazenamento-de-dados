from time import sleep

def typevalue(num):
    if num == 1:
        tipo = 'TB'
    elif num == 2:
        tipo = 'GB'
    elif num == 3:
        tipo = 'MB'
    elif num == 4:
        tipo = 'KB'
    
    return tipo

def linha():
    sleep(0.5)
    print('\n---------------------------------------\n')
    sleep(0.5)


print('---- Conversor de unidades de armazenamento ----\n')

while True:
    print('''Deseja converter quais unidades?

1 - Terabyte
2 - Gibabyte
3 - Megabyte
4 - Kilobyte
''')
    
    esc = int(input('Digite aqui: ').strip())
    if esc not in (1, 2, 3, 4):
        print('\nValor inválido! Insira um valor correto')
        linha()
    else:
        linha()
        break

tipo_valor = typevalue(esc)
valor = float(input(f'Digite o valor ({tipo_valor}): '))

linha()

print('Olá mundo!')