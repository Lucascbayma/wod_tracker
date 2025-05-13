f=open("Arquivo.txt","a")
quant=int(input("Digite a quantidade de tipos de treinos que você deseja: "))
treino=[]
for i in range(quant):
   treino.append(input("Digite o treino que deseja realizar:"+"\n"))
for i in range(quant):
    print("1-Adicionar algum tipo de exercício\n2-Remover algum treino\n3-Mudar algum treino")
    n=int(input("Escolha se você quiser fazer algo com sua lista de treino algum tipo de treino da sua lista:"))
    if n==1:
        treino.append(input("Digite o treino que você deseja realizar: "))
    elif n==2:
        p=int(input("Digite o índice do treino que você deseja excluir: "))
        treino.pop(p-1)
    elif n==3:
        p=int(input("Digite o índice do treino que você deseja modificar: "))
        indi=p-1
        if len(treino)<p-1:
            print("Digite um número correto")
        else:
            nv=input("Digite o novo treino que você deseja colocar: ")
            treino[indi]=nv
    else:
        print("Essa ação não existe!")
      
for i in treino:
   f.write(i + "\n")
print(treino)