from secrets import SystemRandom
random = SystemRandom()

def gerar_cpf():
    cpf_nove_digitos = ''
    # gerando digitos base|regiao fiscal de emissão(9° digito)
    nove_digito = [random.randint(0,9),random.randint(0,9),
                   random.randint(0,9),random.randint(0,9),
                   random.randint(0,9),random.randint(0,9),
                   random.randint(0,9),random.randint(0,9),
                   random.randint(0,9)]
    for digito in nove_digito:
        cpf_nove_digitos += str(digito)
    soma = 0
    # pegar primeiro digito validador dos primeiros nove digitos
    for digitos,rang in enumerate(range(10,1,-1)):
        soma += int(cpf_nove_digitos[digitos]) * rang

    # resto da divisão
    resto_primeiro = soma % 11
    if resto_primeiro == 1 or resto_primeiro == 0:
        primeiro_dv = 0
    else:
        primeiro_dv = 11 - resto_primeiro
    #>>>>>>>>>>>>>>>>>>>>> segundo digito <<<<<<<<<<<<<<<<<<<<<<<<
    dez_digitos = cpf_nove_digitos + str(primeiro_dv)
    nove_anteriores_ao_10digito = dez_digitos[1:]
    soma_segundo = 0
    for indce,numero in enumerate(range(10,1,-1)):
        soma_segundo += int(nove_anteriores_ao_10digito[indce]) * numero
    resto_segundo = soma_segundo % 11
    if resto_segundo == 1 or resto_segundo == 0:
        segundo_dv = 0
    else:
        segundo_dv = 11 - resto_segundo
    return f'{cpf_nove_digitos}{primeiro_dv}{segundo_dv}'
    
print(gerar_cpf())
