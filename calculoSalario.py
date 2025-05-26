numero_funcionario = int(input("Digite o número do funcionário: "));
quantidade_horas = int(input("Digite a quantidade de horas trabalhadas: "));
valor_hora = float(input("Digite o valor da hora trabalhada: "));

salario = quantidade_horas * valor_hora;

print("----- Resumo do Salário -----");
print(f"Número do Funcionário: {numero_funcionario}");
print(f"Quantidade de Horas Trabalhadas: {quantidade_horas} horas");
print(f"Valor da Hora Trabalhada: R$ {valor_hora:.2f}");
print(f"Salário: R$ {salario:.2f}");
print("-----------------------------");