from TicTocToeC import TicTocToe

class MultiPlayer(TicTocToe):

  def __init__(self):
    super(MultiPlayer, self).__init__()
    self.player2 = input("Player 2 Name : ")
    self.player2Sym = '$'
    self.num2 = 0
    self.historyP2 = []
    self.masterHistory.append(self.historyP2)

  def Input(self):
    self.num1 = int(input(f"{self.player1} Enter Board Number as mentioned above : "))
    if self.num1 in self.masterHistory[0]:
      print("You can't select same number again!!!")
    elif self.num1 in self.masterHistory[1]:
      print("Player 2 already selected this number!!!\nTry Again...")
      self.Input()
    else:
      self.historyP1.append(self.num1)
      self.boardM(self.masterHistory)

    self.num2 = int(input(f"{self.player2} Enter Board Number as mentioned above : "))
    self.historyP2.append(self.num2)
    self.boardM(self.masterHistory)

  def boardM(self, history):
    counter = 0
    for i in range(3):
      for j in range(3):
        counter += 1
        if counter in history[0] and len(history[0]) != 0 :
          print(self.player1Sym, end='\t')
        elif counter in history[1] and len(history[1]) != 0:
          print(self.player2Sym, end='\t')
        else:
          print('_', end='\t')
      print()

  def gameRules(self):
    self.Input()

