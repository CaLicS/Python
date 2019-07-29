#chapter 4
##연습문제 1
##"나는", 12 , "개의 사과를 먹었다."

##연습문제 2
##"apple" + "apple" = appleapple
##"apple" * 3 = appleappleapple

##연습문제 3
##x = input("문자열을 입력하시오 : ")
##print(x[0:2] + x[-2:])

##연습문제 4
##x = input("문자열을 입력하시오 : ")
##print(x + "하는 중")

##연습문제 5
##x = input("기호를 입력하시오 : ")
##y = input("중간에 삽입할 문자열을 입력하시오 ; ")
##print(x[0] + y + x[-1])

##연습문제 6
##x = [1, 2, 3, 4]
##print("리스트 = ", x)
##print("리스트 숫자들의 합 = ", x[0] + x[1] + x[2] + x[3])

##연습문제 7
##import turtle
##t = turtle.Turtle()
##t.shape("turtle")
##c1 = input("색상 #1을 입력하시오 : ")
##c2 = input("색상 #2을 입력하시오 : ")
##c3 = input("색상 #3을 입력하시오 : ")
##t.fillcolor(c1)
##t.begin_fill()
##t.circle(50)
##t.end_fill()
##t.up()
##t.fd(100)
##t.down()
##t.fillcolor(c2)
##t.begin_fill()
##t.circle(50)
##t.end_fill()
##t.up()

##t.fd(100)
##t.down()
##t.fillcolor(c3)
##t.begin_fill()
##t.circle(50)
##t.end_fill()

##연습문제 8
import turtle
t = turtle.Turtle()
t.shape("turtle")

x = [0] * 3
y = [0] * 3
x[0] = int(input("x1 : "))
y[0] = int(input("y1 : "))
x[1] = int(input("x2 : "))
y[1] = int(input("y2 : "))
x[2] = int(input("x3 : "))
y[2] = int(input("y3 : "))

t.up()
t.goto(x[0], y[0])
t.down()
t.goto(x[1], y[1])
t.goto(x[2], y[2])
