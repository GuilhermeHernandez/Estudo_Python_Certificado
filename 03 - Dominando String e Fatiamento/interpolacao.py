nome = 'Guilherme'
idade = 23 
profissao = 'Programador'
linguagem = 'Python'
saldo = 500.7984894

dados = {'nome' : 'Guilherme', 'idade' : 23}

print("Nome: %s - Idade: %d" % (nome,idade))

print("Nome: {} - Idade: {}".format(nome,idade))
print("Nome: {1} - Idade: {0}".format(idade,nome))

print("Nome: {nome} - Idade: {idade}".format(nome = nome, idade = idade))
print("Nome: {nome} - Idade: {idade}".format(**dados))

print(f"Nome: {nome} - Idade: {idade}")
print(f"Nome: {nome} - Idade: {idade} - Saldo: {saldo:.2f}")

