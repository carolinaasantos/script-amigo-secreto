import smtplib
import email.message
import random
import os

contador = 0

# Função para enviar um e-mail
def enviar_email(amigo):
    global contador
    
    # Corpo do e-mail que será enviado
    corpo_email = f"""
    <h2>Olá, {amigo['nome']}!</h2>
    <p>Espero que esteja tão animado(a) quanto eu para o nosso Amigo Secreto!</p>
    <p>Então, sem mais demora... O seu amigo secreto é  <b style='font-size: 20px'>{amigo['amigo']}!</b></p>
    <p>Relembrando informações importantes:<br>
    <ul>
        <li><b>Data:</b> Insira a data</li>
        <li><b>Valor mínimo:</b> Insira o valor</li>
    </ul>
    </p>
    <p>Nos vemos lá!! =)</p>
    """

    # Informações do e-mail
    msg = email.message.Message()
    msg['Subject'] = "Sorteio Amigo Secreto"
    msg['From'] = 'seu-email' # Insira o e-mail que vai ser utilizado para os envios
    msg['To'] = amigo['email']
    password = 'sua-senha' # Insira senha configurada para um novo aplicativo no e-mail (senhas de app)
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Logando para realizar o envio dos e-mails
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email enviado ({contador + 1})')
    contador += 1

# Função para sortear o amigo secreto de cada participante
def sortear_amigo(integrantes):
    print('O sorteio está sendo realizado. Aguarde =)\n')

    # Vetor que armazena nome das pessoas
    nomes = []
    for pessoa in integrantes:
        nomes.append(pessoa['nome'])

    # Sorteio dos nomes
    for pessoa in integrantes:
        if pessoa['nome'] in nomes:
            nomes.remove(pessoa['nome'])
            sorteio = nomes[random.randint(0,len(nomes)-1)]
            nomes.append(pessoa['nome'])
        else:
            sorteio = nomes[random.randint(0,len(nomes)-1)]
        nomes.remove(sorteio)
        pessoa['amigo'] = sorteio

    # Envio dos e-mails para cada participante
    comunicar_amigos(integrantes)

# Função para enviar e-mail a todos os participantes
def comunicar_amigos(integrantes):
    for amigo in integrantes:
        enviar_email(amigo)

# Função para coletar dados dos participantes
def coletar_participantes():
    arquivo = 'participantes.txt'
    pessoas = []

    if not os.path.exists(arquivo):
        print(f"Arquivo '{arquivo}' não encontrado. Certifique-se de que ele existe no mesmo diretório.")
        return pessoas

    with open(arquivo, 'r') as file:
        for linha in file:
            linha = linha.strip()
            if not linha:
                continue

            # Campos separados por espaço ou ponto e vírgula
            if ';' in linha:
                partes = linha.split(';')
            else:
                partes = linha.split()

            if len(partes) < 2:
                continue  # linha inválida

            nome = partes[0].strip()
            email = partes[1].strip()

            if nome and email:
                pessoas.append({'nome': nome, 'email': email, 'amigo': ''})

    return pessoas

def __init__():
    pessoas = coletar_participantes()
    sortear_amigo(pessoas)

__init__()
