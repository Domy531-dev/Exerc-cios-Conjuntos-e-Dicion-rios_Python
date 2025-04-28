def cadastro_de_produtos():
    # Cria um dicionário vazio para armazenar os produtos e seus preços
    produtos = {}

    # Pede para o usuário cadastrar 3 produtos e seus preços
    for i in range(3):
        produto = input(f'Digite o nome do {i + 1}º produto: ')
        preco = float(input(f'Informe o preço do produto "{produto}": R$ '))
        produtos[produto] = preco

    # Exibe todos os produtos e seus preços
    print("\nProdutos cadastrados e seus preços:")
    for produto, preco in produtos.items():
        print(f'{produto}: R$ {preco:.2f}')

    # Calcula o preço médio dos produtos
    preco_medio = sum(produtos.values()) / len(produtos)
    print(f'\nPreço médio dos produtos: R$ {preco_medio:.2f}')

# Chama a função
cadastro_de_produtos()
