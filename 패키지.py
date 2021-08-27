# 파이썬 패키지 : 폴더의 개념
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성된다
# __init__.py : python 3.3 부터는 없어 패키지로 인. -> 단 하위 호환을 위해 작성 추천
# 상대경로 : ..(부모 디렉토리) .(현재 디렉토리) -> 모듈 내부에서만 사용

# 예제 1

import sub.sub1.module1 # 서브 패키지 안에 서브1이라는 패키지 안에 모여있는 모듈들 중에서 module1 가져옴
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub2.module2.mod2_test2()

print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2 # alias

module1.mod1_test1()

m2.mod2_test2()

print()
print()

# 예제 3
from sub.sub1 import * #파일 안의 모듈들을 전부 사용할 것이다
from sub.sub2 import *

module1.mod1_test1()

module2.mod2_test2()
