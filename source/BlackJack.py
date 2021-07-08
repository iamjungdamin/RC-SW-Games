from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random

class BlackJack:
    def pressedB50(self):
        self.betMoeny += 50
        if self.playerMoney >= 50:
            self.LbetMoney['text'] = '$'+str(self.betMoeny)
            self.playerMoney -= 50
            self.LplayerMoney['text'] = 'You have $'+str(self.playerMoney)
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('RC-SW-Games/source/blackjack/sounds/chip.wav',SND_FILENAME)
        else:
            self.betMoney -= 50
    def pressedB10(self):
        self.betMoeny += 10
        if self.playerMoney >= 10:
            self.LbetMoney['text'] = '$'+str(self.betMoeny)
            self.playerMoney -= 10
            self.LplayerMoney['text'] = 'You have $'+str(self.playerMoney)
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('RC-SW-Games/source/blackjack/sounds/chip.wav',SND_FILENAME)
        else:
            self.betMoney -= 10
    def pressedB1(self):
        self.betMoeny += 1
        if self.playerMoney >= 1:
            self.LbetMoney['text'] = '$'+str(self.betMoeny)
            self.playerMoney -= 1
            self.LplayerMoney['text'] = 'You have $'+str(self.playerMoney)
            self.Deal['state'] = 'active'
            self.Deal['bg'] = 'white'
            PlaySound('RC-SW-Games/source/blackjack/sounds/chip.wav',SND_FILENAME)
        else:
            self.betMoney -= 1

    def hitPlayer(self,n):  #n: 카드 이미지 라벨 위치
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)    #카드 객체를 player에게 추가
        p = PhotoImage(file='RC-SW-Games/source/blackjack/cards/' + newCard.filename())
        self.LcardsPlayer.append(Label(self.window,image=p))
        self.LcardsPlayer[self.player.inHand()-1].image = p
        self.LcardsPlayer[self.player.inHand()-1].place(x=250+ n*30, y=350)

        self.LplayerPts['text']=str(self.player.value())
        PlaySound('RC-SW-Games/source/blackjack/sounds/cardFlip1.wav',SND_FILENAME)

    def hitDealerDown(self):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='RC-SW-Games/source/blackjack/cards/b2fv.png')
        self.LcardsDealer.append(Label(self.window,image=p))
        self.LcardsDealer[self.dealer.inHand()-1].image = p
        self.LcardsDealer[self.dealer.inHand()-1].place(x=250, y=150)

    def hitDealer(self,n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file='RC-SW-Games/source/blackjack/cards/' + newCard.filename())
        self.LcardsDealer.append(Label(self.window,image=p))
        self.LcardsDealer[self.dealer.inHand()-1].image = p
        self.LcardsDealer[self.dealer.inHand()-1].place(x=280 + n*30, y=150)

    def deal(self):
        self.player.reset()
        self.dealer.reset()
        self.cardDeck = [i for i in range(52)]  #리스트 내장, [0,1,...,51]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer(0)
        self.hitPlayer(1)
        self.hitDealerDown()
        self.hitDealer(0)
        self.nCardsPlayer = 1
        self.nCardsDealer = 0

        self.B50['state'] = 'disabled'
        self.B50['bg'] = 'gray'
        self.B10['state'] = 'disabled'
        self.B10['bg'] = 'gray'
        self.B1['state'] = 'disabled'
        self.B1['bg'] = 'gray'

    def checkWinner(self):
        #딜러의 뒤집어진 카드를 보여주고
        p = PhotoImage(file='RC-SW-Games/source/blackjack/cards/'+self.dealer.cards[0].filename())
        self.LcardsDealer[0]['image'] = p
        self.LcardsDealer[0].image = p
        self.LdealerPts['text'] = str(self.dealer.value())

        #승패 판정
        if self.player.value() > 21:    #패
            self.Lstatus['text'] = 'Player Busts'
            PlaySound('RC-SW-Games/source/blackjack/sounds/wrong.wav',SND_FILENAME)
        elif self.dealer.value() > 21:    #승
            self.Lstatus['text'] = 'Dealer Busts'
            self.playerMoney += self.betMoeny*2
            PlaySound('RC-SW-Games/source/blackjack/sounds/win.wav',SND_FILENAME)
        elif self.player.value() == self.dealer.value():    #비김
            self.Lstatus['text'] = 'Draw'
            self.playerMoney += self.betMoeny
        elif self.player.value() > self.dealer.value():     #승
            self.Lstatus['text'] = 'You won !!'
            self.playerMoney += self.betMoeny*2
            PlaySound('RC-SW-Games/source/blackjack/sounds/win.wav',SND_FILENAME)
        else:                                               #패
            self.Lstatus['text'] = 'You lost'
            PlaySound('RC-SW-Games/source/blackjack/sounds/wrong.wav',SND_FILENAME)
        
        #변수 초기화
        self.betMoeny = 0
        self.LplayerMoney['text'] = 'You have $'+str(self.playerMoney)
        self.LbetMoney['text'] = '$'+str(self.betMoeny)

        self.B50.configure(state='disabled', bg='gray')
        self.B10.configure(state='disabled', bg='gray')
        self.B1.configure(state='disabled', bg='gray')
        self.Hit.configure(state='disabled', bg='gray')
        self.Stay.configure(state='disabled', bg='gray')
        self.Deal.configure(state='disabled', bg='gray')
        self.Again.configure(state='active', bg='white')

    def pressedHit(self):
        self.nCardsPlayer += 1
        self.hitPlayer(self.nCardsPlayer)
        if self.player.value() > 21:
            self.checkWinner()

    def pressedStay(self):
        while self.dealer.value() < 17:
            self.nCardsDealer += 1
            self.hitDealer(self.nCardsDealer)
        self.checkWinner()
        
    def pressedDeal(self):
        self.deal()
        self.Lstatus['text'] = ''
        self.Hit['state'] = 'active'
        self.Hit['bg'] = 'white'
        self.Stay['state'] = 'active'
        self.Stay['bg'] = 'white'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def pressedAgain(self):
        #카드 라벨 이미지 삭제
        for i in range (self.dealer.inHand()):
            self.LcardsDealer[i].configure(bg='green',image='')
        for i in range (self.player.inHand()):
            self.LcardsPlayer[i].configure(bg='green',image='')
        self.LcardsDealer.clear()
        self.LcardsPlayer.clear()

        #점수 라벨, 결과 라벨 초기화
        self.LdealerPts['text'] = ''
        self.LplayerPts['text'] = ''
        self.Lstatus['text'] = ''

        #버튼 초기화
        self.B50.configure(state='active',bg='white')
        self.B10.configure(state='active',bg='white')
        self.B1.configure(state='active',bg='white')
        self.Again.configure(state='disabled',bg='gray')

    def setupButton(self):
        self.B50 = Button(self.window,text='Bet 50',width=6,height=1,font=self.fontstyle2,command=self.pressedB50)
        self.B50.place(x=50,y=500)
        self.B10 = Button(self.window,text='Bet 10',width=6,height=1,font=self.fontstyle2,command=self.pressedB10)
        self.B10.place(x=150,y=500)
        self.B1 = Button(self.window,text='Bet 1',width=6,height=1,font=self.fontstyle2,command=self.pressedB1)
        self.B1.place(x=250,y=500)
        self.Hit = Button(self.window,text='Hit',width=6,height=1,font=self.fontstyle2,command=self.pressedHit)
        self.Hit.place(x=400,y=500)
        self.Stay = Button(self.window,text='Stay',width=6,height=1,font=self.fontstyle2,command=self.pressedStay)
        self.Stay.place(x=500,y=500)
        self.Deal = Button(self.window,text='Deal',width=6,height=1,font=self.fontstyle2,command=self.pressedDeal)
        self.Deal.place(x=600,y=500)
        self.Again = Button(self.window,text='Again',width=6,height=1,font=self.fontstyle2,command=self.pressedAgain)
        self.Again.place(x=700,y=500)

        self.Hit['state'] = 'disabled'
        self.Hit['bg'] = 'gray'
        self.Stay['state'] = 'disabled'
        self.Stay['bg'] = 'gray'
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text='$0',width=6,height=1,font=self.fontstyle,bg='green',fg='cyan')
        self.LbetMoney.place(x=200,y=450)
        self.LplayerMoney = Label(text='You have $1000',width=15,height=1,font=self.fontstyle,bg='green',fg='cyan')
        self.LplayerMoney.place(x=500,y=450)
        self.LplayerPts = Label(text='',width=2,height=1,font=self.fontstyle2,bg='green',fg='white')
        self.LplayerPts.place(x=300,y=300)
        self.LdealerPts = Label(text='',width=2,height=1,font=self.fontstyle2,bg='green',fg='white')
        self.LdealerPts.place(x=300,y=100)
        self.Lstatus = Label(text='',width=15,height=1,font=self.fontstyle2,bg='green',fg='white')
        self.Lstatus.place(x=500,y=300)

    def __init__(self):
        self.window = Tk()
        self.window.title('Black Jack')
        self.window.geometry('800x600')
        self.window.resizable(False,False)
        self.window.configure(bg='green')
        self.fontstyle = font.Font(self.window,size=24,weight='bold',family='Consolas')
        self.fontstyle2 = font.Font(self.window,size=16,weight='bold',family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.player = Player('player')
        self.dealer = Player('dealer')
        self.betMoeny = 0
        self.playerMoney = 1000
        self.nCardsDealer = 0       #카드 이미지 라벨의 위치변수
        self.nCardsPlayer = 0
        self.LcardsDealer = []      #카드 이미지 라벨 리스트
        self.LcardsPlayer = []
        self.deckN = 0              #카드 덱의 인덱스 (카드 덱은 (0,51) 셔플)

        self.window.mainloop()

BlackJack()