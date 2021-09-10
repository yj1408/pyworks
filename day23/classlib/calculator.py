# 계산기 클래스
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

# add() 함수에서 객체 변수가 100이상의 값을 가질수 없도록 재한하는 클라스
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100
        return self.value

cal = MaxLimitCalculator()
cal.add(50)  #50더하기
cal.add(60)  #60 더하기
print(cal.value)   # 100 출력