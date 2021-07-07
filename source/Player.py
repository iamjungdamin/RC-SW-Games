class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []     # Card 클래스 객체를 갖는 리스트
        self.N = 0          # 카드 개수
    
    def inHand(self):
        return self.N

    def addCard(self,c):
        self.cards.append(c)    # Card 클래스 객체
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def value(self):
        # 일단 ACE는 11로 계산하고
        # 점수가 21 이상이면 ACE를 하나씩 1로 변경
        total = 0
        ace = 0

        for i in range(self.N):
            total += self.cards[i].getValue()
            if self.cards[i].getValue() == 1:
                total += 10
                ace += 1
        
        while total > 21 and ace > 0:
            ace -= 1
            total -= 10

        return total
        