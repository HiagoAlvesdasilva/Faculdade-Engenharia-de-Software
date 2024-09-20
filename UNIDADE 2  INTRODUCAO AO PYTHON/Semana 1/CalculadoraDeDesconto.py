# Solicita ao usuário que insira o valor do produto e o percentual de desconto
valor_produto = float(input("Digite o Valor Do Produto: R$ ")) 
percentual_desconto = float(input("Qual o Percentual de desconto: "))

# Verifica se o percentual de desconto está dentro dos limites aceitáveis
if percentual_desconto < 0 or percentual_desconto > 15:
    print("Erro: O Percentual Deve Estar Entre 0% e 15%")
else:
    # Calcular desconto
    desconto = valor_produto * (percentual_desconto / 100)

    # Calcular o valor final
    valor_final = valor_produto - desconto

    # Exibir o valor final da compra
    print(f"Valor com desconto: R$ {valor_final:.2f}")