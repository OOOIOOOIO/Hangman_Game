# 리스트와 비교 중요
# 튜플 자료형(순서, 중복 가능 but 수정, 삭제 불가능) => 불변

# 선언

a = ()
a_1 = tuple()
b = (1, )        # 원소가 1개일 때 무조건 , 찍어줘야됨 안찍으면 그냥 int형임
c = (11, 12, 13, 14)
d = (100, 1000, "Ace", "Base", "Captine")
e = (100, 1000, ("Ace", "Base", "Captine"))
print(type(b))

# 인덱싱
print("Indexing")
print("d : ", d[1])
print("d : ", d[0] + d[1] + d[1])
print("d : ", d[-1])
print("e : ", e[-1])
print("e : ", e[-1][0])
print("e : ", list(e[-1][1]))              #리스트랑 쓰는 법 똑같음

print()

#슬라이싱
print("Slicing")
print("d : ", d[0:3])
print("d : ", d[:])
print("e : ", e[2][:])

print()

# 튜플 연산
print("Calculate tuple")
print("c + d : ", c + d)
print("c * 3 : ", c * 3)

print()

# 튜플 함수
print("tuple func")
a = (5, 2, 3, 1, 4)
print("a : ", a)

print("a : ", a.index(3))     # 요소의 번호를 출력

print("a : ", a.count(2))      # 값이 몇 개 있는지 개수

print()

# 팩킹 & 언팩킹(Packing, Unpacking)

# 팩킹

t = ('one', 'two', 'three', 'four')  # 4개의 요소를 하나로 묶음

print(t)
print(t[0])
print(t[-1])

# 언팩킹_1

(x1, x2, x3, x4) = t

print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3), type(x4))
print(type(t))

print()

# 팩킹과 언팩킹 정리

t2 = 1, 2, 3              # 이런 식으로 괄호 없이 콤마로 이어지면 팩킹
t3 = 1,                   # 항상 요소 1개는 ',' 써주기
print(type(t2))
print(type(t3))

(y1, y2, y3) = t2         # 언팩킹 t2는 튜플  y1, y2, y3은 인트형
print(y1, y2, y3)
print(type(t2), type(y1))

z1, z2, z3 = 5, 6, 7
print(z1, z2, z3)
print(type(z1))


arr = [1, 2, 3, 4]        # 리스트도 팩킹 & 언팩킹 가능
a, b, c, d = arr
print(a, b, c, d)
print(type(a), type(arr))
