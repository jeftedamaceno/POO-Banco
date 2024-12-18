class Conta:
  def __init__(self, numero):
    self.numero = numero
    self.saldo = 0

  def creditar(self, amount):
    self.saldo += amount
    print(f"Valor creditado: {amount:.2f}")
    return self.saldo

  def debitar(self, amount):
    if self.tem_saldo() and self.saldo >= amount:
      self.saldo -= amount
      print(f"Valor Debitado: {amount:.2f}")
    else:
      print("Sem Saldo Suficiente na Conta.")
    return self.saldo

  def tem_saldo(self):
    return self.saldo > 0

  def ver_saldo(self):
    return self.saldo

  def ver_numero(self):
    return self.numero

  def set_saldo(self, saldo):
    self.saldo = saldo
    print(f"Valor do Saldo Setado para: {saldo:.2f}")