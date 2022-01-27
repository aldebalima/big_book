'''
A cifra de Cesar pe uma encriptação antiga usada por Julius Caesar.
Ela encripta letras tocando-as sobre um certo numero de lugares no alfabeto.
Chamado de comprimento de deslocamento de chave.
Por ex. se a chave for 3 então A se torna D, B se torna E e assim por diante.
Para desencriptar a mensagem você deve mudar as letras encriptadas na direção oposta.
Ess programa permite encriptar e deesencriptar mensagens de acordo com esse algoritimo
Mais informações em https://en.wikipedia.org/wiki/Caesar_cipher
TAGS: SHORT, CRYPTOGRAPHY, MATH
'''

from calendar import c
from email import message
from fnmatch import translate
from select import select
from turtle import position
import pyperclip


class CaesarCipher:
    def __init__(self) -> None:
        # Definições de configurações podem ser acrescidas outras chaves
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
        self.MAXKEY = len(self.SYMBOLS)-1
        self.KEY = self.MAXKEY+1
        
        a = 'a'
        while (a not in  ['E','D']):
            a = input('Bem vindo ao algoritmo CIFRA DE CESAR, digite e/E para encriptar e D/d para desencriptar!!')
            a = a.upper()
            if a == 'E':
                self.MODE = 'encrypt'
                while self.KEY not in range(0,self.MAXKEY):
                    self.KEY = input('Digite a chave de encriptação de 0 a {}: '.format(self.MAXKEY))
                    self.KEY = int(self.KEY)
                print('Digite a carta a ser encriptada!!')
                message = input('>>')
                self.message = message.upper()
                # try:
                #     pyperclip.copy(self.encryptCC())
                #     print('Full {}ed text copied to clipboard.'.format(self.MODE))
                    
                # except:
                print(self.encryptCC())
            elif a =='D':
                self.MODE = 'decrypt'
                
                print('Digite a carta a ser encriptada!!')
                message = input('>>')
                self.message = message.upper()
                continuation = 'Y'
                while continuation.upper() == 'Y':
                    self.KEY = self.MAXKEY+1
                    while self.KEY not in range(0,self.MAXKEY):
                        self.KEY = input('Digite a chave de desencriptação de 0 a {}: '.format(self.MAXKEY))
                        self.KEY = int(self.KEY)
                    print(self.desencryptCC())

                    continuation = input('Deseja verificar com outra chave?? Y para sim e N para não')

    def encryptCC(self):
        ''' A encriptação da cifra de cesar seque um padrão simples verifica posição de cada letra na sequencia
        de simbolos então adiciona a essa posição a numero de saltos a serem dados retornando o novo caracter.
        '''
        translated = ''

        for s in self.message:

            if s in self.SYMBOLS:
                # posição de letra principal
                position = self.SYMBOLS.find(s)
                # posição de letra de substituição
                position = position + self.KEY
                # Verificando se valor não estrapolou limite dos simbolos
                if position >= len(self.SYMBOLS):
                    position-=len(self.SYMBOLS)
                translated += self.SYMBOLS[position]
            else:
                translated = translated + s                    
        return translated
    def desencryptCC(self):
        ''' A desencriptação recebe a chave e o texto e executa a tradução '''
        translate = ''
        for s in self.message:
            
            if s in self.SYMBOLS:
                
                position = self.SYMBOLS.find(s)

                position = position - self.KEY

                if position < 0:
                    position = len(self.SYMBOLS) + position
                    translate = translate + self.SYMBOLS[position]
                else:
                    translate = translate + self.SYMBOLS[position]

            else:
                translate += s
        return translate

z = CaesarCipher()