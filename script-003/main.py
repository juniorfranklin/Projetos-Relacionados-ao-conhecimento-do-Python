palavra = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: {type(palavra)}')
print(f'Só tem espaços: {palavra.isspace()}')
print(f'É númerico? {palavra.isnumeric()}')
print(f'É alfabético? {palavra.isalpha()}')
print(f'É alfanumérico? {palavra.isalnum()}')
print(f'Está em maíuscilas? {palavra.isupper()}')
print(f'Está em mínusculas? {palavra.islower()}')
print(f'Está capitalizada? {palavra.istitle()}')
 