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

print('''
Deseja converter quais unidades?

1 - Terabyte
2 - Gibabyte
3 - Megabyte
4 - Kilobyte
''')

while True:
    esc = int(input('Digite aqui: ').strip())
    if esc not in (1, 2, 3, 4):
        print('\nValor inválido! Insira um valor correto')
    else:
        break

    
valor = float(input(f'\nDigite o valor ({typevalue(esc)}): '))