import smtplib
import email.message
import random

# Função para enviar um e-mail
def enviar_email(amigo):
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
    print('Email enviado')

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
        
        # Linha opcional para ver quem tirou quem
        #print(f"{pessoa['nome']} tirou {pessoa['amigo']}")

    # Envio dos e-mails para cada participante
    comunicar_amigos(integrantes)

# Função para enviar e-mail a todos os participantes
def comunicar_amigos(integrantes):
    for amigo in integrantes:
        enviar_email(amigo)

# Função para coletar dados dos participantes
def coletar_participantes():
    # Coletando a quantidade de participantes
    pessoas = []
    print('Quantos participantes terá o seu Amigo Secreto?')
    n = int(input())
    print('')

    # Coletando dados de cada participante
    for i in range (0, n):
        nome = input(f"Nome {i+1}: ")
        email = input(f"Email {i+1}: ")
        pessoas.append({'nome':nome, 'email':email, 'amigo':''})
        print('')

    return pessoas

def __init__():
    pessoas = coletar_participantes()
    sortear_amigo(pessoas)

__init__()