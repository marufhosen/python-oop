class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def res(self):
        if player1 == player2:
            print("Result is TIE. They entered same input")
        else:
            print("Calculatting..................")


player1 = input("Player one choose: ")
player2 = input("Player two choose: ")

res = Game(player1, player2)
res.res()
