# 넘파이, 싸이파이 등에 쓰임
# 집합(set) 자료형(순서, 중복 X, 추가 및 삭제 가능)

# 선언

a = set()

b = set([1, 2, 3, 4, 3, 4, 1, 2])    # 리스트 방식으로 넣어줌
c = set(['a', 'b', 'd', 'e', 'a'])
d = set([1, 2, 'pen', 'cap', 'plate'])
e = {'foo', 'bar', 'baz', 'fooz', 'quz'}   # 키 없으면 세트임
f = {42, 'foo', (1, 2, 3), 3.141592}

print("a : ", type(a), a)      # 저절로 중복 삭제되면서 순서가 맞춰지나?
print("b : ", type(b), b)
print("c : ", type(c), c)
print("d : ", type(d), d)
print("e : ", type(e), e)
print("f : ", type(f), f)
print()

# 튜플 변환(set -> tuple)
t = tuple(b)
print("t : ", type(t), t)
print("t : ", t[0], t[0:3])
print()
# 리스트 변환(set -> list)
li = list(c)
li2 = list(e)

print("li : ", li)
print("li2 : ", li2)
print()

# 집합 자료형 활용

#s1 = set([1, 2, 3, 4, 5, 6])
#s2 = set([4, 5, 6, 7, 8, 9])
# 교집합
#print('s1 & s2 :' s1 & s2)
#print('s1 & s2 :' s1.intersection(s2))

# 합짐합
#print('s1 | s2 :' s1 | s2)
#print('s1 | s2 :' s1.union(s2)))

# 차집합
#print('s1 - s2 :' s1 - s2)
#print('s1 - s2 :' s1.difference(s2))
#print()

# 중복 원소 확인
#print("s1 & s2 :", s1.isdisjoint(s2))    # 교집합이 있으면False가 나옴
#print()

# 부분 집합 확인
#print('subset :' s1.issubset(s2)     # 부분 집합이면 False가 나옴
#print('superset :' s1.issuperset(s2)   # 포함하는지. 맞으면 False가 나옴
#print()

# 추가 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print("s1 : ", s1)    # 추가

s1.remove(2)
print("s1 : ", s1)    # 삭제, 없는 거 삭제하면 에러 발생

s1.discard(3)
print("s1 : ", s1)    # 추가, 없는 거 삭제해도 에러 발생하지 않음

s1.clear()
print("s1 : ", s1)    # 전부 삭제


a = [1, 2, 3]         # 리스트도 가능
a.clear()
print(a)
