treino=[]
ARQUIVO_TREINOS="treinos.txt"
ARQUIVO_METAS="metas.txt"

def carregar_treinos():
    treinos=[]
    try:
        with open(ARQUIVO_TREINOS, "r") as lista:
            for linha in lista:
                partes=linha.strip().split("|")
                if len(partes)==4:
                    treino={
                        "data": partes[0],
                        "tipo": partes[1],
                        "tempo": partes[2],
                        "movimentos": partes[3]
                    }
                    treinos.append(treino)
    except:
        pass
    return treinos

def save_treinos(treinos):
    with open(ARQUIVO_TREINOS, "w") as lista:
        for t in treinos:
            linha = f"{t['data']}|{t['tipo']}|{t['tempo']}|{t['movimentos']}\n"
            lista.write(linha)

def add_treino():
    data=input("Data do treino (dd/mm/aaaa): ")
    tipo=input("Tipo de treino (AMRAP, EMOM, For Time): ").upper()
    tempo=input("Tempo em minutos (ou For Time): ")
    movimentos=input("Movimentos (separe por vírgulas): ")
    
    treino={"data": data, "tipo": tipo, "tempo": tempo, "movimentos": movimentos}
    treinos=carregar_treinos()
    treinos.append(treino)
    save_treinos(treinos)
    print("Treino adicionado com sucesso!")

def visu_treinos():
    treinos=carregar_treinos()
    if not treinos:
        print("Você não tem nenhum treino registrado.")
    for i, t in enumerate(treinos, 1):
        print(f"{i}. {t['data']} | {t['tipo']} | {t['tempo']} | Movimentos: {t['movimentos']}")

def remover_treino():
    visu_treinos()
    i=int(input("Digite o número do treino para remover: "))-1
    treinos=carregar_treinos()
    if 0<=i<len(treinos):
        treinos.pop(i)
        save_treinos(treinos)
        print("O seu treino foi removido!")
    else:
        print("Índice inválido.")

def editar_treino():
    visu_treinos()
    i=int(input("Digite o número do treino para editar: "))-1
    treinos=carregar_treinos()
    if 0<=i<len(treinos):
        print("Deixe vazio para manter o valor atual.")
        novo_tipo=input("Novo tipo: ")
        novo_tempo=input("Novo tempo: ")
        novos_mov=input("Novos movimentos: ")
        if novo_tipo:
            treinos[i]['tipo']=novo_tipo.upper()
        if novo_tempo:
            treinos[i]['tempo']=novo_tempo
        if novos_mov:
            treinos[i]['movimentos']=novos_mov
        save_treinos(treinos)
        print("O seu treino foi editado!")
    else:
        print("Índice inválido.")

def menu():
    while True:
        print("\n----- MENU WOD TRACKER -----")
        print(" 1-Adicionar treino\n 2-Visualizar treino(s)\n 3-Editar treino\n 4-Remover treino\n 5-Filtrar treinos\n 6-Registrar meta\n 7-Ver metas\n 8-Sugerir WOD\n 0-Sair")
        try:
            n=int(input("Escolha uma das opções acima: "))

            if n==1:
                add_treino()
            elif n==2:
                visu_treinos()
            elif n==3:
                editar_treino()
            elif n==4:
                remover_treino()
            else:
                print("Essa opção não existe!")
            
            opcao=input("\nVocê deseja continuar ou sair? ")
            if opcao.lower()=='sair':
                print("Seu programa foi encerrado com sucesso!")
                break
        except ValueError:
            print("Digite apenas números!")
menu()