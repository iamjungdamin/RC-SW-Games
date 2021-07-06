class Card:
    def __init__(self,number):      #number = 0,...,51
        self.x = number // 13       #0,1,2,3 (무늬)
        self.value = number % 13 +1 #1,...13 (숫자)

    def getSuit(self):
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
        return suits[self.x]

    def filename(self):
        return self.getSuit() + str(self.value) + ".png"

    def getValue(self):
        if self.value > 10:         #J,Q,K
            return 10
        else:
            return self.value

import random
c = Card(random.randint(0,51))
