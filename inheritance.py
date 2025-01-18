class Human: # 부모
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("이름: ",self.name)
        print("나이: ",self.age)

class Student(Human): # 자식(부모로부터 상속받음)
    def __init__(self,name,age, studentNum):
        super().__init__(name,age)
        self.studentNum=studentNum
    def introduce(self):
        super().introduce()
        print("학생 넘버는 :", self.studentNum)
    def study(self):
        print("공부하다")

kim=Student("김수미",56,5)
kim.study()
kim.introduce()

lee=Human("abc",13)
lee.introduce()
# lee.study() -> 오류
