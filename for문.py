# for 실습

# for in <collection>
#   <Loop body>

for v1 in range(10) : # 0부터 N-1까지
    print("v1 is : ", v1)

re = [i for i in range(10)] # 리스트 컴프리헨
print(re)
print()

for v2 in range(1, 11) : # 1 ~ 10까지
    print("v2 is : ", v2)
print()

for v3 in range(1, 11, 2) : # 1 ~ 10까지 2 간격으로
    print("v3 is : ", v3)
print()

# 1 ~ 100 합

sum_1 = 0
for v in range(1, 101) :
    sum_1 += v
print("1 ~ 100의 합 : ", sum_1)

print("1 ~ 100의 합 : ", sum(range(1, 101)))
print("1 ~ 400까지 4의 배수의 합 : ", sum(range(4, 401, 4)))
print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 딕셔너리, 집합
# iterable 리터 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ["kim", 'park', 'cho', 'lee', 'choi', 'yoo']

for name in names :
    print("Your name is", name)
print()

# 예제 2

lotto_numbers = [11, 22, 33, 4, 5, 6, 1]

for numbers in lotto_numbers :
    print(numbers)
print()

# 예제 3

word = "Beautiful"

for i in word :
    print(i)
print()

# 예제 4

my_info = {
    "name" : "lee",
    "age" : 33,
    "city" : "seoul"
}

for key in my_info :
    print("key : ", key)

for value in my_info.values() :
    print("value : ", value)
print()

# 예제 5  : 대소문자   .isupper() 대문자인지 확인 .islower() / .lower 소문자()

word_2 = "HiamcDQc"

for n in word_2 :
    if n.isupper() :
        print(n)
    else :
        print(n.upper())
print()

# break

numbers = [14, 3, 7, 10, 24, 17, 2, 33, 15, 36, 34, 98, 12]

for num in numbers :
    if num == 34 :
        print("Find : 34!")
        break
    else :
        print("Not found : ", num)
print()

# continue

lt = ["11", 2, 5, True, 4.3, complex(4)]

for v in lt :
    if type(v) is bool :
        continue
    else :
        print("current type : ", v, type(v))
print()


# for -else : for문을 다 실행하고 값이 안나오면 else문, break가 없어야됌

numbers = [14, 3, 7, 10, 24, 17, 2, 33, 15, 36, 34, 98, 12]

for num in numbers :
    if num == 55 :
        print("Fount : 55")

else :
    print("Not Found : 55")
print()

# 구구단 출력

for i in range(2, 10) :
    for j in range(1, 10) :
        print("{:4d}".format(i * j), end ='') # 4칸 만듬, 왼쪽 정렬
    print()

print()

# 변환 예제
name2 = "Aceman"
#print("reversed : ", reversed(name2))
print("List :", list(reversed(name2)))
print("tuple :", tuple(reversed(name2)))
print("set : ", set(reversed(name2))) # 순서 x
