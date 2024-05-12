# Dicionário de escolha de personagens

equipes = {
    '1' : 'Vingadores',
    '2' : 'X-Men',
    '3' : 'Liga da Justiça',
    '4' : 'Vilões Marvel',
    '5' : 'Vilões DC'
}
vingadores = {
    '1' : 'Thor',
    '2' : 'Homem de Ferro',
    '3' : 'Hulk',
    '4' : 'Capitão América',
    '5' : 'Homem Formiga',
    '6' : 'Vespa',
    '7' : 'Homem Aranha',
    '8' : 'Feiticeira Escarlate',
    '9' : 'Dr. Estranho',
    '10' : 'Visão',
}
xmen = {
    '1' : 'Professor X',
    '2' : 'Ciclope',
    '3' : 'Jean Grey',
    '4' : 'Homem de Gelo',
    '5' : 'Fera',
    '6' : 'Wolverine',
    '7' : 'Tempestade',
    '8' : 'Noturno',
    '9' : 'Vampira (X-Men)',
    '10' : 'Deadpool',
}
liga = {
    '1' : 'Superman',
    '2' : 'Batman',
    '3' : 'Mulher Maravilha',
    '4' : 'Flash',
    '5' : 'Lanterna Verde',
    '6' : 'Aquaman',
    '7' : 'Caçador de Marte',
    '8' : 'Mulher-Gavião',
    '9' : 'Shazan',
    '10' : 'Arqueiro Verde',
}
viloes_marvel = {
    '1' : 'Thanos',
    '2' : 'Loki',
    '3' : 'Venom',
    '4' : 'Juggernaut',
    '5' : 'Magneto',
    '6' : 'Dr. Doom',
    '7' : 'MODOK',
    '8' : 'Ultron',
    '9' : 'Barão Zemo',
    '10' : 'Rei do Crime',
}
viloes_dc = {
    '1' : 'Darkseid',
    '2' : 'Lex-Luthor',
    '3' : 'Coringa',
    '4' : 'Adão-Negro',
    '5' : 'Brainiac',
    '6' : 'Doomsday',
    '7' : 'Bane',
    '8' : 'Sinestro',
    '9' : 'Flash-Reverso',
    '10' : 'Deathstroke',
}
tipo_criacao = {
    '1' : 'relatório de luta',
    '2' : 'probabilidade',
    '3' : 'roteiro'
}
dict_ambiente = {
    '1' : 'Torre dos Vingadores',
    '2' : 'Wakanda',
    '3' : 'Asgard',
    '4' : 'Mansão Wayne',
    '5' : 'Fortaleza da Solidão',
    '6' : 'Helicarrier',
    '7' : 'Sanctum Sanctorum',
    '8' : 'Madripoor',
    '9' : 'Atlanta',
    '10' : 'Saara'
}
dict_turno = {
    '1' : 'dia',
    '2' : 'noite'
}
dict_conhecimento = {
    '1' : 'sim',
    '2' : 'não'
}

# Funções

def selecionar_equipe(num_equipe):
    if num_equipe == 1:
        print('Selecione uma das opções abaixo para a equipe do seu primeiro personagem:\n')
        for key, value in equipes.items():
            print(f'{key} - {value}')
        equipe = input('Selecione o número da equipe da qual o seu primeiro personagem faz parte: \n')
    if num_equipe == 2:
        print('Selecione uma das opções abaixo para a equipe do seu segundo personagem:\n')
        for key, value in equipes.items():
            print(f'{key} - {value}')
        equipe = input('Selecione o número da equipe da qual o seu segundo personagem faz parte: \n')

    return equipe

def selecionar_personagem(equipe, num_equipe):
    if num_equipe == 1:
        if equipe == '1':
            print('Selecione o seu primeiro personagem: ')
            for key, value in vingadores.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu primeiro personagem: \n')
            personagem = vingadores.get(per)        
        elif equipe == '2':
            print('Selecione o seu primeiro personagem:')
            for key, value in xmen.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu primeiro personagem: \n')
            personagem = xmen.get(per)
        elif equipe == '3':
            print('Selecione o seu primeiro personagem: ')
            for key, value in liga.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu primeiro personagem: \n')
            personagem = liga.get(per)
        elif equipe == '4':
            print('Selecione o seu primeiro personagem:')
            for key, value in viloes_marvel.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu primeiro personagem: \n')
            personagem = viloes_marvel.get(per)
        elif equipe == '5':
            print('Selecione o seu primeiro personagem:')
            for key, value in viloes_dc.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu primeiro personagem: \n')
            personagem = viloes_dc.get(per)

    elif num_equipe == 2:
        if equipe == '1':
            print('Selecione o seu segundo personagem:')
            for key, value in vingadores.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu segundo personagem: \n')
            personagem = vingadores.get(per)        
        elif equipe == '2':
            print('Selecione o seu segundo personagem:')
            for key, value in xmen.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu segundo personagem: \n')
            personagem = xmen.get(per)
        elif equipe == '3':
            print('Selecione o seu segundo personagem:')
            for key, value in liga.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu segundo personagem: \n')
            personagem = liga.get(per)
        elif equipe == '4':
            print('Selecione o seu segundo personagem:')
            for key, value in viloes_marvel.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu segundo personagem: \n')
            personagem = viloes_marvel.get(per)
        elif equipe == '5':
            print('Selecione o seu segundo personagem:')
            for key, value in viloes_dc.items():
                print(f'{key} - {value}')
            per = input('Selecione o número do seu segundo personagem: \n')
            personagem = viloes_dc.get(per)

    return personagem

def selecionar_tipo_criacao():
    print('Selecione o tipo de criação desejado:')
    for key, value in tipo_criacao.items():
        print(f'{key} - {value.title()}')
    tipo_resposta = input('Tipo de criação (numérico): \n')
    return tipo_criacao.get(tipo_resposta)

def selecionar_ambiente():
    print('Selecione o ambiente para a batalha:')
    for key, value in dict_ambiente.items():
        print(f'{key} - {value.title()}')
    ambiente = input('Ambiente (numérico): \n')
    return dict_ambiente.get(ambiente)

def selecionar_turno():
    print('Selecione o horário para a batalha:')
    for key, value in dict_turno.items():
        print(f'{key} - {value.title()}')
    turno = input('Horário (numérico): \n')
    return dict_turno.get(turno)

def selecionar_conhecimento():
    print('Eles tem conhecimento prévio sobre o seu oponente? Caso sim, eles tiveram tempo para se preparar para o combate')
    for key, value in dict_conhecimento.items():
        print(f'{key} - {value.title()}')
    conhecimento = input('Conhecimento prévio (numérico): \n')
    conhecimento_previo = dict_conhecimento.get(conhecimento)

    if conhecimento_previo.lower() == 'não':
        conhecimento_previo_input = 'Eles não se conhecem previamente a esta batalha.'
    else:
        conhecimento_previo_input = 'Eles tiveram tempo para analisar os pontos fortes e fracos de seu oponente e se preparar'
    return conhecimento_previo_input


