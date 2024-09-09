class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
    
    def deposito(self, valor):
        if self._validar_valor(valor):
            self._realizar_deposito(valor)
    
    def saque(self, valor):
        if self._validar_saque(valor):
            self._realizar_saque(valor)
    
    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            self._imprimir_movimentacoes()
            print(f"Saldo atual: R$ {self.saldo:.2f}")
    
    def _validar_valor(self, valor):
        """Valida se o valor do depósito ou saque é positivo."""
        if valor <= 0:
            print("O valor deve ser positivo.")
            return False
        return True

    def _validar_saque(self, valor):
        """Valida se o saque pode ser realizado."""
        if len(self.saques) >= 3:
            print("Limite de saques diários excedido.")
            return False
        if valor > 500:
            print("O valor do saque não pode exceder R$ 500,00.")
            return False
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        return True

    def _realizar_deposito(self, valor):
        """Realiza o depósito e atualiza o saldo e o registro de depósitos."""
        self.saldo += valor
        self.depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    
    def _realizar_saque(self, valor):
        """Realiza o saque e atualiza o saldo e o registro de saques."""
        self.saldo -= valor
        self.saques.append(valor)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    
    def _imprimir_movimentacoes(self):
        """Imprime as movimentações de depósito e saque."""
        for deposito in self.depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R$ {saque:.2f}")

# Exemplo de uso
conta = ContaBancaria()
conta.deposito(1000)
conta.saque(200)
conta.extrato()