'''

Função input
    - builtin
    - Ex : nome = input("Digite o seu nome")
    
Função print
    - builtin
    - Ex : print(nome,sobrenome, end='...\n') -> Temina em ... e quebra de linha
    - Ex : print(nome,sobrenome, sep='#')

'''

nome = input("Informe seu nome :")
idade = input("Informe sua idade :")

print(nome,idade , sep=', ')
print(nome,idade , end='...')