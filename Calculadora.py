def calculadora():
  print("Bem vindo(a) à calculadora simples!")
  print(
      "Operações disponíveis: adição(+), subtração(-), multiplicação(*) e divisão(/)"
  )

  try:
    numero1 = float(input("Digite um número: "))
    operacao = (input("Digite a operação(+, -, *, /:"))
    numero2 = float(input("Digite o segundo número:"))

    if operacao == '+':
      resultado = numero1 + numero2
    elif operacao == '-':
      resultado = numero1 - numero2
    elif operacao == '*':
      resultado = numero1 * numero2
    elif operacao == '/':
      resultado = numero1 / numero2
    else:
      print("Operação inválida. Tente novamente.")
      return

    print(f"O resultado da operação é: {resultado}")

  except ValueError:
    print("Entrada válida. Por favor, digite números válidos.")


calculadora()