# 파이썬 리스트, 자료구조에서 중
# 리스트 자료형(순서, 중복, 수정, 삭제 가능)

# 선언

a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Bace', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.52, 'food', 3, 4, False, 3.141592]
g = [1, 2, 3, 4, 5, 6]


# 인덱싱 : 자료형대로 출력
print("Indexing")
print(type(d[3]))
print('d : ', d[0] + d[1] + d[1])
print('d : ', d[-1])
print('d : ', e[-1][1])
print('e : ', e[-1][1])   # 2차원 리스트
print('e : ', list(e[-1][1]))   # 문자열을 리스트로 변환시키면 하나씩 받아짐0

print()

# 슬라이싱 :리스트로 출력됨
print("Slicing")
print(type(d[0:3]))
print('d : ', d[0:3])
print('d : ', d[2:])
print('e : ', e[-1][1:3])  # 잘 봐두자

print()

# 리스트 연산 : 리스트로 출력됨
print("Calculate list")
print('c + d : ', c + d)
print('c * 3 : ', c * 3)
print('Test + c[0] : ', 'Test' + str(c[0])) # c[0]은 정수형이므로 문자형으로 변환시켜줘야

print()

# Identity(id)
print("Id value")
temp = c
print(temp, c)
print(id(temp))    # 일반 변수들은 값이 같을 경우 그 변수들은 같은 주소를 사용
print(id(c))       # 리스트는 = 으로 같다고 했을 경우만 같은 값을 사용
del(c[3])         # c를 삭제했는데
print(temp)       # temp[3]도 똑같이 삭제

print()

# 리스트 수정, 삭제
print("Modify and Delete list")
g[3] = 10
print('g : ', g)
g[1:2] = ['a', 'b', 'c', 'd']      # 슬라이싱 g[1:2] = g[1]에 요소를 넣는거임
print('g : ', g)
g[1] = ['a', 'b', 'c', 'd']        # 값 재정의 리스트를 넣는거임(2차원 리스트됨)
print('g : ', g)
g[1:3] = []            # 빈 값을 넣어 제거함
print('g : ', g)

del(g[2])    # 삭제
print('g : ', g)

print()

# 리스트 함수
print("list func")
a = [5, 2, 3, 1, 4]

kaka = sum(a)       # sum 쓰는법
print("kaka", kaka)

a.append(10)         # 맨 끝에 값을 추가
print('a.append(x) : ', a)

a.sort()            # 오름차순으로 정렬
print('a.sort() : ', a)

a.reverse()         # 내림차순으로 정렬
print('a.reverse() : ', a)

print('a.index(x) : ', a.index(2))   # a[2] 3번째 인덱스를 출력

a.insert(2, 7)      # a.insert(x, y) x자리에 y값을 삽입
print('a.insert(x, y) : ', a)

a.remove(10)       # 원하는 값을 삭제
print('a.remove(x) : ', a)

print(a.pop())    # 마지막 인덱스를 삭제하고 어떤 게 삭제되었는지 출력
print('a.pop() : ', a)

print('a.count(x) :', a.count(3)) # 값이 몇 개 있는지 개수 출력 / 문자도 사용 가능

ex = [8, 9]

a.extend(ex)     # 끝에 가져다 붙임 / 어펜드는 1개씩인게 다른 점
print('a.extend() : ', a)


#반복문 활용
kaka = [1, 2, 3, 4, 5, 6, 7]
while kaka :             # 리스트의 요소가 없어지면 끝남
    data = kaka.pop()
    print(data)
