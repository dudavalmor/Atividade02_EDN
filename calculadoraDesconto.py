nome_produto = "Camiseta";
preco_original = 50.00;
porcentagem_desconto = 0.2;

valor_desconto = preco_original * porcentagem_desconto;
preco_final = preco_original - valor_desconto;
print("----- Resumo do Desconto -----");
print(f"Produto: {nome_produto}");
print(f"Preço Original: R$ {preco_original:.2f}");
print("Porcentagem de Desconto: {:.0%}".format(porcentagem_desconto));
print(f"Valor do Desconto: R$ {valor_desconto:.2f}");
print(f"Preço Final: R$ {preco_final:.2f}");
print("-------------------------------");