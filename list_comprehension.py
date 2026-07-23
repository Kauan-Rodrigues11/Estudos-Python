lista = [numero for numero in range(10)]

print(lista)

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

# nova_lista_produtos = [
#     {**produto} for produto in lista_produtos
# ]

# nova_lista_produtos = [
#     {'nome': produto['nome'], 'preco': produto['preco'] * 2 } if produto['preco'] > 500 else {**produto} for produto in lista_produtos
# ]

# nova_lista_produtos = [
#     {'nome': produto.get('nome'), 'preco': produto.get('preco') * 2 } if produto['preco'] > 500 else {**produto} for produto in lista_produtos
# ]

nova_lista_produtos = [
    {**produto, 'preco': produto.get('preco') * 2 } if produto['preco'] > 500 else {**produto} for produto in lista_produtos
]


print(*nova_lista_produtos, sep='\n')