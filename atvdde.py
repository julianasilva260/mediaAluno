qntdAluno = int(input("digite a quantidade de aluno:"))
for i in range(qntdAluno):
      print("Digite o nome:") 
      nome = input()
      print("digite a 1º nota:")
      n1 = float(input())
      print("digite a 2º nota:")
      n2 = float(input())
      print("digite a 3º nota:")
      n3 = float(input())
      print("digite a 4º nota:")
      n4 = float(input())
      media = (n1+n2+n3+n4)/4
      print("digite a quantidade de faltas do aluno:")   
      faltas = int(input())

if media >= 8:
     print("O",nome, "esta aprovado com:",media)
else:
      print(nome,"esta reprovado e vai ter que fazer recuperação,por que tirou nota baixa",media)
print("digite quanto o", "aluno tirou na recuperação")
recuperacao = float(input())
if recuperacao >= 5:
      print("O aluno tirou",recuperacao ,"na recuperação")
else:
      print("o aluno não passou na recuperação,por que tirou",recuperacao)
if recuperacao < 5:
      print(nome,"esta reprovado por não alcançar a nota da recuperção e ficou com:",recuperacao)
elif faltas > 31:
      print(nome, "esta reprovado com",faltas)

