conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 4000
cheque_especial = 500

if conta_normal :

    if saldo >= saque :
        print('Saque realizado com sucesso !')
    
    elif saque <= (saldo + cheque_especial) :
        print('Saque realizado com uso do cheque especial !')

    else :
        print('Saldo insuficiente !')

elif conta_universitaria:

    if saldo >= saque :
        print('Saque realiado com sucesso !')

    else :
        print('Saldo insuficiente !')

else :
    print('Sistema não reconheceu tipo de conta , entre em contato com seu gerente !')