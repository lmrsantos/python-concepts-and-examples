# class player
# self = name, #winning, #losses, #games, best attempt
# options/functions to:
#    update #winning
#    update #losses
#    update best attempt
import random

def randomword(num):
    words = ['alarm', 'angry', 'basic', 'beach', 'break', 'cabin', 'cable', 'candy', 'catch', 'cause', 'chair', 'chalk', 'chest', 'claim', 'clamp', 'clean', 'climb', 'close', 'cloud', 'coast', 'colar', 'colon', 'color', 'comic', 'cough', 'cover', 'crane', 'crawl', 'crazy', 'credit', 'cross', 'crowd', 'crush', 'curse', 'curve', 'cycle', 'damage', 'dance', 'danger', 'decide', 'delay', 'depth', 'dirty', 'doctor', 'donate', 'doubt', 'dozen', 'drain', 'dream', 'drive', 'empty', 'enemy', 'enjoy', 'enter', 'error', 'escape', 'exceed', 'excuse', 'exit', 'extra', 'faith']
    return words[random.randint(0,num-1)]
class Player():
    def __init__(self, name):
        self.name = name
        self.winning = 0
        self.losses = 0
        self.games = self.winning + self.losses
        self.bestattempt = 0

    def __str__(self) -> str:
        return (f'---------\n{self.name}\nWinning: {self.winning}\nLosses: {self.losses}\nTotal Games: {self.games}\nBest Attempt: {self.bestattempt}')
    
    def update_win(self):
        self.winning += 1
        self.games += 1
        return

    def update_lost(self):
        self.losses += 1
        self.games += 1

    def update_bestattempt(self, current_attempt):
        if self.bestattempt == 0:
            self.bestattempt = current_attempt
        elif current_attempt < self.bestattempt:
            self.bestattempt = current_attempt

# class game receives instatiated player and challenge word
# checl if:
#   letter is in the right position: CAPSLOCK, 
#   letter exists but is in the wrong position: LOWER CASE or 
#   word does not contain the letter: __
# Maximum number of attempts is 6
# Send message when WON, LOST or GAME OVER

class Wordle():
    def __init__(self, player, word):
        self.player = player
        self.word = word
        self.attempt = ["_", "_", "_", "_", "_"]
        self.cont_attempt = 0
        self.message = ""
        self.game_over = False
        self.start = True

    def __str__(self):
        if self.message == "":
            print (f'{self.attempt}\nAttempts: {self.cont_attempt}')
        else:
            print (self.message)

    def play(self, guess):
        # check whether Game Over
        if self.game_over:
            print (f'\n--------\n{guess}\nGame Over')
            return

        if self.start:
            print (f'\n============\n{self.player.name} is playing')
            self.start = False

        # error handling: 5 letters and only letters
        self.message = ""
        if len(guess) != 5:
            self.message = "Please, enter word with 5 letters"
            print (self.message)
            return 
        
        if not guess.isalpha():
            self.message = "Please, enter word with only letters"
            print (self.message)
            return
        
        self.cont_attempt += 1

        # check whether WON
        if guess == self.word:
            self.player.update_win()
            self.player.update_bestattempt(self.cont_attempt)
            self.game_over = True
            print (f'\nAttempt #{self.cont_attempt} - {self.word.upper()}\n---------\nYou WON\n{self.player}')
            return

        wlist = [l for l in self.word]
        self.attempt = ["_", "_", "_", "_", "_"]
        #find UPPERCASES
        for i1, l1 in enumerate(guess):
            for i2, l2 in enumerate(wlist):
                if l1.lower() == l2.lower() and i1 == i2:
                    wlist[i2] = "_"                     
                    self.attempt[i1]=l1.upper()      
        #find LOWERCASES
        for i1, l1 in enumerate(guess):
            for i2, l2 in enumerate(wlist):
                if l2 != "_":
                    if l1.lower() == l2.lower():
                        wlist[i2] = "_"
                        self.attempt[i1]=l1.lower()
        
        print (f'\nAttempt #{self.cont_attempt} - {"".join(self.attempt)}')

        if self.cont_attempt == 6:
           self.player.update_lost()
           self.game_over = True
           print (f'\n---------\nYou LOST\n -> the word was {self.word.upper()}\n{self.player}')

        return

word = randomword(50)
name = input ("Your name: ")
p1 = Player(name)
w = []
index = 0
w.append(Wordle(p1, word))
play = True
while play:
    guess = input ("Enter your guess (a word with 5 letters): ")
    w[index].play(guess)
    if w[index].game_over:
        answer = input ("Do you want continue with a new game (y/n)?")
        if answer.lower() == "n":
            play = False
        else:
            index += 1
            w.append(Wordle(p1, randomword(50)))

p1 = Player('lm')
# w1 = Wordle(p1,"water")
# w1.play("watew")
# w1.play("watea")
# w1.play("water")
# p2 = Player("Rita")
# w2 = Wordle(p2,"queue")
# w2.play("quart")
# w2.play("queue")
# w2.play("quere")
# w3 = Wordle(p1, "water")
# w3.play("carta")
# w3.play("raset")
# w3.play("jsjsj")
# w3.play("ksksk")
# w3.play("aiaia")
# w3.play("lslsl")
# w4 = Wordle(p1, "mango")
# w4.play("manga")
# w4.play("mango")




