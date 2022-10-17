from ddd_repository import ddd_repository 
from ddd import ddd

class interface_user:
    def __init__(self, ddd_repository) -> None:
        self.ddd_repository = ddd_repository
    def solicitar_input_usuario(self) -> str:
        local = str(input("Diga um local: "))
        ddd = int(input("Escolha um ddd: "))
        destino = Destino(local,ddd)

        if not self.ddd_repository.adicionar_destino(destino):
            return "DDD já existente"
        return "DDD adicionado com sucesso!"
    def exibir_destinos(self)-> list:
        return self.ddd_repository
    def saida_usuario(self)-> str:
        ddd = int(input("Diga o ddd: "))
        return (f"DDD: {ddd} Destino: {self.ddd_repository.obter_destino_pelo_ddd(ddd)}")
