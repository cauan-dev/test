vendas = [127, 712 ,2324, 84]
print(vendas[-1])

total_de_soma = sum(vendas)#soma das vendas
print(total_de_soma)

quantidade_de_vendas = len(vendas)#pega a quantidade de vendas
print(quantidade_de_vendas)
valor_max = max(vendas) #pega o maior valor da lista
valor_min = min(vendas)#pega o menor valor da lista
print(valor_max, valor_min)

posicao = vendas.index(712) #procura a posição do numero dentro da lista
print(posicao)

print(vendas[:2])#pega um pedaço da sua lista

produtos = ["S24 ultra", "xaomi 13 ultra"]
precos = [2000, 4000]

print("S24 ultra"in pr odutos)
precos[0] = 3500
print(precos)
precos[1] = precos[1] * 1.1
print(precos)

#append
produtos.append("rog phone 7")#adiciona um item na variavel
precos.append(5000)
print(produtos)
print(precos)

#remove and pop
produtos.remove("rog phone 7")# vc precisa saber qual é o cara inserido
precos.pop(-1)# vc nao precisa saber qual o cara 
print(produtos)
print(precos)

# insert
produtos.insert(1,"rog phone 7")
precos.insert(1, 5000)
print(produtos)
print(precos)

#count
print(produtos.count("rog phone 7")) # conta quantas vezes tem um item

# ordenar
precos.sort() # ordem crescente
print(precos)
precos.sort(reverse=True) # ordem decrescente
print(precos)
