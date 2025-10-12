Mensagem = "Boas Vindas"

print (Mensagem)

nome = input("qual o seu nome?")
print (f'óla, {nome}')

vida_de_heroi = 100
poção_de_cura = 2
espada_magica = False


print("/n_______________________________")
print("voçe se encontra em uma bifurcação da masmorra")
print("caminho da esquerda esta friu e seco")
print("caminho da direta esta quente e umido")
print("___________________________________")

decisao = input("Qual caminho você escolhe? (Digite 'esquerda' ou 'direita'): ")

if decisao.lower() == "esquerda":
    espada_magica = False
    print("caminho da esquerda esta friu e seco, de repente o chão cede e voce cai")
    vida_de_heroi = vida_de_heroi - 70
    print(f"{nome} voce perdeu - 70 de sua vida! {vida_de_heroi}")
    
    if poção_de_cura > 0:
        print(f"voce tem {poção_de_cura} para usar")
        resposta_poção = input("gostaria de usar a poção? (sim/não):")
        if resposta_poção.lower == "sim":
            vida_de_heroi = vida_de_heroi + 30
            poção_de_cura = poção_de_cura - 1
            print('n/ voce usou a poção e recuperou 40 de vida')
            print(f"sua vida agora é {vida_de_heroi} HP")
        else:
            vida_de_heroi = 30
            print("voce decide guarda a poção para mais tarde")

if decisao.lower() == "direita":
    print("caminho da direta esta quente e umido")
espada_magica = True

if vida_de_heroi > 40:
    print(f"checando sua vida {vida_de_heroi}")
    print("vitoria")

else: print("voce perdeu")