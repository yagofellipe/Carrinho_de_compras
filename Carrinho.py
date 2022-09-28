class CarrinhoDeCompras:
    def __init__(self):
      self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
      self.nome = nome
      self.valor = valor

class Serviço:
    def __init__(self, nome, valor):
      self.nome = nome
      self.valor = valor

carrinho = CarrinhoDeCompras()

pi = Produto('roteador', 300)
serv = Serviço('instalador',100)

carrinho.inserir_produto(pi)
carrinho.inserir_produto(serv)

carrinho.lista_produto()
print(carrinho.soma_total())