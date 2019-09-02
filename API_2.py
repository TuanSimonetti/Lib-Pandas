import matplotlib.pyplot as plt


dados = open("C:/Users/PicPay/Desktop/users.csv").readlines()

x = []
y = []
z = []
pesquisa = str(input("Me informe o ID, nome ou username: "))

for i in range(len(dados)):

    linha = dados[i].split(";")
    x.append(str(linha[0]))
    y.append(str(linha[1]))
    z.append(str(linha[2]))

plt.plot(x, y, z)
plt.title("Users")
plt.