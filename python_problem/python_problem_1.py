import random

num = 0

player1 = "Player"
player2 = "Computer"
player = player2

class NotInRangeError(Exception):
  def __init__(self):
    super().__init__('1,2,3 중 하나를 입력하세요')

def SwitchTurn():
  global player
  if player == player2:
    player = player1
  else:
    player = player2

def brGame():
  global player
  global num
  while True:
    try:
      if player == "Player":
        num_input=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
      elif player == "Computer":
        num_input = random.randint(1,3)
      if num_input not in range(1,4):
        raise NotInRangeError
    except ValueError:
      print("정수를 입력하세요")
    except NotInRangeError:
      print("1,2,3 중 하나를 입력하세요")
    else:
      break

  for i in range(0,num_input):
    num = num + 1
    print(player + " : " + str(num))
    if num == 31:
      break
  SwitchTurn()

while num < 31:
  brGame()

print(player,"win!")