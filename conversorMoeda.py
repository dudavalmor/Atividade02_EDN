valorReal = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

valorDolar = valorReal / taxaDolar
valorEuro = valorReal / taxaEuro

print("----- Resumo Conversor de Moedas -----");
print(f"Valor em Reais: R$ {valorReal:.2f}");
print(f"Valor em dólares: US$ {valorDolar:.2f}") 
print(f"Valor em Euros: € {valorEuro:.2f}");
print("-------------------------------------");


