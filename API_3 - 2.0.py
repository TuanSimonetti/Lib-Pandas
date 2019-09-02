#importação da biblioteca pandas. Essa biblioteca(lib) é util para adminsitração de Data Science
import pandas as pd

# Leitura e reconhecimento do algoritmo do banco de dados "users - Copia.csv"
dataset = pd.read_csv('C:/Users/PicPay/Desktop/users.csv', sep=',')
print('')
print('')
# menu
r = ("s")
while r == "s":
    pesquisa = str(input('Você deseja buscar pelo ID, Nome ou Username? '))

    if pesquisa == "ID":
        usuário = str(input('Qual o ID do usuário? '))
        print('')
        print(dataset.loc[dataset['ID'] == str(usuário)])
        print('')
        print('')

    if pesquisa == "Nome":
        usuário = str(input('Qual NOME do usuário? '))
        print('')
        print(dataset.loc[dataset['Nome'] == str(usuário)])
        print('')
        print('')

    if pesquisa == "Username":
        usuário = str(input('Qual o USERNAME do usuário? '))
        print('')
        print(dataset.loc[dataset['Username'] == str(usuário)])
        print('')
        print('')

    if pesquisa == "n":
        break

print('')
print('')
print("PESQUISA ENCERRADA.")
