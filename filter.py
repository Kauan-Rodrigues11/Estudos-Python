# lista = [n for n in range(10)]

# nova_lista = [n * 2 for n in lista if n * 2 > 5]

# numero = lambda x: x > 2
# quadrado = lambda x: x ** 2

# maior_que_5 = lambda x: x > 5

# lista_maior_que_5 = []
# for n in lista:
#     if maior_que_5(n):
#         lista_maior_que_5.append(n)

# print(lista_maior_que_5)
        

lista_produtos = [
    {
        'nome': 'bicicleta',
        'preco': 1299
    },
    {
        'nome': 'patins',
        'preco': 390
    },
    {
        'nome': 'bola de futsal',
        'preco': 150
    },
    {
        'nome': 'skate',
        'preco': 700
    }

]

lista_numeros = [1, 2, 4, 8, 16, 32]

def filtro(num):
    if num > 5:
        return True
    else:
        return False
    
def filtro_dict(dict):
    if dict['preco'] > 1000:
        return True
    else:
        return False


# nova_lista_produtos = filter(lambda p: p['preco'] > 10, lista_produtos)

nova_lista_produtos = filter(filtro_dict, lista_produtos)

print(*nova_lista_produtos)
