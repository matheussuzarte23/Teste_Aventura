Mensagem = "Boas Vindas"

print (Mensagem)

nome = input("qual o seu nome?")
print (f'óla, {nome}')

vida_de_heroi = 100
poção_de_cura = 2
espada_magica = False


decisao = input("Qual caminho você escolhe? (Digite '8' ou '9'): ")

def executar_caminho_esquerda(vida_atual, pocoes_atuais):
    vida_atual -= 70
    print(f"voce perdeu 30 pontos de vida!, vida atual {vida_atual} HP.")
    if pocoes_atuais > 0:
        print(f"voce tem {pocoes_atuais} poções de cura")
        resposta = input("gostaria de usar uma poção? sim/não:")()
        if resposta == "sim":
            vida_atual += 30
            pocoes_atuais -= 1
            print(f"voce usou a poção, Vida agora é {vida_atual} HP.")
        else:
            print(f"voce decidi guardar a poção")
    
    return vida_atual, pocoes_atuais

if decisao == "8":
    espada_magica = False
    print("caminho 8 esta friu e seco, de repente o chão cede e voce cai")
    vida_de_heroi = vida_de_heroi - 70
    print(f"{nome} voce perdeu - 70 de sua vida! {vida_de_heroi}")
    
    if poção_de_cura > 0:
        print(f"voce tem {poção_de_cura} para usar")
        resposta_poção = input("gostaria de usar a poção? (sim/não):")
        if resposta_poção == "sim":
            vida_de_heroi = vida_de_heroi + 30
            poção_de_cura = poção_de_cura - 1
            print('n/ voce usou a poção e recuperou 30 de vida')
            print(f"sua vida agora é {vida_de_heroi} HP")
        else:
            print("voce decide guarda a poção para mais tarde")

if decisao == "9":
    print("caminho da direta esta quente e umido")
    espada_magica = True

if vida_de_heroi > 40:
    print(f"checando sua vida {vida_de_heroi}")
    print("vitoria")

else:print("voce perdeu")

