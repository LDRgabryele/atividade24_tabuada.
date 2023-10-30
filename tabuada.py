# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
numero= int(input ("digite um número: "))
for tabuada in range(11):
    resultado = tabuada * numero
    print (f"{tabuada} * {numero} = {resultado}")