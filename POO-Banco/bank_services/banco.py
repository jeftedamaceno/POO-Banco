from bank_services.conta import Conta
from bank_services.conta_poupanca import ContaPoupanca
import random

class Banco:
  def __init__(self, account_length=100, name="Banco"):
    self.contas = [None] * account_length
    self.indice = 0
    self.name = name
    self.id = random.randint(1000, 9999)

  def cadastrar(self, conta):
    self.contas[self.indice] = conta
    self.indice += 1

  def procurar_conta(self, numero):
    result = None

    print("numero:", numero)

    for conta in self.contas:
      if conta != None and conta.ver_numero() == numero:
        result = conta
        break

    return result

  def creditar(self, numero, valor):
    conta = self.procurar_conta(numero)
    if conta:
      conta.creditar(valor)
    else:
      print("Conta Inexistente.")

  def debitar(self, numero, valor):
    conta = self.procurar_conta(numero)
    if conta:
      conta.debitar(valor)
    else:
      print("Conta Inexistente.")

  def saldo(self, numero):
    conta = self.procurar_conta(numero)
    if conta:
      print(f"Saldo Disponível: {conta.ver_saldo():.2f}")
    else:
      print("Conta Inexistente.")

  def criar_conta(self):
    numero = random.randint(1000, 9999)
    account_type = input("Digite o tipo de conta (1 - Conta Corrente, 2 - Conta Poupança): ").strip()
    conta = None
    if account_type == "1":
      conta = Conta(numero)
    else:
      conta = ContaPoupanca(numero)
    self.cadastrar(conta)
    print(f"Conta criada com sucesso. Número da conta: {numero}")

  def transferir(self, origem, destino, valor):
    conta_origem = self.procurar_conta(origem)
    conta_destino = self.procurar_conta(destino)

    if conta_origem and conta_destino:
      conta_origem.debitar(valor)
      conta_destino.creditar(valor)
    else:
      print("Uma das contas não existe.")

  def get_nome(self):
    return self.name

  def __display(self):
    for conta in self.contas:
      if conta:
        print(f"Conta: {conta.ver_numero()} Saldo: {conta.ver_saldo()}")

  def _length(self):
    return self.indice

  def get_id(self):
    return self.id