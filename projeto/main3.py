treino = []
cont=0
ARQUIVO_TREINOS = "treinos.txt"
ARQUIVO_METAS = "metas.txt"

def validar_data(data):
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return False
    try:
        dia, mes, ano = map(int, data.split('/'))
        return 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= ano <= 9999
    except:
        return False

def validar_tempo(tempo, tipo):
    if tipo == "FOR TIME":
        return tempo.strip() != ""
    try:
        return int(tempo) > 0
    except:
        return False

def validar_tipo(tipo):
    return tipo in ["AMRAP", "EMOM", "FOR TIME"]

def validar_movimentos(movimentos):
    if not movimentos or ',' not in movimentos:
        return False
    # Verifica se contém apenas letras, espaços e vírgulas
    for char in movimentos:
        if not (char.isalpha() or char == ' ' or char == ','):
            return False
    # Verifica se cada movimento não está vazio
    mov_list = [mov.strip() for mov in movimentos.split(',')]
    return all(mov for mov in mov_list)

def carregar_treinos():
    treinos = []
    try:
        with open(ARQUIVO_TREINOS, "r") as lista:
            for linha in lista:
                partes = linha.strip().split("|")
                if len(partes) == 4:
                    treino = {
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
    data = input("Data do treino (dd/mm/aaaa): ")
    tipo = input("Tipo de treino (AMRAP, EMOM, For Time): ").upper()
    tempo = input("Tempo em minutos (ou For Time): ")
    movimentos = input("Movimentos (separe por vírgulas): ")
    if not validar_data(data):
        print("Data inválida. Tente novamente.")
        return
    if not validar_tipo(tipo):
        print("Tipo inválido. Tente novamente.")
        return
    if not validar_tempo(tempo, tipo):
        print("Tempo inválido. Tente novamente.")
        return
    if not validar_movimentos(movimentos):
        print("Movimentos inválidos. Tente novamente.")
        return
    # Verifica se o treino já existe
    
    treino = {"data": data, "tipo": tipo, "tempo": tempo, "movimentos": movimentos}
    treinos = carregar_treinos()
    treinos.append(treino)
    save_treinos(treinos)
    print("Treino adicionado com sucesso!")

def visu_treinos():
    treinos = carregar_treinos()
    if not treinos:
        print("Você não tem nenhum treino registrado.")
    for i, t in enumerate(treinos, 1):
        print(f"{i}. {t['data']} | {t['tipo']} | {t['tempo']} | Movimentos: {t['movimentos']}")

def remover_treino():
    visu_treinos()
    i = int(input("Digite o número do treino para remover: "))-1
    treinos = carregar_treinos()
    if 0 <= i < len(treinos):
        treinos.pop(i)
        save_treinos(treinos)
        print("O seu treino foi removido!")
    else:
        print("Índice inválido.")

def editar_treino():
    visu_treinos()
    i = int(input("Digite o número do treino para editar: "))-1
    treinos = carregar_treinos()
    if 0 <= i < len(treinos):
        print("Deixe vazio para manter o valor atual.")
        novo_tipo = input("Novo tipo: ")
        novo_tempo = input("Novo tempo: ")
        novos_mov = input("Novos movimentos: ")
        if novo_tipo:
            treinos[i]['tipo'] = novo_tipo.upper()
        if novo_tempo:
            treinos[i]['tempo'] = novo_tempo
        if novos_mov:
            treinos[i]['movimentos'] = novos_mov
        save_treinos(treinos)
        print("O seu treino foi editado!")
    else:
        print("Índice inválido.")

def filtrar_treinos():
    tipo = input("Filtrar por tipo (ex: AMRAP): ").upper()
    movimento = input("Filtrar por movimento (ex: snatch): ").lower()
    treinos = carregar_treinos()
    encontrados = []
    for t in treinos:
        if (not tipo or t['tipo'] == tipo) and (not movimento or movimento in t['movimentos'].lower()):
            encontrados.append(t)
    if not encontrados:
        print("Nenhum treino encontrado.")
    for t in encontrados:
        print(f"{t['data']} | {t['tipo']} | {t['tempo']} | Movimentos: {t['movimentos']}")

def registrar_meta():
    meta = input("Digite sua meta: ")
    with open(ARQUIVO_METAS, "a", encoding="utf-8") as f:
        f.write(meta + "\n")
        
    print("Sua meta foi registrada!")
cont+=1

def ver_metas():
    for i in range (cont):
        ARQUIVO_METAS=open("metas.txt", "r", encoding="utf8")
        print(ARQUIVO_METAS.readlines())
    
import random    
    
def sugestao_wod():
   
    categorias = ["AMRAP", "EMOM", "For time"]
    movimentos_base = ["burpee", "snatch", "clean", "push-up", "pull-up", "air squat", "lunges", "kettlebell swing"]

    categoria = random.choice(categorias) #escolha de um elemento aleatório de categoria  (.choice)                  categoria == categorias
    if categoria != "For Time":
        tempo = f"{random.randint(5, 20)} minutos" #.randint --> Escolhe aleatoriamente um número inteiro entre 5 e 20, incluindo o 5 e o 20. 
    else:
        tempo = "For Time"

    movimentos = ", ".join(random.sample(movimentos_base, 3))    #escolha de  3 movimentos diferentes aleatórios da lista 

    print(f"\nSugestão de WOD:")
    print(f"Categoria: {categoria}")
    print(f"Tempo: {tempo}")
    print(f"Movimentos: {movimentos}")

def menu():
    while True:
        print("\n----- MENU WOD TRACKER -----")
        print(" 1-Adicionar treino\n 2-Visualizar treino(s)\n 3-Editar treino\n 4-Remover treino\n 5-Filtrar treinos\n 6-Registrar meta\n 7-Ver metas\n 8-Sugerir WOD\n 0-Sair")
        try:
            n = int(input("Escolha uma das opções acima: "))
            if n == 1:
                add_treino()
            elif n == 2:
                visu_treinos()
            elif n == 3:
                editar_treino()
            elif n == 4:
                remover_treino()
            elif n == 5:
                filtrar_treinos()
            elif n == 6:
                registrar_meta()
            elif n==7:
                ver_metas()
            elif n==8:
                sugestao_wod()
            else:
                print("Essa opção não existe!")
            
            opcao = input("\nVocê deseja continuar ou sair? ")
            if opcao.lower() == 'sair':
                print("Seu programa foi encerrado com sucesso!")
                break
        except ValueError:
            print("Digite apenas números!")

menu()

def pos_treino():
    while True:
        print("\n----- MENU WOD TRACKER -----")
        print("Digite o seu tipo de treino para receber o melhor pós-treino", "\n")
        print("1 - AMRAP", "2 - EMOM", "3 - For Time")
        try:
            tipo=int(input("Escolha o seu tipo de treino: "))

            if tipo==1:
                print("Opte por carnes magras, ovos, carboidratos complexos e água")
            elif tipo==2:
                print("Opte por frango, peixes, carboidratos complexos e água")
            elif tipo==3:
                print("Opte por frango, ovos, quejos, frutas, carboidratos e água")
            else:
                print("Opção de treino inválida")
            
            opcao=input("\nVocê deseja continuar ou sair? ")
            if opcao.lower()=="sair":
                print("Seu programa foi encerrado com sucesso!")
                break
        except ValueError:
            print("Digite apenas números!")
pos_treino()
