
# 파이썬 클래스

# OOP(객체 지향 프로그래밍), self, , 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이
# 객체와 인스턴스의 차이

# 클래스 변수 : 직접 접근 가능
# 인스턴스 변수 : 객체마다 별도 존재

# 예제 1

class Dog :               # (object) 생략가능. 항시 상속(pass, super())하기 떄문
    # 클래스 속성
    species = 'firstdog'    # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age) : # 자바 생성자같은 거 self
        self.name = name    # 인스턴스 변수
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("mikky", 2)
print()


# 비교

print(a == b, id(a), id(b), id(c))
print()

# 네임스페이스 : 객체를 인스턴스화 할 때 자기만의 저장된  공간
print("dog1 : ", a.__dict__) # 딕셔너리 형태로 출력
print("dog2 : ", b.__dict__)
print()

# 인스턴스 속성 확인 : 독립적
print("{} is {} and {} is {}".format(a.name, a.age, b.name, b.age))
print()

# 클래스 속성 : 공유
print(Dog.species)
print(a.species)
print(b.species)
print()

# 예제 2
# self의 이해

class SelfTest() :
    def func1() :   # self가 없으면 클래스 메소드임
        print("Func1 called")
    def func2(self) :
        print(id(self))
        print("Fun2 called")

f = SelfTest()

#print(dir(f))  # 사용할 수 있는 메소드 볼 수 있음
print(id(f))
print()

#f.func1()    # 예외 발생, 클래스 메소드라서 그럼
f.func2()     # id(f)랑 고유값이 같음.
print()

SelfTest.func1()   # 클래스로 바로 호출
#SelfTest.func2()  # 예외 발생, 인스턴스 메소드라서 그럼
SelfTest.func2(f)  # 인스턴스 객체 넣어주면 됨
print()

# 예제 3
# 클래스 변수, 인스턴스 변수

class Warehouse :
    stock_num = 0  # 클래스 변수

    def __init__(self, name) :    #초기화(선언)될 때마다 stock_num에 + 1
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self) :
        Warehouse.stock_num -= 1

user1 = Warehouse('lee')
user2 = Warehouse('cho')

print(Warehouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)           #__dict__ 네임스페이스 확인
print(user2.__dict__)
print("before : ", Warehouse.__dict__)
#Warehouse.stock_num = 50   # 직접 수정할 수도 있음
print(user1.stock_num)
print(user2.stock_num)

del user1
print("after : ", Warehouse.__dict__)
print(Warehouse.stock_num)            # __del__ 실행된거
print()


# 예제 4
class Dog2() :               # (object) 생략가능. 항시 상속하기 떄문
    species = 'firstdog'    # 클래스 속성
    def __init__(self, name, age) :
        self.name = name    # 초기화/인스턴스 속성
        self.age = age

    def info(self) :
        return "{} is {} yers old".format(self.name, self.age)

    def speak(self, sound) :
        return "{} says {}!".format(self.name, sound)
         #  단지 함수 안에 있는 매개변수일 뿐임

c = Dog2("juil", 4)   # 인스턴스 생성
print(c.info())      # 메소드 호출
print(c.speak("wawwaw"))
print()

d = Dog2("marry", 10)
print(d.info())
print(d.speak("akakakak"))
