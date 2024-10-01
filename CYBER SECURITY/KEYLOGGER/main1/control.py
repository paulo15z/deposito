from pynput.keyboard import Controller #chama a biblioteca, mas apenas oq vou precisar

# (X,Y) left to right, top to bottom
def controlMouse():                 #define a função
    mouse = Controller()            
    mouse.position = (10,20)        #define os valores da posiçao

## controlMouse()                      #ativa a função
# muda a posição do cursor


def controlKeyboard():                  #define a função 
    keyboard = Controller()             
    keyboard.type("IM something else") #define oq vai ser escrito

controlKeyboard()                   #ativa a função

# WARNING lembrar de alterar a bibiloteca, pynput.mouse pro mouse, e pynput.keyboard pro teclado