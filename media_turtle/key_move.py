# 키보드로 조종하기

import turtle as t

def turn_right():
    t.setheading(0)  #오른쪽 화살키 각도 - 0
    t.forward(10)

def turn_up():
    t.setheading(90) #위로 가는 화살키 각도 -90
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()        # 선 지우기


t.shape("turtle")
t.onkeypress(turn_right, "Right")  # 키 조종 함수
t.onkeypress(turn_up, "Up")  # 키 조종 함수
t.onkeypress(turn_left, "Left")  # 키 조종 함수
t.onkeypress(turn_down, "Down")  # 키 조종 함수
t.onkeypress(clear, "Escape")
t.listen()                           # 실행 대기

t.mainloop()