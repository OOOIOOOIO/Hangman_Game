# 파이썬 외장(External) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutill, temfile, time, random 등

# 예제 1
import sys
print(sys.argv) # 값을 불러옴 구글에 쳐보기

# 예제 2(강제 종료)
# sys.exit()

# 예제 3(파이썬 패키지 위치)
print(sys.path)

# pickle : 객체(클래스 딕셔너리 리스트 튜플 등) 파일 읽기, 쓰기
import pickle

# 예제 4(쓰기)
f = open("test.obj", "wb")
obj = {1: 'pyton', 2 : 'study', 3: 'base'}
pickle.dump(obj, f)
f.close()

#예제 5(읽기)
f = open("test.obj", "rb")
data = pickle.load(f)
print(data, type(data))
f.close()
print()
# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 관련
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제 6
import os # 딕셔너리 형태
print(os.environ)
print(os.environ['USERNAME'])
print()

# 예제 7(현재 경로)
print(os.getcwd())
print()
# time : 시간 관련 처리
import time

# 예제 8
print(time.time()) # 시 분 초로 출력
print()

# 예제 9 (형태 변환)
print(time.localtime(time.time())) # 분해해서 보여줌
print()

# 예제 10(간단 표현)
print(time.ctime())
print()

# 예제 11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# %Y 년, %m 월, %d 일, %H 시, %M 분, %S 초 대소문자 구분해야됨

# 예제 12(시간 간격 발생)
for i in range(5) :
    print(i)
    #time.sleep(1) # 초를 넣음, 1초 뒤 실행됨

print()

# random : 난수 리턴
import random

# 예제 13
print(random.random()) # 0 ~ 1 실수

# 예제 14
print(random.randint(1, 10)) # 1 ~ 10 정수
print(random.randrange(1, 10)) # 1 ~ 9 정수
print()

# 예제 15 (섞기)
d = [1, 2, 3, 4, 5]
random.shuffle(d)
print(d)
print()

# 예제 16(무작위 선택)
c = random.choice(d)
print(c)

# webbrowser : 본인 os의 웹 브라우저를 실행합니다.
import webbrowser

webbrowser.open("http://naver.com") # 네이버 켜짐 개신기

webbrowser.open_new("http://naver.com") # 새 창으로 열기
