#함수 이름은 변경 가능합니다.

students = dict()

class NotPositiveIntError(Exception):
  def __init__(self):
    super().__init__('Score is not positive integer!')

class NameExistError(Exception):
  def __init__(self):
    super().__init__('Already exist name!')

class EmptyDictError(Exception):
  def __init__(self):
    super().__init__('No student data!')

class MissGradingError(Exception):
  def __init__(self):
    super().__init__("There is a student who didn't get grade.")

##############  menu 1
def Menu1(name, mid, final, avg) :
  students[name] = [mid, final, avg, 0]

##############  menu 2
def Menu2(students) :
    #학점 부여 하는 코딩
    for k, v in students.items():
      if v[3] == 0:
        if v[2] >= 90:
          grade = 'A'
        elif v[2] >= 80:
          grade = 'B'
        elif v[2] >= 70:
          grade = 'C'
        else:
          grade = 'D'
        v[3] = grade

##############  menu 3
def Menu3() :
    #출력 코딩
    k = list(students.keys())
    v = list(students.values())
    print('-------------------------------')
    print('name\tmid\tfinal\tgrade')
    print('-------------------------------')
    for i in range(len(k)):
      print(k[i],'\t',v[i][0],'\t',v[i][1],'\t',v[i][3])

##############  menu 4
def Menu4(name):
    #학생 정보 삭제하는 코딩
    del students[name]

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        try:
          name, mid, final = input('Enter name mid-score final-score: ').split()

        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
          if name in students: # 이미 존재하는 이름
            raise NameExistError
                
          if not mid.isdecimal() or not final.isdecimal(): # 입력 점수 값이 정수인지
            raise NotPositiveIntError
          
          if int(mid) < 0 or int(final) <0: # 입력 점수 값이 양의 정수인지
            raise NotPositiveIntError
          
          name = name
          mid = int(mid)
          final = int(final)
          avg = round((mid + final) / 2, 1)
            
        except NameExistError as e:
          print(e)
        except NotPositiveIntError as e:
          print(e)
        except ValueError as e: # 데이터 입력 갯수
          print('Num of data is not 3!')

        #예외사항이 아닌 입력인 경우 1번 함수 호출
        else:
          Menu1(name, mid, final, avg)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        try:
          if not bool(students):
            raise EmptyDictError

        except EmptyDictError as e:
          print(e)

        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        else:
          Menu2(students)
          print('Grading to all students.')

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        try:
          if not bool(students):
            raise EmptyDictError
          
          for k, v in students.items():
            if v[3] == 0:
              raise MissGradingError

        except EmptyDictError as e:
          print(e)

        except MissGradingError as e:
          print(e)
        
        #예외사항이 아닌 경우 3번 함수 호출
        else:
          Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        try:
          if not bool(students):
            raise EmptyDictError

        except EmptyDictError as e:
          print(e)

        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        else:
          del_name = input('Enter the name to delete: ')

        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
          if del_name in students:
              Menu4(del_name)
              print(del_name, 'student information is deleted.')
          else:
              print('Not exist name!')
  
    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print('Exit Program!')
        break

    else :
        #"Wrong number. Choose again." 출력
        print('Wrong number. Choose again.')