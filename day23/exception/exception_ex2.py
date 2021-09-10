
# 다중 예외

try:
    data = [59, 0, 4, 116, 303]
    x = input("정수 입력(0~4까지 입력해주세요)")
    num = int(x)
    print(data[num])
except IndexError as exception:     #IndexError as exception - 생략가능
    print("0~4까지 입력해 주세요.")
except ValueError:
    print("값에 문제가 있습니다.")