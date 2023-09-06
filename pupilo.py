
opcao = 0

def selecione_resultado():
    if opcao == 1:
        nome = input ("Digite seu nome:")
        data = int(input ("Informe Ano de nascimento:"))
        valor1 = 2023
        valor2 = data 
        idade = valor1 - valor2

        def calcular_idade():
            if idade >= 18:
                print("Venha buscar sua reservista\n\n")
        
            elif idade <= 18:
                print("Se aliste\n\n")
        calcular_idade()
    else:
        print("Escolha inválida.\n\n")

while True:
    opcao = int(input("Selecione uma opção: \n1 - Consultar alistamento. \n2 - Sair:\n\nDigite aqui: "))
    if(opcao == 2):
        print("Você saiu do programa")
        break
    else:
        selecione_resultado()