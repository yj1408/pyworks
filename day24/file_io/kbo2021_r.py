# 리스트 읽기

try:
    f = open("c:/pyfile/kbo2021.txt", 'r')
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')