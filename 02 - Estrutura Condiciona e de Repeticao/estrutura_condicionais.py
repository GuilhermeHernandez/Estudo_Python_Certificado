'''

Permite desvio de fluxo de controle ,  quando determinadas expressões logicas são atendidas 

    - if 
    - if / else 
    - if / elif / else 

'''

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

# ---> Modelo 1
# if idade >= MAIOR_IDADE :
#     print("Maior de idade , pode tirar a CNH")

# if idade < MAIOR_IDADE :
#     print("Menor de idade , não pode tirar a CNH !!!")

# ---> Modelo 2
# if idade >= MAIOR_IDADE:
#     print("Maior de idade , pode tirar a CNH")

# else:
#     print("Menor de idade , não pode tirar a CNH !!!")

# ---> Modelo 3
if idade >= MAIOR_IDADE:
    print("Maior de idade , pode tirar a CNH")

elif idade >= IDADE_ESPECIAL:
    print("Pode fazer apenas aula teorica!")

else:
    print("Ainda não pode tirar a CNH")