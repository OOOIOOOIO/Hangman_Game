# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(lamda)

#함 수 정의 방법
# def fuction_name(parameter) :
#   code

# 예제 1
def first_func(n) :
    print("Hello, ", n)

word = "seong ho"

first_func(word)
print()

# 예제 2
def return_func(m) :
    value = "Hello, " + str(m)
    return value

k = return_func("Good boy")
print(k)
print()

# 예제 3 (다중반환)
def func_mul(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)    # x = y1, y = y2, z = y3

print(x, y, z)
print()

# 튜플 리턴
def func_mul2(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3) # 기본이 튜플형

q = func_mul2(20)
print(type(q), q)
print()

# 리스트 리턴
def func_mul3(x) :
    y1 = x * 2
    y2 = x * 3
    y3 = x * 4
    return [y1, y2, y3]

p = func_mul3(30)
print(type(p), p, set(p)) # set은 무작위로  됨
print()

# 딕셔너리 리턴
def func_mul4(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul4(40)
print(type(d), d, d.get('v2'), d.items(), d.keys(), d.values())

# 중요
# *args, **kwargs

# *args(언팩킹)
print(" *args 쓰는 법")
def args_func(*args) : #매개변수 명 자유, 튜플형태로 보낼 때, 묶음으로 보낼 떄
    for i, v in enumerate(args) :
        print("Result : {} ".format(i), v)
    print("--------")

args_func("Lea")
args_func("Lea", "Park")
args_func("Lea", "Park", "kim")
print()

# **kwargs(언팩킹)
print(" **kwrags 쓰는 법")
def kwargs_func(**kwargs):   #딕셔너리형태로 보낼 때,
    for v in kwargs.keys() :
        print("{} :".format(v), kwargs.get(v))
    print("------")

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'park')
kwargs_func(name1 = 'Lee', name2 = 'park', name3 = 'choi')
print()

# 전체 혼합
def example(args_1, args_2, *args, **kwargs) :
    print(args_1, args_2, args, kwargs)

example(10, 20, "lee", "kim", "park", age = 10, age2 = 20, age3 = 30)
print()

# 중첩함수
def nested_func(num) :        #자식함수는 따로 실행
    def func_in_func(num) : # 3
        print("asd", num)
    print("In func") # 1
    func_in_func(num + 100) # 2

nested_func(100)
print()


# 람다식 예제
# 메모리 절약, 가독성 향상, 코드
# 함수는 객체 생성 -> 리로스(메모리)에 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# 일반적 함수
def mul_func(x, y) :
    return x * y

q = mul_func        # 이렇게도 할 수도 있음
print(q(10, 50))
print()

# 람다식
lambda_mul_func = lambda x, y : x * y
print(lambda_mul_func(10, 50))
print()


def func_final(x, y, func) :
    print(x * y * func(100,100))     #함수가 즉시 필요할 때,
                                    # 람다식은 이름이 되게 자유로움
func_final(10, 20, lambda x, y : x * y)
