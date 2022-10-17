from ddd import ddd
from ddd_repository import ddd_repository
from interface_user import interface_user


ddd_repository = DDDREPOSITORY()
ddd_repository.set_ddd_item(ddd("Brasilia", 61))
ddd_repository.set_ddd_item(ddd("Salvador", 71))
ddd_repository.set_ddd_item(ddd("Sao Paulo", 11))
ddd_repository.set_ddd_item(ddd("Rio de Janeiro", 21))
ddd_repository.set_ddd_item(ddd("Juiz de Fora", 32))
ddd_repository.set_ddd_item(ddd("Campinas", 19))
ddd_repository.set_ddd_item(ddd("Vitoria", 27))
ddd_repository.set_ddd_item(ddd("Belo Horizonte", 31))

print(ddd_repository)

interface_user = INTERFACE_USER(ddd_repository)

while interface_user.get_interaction():
    pass
