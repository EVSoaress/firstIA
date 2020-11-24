def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    idade = kwargs.get('idade')
    sb = kwargs.get('sb')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

    print(nome)

    if sb is not None:
        print(sb)
    else:
        print('Sobrenome não existe')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome="Erick", sobrenome="Soares",idade = '18')