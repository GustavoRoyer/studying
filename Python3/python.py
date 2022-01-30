
class EstoqueClientes:
    def __init__(self, cnpj, cliente, estoque_placas_carro, estoque_placas_moto, media_carro, media_moto):
        self.__codigo = 0
        self.__cnpj = cnpj
        self.__estoque_carro = estoque_placas_carro
        self.__estoque_carro = estoque_placas_moto
        self.__media_carro = media_carro
        self.__media_moto = media_moto
        self.__cliente = cliente

    def add_cliente(self, cnpj, nome):
        self.__codigo += 0
        self.__cnpj = cnpj
        self.cliente = nome
        self.__estoque_carro = 0
        self.__estoque_moto = 0
        self.__media_carro = 0
        self.__media_moto = 0


        

    def deposita(self, valor):
        self.__saldo += valor

        