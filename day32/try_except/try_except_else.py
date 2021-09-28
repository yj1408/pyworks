# try ~ except ~ else
# 오류가 없을 때 try ~ else 가 실행
# 오류가 있을 때 try ~ except 가 실행
# finally는 항상 실행 - 외부장치를 초기화, 종료할때 사용
try:
    print("1번")
    with open('animal.txt', 'r') as f:
        lines = f.readline()

except:
    print("2번")

else:
    print("3번")
    for i in lines:
        print(i, end='')

finally:
    print("4번")