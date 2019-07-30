#chapter 5
##연습문제 1
##age = 20
##if (age < 20):
##    print("20살 미만")
##else:
##    print("20살 이상")

##연습문제 2
##age = 20
##if (age >= 30 and age <= 50):
##    print("dd")
##else:
##    print("dd")

##연습문제 3
##x = int(input("현재 온도를 입력하시오 : "))
##if (x >= 25):
##    print("반바지를 입으세요")
##else :
##    print("긴바지를 입으세요")

##연습문제 4
##x = int(input("성적을 입력하시오 : "))
##if (x >= 90):
##    print("A학점 입니다.")
##elif (x < 90 and x >= 80):
##    print("B학점 입니다.")
##elif (x < 80 and x >= 70):
##    print("C학점입니다.")
##elif (x < 70 and x >= 60):
##    print("D학점입니다.")
##else :
##    print("F학점입니다.")

##연습문제 5
##import random
##x = random.randint(1, 100)
##y = random.randint(1, 100)
##z = int(input(str(x)+"-"+str(y)+"="))
##if (z == x - y):
##    print("맞았습니다.")
##else:
##    print("틀렸습니다.")

##연습문제 6
##x = int(input("정수를 입력하시오 : "))
##if (x % 2 == 0 and x % 3 == 0):
##    print("2와 3으로 나누어 떨어집니다.")
##else :
##    print("2와 3으로 나누어 떨어지지 않습니다.")

##연습문제 7
import random
x = random.randint(0, 99)
y = int(input("복권번호를 입력하시오 (0에서 99사이) : "))
print("당첨번호는", x, "입니다.")

x1 = x // 10
x2 = x % 10
y1 = y // 10
y2 = y % 10

if (x == y):
    print("당첨금은 100만원 입니다.")
elif (x1 == y1 or x1 == y2 or x2 == y1 or x2 == y2):
    print("당첨금은 50만원 입니다.")
else:
    print("꽝입니다.")


