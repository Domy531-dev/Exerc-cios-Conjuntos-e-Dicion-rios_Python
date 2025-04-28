def cadastrar_cidades():
    # Cria um conjunto vazio
    cidades = set()

    # Pede para o usuário digitar 8 nomes de cidades
    for i in range(8):
        cidade = input(f'Digite o nome da cidade {i + 1}: ')
        cidades.add(cidade)

    # Exibe o número de cidades diferentes
    print(f'\nNúmero de cidades diferentes cadastradas: {len(cidades)}')

    # Exibe o conjunto completo de cidades
    print(f'Cidades cadastradas: {cidades}')

# Chama a função
cadastrar_cidades()
