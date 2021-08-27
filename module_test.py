#모듈 사용 실습

import sys

print(sys.path)  # 경로, 파일에 있는 파일들 불러올 수 있음 ex) import 리스

print(type(sys.path))   #리스트형


# 모듈 경로 삽입
#sys.path.append('C:/인프론 파이썬 레벨 1')   # 폴더 이름

#print(sys.path)

#import 모듈   # 파일 이름 , 원래 파일에서 print문을 삭제 혹은 주석처리 해야됨

# 모듈 사용
#print(모듈.power(10, 3))


import 모듈

print(모듈.add(300, 1010))
