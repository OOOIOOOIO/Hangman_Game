# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성요소를 모아놓은 파일

def add(x, y) :
    return x + y

def subtract(x, y) :
    return x - y

def multiply(x, y) :
    return x * y

def divide(x, y) :
    return x / y

def power(x, y) :
    return x ** y



# print(" - " * 15)
# print("called! inner!")
# print(add(5, 5))
# print(subtract(15, 5))
# print(multiply(5, 5))
# print(divide(25, 5))
# print(power(5,3))
# print(" - " * 15)

# __name__ 사용
if __name__ == "__main__" :    #메인 키워드 해 줘야 불러올 떄 print가 안열림
    print(" - " * 15)         #하지만 여기서 돌리면 출력됨
    print("called! inner!")
    print(add(5, 5))
    print(subtract(15, 5))
    print(multiply(5, 5))
    print(divide(25, 5))
    print(power(5,3))
    print(" - " * 15)
