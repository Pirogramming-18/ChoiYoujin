num = 0

player1 = "PlayerA"
player2 = "PlayerB"
player = player2

class NotInRangeError(Exception):
  def __init__(self):
    super().__init__('1,2,3 중 하나를 입력하세요')

while num < 31:
  try:
    num_input=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    if num_input not in range(1,4):
      raise NotInRangeError
    if player == player2:
      player = player1
    else:
      player = player2
  except ValueError:
    print("정수를 입력하세요")
  except NotInRangeError:
    print("1,2,3 중 하나를 입력하세요")
  else:
    for i in range(0,num_input):
      num = num + 1
      print(player + " : " + str(num))
      if num == 31:
        break