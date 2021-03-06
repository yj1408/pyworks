#학생 클래스
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("학생이 배웁니다.")

    def __str__(self):    #객체의 정보 출력
        return "이름 : {0}, 학년 : {1}".format(self.name, self.grade)

#자동차 클래스
class Car:
    def __init__(self, model, color, cc):
        self.model = model
        self.color = color
        self.cc = cc

    def forward(self):
        pass

    def backward(self):
        pass

    def turn_right(self):
        pass

    def turn_left(self):
        pass

# 사원 클래스
class Employee:
    serial_num = 1000 #기준번호 - 클래스 변수

    def __init__(self, name):
        Employee.serial_num += 1    # 1증가
        self._empid = Employee.serial_num   #사원 번호
        self._name = name

    def getempid(self):
        return self._empid

    def getname(self):
        return self._name

e1 = Employee("한강")
print("사번 : " + str(e1.getempid()) + ", 이름 : " + e1.getname())

e2 = Employee("남한강")
print("사번 : " + str(e2.getempid()) + ", 이름 : " + e2.getname())

e3 = Employee("남한강")
print("사번 : " + str(e3.getempid()) + ", 이름 : " + e3.getname())