from interface_user import interface_user
from ddd import Destino
from ddd_repository import ddd_repository


def test_solicitar_input_usuario():
    retorna_destino = Destino(77,"Cogulandia")
    repository = ddd_repository()
    interface = interface_user(repository)
    repository.adicionar_destino(retorna_destino)
  

    #Act

    ddd_existe = interface.solicitar_input_usuario()
    ddd_nao_existe = interface.solicitar_input_usuario()
    #Assert
    assert ddd_existe == "DDD já existente"
    assert ddd_nao_existe == "DDD adicionado com sucesso!"