# 파일 읽기 및 쓰기

# 읽기 모드 : r, 쓰기 모드 : w, 추가 모드 : a, 텍스트 모드 : t, 바이너리 모드 : b
# 상대 경로 :  ('../')  상위 위치, ./ 현재 위치
# 절대 경로 : ('C:\Django\example.......')

# 파일 읽기(Read)
# 예제 1

#f = open('C:\Users\polit\Desktop\인프론 파이썬 레벨 1\resource\it_news')
f = open('./resource/it_news.txt', 'r', encoding = 'UTF-8')
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
cts = f.read()
print(cts)
# 반드시 닫기
f.close()
print()

# 예제 2
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f :
    c = f.read()
    print(c)
    print(iter(c))
    print(list(c))

print()

# 예제 3
# read() : 전체 읽기, read(10) -> 10바이트 불러오기
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f :
    c = f.read(20)
    print(c)
    c = f.read(20) # 내부적으로 커서가 있다는 걸 보여줌
    print(c)
    f.seek(0.0) # 처음오로 돌아감
    c = f.read(20)
    print(c)

print()

# 예제 4
# readline : 한 줄 씩 읽기
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f :
    line = f.readline()
    print(line)
    line = f.readline() # 반복문으로 출력하는게 효율적0
    print(line)

# 예제 5
# readlines : 전체를 읽은 후 라인 단위 리스트로 저장
with open('./resource/it_news.txt', 'r', encoding = 'UTF-8') as f :
    lines = f.readlines()
    print(lines)
    print()
    for c in lines :
        print(c, end ='')


# 파일 쓰기(write)
# 예제 1 : write (덮어씀)
with open('./resource/contents1.txt', 'w') as f :
    f.write('i love python\n')

# 예제 2 : append
with open('./resource/contents1.txt', 'a') as f :
    f.write('lululalla')

# 예제 3
#writelines : 리스트 -> 파일
with open('./resource/contents1.txt', 'w') as f :
    list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
    f.writelines(list)

# 예제 4
with open('./resource/contents1.txt', 'w') as f :
    print('Test Text Write!', file = f) # 파일에 출력해줌
