# strip() - 공백 문자 제거
# lstrip() - 왼쪽 공백 문자 제거, rstrip() - 오른쪽 공백 제거

s1 = "  hi, soo"
print(s1.lstrip())

s2 = "hi, soo! "
print(s2.lstrip())

s3 = "   hi, soo! "
print(s3.lstrip())


txt = "       banana       "
x = txt.strip()
print("0f all fruits", x, "is my favorite!!")