from bank_services.banco import Banco

class Cidade:
  def __init__(self):
    self.name = input("Digite o nome da cidade: ")
    self.create_bank()
    self.bank_operation()

  def create_bank(self):
    self.bank = Banco()
    print(f"Banco da cidade de {self.name} criado com sucesso.\n")
  
  def bank_operation(self):
    while True:
      functionalities = f"""
      {'Ações disponíveis':-^23}
      1 - Cadastrar Conta
      2 - Creditar
      3 - Debitar
      4 - Saldo
      5 - Transferir
      6 - Sair
      {'-':-^23}

      """
      print(functionalities)
      option = input("Digite a opção desejada: ")

      match option:
        case "1":
          self.bank.criar_conta()
        case "2":
          amount = float(input("Digite o valor a ser creditado: ").strip())
          number = int(input("Digite o número da conta: ").strip())
          self.bank.creditar(number, amount)
        case "3":
          amount = float(input("Digite o valor a ser debitado: ").strip())
          number = int(input("Digite o número da conta: ").strip())
          self.bank.debitar(number, amount)
        case "4":
          number = int(input("Digite o número da conta: "))
          self.bank.saldo(number)
        case "5":
          origin = int(input("Digite o número da conta de origem: ").strip())
          destination = int(input("Digite o número da conta de destino: ").strip())
          amount = float(input("Digite o valor a ser transferido: ").strip())
          self.bank.transferir(origin, destination, amount)
        case "6":
          break
        case _:
          print("Opção inválida.\n")

if __name__ == "__main__":
  Cidade()