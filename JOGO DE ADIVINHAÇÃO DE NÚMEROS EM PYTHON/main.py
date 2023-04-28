from random import randint
cont = 1
client = int(input("Escolha um número de 1 a 100: "))
maquina = randint(1,100)              #fazendo a contagem, sorteando o número da máquina e guardando a estimativa do jogador

while (maquina != client):            
    if maquina > client:
        client = int(input(f"O número {client} foi um chute BAIXO, Tente novamente: "))
        cont += 1
    else:
        client = int(input(f"O número {client} foi um chute ALTO, Tente novamente:"))
        cont += 1
print(f"vc acertou, número de tentativas = {cont}")