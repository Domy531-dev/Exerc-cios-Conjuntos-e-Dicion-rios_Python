def cursos_ofertados():
    # Definindo os conjuntos de cursos
    cursos_manha = {'Matemática', 'Física', 'Biologia', 'Química', 'História'}
    cursos_noite = {'Matemática', 'Programação', 'Física', 'Geografia', 'História'}

    # Interseção: cursos oferecidos em ambos os turnos
    cursos_comum = cursos_manha & cursos_noite
    print(f'Cursos disponíveis em ambos os turnos (interseção): {cursos_comum}')

    # Diferença: cursos disponíveis somente de manhã
    cursos_so_manha = cursos_manha - cursos_noite
    print(f'Cursos disponíveis somente pela manhã: {cursos_so_manha}')

    # Diferença: cursos disponíveis somente à noite
    cursos_so_noite = cursos_noite - cursos_manha
    print(f'Cursos disponíveis somente à noite: {cursos_so_noite}')

# Chama a função
cursos_ofertados()

