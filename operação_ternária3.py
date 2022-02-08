idade = input("Digite sua idade: ")

if not idade.isnumeric():
    print("Você precisa digitar apenas números")

else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    mensagem = "Pode acessar." if maior_de_idade else "Não pode acessar."

    print(mensagem)