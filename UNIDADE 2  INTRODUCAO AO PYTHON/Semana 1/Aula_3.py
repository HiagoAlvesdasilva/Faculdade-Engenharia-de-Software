#Estruturas= de repetiçao 'for'

numeros = [1, 2, 3, 4, 5]

for num in numeros:
  print(num)

#Estrutura de Repetiçao 'while'

numero = int(input("Digite Um Numero (Ou 0 Para Sair): "))

while numero != 0:
 if numero % 2 == 0:
    print("O Numero é Par")
 else:
    print("O Numero é Impar")
 numero = int(input("Digite Ouro Numero (Ou 0 Para Sair): "))

#Controle de Repetiçao: Funçao "range"

#Repetiçao Por Quantidade: observe que a contagem começa em 0 vai ate 4 
for x in range (5):
  print(x)

#Limites Inicial e Superior: observe que a contagem começa em 2 e vai ate 6 
for y in range (2,7):
  print(y)

#Com Incremento: observe que a começa om 1 porem faz a conta de 2 em 2 e vai ate o 9 
for z in range (1, 11, 2):
  print(z)

#PARE ou CONTINUE

#BREAK
for numero in range (1, 11):
  if numero % 2 == 0:
    print("O Primeiro Numero PAR Encontrado Foi: ", numero)
    break


#CONTINUE
for numero in range(1, 11):
  if numero == 5:
    continue
  print(numero)


#Aplicando a Aula 

#Lista de Filmes
filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

#Menu Inicial 
print("Ola Boas Vindas!!!")
print("Voce Ira Classificar Uma Sequencia De 5 Filmes Podendo Avalia-los com uma nota de 0 a 5")
print("Digite '0' a Qualquer Momento Caso Queira Parar")

#Loop Para Iterar Cada Item Na Lista
for filme in filmes:
    #Solicitando a classificaçao ao usuario
    classificacao = input(f"Como Voçe Classificaria {filme} de 1 a 5? (Ou 0 Para Parar)")

    #Verifica Se O Usuario Deseja Parar
    if classificacao == '0':
      print("Que Pena Volte Uma Proxima Vez ")
      break

    #Converte a Classificaçao Para um Numero Inteiro
    classificacao = int(classificacao)

    #Verifica Se o Usuario Digitou Um Numero Valido
    if classificacao < 1 or classificacao > 5:
      print("Numero Invalido ")