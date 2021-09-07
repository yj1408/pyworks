# 전역 변수 사용하기 - global 키워드 사용


def one_up():
    global x     
    x += 1
    return x


x = 1 #x는 전역 변수 : 프로그램이 종료되면 소멸됨, 값을 공유, 누
print(one_up())
print(one_up())
print(one_up())
