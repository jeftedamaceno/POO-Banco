from bank_services.banco import Banco

class BancoLista(Banco):
  def __init__(self, length):
    self.bancos = []

  def append(self, conta):
    self.bancos.append(conta)

  def insert(self, index, conta):
    self.bancos.insert(index, conta)

  def pop(self, index):
    self.bancos.pop(index)

  def empty(self):
    return self.bancos == []

  def find_by_id(self, bank_id):
    result = None

    for banco in self.bancos:
      if banco.get_id() == bank_id:
        result = banco
        break

    return result

  def find_by_name(self, bank_name):
    result = None

    for banco in self.bancos:
      if banco.get_nome() == bank_name:
        result = banco
        break

    return result

  def remove(self, bank_id):
    self.bancos.remove(self.find_by_id(bank_id))

  def length(self):
    return len(self.bancos)

  def show(self):
    for banco in self.bancos:
      info = f"""
      {'Informações do Banco':-^23}
      Nome: {banco.name}
      ID: {banco.get_id()}
      Número de Contas: {banco._length()}
      {'-':-^23}
      """

      print(info)


if __name__ == "__main__":
  banco = BancoLista(100)
  banco.append(Banco(100, "Banco do Brasil"))
  banco.append(Banco(100, "Banco Itaú"))
  banco.append(Banco(100, "Banco Bradesco"))
  banco.show()
  bank = banco.find_by_name("Banco Itaú")
  banco.remove(bank.get_id())
  banco.show()
  banco.pop(0)
  banco.show()
  banco.insert(0, Banco(100, "Banco Santander"))
  banco.show()
  print(banco.empty())
  print(banco.length())
  print(banco.find_by_id(1002))
  print(banco.find_by_id(1001))