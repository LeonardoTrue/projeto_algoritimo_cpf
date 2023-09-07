import re
cpf = '99905577726'


def buscando_digitos_validadores(cpf):
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

# função que irar validar o padrao recebido
# e chamar a função: buscando_digitos_validadores
def validar_padrao_cpf(cpf):
    padrao_cpf = re.compile(r'^(\d{3})\.(\d{3})\.(\d{3})-(\d{2})$')
    if padrao_cpf.match(cpf):
        padrao_recebido = cpf
        # tirando caracteres nao numericos
        cpf_limpo = str(padrao_recebido).replace('.','',).replace('-','')
        print(padrao_recebido)
        # [:9] -> pega os 9 primeiros digitos para gerar os DV
        cpf_de_retorno = buscando_digitos_validadores(cpf_limpo[:9])
        print(cpf_de_retorno)
        if cpf_de_retorno == cpf_limpo:
            print('\033[32mValido\033[m')
        else:
            print('\033[31mInvalido\033[m')
    else:
        # [:9] -> pega os 9 primeiros digitos para gerar os DV
        cpf_de_retorno = buscando_digitos_validadores(cpf[:9])
        if cpf_de_retorno == cpf:
            print('\033[32mValido\033[m')
        else:
            print('\033[31mInvalido\033[m')
validar_padrao_cpf(cpf)












    