""" Paradoxo da simulação da data do aniversário.
Mais informações em https://en.wikipedia.org/wiki/Birthday_problem
Tags: short, math, simulation"""

import datetime, random

class BirthdayParadox():
    """ Retorna uma lista de datas randomicas de aniversários """

    def getBirthday(self, numberOfBirthdays):
        birthdayList =[]

        for i in range(numberOfBirthdays):
            """ O ano não é importante para a simulação, contanto que todos
            os aniversários contenham o mesmo ano"""
            ## Primeiro dia do ano
            startOfYear = datetime.date(2021,1,1)
            
            ## Pegar dia randomico no ano 
            randomNumberOfDays = datetime.timedelta(random.randint(0,364))
            birthday = startOfYear + randomNumberOfDays
            birthdayList.append(birthday)
            
        return birthdayList

    def getMatchBirthday(self, birthdayList):
        for a in birthdayList:
            print (a)


a = BirthdayParadox()
a.getBirthday(8)
a.getMatchBirthday()