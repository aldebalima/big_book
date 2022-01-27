'''Este programa usa multiplas linhas de letras como um BIMAP, uma imagem 2D com apenas
duas cores possíveis para cada pixel, para determinar como apresntará a mensagem do usuário
Nesse BITMAP o caracter espaço representa espaços vazios, e todos os outros caracters são
recolocados por caracteres na mensagem do usuário. O BITMAP  fornecido e reordenado em um coração
mas você pode modificar para qualquer imagem que queiras. A simpicidade do sistema do binario de caracter de espaço 
ou mensagem tona-lhe bom para iniciantes.
'''
import re
from types import new_class
message = input('Digite a mensagem a ser remodelada!!')
input1 =[]
input2=[]
bitmap = """
....................................................................
              ******        ******
             ********      ********
            ***********  ***********
           **************************
            ************************
             *********************
              *******************
               *****************
                ***************
                  ***********
                    *******
                      ***
                       *
...................................................................."""


# Loop over each line in the bitmap:
for line in bitmap.splitlines():
# Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            
            # Print a character from the message:
         
            print(message[i % len(message)], end='')
    print() # Print a newline.