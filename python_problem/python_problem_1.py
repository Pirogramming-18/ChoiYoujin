num = 0

class NotInRangeError(Exception):
  def __init__(self):
    super().__init__('1,2,3 중 하나를 입력하세요')

while True:
  try:
    num_input=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
    if num_input not in range(1,4):
      raise NotInRangeError
  except ValueError:
    print("정수를 입력하세요")
  except NotInRangeError:
    print("1,2,3 중 하나를 입력하세요")
  else:
    break