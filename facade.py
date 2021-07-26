#Façade

class Agente:

    def __init__(self):
        print("[ G ]  - Gerenciador....")
    
    def gerenciador(self):
        self.artefato = ProducaoUm()
        self.artefato.momento()

        self.nicho = ProducaoDois()
        self.nicho.fabricado()

        self.produto = ProducaoTres()
        self.produto.preparado()

        self.conteudo = ProducaoQuatro()
        self.conteudo.desenvolvido()

class ProducaoUm:

    def __init__(self):
        print("\nArtefato de criação")

    def _on(self):
        print("Este artefato esta operante")
        return True
    def momento(self):
        if self._on():
            print("[ okay ] - vruuummm...")


class ProducaoDois:
    def __init__(self):
        print("\nImplementos de nicho  para criação")

    def fabricado(self):
        print("[ complemento ] - Adicionar  melhora...")
        implemento =["Xx1", "Xx2", "Xx3", "Xx4", "Xx5","Xx6"]
        for i in range(len(implemento)):
            print(f'[ {i} ] - ',implemento[i])

class ProducaoTres:
    def __init__(self):
        print("\nProduto finalizado")

    def preparado(self):
        print("[ Produto ] -  Produto averiguado...")


class ProducaoQuatro:
    def __init__(self):
        print("\nConteudo exclusivo")

    def desenvolvido(self):
        confirmacao = """
| - :  .... 1
| - :  .... 2
| - :  .... 3
| - :  .... 4
""" 
        print(confirmacao)


class Solicitante:
    def __init__(self):
        print("[ USER ] - Solicitante")
    def necessidades(self):
        print("[ >> ] - Gerenciador de andamento de pedido ...")

    proc = Agente()
    proc.gerenciador()

    def __del__(self):
        print("[ Organização ] ... Sucesso\n ")


if __name__ == '__main__':
    pessoa = Solicitante()
    pessoa.necessidades()