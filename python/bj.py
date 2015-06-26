import numpy as np

class blackjack:

    def __init__(self):
        self.used = []
        self.playercards = []
        self.dealercards = []
        self.score = {'player':0, 'dealer':0}
        self.ace = False
        self._start()



    def hit(self): #for player only
        self._deal('player')
        #print self.playercards, self.score['player']
        #print self.used
        if self.score['player'] > 21:
            print ""
            print "Your hand:",
            for i in range(len(self.playercards)):
                if i == len(self.playercards)-1:
                    print self.playercards[i]
                else:
                    print(self.playercards[i]+','),
            print ("Your score: "+
                   str(self.score['player']))
            print ""
            print "BUST!"
            print "You lost"
            print "Better luck next time..."
        else:
            print ""
            print "Your hand:",
            for i in range(len(self.playercards)):
                if i == len(self.playercards)-1:
                    print self.playercards[i]
                else:
                    print(self.playercards[i]+','),
            print("Your score: "+ 
                  str(self.score['player']))
            print ""
            print "hit or stay?"



    def stay(self):
        print ""
        print "Your hand:",
        for i in range(len(self.playercards)):
            if i == len(self.playercards)-1:
                print self.playercards[i]
            else:
                print(self.playercards[i]+','),
        print "Your score:", str(self.score['player'])
        self._dealerturn()
        print ""
        if self.score['dealer']>21:
            print "Dealer's hand:",
            for i in range(len(self.dealercards)):
                if i == len(self.dealercards)-1:
                    print self.dealercards[i]
                else:
                    print(self.dealercards[i]+','),
            print ""
            print "Dealer Busted!"
            print "Congrats, you won!"
        else:
            print "Dealer's hand:",
            for i in range(len(self.dealercards)):
                if i == len(self.dealercards)-1:
                    print self.dealercards[i]
                else:
                    print(self.dealercards[i]+','),
            print "Dealer score:", str(self.score['dealer'])
            print ""
            if self.score['player'] > self.score['dealer']:
                print "You Won!"
            elif self.score['player'] < self.score['dealer']:
                print "Dealer Won!"
                print "Better luck next time..."
            else:
                print("Tied! looks like you'll have to",
                      " play again!")



    def _dealerturn(self):
        for i in range(5):
            if self.score['dealer'] <= 16:
                self._deal('dealer')
                


    def _start(self):
        for i in range(2):
            self._deal('player')
            self._deal('dealer')
        #print self.playercards, self.score['player']
        #print self.dealercards, self.score['dealer']
        #print self.used
        print ""
        print "Your hand:",
        for i in range(len(self.playercards)):
            if i == len(self.playercards)-1:
                print self.playercards[i]
            else:
                print(self.playercards[i]+','),
        print "Your score:", self.score['player']
        print ""
        print "Dealer's hand: XX,", self.dealercards[1]
        print ""
        print "hit or stay?"



    def _deal(self, person):
        card = np.random.randint(1,53)
        if card not in self.used:
            self.used.append(card)
            self._cardvalueandsuit(card, person)
        else:
            self._deal(person)



    def _scorecard(self, cardvalue, person):
        if self.ace == False:
            self.score[person] += cardvalue
        else:
            if self.score[person] + cardvalue <= 21:
                self.score[person] += cardvalue
            else:
                self.score[person] += (cardvalue -10)



    def _namecard(self, person, cardsuit, cardnum):
        if person == 'player':
            self.playercards.append(cardnum+cardsuit)
        else:
            self.dealercards.append(cardnum+cardsuit)



    def _cardvalueandsuit(self, card, person):
        suits = ['C', 'S', 'H', 'D']
        if card <= 4:
            cardnum = '2'
            cardvalue = 2
            for i in range(4):
                if card == i+1:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 8:
            cardnum = '3'
            cardvalue = 3
            for i in range(4):
                if card == i+5:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 12:
            cardnum = '4'
            cardvalue = 4
            for i in range(4):
                if card == i+9:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 16:
            cardnum = '5'
            cardvalue = 5
            for i in range(4):
                if card == i+13:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 20:
            cardnum = '6'
            cardvalue = 6
            for i in range(4):
                if card == i+17:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 24:
            cardnum = '7'
            cardvalue = 7
            for i in range(4):
                if card == i+21:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 28:
            cardnum = '8'
            cardvalue = 8
            for i in range(4):
                if card == i+25:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 32:
            cardnum = '9'
            cardvalue = 9
            for i in range(4):
                if card == i+29:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 36:
            cardnum = '10'
            cardvalue = 10
            for i in range(4):
                if card == i+33:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 40:
            cardnum = 'J'
            cardvalue = 10
            for i in range(4):
                if card == i+37:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 44:
            cardnum = 'Q'
            cardvalue = 10
            for i in range(4):
                if card == i+41:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        elif card <= 48:
            cardnum = 'K'
            cardvalue = 10
            for i in range(4):
                if card == i+45:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
        else: #Ace
            self.ace == True
            cardnum = 'A'
            if self.score[person] + 11 > 21:
                cardvalue = 1
            else:
                cardvalue = 11
            for i in range(4):
                if card == i+49:
                    cardsuit = suits[i]
            self._scorecard(cardvalue, person)
            self._namecard(person, cardsuit, cardnum)
            
