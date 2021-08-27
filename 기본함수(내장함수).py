# 파이썬 내장(Built-in) 함수
# 자주 사용하는 함수 위주로 실습
# 사용하다보면 자연스럽게 숙달

# 절대값
# abs()
print(abs(-3))
print()

# all(), any() : iterable 요소 검사(참 or 거짓)
print(all([1, 2, 3])) # and, 하나라도 False 요소가 있으면 False 출력 0, '' ...
print(any([1, 2, 0])) # or, 하나라도 True 요소가 있으면 True
print()

#chr(), ord() : 아스키 -> 문자 / ord : 문자 -> 아스키
print(chr(67))
print(ord('C'))
print()

# enumerate() : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'cdf', 'asdf']) :
    print(i, name)
print()

# filter(함수, 값) : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값만 추출

def conv_pos(x) :
    return (abs(x)) > 2

print(list(filter(conv_pos, [1, 2, 3, 4 ,-5, -6]))) # 값이 그대로 출력
print(list(filter(lambda x : abs(x) > 2, [1, 2, 3, 4 ,-5, -6]))) # 람다식
print()

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))
print()

# len() : 요소의 길이 반환
print(len('asdfaasd'))
print(len([1, 2, 3, 4, 5, 6]))
print()

# max(), min() : 최대값, 최소값, Iterable에서만 가능
print(max([1, 2, 3]))
print(max('abcdefg'))
print(min([1, 2, 3]))
print(min('abcdefg')) # 공백이 있을 경우 공백이 최소값
print()

# map(함수, 값) : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x) :
    return abs(x)

print(list(map(conv_abs, [1, 2, 3, 4, -5, -6, -7])))
print(list(map(lambda x : abs(x), [1, 2, 3, 4, -5, -6, -7])))
print()

# pow(밑, 지수) : 제곱값 반환
print(pow(2, 5))
print()

# range() : 반복가능한 객체(Iterable) 반환
print(list(range(0, -10, -1)))
print(list(range(0, 10, 1)))
print()

# round() : 반올림
print(round(6.5618, 2)) # 소숫점 두번째 자리 반올림해라
print()

# sorted() : 반복가능한 객체(Iterable) 정렬후 반환
print(sorted([5,6,5,3,2])) # 오름차순 정렬

a = sorted([10,20,50,3,2])
print(a)  # 값을 반환

b = [90,6,5,80,2]
b.sort()    # sort 쓰는 법
print(b)
print()

# sum() : 반복가능한 객체(Iterable)  반환
print(sum([1, 2, 3, 4, 5]))
print(sum(range(1, 10)))
print()

# type : 자료형 확인
print(type(3))
print(type('lala'))
print(type({}))
print(type([]))
print(type(()))

# zip() : 반복가능한 객체(Iterable)의 요소를 묶어서 반환, 형 변환해줘야됨
print(list(zip([10, 20 ,30], [40, 50, 60]))) # 짝 맞춰서 튜플로 반환
print(list(zip([10, 20 ,30], [40, 50]))) # 짝 없으면 반환 안해줌

a = dict(zip([10, 20 ,30], [40, 50]))
print(a.keys())
