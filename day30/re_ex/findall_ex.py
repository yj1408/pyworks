# findall() 함수 - 내용을 리스트로 반환
import re

str = "Two is too"
m1 = re.findall("T[ow]o", str)
print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE)
print(m2)

pat = re.compile("T[^w]o")
m3 = re.findall(pat, str)
print(m3)