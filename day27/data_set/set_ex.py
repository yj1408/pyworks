# Set 자료 구조
# 순서가 없고, 중복이 불가

s = {2, 4, 6, 8}
print(s)

# 요소 추가 - add(x)
s.add(10)
s.add(4)  # 중복 기억
print(s)

# 요소 삭제 - remove(x)
s.remove(10)
s.remove(6)
print(s)

str = set("Hello")       #list() set=()
print(str)

# 중복 제거후 출력
name = set(['콩쥐', '팥쥐', '콩쥐'])
print(name)