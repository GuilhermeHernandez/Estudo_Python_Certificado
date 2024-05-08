'''

Conversão de tipo

    Em alguns momentos é necessario alterar o tipo de uma variavel .


    Inteiro -> Float
        - preco = 10
        - preco = float(preco)
        - 10.0

    Float -> Inteiro
        - preco = 10.56651
        - preco = int(preco)
        - 10

    Conversão por divisão

        - preco / 2 = 5.0 -> Float
        - preco // 2 = 5 -> Int

    Numerico -> String (Quando queremos concatenar numero com texto)

    - preco = 10.50
    - idade = 23

    - str(preco) -> 10.5
    - str(idade) -> 23

    - texto = f'idade :{idade} , preco :{preco}'
    - texto 

    Erro de conversão
    
    preco = 'python'
    print(float(preco))


'''
# ---> Conversão de inteiro
print(int(1.0))
print(int(1.9))

# ---> String para inteiro
print(int('10'))

# ---> String para float
print(float('10.5494'))

# ---> inteiro para float
print(float(100))

# ---> float para string
print(str(10.00))

valor = 10
valor_str = str(valor)

print(type(valor))
print(type(valor_str))