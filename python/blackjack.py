import numpy as np
'''
This will create a pyton object 'Blackjack'
It takes one argument, the number of plaers.
For now, the number of players MUST be 1.
Next, the player will use the function 'play()' to play Blackjack.
The function has two possible arguments: 'hit' or 'stay'.
Simple enough? Try it out.
'''

class Blackjack:

    def __init__(self, players):
        self.used = []
        self.players = players
        assert (self.players==1), "This is a one player game."
        self.suits = {0:'C',1:'S',2:'H',3:'D'}
        self.cards = {0:'A',1:'2',2:'3',3:'4',4:'5',5:'6',
                      6:'7',7:'8',8:'9',9:'10',10:'J',11:'Q',
                      12:'K'}
        self.dealer = []
        self.player = []
        for i in range(2):
            self._dealplyr()
            self._dealdlr()
        print ("Your hand: "+
               self.player[0][0]+
               self.player[0][1]+" "+
               self.player[1][0]+
               self.player[1][1])
        print ("Dealer's hand: XX "+
               self.dealer[1][0]+
               self.dealer[1][1])
        #print self.player
        #print self.dealer
        #print self.used

    def _dealplyr(self):
        plyrsuit = np.random.randint(0,3)
        plyrvalue = np.random.randint(0,12)
        plyrcard = [self.suits[plyrsuit],self.cards[plyrvalue]]
        if plyrcard in self.used:
            self._dealplyr()
        else:
            self.used.append(plyrcard)
            self.player.append(plyrcard)

    def _dealdlr(self):
        dlrsuit = np.random.randint(0,3)
        dlrvalue = np.random.randint(0,12)
        dlrcard = [self.suits[dlrsuit],self.cards[dlrvalue]]
        if dlrcard in self.used:
            self._dealdlr()
        else:
            self.used.append(dlrcard)
            self.dealer.append(dlrcard)
        
    def play(self, arg):
        assert (arg=='hit' or arg=='stay'), "must pass 'hit' or 'stay' as arg."
        if arg == 'hit':
            self._dealplyr()
            print ("Your hand:"),
            for i in range(len(self.player)):
                if i == len(self.player)-1:
                    print (self.player[i][0]+
                           self.player[i][1])
                    print ("Dealer's hand: XX "+
                           self.dealer[1][0]+
                           self.dealer[1][1])
                        #print self.used
                    self._scoreplyr()
                else:
                    print (self.player[i][0]+
                           self.player[i][1]), 
        if arg == 'stay':
            self._scoreplyr()
            print "Your score is: ", self.plyrscore
            self._dealerturn()
            print "Dealer's score is: ", self.dlrscore
            if self.dlrscore<=21 and self.plyrscore<=21:
                if self.dlrscore > self.plyrscore:
                    print "Dealer Won."
                    print "Better luck next time..."
                elif self.dlrscore == self.plyrscore:
                    print "DRAW! No winner today!"
                else:
                    print "You Won! Congratulations!"

    def _dealerturn(self):
        self._scoredlr()
        for i in range(5):
            if self.dlrscore <= 16:
                self._dealdlr()
                self._scoredlr()

    def _scoredlr(self):
        dlrscorelow = 0
        dlrscorehigh = 0
        for i in range(len(self.dealer)):
            if self.dealer[i][1] == '2':
                dlrscorelow += 2
                dlrscorehigh += 2
            elif self.dealer[i][1]=='3':
                dlrscorelow += 3
                dlrscorehigh += 3
            elif self.dealer[i][1]=='4':
                dlrscorelow += 4
                dlrscorehigh += 4
            elif self.dealer[i][1]=='5':
                dlrscorelow += 5
                dlrscorehigh += 5
            elif self.dealer[i][1]=='6':
                dlrscorelow += 6
                dlrscorehigh += 6
            elif self.dealer[i][1]=='7':
                dlrscorelow += 7
                dlrscorehigh += 7
            elif self.dealer[i][1]=='8':
                dlrscorelow += 8
                dlrscorehigh += 8
            elif self.dealer[i][1]=='9':
                dlrscorelow += 9
                dlrscorehigh += 9
            elif self.dealer[i][1]=='10':
                dlrscorelow += 10
                dlrscorehigh += 10
            elif self.dealer[i][1]=='J':
                dlrscorelow += 10
                dlrscorehigh += 10
            elif self.dealer[i][1]=='Q':
                dlrscorelow += 10
                dlrscorehigh += 10
            elif self.dealer[i][1]=='K':
                dlrscorelow += 10
                dlrscorehigh += 10
            elif self.dealer[i][1]=='A':
                if dlrscorehigh + 11 <= 21:
                    dlrscorelow += 11
                    dlrscorehigh += 11
                elif dlrscorelow + 11 <= 21:
                    dlrscorelow += 11
                    dlrscorehigh += 1
                else:
                    dlrscorelow += 1
                    dlrscorehigh += 1
            #print dlrscorelow, dlrscorehigh
            if dlrscorehigh > 21:
                self.dlrscore = dlrscorelow
            else:
                self.dlrscore = dlrscorehigh
            if self.dlrscore > 21:
                print "Dealer Busted!"
                print "You Won!"

    def _scoreplyr(self):
        plyrscorelow = 0
        plyrscorehigh = 0
        self.ace = False
        for i in range(len(self.player)):
            if self.player[i][1] == '2':
                plyrscorelow += 2
                plyrscorehigh += 2
            elif self.player[i][1]=='3':
                plyrscorelow += 3
                plyrscorehigh += 3
            elif self.player[i][1]=='4':
                plyrscorelow += 4
                plyrscorehigh += 4
            elif self.player[i][1]=='5':
                plyrscorelow += 5
                plyrscorehigh += 5
            elif self.player[i][1]=='6':
                plyrscorelow += 6
                plyrscorehigh += 6
            elif self.player[i][1]=='7':
                plyrscorelow += 7
                plyrscorehigh += 7
            elif self.player[i][1]=='8':
                plyrscorelow += 8
                plyrscorehigh += 8
            elif self.player[i][1]=='9':
                plyrscorelow += 9
                plyrscorehigh += 9
            elif self.player[i][1]=='10':
                plyrscorelow += 10
                plyrscorehigh += 10
            elif self.player[i][1]=='J':
                plyrscorelow += 10
                plyrscorehigh += 10
            elif self.player[i][1]=='Q':
                plyrscorelow += 10
                plyrscorehigh += 10
            elif self.player[i][1]=='K':
                plyrscorelow += 10
                plyrscorehigh += 10
            elif self.player[i][1]=='A':
                if plyrscorehigh + 11 <= 21:
                    plyrscorelow += 11
                    plyrscorehigh += 11
                elif plyrscorelow + 11 <= 21:
                    plyrscorelow += 11
                    plyrscorehigh += 1
                else:
                    plyrscorelow += 1
                    plyrscorehigh += 1
        #print plyrscorelow, plyrscorehigh
        if plyrscorehigh > 21:
            self.plyrscore = plyrscorelow
        else:
            self.plyrscore = plyrscorehigh
        if self.plyrscore > 21:
            print "BUST!"
            print "Better luck next time..."
