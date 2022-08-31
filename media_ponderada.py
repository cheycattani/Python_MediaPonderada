#  Faça um programa para calcular a média ponderada de um aluno. Para isso, peça ao usuário os pesos das
#  duas provas e as notas do aluno. Ao final, imprima a média ponderada do aluno.


peso1 = float(input('Peso da nota 1: '))
peso2 = float(input('Peso da nota 2: '))
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = ((nota1*peso1) + (nota2*peso2)) / (peso1+peso2)
print('Sua média ponderada será:', round(media, 2))

#  para arredondar um número decimal, basta adicionar o round (deseja arredondar, quantas casas)

