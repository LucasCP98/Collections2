usuarios_machine_learn = [1, 2, 3, 4, 5]
usuarios_big_data = [6, 7, 8, 9, 10, 2]
setando = set(usuarios_machine_learn)  # Set cria um conjunto e elimina os números repetidos.
print(setando)

adicionando = frozenset(usuarios_big_data)  # ele vai congelar a lista, tornando-a imutavel, caso eu tente adiciona algo dará erro, nem aparece o apeend mais.
# print(adicionando.append()) "'frozenset' object has no attribute 'append'"
print(adicionando)

