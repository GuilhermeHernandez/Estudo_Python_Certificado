'''

Usamos para saber quando uma variavel aponta para determinado objeto

'''

curso_python = 'Curso de Python'
nome_curso = curso_python
saldo , limite = 200 , 200

print(curso_python is nome_curso)
print(curso_python is not nome_curso)
print(saldo is limite)