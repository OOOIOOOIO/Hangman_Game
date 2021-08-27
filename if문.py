# if 문

# 기본 형식
print(type(True)) # 0이 아닌 숫자, 문자,문자열 "abc", [1, 2, 3], (1, 2, 3)
print(type(False)) # 0, 빈 문자 "", [], (), {} 빈 것들.

# 예 1
if True :
    print("Good")

if False :
    print("Bad")
print()

# 예 2
if False :
    print("Bad!")

else :
    print("Good!")
print()

# 관계 연산자
# >, >=, <, <=, ==, !=

# 예 3
city = ""
if city : # 빈 문자열이기에 False
    print("You are in :", city)

else :
    print("Please enter your city")
print()

city2 = "Seoul"
if city2 : # 빈 문자열이기에 False
    print("You are in :", city2)

else :
    print("Please enter your city")
print()


# 논리연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print("and : ", a > b and b > c) # a > b > c
print("or : ", a > b or b > c)
print("not : ", not a > b)
print("not : ", not b > c)
print()

# 산술, 관계, 논리 우선순위
# 산술 > 관계 > 논리
print("e1 : ", 3 + 12 > 7 + 3)
print("e2 : ", 5 + 10 * 3 > 7 + 3 * 20)
print("e3 : ", 5 + 10 > 3 and 7 + 3 == 10)
print("e4 : ", 5 + 10 > 0 and not 7 + 3 == 10)
print()

score_1 = 90
score_2 = "A"

# 복수의 조건이 모두 참일 경우 실행
if score_1 >= 90 and score_2 == "A" :
    print("Pass")
else :
    print("Fail")
print()
# 예 5
id_1 = "vip"
id_2 = "admin"
grade = "platinum"

if id_1 == "vip" or id_2 == "admin" :
    print("관리자 입장")

if id_2 == "admin" and grade == "platinum" :
    print("최상위 관리자")
print()
# 예 6
# 다중 조건문

num = 90

if num >= 90 :
    print("Grade : A")
elif num >= 80 :
    print("Grade : B")
elif num >= 70 :
    print("Grade : C")
else :
    print("과락")
print()

#예 7
# 중첩 조건문

grade = "A"
total = 95

if grade == "A" :
    if total >= 90 :
        print("장학금 100%")
    elif total >= 80 :
        print("장학금 80%")
    else :
        print("장학금 50%")
else :
    print("장학금 없음")
print()


# in, not in

q = [10, 20, 30] # 리스트
w = {70, 80, 90, 100} # 집합
e = {"name" : "lee", "city" : "seoul", "grade" : "A"} # 딕셔너리
r = (10, 12, 14) # 튜플

print("name" in e)   # 딕셔너리는 키 값으로
print("seoul" in e.values()) # 딕셔너리 밸류로 와우~!
