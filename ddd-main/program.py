from ddd import Destino
from ddd_repository import ddd_repository
from interface_user import interface_user


ddd_repository = ddd_repository()
ddd_repository.adicionar_destino(Destino(61,"Brasilia" ))
ddd_repository.adicionar_destino(Destino(71,"Salvador" ))
ddd_repository.adicionar_destino(Destino(11,"Sao Paulo" ))
ddd_repository.adicionar_destino(Destino(21,"Rio de Janeiro" ))
ddd_repository.adicionar_destino(Destino(32,"Juiz de Fora" ))
ddd_repository.adicionar_destino(Destino(19,"Campinas" ))
ddd_repository.adicionar_destino(Destino(27,"Vitoria" ))
ddd_repository.adicionar_destino(Destino(31,"Belo Horizonte" ))

print(ddd_repository)

interface_user = interface_user(ddd_repository)

print(interface_user.saida_usuario())
