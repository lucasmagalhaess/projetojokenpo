from time import sleep
from random import randint  

def jogar ():

    print("#######################")
    print("Bem vindo ao JO KEN PO!")
    print("#######################")

    total_tentativas = 5
    placar_player = 0
    placar_computador = 0

    for rodada in range (1, total_tentativas + 1):
        print(f"Tentativa {rodada} de {total_tentativas}")
        print("""Escolha sua opção:
        [0] Pedra
        [1] Papel
        [2] Tesoura""")
        player = int(input( "Digite sua escolha: "))
        if (player < 0 or player > 2):
            continue


        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!!!")
        sleep(1)

        opções = ("Pedra", "Papel", "Tesoura")   
        computador = randint(0, 2)
        print("Você escolheu --> {}".format(opções[player]))
        print("Computador escolheu --> {}". format(opções[computador]))
        sleep(2)

        if (computador == 0):
            if (player == 0):
                print("Empate!")
            elif(player == 1):
                print("Você Ganhou!")
                placar_player +=1
            elif(player == 2):
                print("Você mamou!")
                placar_computador +=1

        if (computador == 1):
            if (player == 0):
                print("Você mamou!")
                placar_computador +=1
            elif(player == 1):
                print("Empate!")
            elif(player == 2):
                print("Você ganhou!")
                placar_player +=1

        if (computador == 2):
            if (player == 0):
                print("Você ganhou!")
                placar_player +=1
            elif(player == 1):
                print("Você mamou!")
                placar_computador +=1
            elif(player == 2):
                print("Empate!")  
        sleep(2)            
                
        
        print("\nResultado final:")
        print(f"Você {placar_player}", "X", f"{placar_computador}", "Computador")
        sleep(2)


    sleep(2)
    if    (f"{placar_player}" > f"{placar_computador}"):
        print("Você ganhou a melhor de 5! Parabéns!")
    elif  (f"{placar_player}" < f"{placar_computador}"):
        print("Você perdeu a melhor de 5! Se fodeu!")
    elif  (f"{placar_player}" == f"{placar_computador}"):
        print("Empate na melhor de 5!")

    sleep(2)
    print("############")
    print("FIM DO JOGO!")    
    print("############")

if (__name__ == "__main__"):
    jogar()