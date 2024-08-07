import os
import copy as c

def capture_cpf(): # function para coletar os inputs do usuário e tratar se são dígitos válidos

    for i in range(11):
        while True:
            try:
                cpf = int(input(f"Digite o {i+1} dígito do seu CPF: "))

                cpf_trat = len(str(cpf))

                if cpf_trat == 1:
                    list_cpf.append(cpf)

                else:
                    print("Digite apenas um número:")
                    continue
                
                break
            except ValueError:
                print("Digite apenas números!")
                continue

    return list_cpf

def multiplication_digit_cpf(insert_cpf): # function que multiplica os CPFs
    for i in range(11):
        number = insert_cpf[i] * (10 - i)
        list_cpf_mult.append(number)
    return list_cpf_mult

def calc_digit_one(list_cpf_mult): # function que descobre o valor do primeiro dígito
    sum_cpf = 0
    for i in range(9):
        sum_cpf = sum_cpf + list_cpf_mult[i]

    one_digit = sum_cpf * 10 # regra de negócio 
    one_digit = one_digit % 11 # regra de negócio

    if one_digit > 9:
        one_digit = 0

    return one_digit

def calc_digit_two(list_cpf_mult): # function que descobre o valor do segundo dígito
    sum_cpf = 0
    for i in range(10):
        sum_cpf = sum_cpf + list_cpf_mult[i]

    two_digit = sum_cpf * 10 # regra de negócio 
    two_digit = two_digit % 11 # regra de negócio

    if two_digit > 9:
        two_digit = 0  

    return two_digit

def verification_cpf(cpf_user,primary_digit,second_digit): # function que verifica se o CPF é válido ou não
    clone_cpf = c.deepcopy(cpf_user)
    del clone_cpf[10]
    del clone_cpf[9]
    clone_cpf.append(primary_digit)
    clone_cpf.append(second_digit)

    if clone_cpf == cpf_user:
        program_response = "CPF VÁLIDO !✔️"
    else:
        program_response = "CPF INVÁLIDO !❌"

    return program_response

while True: # loop que recoeça o programa

    cpf_trat = ""
    list_cpf = []
    cpf_gerado = []
    list_cpf_mult = []

    cpf_user = capture_cpf()

    cpf_mult=multiplication_digit_cpf(cpf_user)

    primary_digit = calc_digit_one(cpf_mult)

    second_digit = calc_digit_two(cpf_mult)

    response_finally = verification_cpf(cpf_user,primary_digit,second_digit)
    print(f"\n{response_finally}")

    print("\nResponda com 'sim' ou 'não'")
    response_user = input("Deseja recomeçar? ")

    if response_user.upper().startswith("S"):
        print()
        os.system("cls")
        continue
    else:
        os.system("cls")
        print("Inté meu mano!🤘")
        break
