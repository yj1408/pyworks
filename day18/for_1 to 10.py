# for문 사용하기
# range(시작값,종료값(종료+1),증가값)
# 1은 기본이므로 생략 가능
for i in range(1, 11, 1):
    print(i, end=" ")   #end=" " :옆으로 출력

print()

# 0 ~ 9 출력 : 초기값이 없는 경우 0부터 시작임
for i in range(10):
    print(i, end=" ")
    
print()

# 1 ~ 10 중 홀수 출력
for i in range(1, 11, 2):
    print(i, end=" ")

print()

# 1 ~ 10 중 짝수 출력
for i in range(1, 11, 1):
    if i % 2 == 0:
        print(i, end=" ")
