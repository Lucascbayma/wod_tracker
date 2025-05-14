treino=[]
f=open("Arquivo.txt", "a")

qnt=int(input("Digite a quantidade de exercícios que você deseja adicionar: "))

for i in range(qnt):
    treino.append(input(f"Digite o {i+1}° exercício que deseja realizar:"))

while True:
    opcao=input("\nVocê deseja continuar ou sair? ")

    if opcao.lower()=='sair':
        break
    else:
        print("1-Adicionar exercício\n2-Visualizar exercício(s)\n3-Mudar exercício\n4-Remover exercício")
        n=int(input("Escolha uma das opções acima: "))

        if n==1:
            treino.append(input("Digite o exercício que você deseja adicionar: "))
        elif n==2:
            for indice, item in enumerate(treino, start=1):
                print(f"{indice}- {item}")
        elif n==3:
            p=int(input("Digite o índice do exercício que você deseja modificar: "))
            if p<1 or p>len(treino):
                print("Índice inválido!")
            else:
                nv=input("Digite o novo exercício que você deseja colocar: ")
                treino[p-1]=nv
        elif n==4:
            p=int(input("Digite o índice do exercício que você deseja excluir: "))
            if p<1 or p>len(treino):
                print("Índice inválido!")
            else:
                treino.pop(p-1)
        else:
            print("Essa ação não existe!")

for item in treino:
    f.write(item + "\n")

f.close()
print("O seu treino foi salvo e o programa foi encerrado!")