# mensageiro mobile 1.0
import phonenumbers
from phonenumbers import geocoder, timezone

# função para análise de telefone
def analisar_numero(numero):
    try:
        # análise do número
        analise_numero = phonenumbers.parse(numero, None)
        # verifica se é válido
        if phonenumbers.is_valid_number(analise_numero):
            return True, analise_numero
        else:
            return False, None
    except phonenumbers.NumberParseException:
        # trata exceção se ocorrer um erro ao analisar o número
        return False, None


def inform_numero(analise_numero):
    # descobrindo o local associado ao número 
    pais = geocoder.description_for_number(analise_numero, "pt")
    # descobrindo o fuso horário associado
    fuso = timezone.time_zones_for_number(analise_numero)
    return pais, fuso[0] if fuso else None

# solicitação ao usuário do número de telefone
numero = input("Digite o número do telefone (Exemplo: +55 83 99725-7632): ")

# verificando se o número é válido
valido, analise_numero = analisar_numero(numero)

# pedindo as informações do número
if valido:
    pais, fuso_horario = inform_numero(analise_numero)
    # se o fuso horário estiver disponível
    if fuso_horario:
        print(f"Telefone apto. Local: {pais}. Fuso Horário: {fuso_horario}")
        mensagem = input("Digite a mensagem que quer mandar: ")
        print(f"A mensagem enviada para o número de telefone {numero} é: {mensagem}")
    else:
        # se o fuso horário não estiver disponível
        print(f"O fuso horário do número {numero} não está disponível.")
else:
    # caso o número não seja válido
    print("O número do telefone é inválido.")