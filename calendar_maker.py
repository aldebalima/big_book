'''
Esse programa gera arquivos printaveis de calendários mensais 
para o mês e o ano que você coloca de input. Datas de calendários são
um tópico complicado em programação devido a existência de muitas regras diferentes
para determinar o numero de dias em um mês, que ano é ano bissexto, 
em qual dia da semana uma data particular cai.
Esse programa foca em gerar uma string multilinha para a página do calendário.
'''
import datetime
from random import choice
import math

class Calendar:
    '''Classe para obj calendário retorna um calendário com as fases lunares em siglas'''
    def __init__(self) -> None:
        self.week_day_list = ('Sunday', 'Mondey', 'Tuesday', 'Wednesday', 'Thusday',
                               'Friday', 'Saturday')
        
        self.week_day_list_pr = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta',
                               'Sexta', 'Sábado')
        
        self.month_years_list = ('January', 'February', 'March', 'April', 'May', 'June'
                                 'July', 'August', 'September', 'October', 'November', 'Dezember')
        ## @TODO Sem Validação
        choice_year = input('Digite o ano para geração do calendário: ')
        choice_month = input('Digite o mês a ser gerado de 1 a 12: ')        
        self.getCalendar(int(choice_year), int(choice_month))

    def getCalendar(self, choice_year, choice_month):    
        ''' Função de criação de calendário'''
        calendar_text = ''
        ## cabeçalho do calendário
        calendar_text += ' '*34+ self.month_years_list[choice_month-1]+' '+str(choice_year)+'\n' 
        ## preparando cabeçalho dias da semana
        for week_d in self.week_day_list_pr:
            len_week = len(week_d)
            points_ = 11-len_week
            points_left = math.ceil(points_/2)
            points_rigth = 11 - len_week - points_left
            calendar_text += '.'*points_left + week_d + '.'*points_rigth
        
            
        calendar_text+='\n' 
        ## Fora do loop 
        # Cria obj data
        current_date = datetime.date(choice_year, choice_month, 1)
        # verifica se o dia da semana é o primeiro da lista 'Sunday ou Domingo'
        while current_date.weekday() != 6:
            ## Regredindo data
            current_date -= datetime.timedelta(days=1)

        while True:

            
            calendar_text+= '+----------'*7+'+\n'
            calendar_text+='|'
            for i in range(7):
              
                day_number = str(current_date.day).rjust(2)
                m_phase = self.moon_phase(choice_year, choice_month, current_date.day)

                calendar_text+= day_number+'    '+ m_phase +'|'
                #px dia
                current_date += datetime.timedelta(days=1)
                
            ## Pegar o dia da semana para descrição
            calendar_text+= '\n'
            for s in range(0,3):
                calendar_text+= '|          '*7 +'|\n'
            
            # Verificando se  mes ainda compativel 
            if current_date.month != choice_month:
                break
        
        calendar_text+= '+----------'*7
        calendar_text+='+\n'
        calendar_text+='Salvo no arquivo calendar.txt'
        doc_create = open('calendar.txt', 'a')
        doc_create.write(calendar_text)
        doc_create.close()
        
        #print(calendar_text)
    def moon_phase(self, year, month, day):
        ''' Função para verificar e retornar fase lunar'''
        if month<3:
            year -=1
            month += 12
        month+=1
        annual_constant = 365.25 * year
        month_contatnt = 30.6 * month
        moon_cicle = 29.5305882
        days_elapsed = (annual_constant+month_contatnt+day - 694039.09)/moon_cicle
        days_elapsed -= int(days_elapsed)
        moon_ph = round(days_elapsed * 8) 
        if moon_ph>=8:
            moon_ph=0
        moon_ph =str(moon_ph)
        switch = {
            
            "0": self.new_moon(),
            "1": self.waxing_crescent_moon(),
            "2": self.quarter_moon(),
            "3": self.waxing_gibbous_moon(),
            "4": self.full_moon(),
            "5": self.waning_gibbous_moon(),
            "6": self.last_quarter_moon(),
            "7": self.waning_crescent_moon()

        }
        case = switch.get(moon_ph, self.default())
        return case
    def default(self):
        #return 'valor padrão'
        return 'S I'
    def new_moon(self):
        #return 'Lua Nova'
        return 'L  N'
    def waxing_crescent_moon(self):
        #return 'Lua Crescente'
        return 'L  C'
    def quarter_moon(self):
        #return 'Primeiro quarto'
        return 'P  Q'
    def waxing_gibbous_moon(self):
        #return 'Crescente Gibosa'
        return 'C  G'
    def full_moon(self):
        #return 'Lua cheia'
        return 'L CH'
    def waning_gibbous_moon(self):
        #return 'Minguante Gibosa'
        return 'M  G'
    def last_quarter_moon(self):
        #return Ultimo quarto
        return 'U  Q'
    def waning_crescent_moon(self):
        #return Lua minguante#
        return 'L  M'










a = Calendar()
