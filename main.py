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
        

print('---- Conversor de unidades de armazenamento ----')

while True:
    print('''
Deseja converter quais unidades?

1 - Terabyte
2 - Gibabyte
3 - Megabyte
4 - Kilobyte
''')
    esc = int(input('Digite aqui: ').strip())
    if esc not in (1, 2, 3, 4):
        print('\nValor inválido! Insira um valor correto')
        sleep(1)
        print('\n---------------------------------------')
        sleep(1)
    else:
        sleep(0.5)
        print('\n---------------------------------------')
        sleep(0.5)
        break

tipo_valor = typevalue(esc)
valor = float(input(f'\nDigite o valor ({tipo_valor}): '))

