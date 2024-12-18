from bank_services.conta import Conta

class ContaPoupanca(Conta): 
  def __init__(self, numero):
    super().__init__(numero)

  def render_juros(self, taxa):
    self.creditar(self.saldo * taxa)

  def ver_saldo(self):
    self.render_juros(0.1)
    return self.saldo