from time import sleep


def linha():
    sleep(0.5)
    print('\n---------------------------------------\n')
    sleep(0.5)


def GB_TB(gb):
    tb = gb / 1024
    return tb


def GB_MB(gb):
    mb = gb * 1024
    return mb


def GB_KB(gb):
    kb = gb * 1024 ** 2
    return kb


print('---- Conversor de unidades de armazenamento ----\n')

valor = float(input(f'Digite o valor a ser analisado (GB): '))

linha()

print(f'GB para TB: {GB_TB(valor)}')
linha()
print(f'GB para MB: {GB_MB(valor)}')
linha()
print(f'GB para KB: {GB_KB(valor)}')
linha()

print('<< Obrigado por testar :) >>')
