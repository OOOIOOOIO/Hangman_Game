# 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서 x, 키 중복 허용 x, 수정 및 삭제 가능)

# 선언   {키 : 밸류}

a = {'name' : 'kim', 'phone' : '01020057950', 'birth' : '980111'}

b = { 0 : 'Hello'}           # 키 값은 숫자 문자 다

c = {'arr' : [1, 2, 3, 4]}   # 밸류에 리스트 튜플 등 넣을 수 있음

d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 25,
    'Grade' : 'A',
    'Status' : True
}

e = dict([                   # 리스트 안에 튜플 형태로 ,
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 25),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 24,
    Grade = 'A',
    Status = True
)

# arr = [f1, f2 ,f3 ...] 정보를 이런식으로 정리할 수 있음

print("a : ", type(a), a)
print("b : ", type(b), b)
print("c : ", type(c), c)
print("d : ", type(d), d)
print("e : ", type(e), e)
print("f : ", type(f), f)

print()

# 출력

print("a : ", a['name'])           # 확실할 경우 속성으로 접근. 키가 없으면 에러 발생
print("a : ", a.get('name'))       # get으로 많이 가져옴. 키가 없으면 none 출력
print()
print("b : ", b[0])
print("b : ", b.get(0))
print()
print("f : ", f['City'])
print("f : ", f.get('Age'))
print()


# 딕셔너리 추가
a['address'] = 'busan'      # 마지막에 추가
print("a : ", a)
print("a : ", len(a))       # 키의 개수.
print()

# 딕셔너리 함수 dict_keys, dict_values, dict_items : 반복(__iter__)에서 사용 가능

print("a : ", a.keys())     # 키 값들만 가져옴
print("b : ", b.keys())
print("c : ", c.keys())
print()

print("a : ", list(a.keys()))  # 리스트로 형변환해서 우리가 편하게 쓰게할 수도 있음
print("f : ", list(f.keys()))
print()

print("a : ", a.values())     # 밸류 값들만 가져옴
print("c : ", c.values())
print()

print("a : ", list(a.values()))   # 마찬가지로 리스트로 형 변환해서 편하게~~
print("c : ", list(c.values()))
print()

print("a : ", a.items())        # 딕셔너리의 키와 밸류가 튜플 형태로 짝 지어서 출력
print("c : ", c.items())
print()

kaka = list(a.items())
print(kaka[0][0])

print("a : ", list(a.items())) # 리스트로 형 변환, 딕셔너리는 튜플 형태로 저장되어 있음
print("c : ", list(c.items()))
print()

print("길이 : ", len(a))
print("a : ", a.pop('name'))    # 밸류값이 출력되고 키, 밸류 삭제
print(a)
print("길이 : ", len(a))
print()

print("f : ", f.popitem())    #임의로 하나가 삭제됨
print(f)
print()

print("a : ", "lacation" in a)
print()

print(a)
a.update(birth = '960823')      # 수정하는 법
print(a)
