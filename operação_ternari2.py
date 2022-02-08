#idade = 18

#if idade >= 18
#    print("Pode acessar")
#else:
#    print("Não pode acessar")

idade = int(input("Idade: "))
maior_de_idade = (idade >=18)
mensagem = "Pode acessar" if maior_de_idade else "Não pode acessar"
print(mensagem)

