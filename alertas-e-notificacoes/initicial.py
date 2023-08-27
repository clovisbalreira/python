#pegar a informação você quer
import requests
#https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL
requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])
print(cotacao)

import smtplib
import email.message

#enviar um aviso- email
def enviar_email(cotacao):  
    corpo_email = f"""
    <p>Dolar esta abaixo de R$5,20 Cotação atual: R${cotacao}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'remetente'
    msg['To'] = 'destinatario'
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

if cotacao < 5.20:
    enviar_email(cotacao)
    
#deploy