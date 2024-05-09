'''

Estrutura de repetições 

    São estruturas utilizadas para repetir um trecho de codigo determinada vezes .

    - for -> Usado quando sabemos o numero de vezes exato que nosso bloco deve executar ou percorrer um objeto iteravel


'''

texto = str(input("Informe um texto:"))
VOGAIS = 'AEIOU'

for letra in texto:
    
    if letra.upper() in VOGAIS:
        print(letra,end='')

else: 
    print("\nProcessamento finalizado !\n")

# ---> Aprendendo a função range
for numero in range(11):
    print(numero,end=' ')
    print('')


for numero in range(0,51,5):
    print(numero,end=' ')


