import random

class RouletteGame:
    def __init__(self):
        self.chips = 10

    def play_round(self):
        bets = self.get_bets()
        
        if self.chips == 0:
            print("GAME OVER")
            return
        
        result = random.randint(0, 36)
        
        print(f"De uitkomst is: {result}")
        
        winnings = 0
        for bet in bets:
            if bet == result:
                winnings += 35
        
        self.chips += winnings - len(bets)
        
        if winnings > 0:
            print(f"Gefeliciteerd! Je wint {winnings} chips!")
        
        print(f"Je hebt nu {self.chips} chips over.")
    
    def get_bets(self):
        bets = []
        while True:
            bet = input("Zet in op een getal tussen 0 en 36 (of typ STOP om te spelen): ").upper()
            if bet == 'STOP':
                break
            
            try:
                bet_num = int(bet)
                if 0 <= bet_num <= 36:
                    if self.chips > 0:
                        bets.append(bet_num)
                        self.chips -= 1
                    else:
                        print("Je hebt geen chips meer over!")
                else:
                    print("Ongeldige inzet. Kies een getal tussen 0 en 36.")
            except ValueError:
                print("Ongeldige invoer. Voer een getal tussen 0 en 36 in of typ STOP.")
        
        print("rien ne va plus")
        return bets

if __name__ == '__main__':
    game = RouletteGame()
    
    while game.chips > 0:
        game.play_round()
