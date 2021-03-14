import time

def clear():
    print("\n" * 50)

resposta = None

while resposta == None:
    clear()
    print("Você está em uma floresta e a sua frente tem uma estrada, o que você faz?")
    print("1: Passa por ela")
    print("2: Senta e chora por algum motivo")
    print("3: Decide ser um rebelde e passa a andar fora da estrada")
    resposta = int(input("O que você irá fazer?\n"))

    if resposta == 1:
        print("Andando pela estrada...")
    elif resposta == 2:
        print("Você está chorando na estrada")
    elif resposta == 3:
        print ("A polícia da grama da floresta te para e te dá uma multa")
    else:
        print("Resposta inválida, tente novamente")
        resposta = None

count = 0
while count <= 10:
    print("...")
    time.sleep(0.5)
    if count == 10:
        print("De repente, mais que repente, você morre\n")
        time.sleep(3)
        print("FIN")
        time.sleep(3)
    count += 1
        
print("Aperte ENTER para terminar o jogo...")
input()