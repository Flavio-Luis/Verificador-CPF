import os

condicao = True

while condicao:

    list_cpf = []
    list_cpf_mult = []
    cpf_nine_digit = ""
    cpf_gerado = []

    for i in range(11): # for para ter apenas 11 dígitos no CPF
        while True: # while para retornar toda vez que o cliente digitar letra ou mais de um número por vez

            try: # try para tratar o erro ao digitar letra no lugar de número
                cpf = int(input(f"Digite o {i+1} dígito do seu CPF: "))

                cpf_trat = len(str(cpf)) # usei o typecast para converter o cpf em str, e com isso usar o len() para que a variavel cfop_trat, recebe quantos caracteres tem dentro da string, porque ela é iteravel, e o programa só aceita um dígito por vez

                if cpf_trat == 1: # analisando se o usuário digitou apenas um dígito
                    list_cpf.append(cpf) # se digitou apenas um dígito ele adiciona esse cpf na lista list_cpf
                    cpf_gerado.append(cpf) # criei uma nova list para armazenar os noves primeiros dígitos do usuário, os dois últimos números eu vou exluir depois, para uma explicação mais clara, confira a OBS no rodapé

                else:
                    print("Digite apenas um número!")
                    continue

                break
            except ValueError:
                print("Digite apenas números!")
                continue
    
    for i in range(9): # loop para colocar os valores multiplicados em uma outra lista
        number = list_cpf[i] * (10-i)
        list_cpf_mult.append(number)

    number = 0 # nova atribuição para a variavel number, para realizar ioutro loop

    for i in range(9): # loop para somar todos os valores duplicados e armazenar na variavel "number"
        number = number + list_cpf_mult[i]
    
    number = number * 10 # conta da regra de negócio
    number = number % 11 # conta da regra de negócio

    if number > 9: # condição para validar se o resultado é maior que 9
        one_digit = 0
    else:
        one_digit = number

    list_cpf_mult.clear() # exclui os dados da lista, para não ter que criar outra, pois como eu já armazei o valor do primeiro dígito na variavel one_digit, não tem o porque eu deixar essa lista com os dados antigos

    for i in range(10): # loop para colocar um uma outra lista os valores multiplicados
        number = list_cpf[i] * (11-i)
        list_cpf_mult.append(number)


    number = 0 # nova atribuição para a variavel number, para realizar ioutro loop

    for i in range(10): # loop para somar todos os valores duplicados e armazenar na variavel "number"
        number = number + list_cpf_mult[i]
    
    number = number * 10 # conta da regra de negócio
    number = number % 11 # conta da regra de negócio

    if number > 9: # condição para validar se o resultado é maior que 9
        two_digit = 0
    else:
        two_digit = number

    
    del cpf_gerado[10] # foi necessário apagar o indice 10 e 9 dessa lista de cpf_gerado, confira o porque na observação no rodapé
    del cpf_gerado[9]
    cpf_gerado.append(one_digit)  # foi necessário adicionar esses dados na lista, confira a OBS no rodapé 
    cpf_gerado.append(two_digit)


    if cpf_gerado == list_cpf: # conferindo se as duas listam batem, se bater CPF válido, se não bater, inválido
        print("\nCPF VÁLIDO ✔")
    else:
        print("\nCPF INVÁLIDO ❌\n")
   

    print("\nResponda com 'sim' ou 'nao'") # capacidade de encerrar o programa ou recomeçar
    resposta=(input("Deseja continuar?")).upper().startswith("S")

    if resposta:
        print()
        os.system("cls")
        condicao = True
    else:
        os.system("cls")
        print("Até mais!😁")
        break
