class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")
    
    def saque(self, valor):
        if len(self.saques) >= 3:
            print("Limite de saques diários excedido.")
        elif valor > 500:
            print("O valor do saque não pode exceder R$ 500,00.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    
    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso
conta = ContaBancaria()
conta.deposito(1000)
conta.saque(200)
conta.extrato()