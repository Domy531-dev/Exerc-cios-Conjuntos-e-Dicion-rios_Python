def verificar_paises():
    # Conjunto fixo com os nomes dos países da América do Sul
    paises_sul_america = {'Argentina', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela'}

    # Pede ao usuário para digitar 3 países e verifica se eles pertencem ao conjunto
    for i in range(3):
        pais = input(f'Digite o nome do {i + 1}º país: ')
        
        # Verifica se o país pertence ou não ao conjunto
        if pais in paises_sul_america:
            print(f'O país "{pais}" pertence à América do Sul.')
        else:
            print(f'O país "{pais}" NÃO pertence à América do Sul.')

# Chama a função
verificar_paises()
