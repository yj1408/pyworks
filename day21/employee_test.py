from day21.libs.myclass import Employee

e1 = Employee("한강")
print("사번 : " + str(e1.getempid()) + ", 이름 : " + e1.getname())

e2 = Employee("남한강")
print("사번 : " + str(e2.getempid()) + ", 이름 : " + e2.getname())

e3 = Employee("남한강")
print("사번 : " + str(e3.getempid()) + ", 이름 : " + e3.getname())