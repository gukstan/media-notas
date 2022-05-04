#Pedir nome
nome = input("Digite o seu primeiro nome: ")
sobrenome = input("Digite o seu último sobrenome: ")

#Pedir as notas
port = float( input("Digite a sua nota de Português: "))
ing = float( input("Digite a sua nota de Inglês: "))
mat = float( input("Digite a sua nota de Matemática: "))
geo = float( input("Digite a sua nota de Geografia: "))

#Calcular a média
media = (port + ing + mat + geo) / 4

#Condição para ser aprovado: média maior ou igual a 5
if (media>=5):
    #Mostrar aprovação
    print("Parabéns,", nome, sobrenome + ", você foi aprovado!" " A sua nota média é:", media)
    #Mostrar reprovação
else:
    print("Infelizmente você foi reprovado,", nome, sobrenome + ". Sua nota média é:", media)