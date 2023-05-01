num1 = float(input('Digite um número em metro: '))
print(f'A medida de {num1}m corresponde a:')
print(f'{num1/1000}km\n{num1/100}hm\n{num1/10}dam\n{num1*10:.0f}dm\n{num1*100:.0f}cm\n{num1*1000:.0f}nn')
