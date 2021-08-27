#문자열 생성

str = "i am python" # '', "", """~""", '''~'''

print(len(str)) # 문자열 길이 공백 포함

print()

# 빈 문자열 생성
str_t1 = ''   #'', ""
# str_t2 = str()

# 이스케이프 문자 사용

print("i'm boy")
print('i\'m boy') # ' ' 이거로 묶고 싶으면

escape_str = "Do you have a \"retro game\"?"

print(escape_str)

print()

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line\nCheck!"
print(t_s1)
print(t_s2)

print()

# Raw String
raw_s1 = r'D:\python\test' # r붙여서 사용. \ escape문자 쓰지 않고 있는 그대로 출력하고 싶을 떄
print(raw_s1)

print()

# 멀티라인 입력 \ 사용해서 보기 편하게.
multi_str = \
"""
string
multi Line
test
"""

print(multi_str)

print()

# 문자열 연산

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "Hi hi hi hi"
str_o4 = "Bye bye bye"

str = "apiinbmck"
str2 = "abc321"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('y' not in str_o1)

print()

# 문자열 함수
print("Capitalize : ", str_o1.capitalize()) # 첫 글자 대분자로
print("endswith : ", str_o2.endswith('e')) #마지막 문자가 어떻게 끝나는지 T or F
print("replace : ", str_o1.replace('thon', 'gd')) #thon을 good으로 바꿔줌
print("sorted : ", sorted(str_o1)) # 정렬
print("sort : ", sorted(str)) # 정렬
print("sort2 : ", sorted(str2)) # 정렬
print("split : ", str_o4.split(' ')) # 단어, 문장 단위로 분리할 때 쓰임

print()

# 반복(시퀸스)
im_str = "Good Boy!"

print(dir(im_str)) # 속성 /  __iter__ : 반복할 수 있다는 뜻

for i in im_str :
    print(i)
print()
# 슬라이싱
str_s1 = "Nice python"
print(len(str_s1))
print(str_s1[0:3]) # [0:3] -> 0~2번까지 나옴. 마지막 수 -1번쨰까지
print(str_s1[5:]) # 5부터 끝까지
print(str_s1[:len(str_s1)]) # 처음부터 끝까지
print(str_s1[1:9:2]) # 1부터 9까지 2칸씩 출력
print(str_s1[-5:]) # 마이너스는 -1부터 시작
print(str_s1[1:-2]) # 1부터 -3까지 출력 -2에서 -1해줘야됨  --슬라이싱은 마지막 값에 항상 -1
print(str_s1[::2]) # 처음부터 끝까지 2칸씩
print(str_s1[::-1]) #거꾸로 출력

print()

# 아스키 코드(또는 유니코드)

print(ord('a')) #아스키코드를 번호로 보여줌
print(ord('z')) #아스키코드를 번호로 보여줌
print(chr(122)) # 번호를 아스키코드로 보여줌
