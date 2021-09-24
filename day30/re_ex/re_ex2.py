# '*' 와 '+' 의 차이
import re

p = re.compile("ca*t")  #정규식

m1 = re.findall(p, "ceat")
print(m1)

m2 = re.findall(p, "ct")
print(m2)

p2 = re.compile("ca*t")    # 정규식

m1 = re.findall(p2, "ceat")
print(m1)

m2 = re.findall(p2, "ct")
print(m2)