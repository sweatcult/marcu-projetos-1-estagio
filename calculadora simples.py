# calculadora das 4 operações
import operator

# dicionário de operadores
dict_operadores = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# loop principal
while True:
    print("Calculadora Simples:")
    print("")
    print("Escolha sua operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair da calculadora")
    print("")

    # solicita a escolha da operação ao usuário
    opcao = int(input("Digite sua opção (1/2/3/4/5): "))

    # verifica se o usuário deseja sair
    if opcao == 5:
        print("Saindo da calculadora.")
        break

    # verifica se a opção é inválida e continua o loop
    if opcao < 1 or opcao > 4:
        print("Opção inválida.")
        continue

    # solicita os números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("")

    # verifica se ambos os números são inteiros
    if num1.is_integer() and num2.is_integer():
        num1 = int(num1)
        num2 = int(num2)

    # obtém o operador com base na escolha do usuário
    operador = list(dict_operadores.keys())[opcao - 1]

    # verifica se a operação é uma divisão por zero
    if operador == '/' and num2 == 0:
        print("Erro: Divisão por zero.")
        print("")
        print("Deseja realizar uma nova operação?")
        print("1. Sim")
        print("2. Não")
        nova_op = float(input("Digite aqui o seu valor (1/2): "))
        print("")
        if nova_op == 1:
            continue
        elif nova_op == 2:
            break
    else:
        # realiza a operação e exibe o resultado
        resultado = dict_operadores[operador](num1, num2)
        print(f"{num1} {operador} {num2} = {resultado}")
        print("")
        # caso deseje ou não realizar outra operação
        print("Deseja realizar uma nova operação?")
        print("")
        print("1. Sim")
        print("2. Não")
        print("")
        nova_op = float(input("Digite aqui o seu valor (1/2): "))     
        if nova_op == 1:
            continue
        elif nova_op == 2:
            print("Saindo da calculadora")