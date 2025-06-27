from math import tan, radians
a = b = l = 1

while True:
    print('='*40)
    print(f'{'CÁLCULO DE PARÂMETROS URBANISTÍCOS':^40}')
    print(f'{'Construído por RAFAEL MILAGRE':^40}')
    print(f'{'Cidade: Divinópolis/MG':^40}')
    print('='*40)

    pergunta0 = int(input('''Qual gabarito deseja calcular? 
    
[ 1 ] - GABARITO FRONTAL

[ 2 ] - GABARITO LATERAL 

[ 3 ] - GABARITO DE FUNDO

OPÇÃO: '''))
    if pergunta0 == 1:
        a = float(input('Digite o nivel da intersecção direita do alinhamento: '))
        b = float(input('Digite o nivel a intersecção esquerda do alinhamento: '))
        l = float(input('Digite a largura da via: '))
        pergunta2 = int(input('''Gostaria de adicionar um afastamento FRONTAL? 
[ 1 ] - SIM 
[ 2 ] - NÃO 
OPÇÃO: '''))
        media = (a + b) / 2
        ha = (l * tan(radians(65))) + 8

        if pergunta2 == 1:
            af = float(input('Qual é o afastamento FRONTAL? '))
            h2 = af * tan(radians(65))
            print('=' * 40)
            print(f'{'CÁLCULO DE GABARITO FRONTAL':^40}')
            print('=' * 40)
            print(f'''A altura máxima da sua edificação no alinhamento considerando o
afastamento frontal de {af}m e de acordo com os níveis informados será de \033[1m{ha + media + h2:.3f}m\033[m.''')

        elif pergunta2 == 2:
            print('=' * 40)
            print(f'{'CÁLCULO DE GABARITO FRONTAL':^40}')
            print('=' * 40)
            print(f'''A altura máxima da sua edificação no alinhamento sem considerar
afastamento frontal e de acordo com os níveis informados será de \033[1m{ha + media:.3f}m\033[m.''')

    elif pergunta0 == 2:
        questao = int(input('''Qual referência gostaria de usar? 
[ 1 ] - INTERSEÇÃO ALINHAMENTO 
[ 2 ] - PONTO MÉDIO LATERAL 
OPÇÃO: '''))
        if questao == 1:
            a = float(input('Digite o nivel da interseção direita do alinhamento: '))
            b = float(input('Digite o nivel a interseção esquerda do alinhamento: '))
            add = float(input('Digite o afastamento minimo da divisa direita: '))
            ade = float(input('Digite o afastamento minimo da divisa esquerda: '))

            hed = (add * tan(radians(60))) + 17.50
            hee = (ade * tan(radians(60))) + 17.50

            print('')
            print('=' * 40)
            print(f'{'CÁLCULO DE GABARITO LATERAL DIREITA':^40}')
            print('=' * 40)
            print(f'''A altura máxima da sua edificação na lateral direita 
de acordo com os níveis informados será de \033[1m{hed + a:.3f}m\033[m.''')

            print('')
            print('=' * 40)
            print(f'{'CÁLCULO DE GABARITO LATERAL ESQUERDA':^40}')
            print('=' * 40)
            print(f'''A altura máxima da sua edificação na lateral esquerda 
de acordo com os níveis informados será de \033[1m{hee + b:.3f}m\033[m.
''')
        elif questao == 2:
            a = float(input('Digite o nivel do ponto médio da lateral direita: '))
            b = float(input('Digite o nivel do ponto médio da lateral esquerda: '))
            add = float(input('Digite o afastamento minimo da divisa direita: '))
            ade = float(input('Digite o afastamento minimo da divisa esquerda: '))

            hed = (add * tan(radians(60))) + 17.50
            hee = (ade * tan(radians(60))) + 17.50

            print('')
            print('=' * 40)
            print(f'{'CÁLCULO DE GABARITO LATERAL DIREITA':^40}')
            print('=' * 40)
print(f'''A altura máxima da sua edificação na lateral direita 
        de acordo com os níveis informados será de \033[1m{hed + a:.3f}m\033[m.''')

            print('')
            print('=' * 40)
            print(f'{'CÁLCULO DE GABARITO LATERAL ESQUERDA':^40}')
            print('=' * 40)
            print(f'''A altura máxima da sua edificação na lateral esquerda 
de acordo com os níveis informados será de \033[1m{hee + b:.3f}m\033[m.
''')