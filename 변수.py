# 변수

x = y = z = 700
y
print(x, y, z)


# 선언

var = 755

# 재선언

var = "Change value"

print(var)
print(type(var))


# Object Refrence
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# ex.1
print(300)
print(int(300))

print()

# ex.2

n = 777
print(n, type(n))
print()

m = n #  m -> 777 <- # n

print(m, n)

m = 444

print(m, n)

print()

# id(identity)확인 : 객체의 고유값 / 값에 따라 고유값이 생성됨

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))

print()

n = 800
print(id(m))
print(id(n))
print(id(m) == id(n))


# 다양한 변수 선언

#Camel Case : numberOfColleageGraduation ->메서드 생성할

# Pascal Case : NumberofColleageGraduation ->클래스 선언할  떄

#Snake Case : number_of_college_graduation -> 변수 선언할 때


# 예약어는 변수명으로 불가능 clss, for, if 등등등
