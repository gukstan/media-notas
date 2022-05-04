#Pedir as notas
port = float( input("Digite a sua nota de Português: "))
ing = float( input("Digite a sua nota de Inglês: "))
mat = float( input("Digite a sua nota de Matemática: "))
geo = float( input("Digite a sua nota de Geografia: "))

#Calcular a média
media = (port + ing + mat + geo) / 4

#Mostrar a média
print("A sua nota média é: ", media)