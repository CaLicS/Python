#chapter 2
##연습문제 1
##name = input("이름을 입력하시오 : ")
##age = int(input("나이를 입력하시오 : "))
##print(name,"씨는", 100-age+2019, "년에 100살이시네요!")

##연습문제 2
##num1 = int(input("첫 번째 숫자를 입력하시오 : "))
##num2 = int(input("두 번째 숫자를 입력하시오 : "))
##num3 = int(input("세 번째 숫자를 입력하시오 : "))
##print(num1, num2, num3, "의 평균은", (num1 + num2 + num3)/3, "입니다.")

##연습문제 3
##r = int(input("반지름을 입력하시오 : "))
##print("반지름이", r, "인 원의 넓이 : ", 3.141592*r**2)

##연습문제 4
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##
##radius = 50
##
##t.circle(radius)
##radius = radius + 20
##
##t.up()
##t.goto(100,0)
##t.down()
##t.circle(radius)
##radius = radius + 20
##
##t.up()
##t.goto(200,0)
##t.down()
##t.circle(radius)

##연습문제 5
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##
##side = 100
##
##t.fd(side)
##t.lt(120)
##t.fd(side)
##t.lt(120)
##t.fd(side)
##t.lt(120)

##연습문제 6
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##
##side = 200
##
##t.fd(side)
##t.lt(120)
##t.fd(side)
##t.lt(120)
##t.fd(side)
##t.lt(120)
##side 변수값만 바꾸어 주면 된다.

##연습문제 7
##import turtle
##t=turtle.Turtle()
##t.shape("turtle")
##
##side = 100
##angle = 90
##
##for a in range(4):
##    for b in range(3):
##        t.fd(side)
##        t.lt(angle)
##    t.fd(side)
