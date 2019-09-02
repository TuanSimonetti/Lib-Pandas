import csv

# Leitura do banco de dados
with open('C:/Users/PicPay/Desktop/users.csv', 'r') as banco_de_dados:
    ler = csv.reader(banco_de_dados)
    print("Banco de Dados carregado com sucesso")
    r = 's'
    while r == 's':
        print('\n', '')
        print('=' * 100)
        print('')
        print('M E N U')
        print('')
        print('=' * 100)
        print('')
        print('Qual a informação especifica você deseja pesquisar:')
        print('')
        print('1) ID;')
        print('2) Nome;')
        print('3) Username;')
        print('')
        resposta = str(input('Qual das opções você deseja pesquisar [inserir o número correspondete]: R.: '))


        if resposta == '1':
            id = str(input('Por gentileza, qual ID eu devo pesquisar: '))
            id in banco_de_dados
            if encontrar = True:
                return(encontrar)
            else:
                print('Esta pessoa não se encontra cadastrada em nosso banco de dados. Deseja realizar nova pesquisa?')

        if resposta == '2':
            nome = str(input('Por qual NOME eu devo pesquisar: '))
            encontrar = nome in banco_de_dados
            if encontrar = True:
                return(encontrar)
            else:
                print('Esta pessoa não se encontra cadastrada em nosso banco de dados. Deseja realizar nova pesquisa?')

        if resposta == '3':
            username = str(input('Por qual USERNAME eu devo pesquisar: '))
            encontrar = username in banco_de_dados
            if encontrar = True:
                return(encontrar)
            else:
                print('Esta pessoa não se encontra cadastrada em nosso banco de dados. Deseja realizar nova pesquisa?')

        r = str(input('Deseja resetar a calculadora para realizar novas simulações [s/n]? R.: '))
    banco_de_dados.close()