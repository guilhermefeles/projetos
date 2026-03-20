# Cálculo do consumo de energia em kWh / entrada de dados
aparelho = input("Informe o aparelho que deseja calcular o consumo de energia: ")
potencia = float(input("Informe a potência do aparelho em watts: "))
tempo = float(input("Informe o uso diário do aparelho em horas: "))
consumoMensal = (potencia * tempo * 30) / 1000

# Saída formatada
print(
f"""
{'-'*50}

{"":<5}Aparelho: {aparelho}
{"":<5}Consumo Mensal: {consumoMensal:.2f} kWh

{"":<5}Valor a pagar: R$ {consumoMensal * 0.75:.2f}

{'-'*50}
""")