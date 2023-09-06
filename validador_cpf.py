cpf = '51383450013'
nove_primeiros = cpf[:9]

def buscando_digitos_validador(cpf):
    # soma
    multiplicacao = 0
    # logica de calculo
    for v,dig in enumerate(range(10,1,-1)): 
        multiplicacao += int(cpf[v]) * dig
    # pegando o resto da divisão da soma total da multiplicação!
    resto_divisao = multiplicacao % 11
    # condição para validar digito 0
    if resto_divisao == 1 or resto_divisao == 0:
        primeiro_dv = 0
    else:
        primeiro_dv = 11 - resto_divisao
    #>>>>>>>>>>>>>>>>>>> segundo digito <<<<<<<<<<<<<<<<<<<<<
    #logica
    primeiros_dez_digitos = cpf + str(primeiro_dv)
    nove_anterior_ao_primeiro_dv = primeiros_dez_digitos[1:]
    multiplicacao_segundo = 0
    # logica de calculo segundo digito
    for v,dig in enumerate(range(10,1,-1)): 
        multiplicacao_segundo += int(str(nove_anterior_ao_primeiro_dv)[v]) * dig
    # pegando o resto da divisão da soma total da multiplicação_segundo!
    resto_divisao_segundo = multiplicacao_segundo % 11
    # condição para validar digito 0
    if resto_divisao_segundo == 1 or resto_divisao_segundo == 0:
        segundo_dv = 0
    else:
        segundo_dv = 11 - resto_divisao_segundo
    return f'{cpf}{primeiro_dv}{segundo_dv}'

cpf_retornado = buscando_digitos_validador(nove_primeiros)
print(cpf_retornado)

# validando cpf
if cpf_retornado == cpf:
    print('\033[32mvalido\033[m')
else:
    print('\033[31minvalido\033[m')








    