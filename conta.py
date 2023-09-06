a = 2
b = 1

equacao = input ("Digite a fórmula geral da equação linear (a * x + b): ")
print (f"\na entrada do usuário {equacao} é do tipo {type(equacao)}")

for x in range(11):
    y = eval(equacao)
    print (f"\nResultado de aquacão para x = {x} é {y}")