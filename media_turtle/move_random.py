# 마음대로 걷는 거북이

import turtle as t
import random

t.shape('turtle')
t.speed(5)
t.bgcolor("blue")
t.color("white")
for x in range(100):
    angle = random.randint(1, 360)  # 1~360도 랜덤한 각도
    t.forward(10)
    t.setheading(angle)


