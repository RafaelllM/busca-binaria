def busca_bi(lista, objeto):
    pass

def sequencia(lista, objeto):
    posicao = 0
    for i in lista:
        posicao += 1
        if i == objeto:
            return f'O "{objeto}" foi encontrado na posição [{posicao}]'

def executar(lista, objeto):
    if len(lista) < 127:
        sequencia(lista, objeto)
    else:
        busca_bi(lista, objeto)




lista =  input('insira uma lista: ')
item = input('diga qual elemento voce quer encontrar: ')
resultado = executar(lista, item)
print(resultado)
