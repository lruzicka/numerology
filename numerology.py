#!/usr/bin/python3


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.calcTable = {'A':1,'Á':1,  'J':1, 'S':1,'Š':1,  'B':2, 'K':2, 'T':2, 'Ť':2,'C':3, 'Č':3, 'L':3, 'U':3, 'Ú':3, 'Ů':3, 'D':4, 'Ď':4, 'M':4, 'V':4,'E':5, 'É':5, 'Ě':5,
                                    'N':5,'Ň':5, 'W':5,'Ö':5, 'F':6, 'O':6,'Ó':6,  'X':6,'G':7, 'P':7, 'Y':7, 'Ý':7,'H':8, 'Q':8, 'Z':8,'Ž':8,'I':9,'Í':9, 'Ü':9, 'R':9, 'Ř':9}
        self.risks = [7, 16, 25, 34, 52, 61, 70, 79, 88, 92]
        self.highrisks = [29, 40, 43]
    
    def gcalc(self, word): 
        '''Calculates the gross number from the word.'''
        word = list(word)
        total = 0
        for letter in word:
            value = self.calcTable[letter]
            total = total + value
        return(total)
        
    def reduce(self, number): 
        '''Reduces gross numbers to netto numbers.'''
        if number == 11 or number == 22:  # Numbers 11 or 22 should not be reduced.
            total = number
        else:
            total = number
            size = len(str(total)) 
            if size > 1:
                while size > 1: # Repeats until the number is not fully reduced to one digit only.
                    if total == 11 or total == 22: #Numbers 11 or 22 should not be reduced.
                        break
                    word = str(total)
                    word = list(word)
                    total = 0 
                    for letter in word:
                        total = total +int(letter)
                    size = len(str(total))
                    
            else:
                total = number
        return(total)
        
    def ncalc(self, word): 
        '''Calculates the netto numbers.'''
        word = list(word)
        total = self.gcalc(word)
        total = self.reduce(total)
        return(total)
    
    def getInNum(self): 
        '''Returns the numeric value of the first letter in a name.'''
        nletter = list(self.name)
        nletter = nletter[0]
        total = self.calcTable[nletter]
        return(total)
        
    def getIsNum(self): 
        '''Returns the numeric values of the first letter in a surname.'''
        sletter = list(self.surname)
        sletter = sletter[0]
        total = self.calcTable[sletter]
        return(total)
        
    
    def getWest(self):
        '''Returns the number for the western part of cross.'''
        west = self.ncalc(self.name)
        return(west)
        
    def getEast(self):
        '''Returns the number for the eastern part of cross.'''
        east = self.ncalc(self.surname)
        return(east)
    
    def getNorth(self):
        '''Returns the personal number.'''
        total = self.getInNum()+self.getIsNum()
        total = self.reduce(total)
        return(total)
    
    def getFirst(self):
        '''Returns the number of the first life trimester.'''
        total = self.gcalc(self.name) + self.gcalc(self.surname)
        return(total)
    
    def getSecond(self):
        '''Returns the number of the second life trimester.'''
        total = self.getNorth() + self.getFirst()
        return(total)
        
    def getThird(self):
        '''Returns the number of the third life trimester.'''
        total = (self.gcalc(self.name)+self.getNorth()) + (self.gcalc(self.surname)+self.getNorth())
        return(total)
        
    def getSouth(self):
        '''Returns the number in the southern part of cross.'''
        total = self.reduce(self.getThird())
        return(total)
        
    def calcCross(self):
        '''Returns the values of the horizontal and vertical additions on the cross.'''
        horizontal = self.getWest()+self.getEast()
        vertical = self.getNorth()+self.getSouth()
        middle = horizontal + vertical
        return(horizontal,vertical,middle)
        
    def getLowest(self):
        number = self.getThird()
        size = len(str(number))
        if size > 1:
            number = list(str(number))
            total = 0
            for num in number:
                total = total + int(num)
        else:
            total = number
        return(total)
     
    def getRisk(self,number):
        '''Finds out whether a number is a risk number.'''
        if number in self.risks:
            risk = '!'
        elif number in self.highrisks:
            risk = 'X'
        else:
            risk = ''
        return(risk)
        
    def getFlow(self, number):
        '''Finds out whether there is an energy leak.'''
        if number == 8:
            flow = 'EF'
        elif number%8 == 0:
            flow = 'PEF'
        else:
            flow = ''
        return(flow)

class PrintCross:
    '''Prints out all values in the cross (no background though).'''
    def __init__(self, person):
        self.person = person
            
    def printCross(self):
        print('                            {}                                '.format(self.person.getNorth()))
        print('                                                               ')
        print('               {}                           {}                 '.format(self.person.getInNum(), self.person.getIsNum()))
        print('                                                              ')                                           
        print('{}                                                           {}'.format(self.person.getWest(), self.person.getEast()))
        print('                            {}                               '.format(self.person.getFirst()))
        print('                                                           ')
        print('             {}            {}             {}                 '.format(self.person.gcalc(name), self.person.getSecond(), self.person.gcalc(surname)))
        print('                                                            ')
        print('                            {}                               '.format(self.person.getThird()))
        print('                                                             ')
        print('               {}                         {}                 '.format((self.person.gcalc(name)+self.person.getNorth()), (self.person.gcalc(surname)+self.person.getNorth())))
        print('                            {}                               '.format(self.person.getLowest()))
        print('                                                             ')
        print('                            {}                               '.format(self.person.getSouth()))

class PrintNums:
    def __init__(self, person):
        self.person = person
        
    def printNums(self):
        print("Výpočet pro jméno:",self.person.name, self.person.surname)
        print("=============================================================")
        print("Hrubé číslo jména:", self.person.gcalc(name), self.person.getRisk(self.person.gcalc(name)))
        print("Hrubé číslo příjmení:", self.person.gcalc(surname), self.person.getRisk(self.person.gcalc(surname)))
        print("-------------------------------------------------------------")
        print("Čisté číslo jména (západ):", self.person.getWest(), self.person.getRisk(self.person.getWest()))
        print("Čisté číslo příjmení (východ):", self.person.getEast(), self.person.getRisk(self.person.getEast()))
        print("Číslo osobnosti (sever):", self.person.getNorth(), self.person.getRisk(self.person.getNorth()))
        print("Číslo (jih):", self.person.getSouth(), self.person.getRisk(self.person.getSouth()))
        print("-------------------------------------------------------------")
        print("Číslo iniciály jména: ", self.person.getInNum(), self.person.getRisk(self.person.getInNum()))
        print("Číslo iniciály příjmení: ", self.person.getIsNum(), self.person.getRisk(self.person.getIsNum()))
        print("-------------------------------------------------------------")
        print("Číslo první fáze života: ", self.person.getFirst(), self.person.getRisk(self.person.getFirst()))
        print("Číslo druhé fáze života: ", self.person.getSecond(), self.person.getRisk(self.person.getSecond()))
        print("Číslo třetí fáze života: ", self.person.getThird(), self.person.getRisk(self.person.getThird()))
        print("Pomocné číslo je: ", self.person.getLowest(), self.person.getRisk(self.person.getLowest()))
        print("-------------------------------------------------------------")
        kname = self.person.gcalc(name)+self.person.getNorth()
        ksurname = (self.person.gcalc(surname)+self.person.getNorth())
        print("Číslo kombinace jména a osobnosti (vlevo dole):", kname, self.person.getRisk(kname))
        print("Číslo kombinace příjmení a osobnosti (vpravo dole):", ksurname, self.person.getRisk(ksurname))
        print("-------------------------------------------------------------")
        hor, ver, sum = self.person.calcCross()
        print("Horizontální výpočet kříže: ", hor, self.person.getRisk(hor), self.person.getFlow(hor))
        print("Vertikální výpočet kříže: ", ver, self.person.getRisk(ver), self.person.getFlow(ver))
        print("Součet kříže: ", sum, self.person.getRisk(sum), self.person.getFlow(sum))
        print("=============================================================")


incoming = input("Zadejte vaše jméno a příjmení (Jan Novák): ")
incoming = incoming.upper()
incoming = incoming.split(" ")

name = incoming[0]
surname = incoming[1]

person = Person(name, surname)
calculation = PrintNums(person)
calculation.printNums()

choice = input("Chcete zobrazit kříž pro toto jméno? (a/n): ")
choice = choice.upper()
if choice == 'A':
    cross = PrintCross(person)
    cross.printCross()
else:
    pass
