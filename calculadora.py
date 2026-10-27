# Calculadora em Python


def mostrar_menu():
    print("=" * 42)
    print("          CALCULADORA EM PYTHON")
    print("=" * 42)
    print("  1 - Adição")
    print("  2 - Subtração")
    print("  3 - Multiplicação")
    print("  4 - Divisão")
    print("  0 - Sair")
    print()


def pedir_numero(texto):
    # fica pedindo até o usuário digitar um número válido
    while True:
        valor = input(texto).replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido! Digite apenas números.")


def tirar_zero_extra(numero):
    # mostra 20.0 como 20, mas deixa 3.5 como 3.5
    if numero == int(numero):
        return int(numero)
    return numero


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


continuar = "s"

while continuar == "s":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("\nErro: opção inválida. Escolha entre 0 e 4.\n")
        continue

    numero1 = pedir_numero("Primeiro número: ")
    numero2 = pedir_numero("Segundo número: ")
    print()

    if opcao == "1":
        resultado = somar(numero1, numero2)
        simbolo = "+"
    elif opcao == "2":
        resultado = subtrair(numero1, numero2)
        simbolo = "-"
    elif opcao == "3":
        resultado = multiplicar(numero1, numero2)
        simbolo = "x"
    else:
        simbolo = "/"
        if numero2 == 0:
            resultado = None
        else:
            resultado = dividir(numero1, numero2)

    if resultado is None:
        print("Erro: divisão por zero não é permitida.")
    else:
        n1 = tirar_zero_extra(numero1)
        n2 = tirar_zero_extra(numero2)
        res = tirar_zero_extra(resultado)
        print(f"Resultado: {n1} {simbolo} {n2} = {res}")

    print()
    continuar = input("Outro cálculo? (s/n): ").lower()
    while continuar != "s" and continuar != "n":
        continuar = input("Digite apenas s ou n: ").lower()

    if continuar == "s":
        print("\n---------- MENU PRINCIPAL ----------")

print("Programa encerrado.")
