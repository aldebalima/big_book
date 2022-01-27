import random 

class Bagels:
    NUM_DIGITS = 3 # Número de digitos do número a ser acertado.
    MAX_GESSES = 10 # Número limite de tentativas para acertar.

    def __init__(self):

       
        choiceContinue ='Y'
        # Configuração ou jogar
        self.setConfigurations()
        print(''' Bagels, um jogo de dedução lógica.
                  Eu estou pensando em um numero com {} - digítos que não se repetem.
                  Tente adivinhar qual é esse número. Aqui estão algumas dicas:
                  Quando eu disser:
                    Pico -> Um digito está correto porem na posição errada
                    Fermi -> Um digito está correto e na posição correta
                    Bagels -> Nenhum digito está correto
                Por exemplo, se o número secreto fosse 248 
                e seu paupite fosse 843, a dica seria FERMI PICO.'''.format(self.NUM_DIGITS)
            )
        # Loop para continuação do jogo.
        while choiceContinue.upper() != 'N':
            #Criação de novo número randômico para jogo
            secret = self.getSecretNumber()
            #print(secret)
            # Loop para solicitar escolhas variando até o limite de chances.
            numberChoice = 1
            while numberChoice <= self.MAX_GESSES:
                
                print(''' Benvenido to Infos essa é a sua chance de nº:{}
                        Pico -> Um digito está correto porem na posição errada
                        Fermi -> Um digito está correto e na posição correta
                        Bagels -> Nenhum digito está correto
                        I - Digite apenas números inteiros.
                        II - Avalie a resposta com atenção.
                        III - Para sua sorte apenas números válidos contam como escolhas reais para validação!
                     '''. format(numberChoice))    
                
                choice = self.getChoice()
                clues = self.getClues(choice, secret)
                if clues == True:
                    print('Acertou na mira!!')
                    break
                else:
                    print(clues)
                # Incremental do máximo de chances        
                numberChoice +=1
            print('O segredo é: {}'.format(secret))
            # Linha para escolha de continuação do jogo
            choiceContinue = input('Você quer jogar novamente? Y/y -> Yes | N/n -> No:' )
    
    def getSecretNumber(self):
        """ Retorna uma string dos números feita com os limites de números de digitos"""

        # Listas podes ser reordenadas, Tuplas não. 
        numbers = list('0123456789') 
        # Reordena lista
        random.shuffle(numbers)
        
        secret = ''
        # Montagem do número a ser acertado
        for i in range(self.NUM_DIGITS):
            secret += str(numbers[i])
        return secret
    
    def getChoice(self):
        """ Validação da escolha do usuário e retorno do valor setado """
        checks = False
        choice =0 
        print('Sistema já definiu um número!!')
        while checks !=True:
            try:
                choice = int(input('Escolha:'))
                checks = True
                # Verificar se é número positivo
                if (choice<0):
                    checks = False
                    print('Escolha inválida!! Nº digitado não positivo!')
                # Verificar tamanho da escolha
                
                if(checks == True):
                    if(len(str(choice)) != self.NUM_DIGITS):
                        print('Escolha inváldia!! Nº digitado não possui {} digitos'. format(self.NUM_DIGITS))
                        checks = False
            except:
                print("Escolha inválida!! Nº digitado não inteiro") 
                checks = False
                break
                        
        return str(choice)
    def getClues(self,choice, secret):
        '''Retorna uma string com as dicas'''
        if(choice == secret):
            return True
        clues=[]

        for i in range(len(choice)):
            if choice[i] == secret[i]:
                clues.append('FERMI')
            elif choice[i] in secret:
                clues.append('PICO')
            
        if len(clues) == 0:
            clues.append('BAGELS')
        else:
            clues.sort()
        
        return ' '.join(clues)
    def setConfigurations(self):
        ''' Configurando tamanho do numero a ser adivinhado!'''
        print('Configure o desafio!!')
        go_to_game='N'
        while go_to_game.upper() == 'N':            
            num_digits = int(input('Digite o número de digitos do número a ser formado!! O valor não pode ser inferior a 3. '))
            while num_digits < 3:
                num_digits = int(input('O valor não pode ser inferior a 3. Digite o número de digitos do número a ser formado!!'))
                if(isinstance(num_digits, int) ):
                    print('Digite apenas numeros inteiros!!!!')
            print('O número de tentativas é calculado automáticamente!!!')
            self.setNumDigits(num_digits)
            # Pós configurado verifica se usuário que continuar o jogo
            go_to_game = input('Você quer iniciar o jogo? Y/y -> Yes | N/n -> No:' )
            if go_to_game not in ['Y', 'N', 'n', 'y']:
                print('Opção inválida!!')
    
    def setNumDigits(self,value):
        self.NUM_DIGITS = value
        self.setMaxGesses(value)
        
    def setMaxGesses(self, value):
        self.MAX_GESSES = int(10*value/3)

    
a = Bagels()
