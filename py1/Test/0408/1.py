class Person:
    def __init__(self, name, age): # 생성자 함수
        self.name = name
        self.age = age

    def say_hello(self, to_name):
        print("안녕! " + to_name + " 나는 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + " 그리고 나는 " + str(self.age) + "살이야")

# p = Person()
# p.say_hello()

seuni = Person("스니", 24)
michael = Person("마이클", 30)
jenny = Person("제니", 15)

seuni.introduce()
michael.introduce()
jenny.introduce()

seuni.say_hello("철수")
michael.say_hello("영희")
jenny.say_hello("민희")

