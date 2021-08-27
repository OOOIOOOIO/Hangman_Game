# while 실습
# while <expr> :
#   <statement(s)>


# 예제 1
n = 5
while n > 0 :
    print(n)
    n -= 1
print()

# 예제 2
a = ["foo", "bar", "Bas"]

while a :  # True라는 뜻
    print(a.pop(0))   # pop(0)은 첫번째부터 / pop()는 맨 끝부터
print()

# 예제 3 break
n = 5
while n > 0 :
    n -= 1
    if n == 2 :   # 2는 출력이 안됌
        break
    print(n)     # 4, 3
print("Loop Ended")
print()

# 예제 4 continue
m = 5
while m > 0 :
    m -= 1
    if m == 2 :
        continue
    print(m)   # 2 제외하고 출력됨
print("Loop Ended")
print()

# 예제 5
i = 1
while i <= 10 :
    print(i)
    if i == 6 :
        break
    i += 1
print()

# 예제 6
n = 10
while n > 0 :
    n -= 1
    print(n)
    if n == 5 :
        break
else :            # 정상적으로 for문이나 while문이 끝나고 실행됨 break 같이 강제로 끝나면 안됨
    print("else out.")
print()

# 예제 7
a = ["foo", "bar", "baz", "qux"]
s = "qux"
i = 0

while i < len(a) :
    if a[i] == s :
        print("found", s)
        break
    i += 1
else :
    print(s, "not found in list")
print()

# 무한반복
# while True :
#   <~>

# 예제 8
a = ["foo", "bar", "baz", "qux", "rorl"]

while a :
    if not a :    # a가 빠져나가 요소가 없어지면 False가 되므로 빠져나옴
        break
    print(a.pop())
