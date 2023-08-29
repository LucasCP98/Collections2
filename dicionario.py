dicionario = {
    "carro": 1,
    "moto": 2,
    "bicicleta": 3,
    "caminhão": 4,
    "lancha": 5,
}
verificar_valor = dicionario.get("triciclo", 0)  # Interessante, se não existir o valor passado "triciclo", return 0
# FIXME: Nesse caso do get devolver o valor 0, tem como fazer como padrão importando collections
deletar_valor = dicionario.pop("carro")  # remove o item do dicionario
del dicionario["lancha"]  # tbm remove o item do dicionario
dicionario.popitem()  # remove o ultimo item do dic
print("carro, removido", dicionario)
print(dicionario["moto"])
print(type(dicionario))

