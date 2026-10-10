
print("Olá aluno, favor informe as notas solicitadas abaixo para verificação da situação no sistema")
nota_01 = float(input("Informe a nota 1: "))
nota_02 = float(input("Informe a nota 2: "))
nota_03 = float(input("Informe a nota 3: "))
nota_04 = float(input("Informe a nota 4: "))
notas = [nota_01, nota_02, nota_03, nota_04]

maxima = (max(notas))
minimo = (min(notas))

print(f"Informo que sua nota máxima é {maxima}, a minima é {minimo} e a soma de todas as notas é {sum(notas)}")

media = float(sum(notas)/len(notas))

if media >= 6:
    print(f"Sua média é {media}, portanto você está aprovado!")
else:
    print(f"Sua média é {media}, portanto você está reprovado!")  
