'''

String e Fatiamentos
    
    Metodos 
        - upper() -> Maiuscula
        - lower() - Minuscula
        - title() -> Nome para titulo

        - strip() -> Remove espaços em branco
        - lstrip() -> Remove espaços em branco da esquerda
        - rstrip() -> Remove espaços em branco da direita

        - center(num_caracter,"expressão") -> Centralizada uma palavra pela as expressões
        - "expressao".join(variavel) -> Junta a expressão a cada itevavel



'''

nome = 'guilheMe'

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = '    ola mundo !'

print(texto)
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

menu = ' Python '

print("------- Python -------")
print(menu.center(16 , "-"))