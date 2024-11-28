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
      situacao = "aprovado"
elif media >= 5:
      recuperacao = float(input()) #ler a nota da recuperacao
      if recuperacao > (10-media):
            situacao = 'aprovado' 
      else: 
           print(nome ,"não passou na recuperação e está REPROVADO,com a nota:",recuperacao)

if faltas > 31:
       print(nome, "esta reprovado com",faltas,"faltas")
print("O aluno passou!")


print( "RELATORIO","\n" ,"nome:",nome,"\n", " notas:", n1, n2, n3, n4, "\n  média:", media, "\n faltas:", faltas,)