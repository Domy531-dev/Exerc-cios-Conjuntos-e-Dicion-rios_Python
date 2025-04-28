def analisador_de_caracteres():
    # Pede ao usuário para digitar uma frase
    frase = input('Digite uma frase: ')
    
    # Cria um conjunto para armazenar caracteres únicos
    caracteres_unicos = set(frase)

    # Exibe a quantidade de caracteres diferentes
    print(f'\nQuantidade de caracteres diferentes: {len(caracteres_unicos)}')

    # Exibe os caracteres únicos
    print(f'Caracteres diferentes: {caracteres_unicos}')

# Chama a função
analisador_de_caracteres()

