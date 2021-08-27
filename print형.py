#separate : 옵션 한 문장 안에서 문자 사이사이 삽입시키는 역할

print('a', 'b', 'c', 'd', 'e', sep = '')
print('010', '2005', '7950', sep = '-')
print('polite159', 'gmail.com', sep = '@')

print() #한 칸 띄움

a = 10
b = 20
c = "Asd"
print("{1} + {0}".format(a, b)) # {0} {1} ...로 순서를 정할 수 있음
print("%d + %d"%(a, b))

print()
#end 옵션 : 다음 문장과의 연결시키는 역학


print("Welcome to", end = ' ')
print("Seongho's", end = ' ')
print("home")

print()

# file 옵션

import sys

#print('lulul', file = sys.stdout)
#print("hi hello", file = 'text.txt') # hi hello를 외부의 text.txt 파일어 넣

print()

# format 사용법(d, s, f)   =>(정수, 문자, 실수)

print('%s\t\t%s' %( 'one', 'two')) # %s %s 사이에 , 쓰면 ,도 출력
print('{},, , , , , , ,  {}'.format('one', 'two')) # {} {} 사이에 , 쓰면 마찬가지로 ,도
print('{2} {0} {1}'.format('one', 'two', 'three')) # {0} {1} {2} 순서가 정해져 있는데 {2} {0} {1} 이런식으로 순서를 지정할 수도 있음

print()

# %s 사용법
print("<우측 좌측 정렬 사용법")
print("%10s" % ('56789')) # 10자리를 만들어 놓고 우측 정렬로 출력
print("{:>10}".format('56789')) # 인위적으로 :>을 사용해 우측 정렬로 -

print("%-10s" % ('01234')) # 10자리를 만들어 놓고 좌측 정렬로 출력
print("{:10}".format('01234')) # 인위적으로 :을 사용해 좌측 정렬로 -

print("{:@>10}".format('56789')) # 공백에 원하는 문자로 채우기

print("{:^10}".format('56789')) # 중앙 정렬

print("%5s" % ('abcdefghi')) # 5글자가 넘어도 출력 됨
print("%.5s" % ('abcdefghi')) # 5글자만 딱.

print("{:10.5}".format('0123456789')) # 공간은 10개를 가지고 있는데 5글자만 나와

print()

# %d 사용법

print("%d %d" %(1, 2))
print("{} {}".format(1, 2))

print('%4d' %(10))
print('{:4d}'.format(10))

print()

# %f 사용법

print('%f' %(3.141592))
print('%.3f' %(3.141592)) # 소수부 3자리 출력
print('{:f}'.format(3.141592))
print('%06.2f' %(3.141592)) # 총 6자리에 정수부부 3자리 출력 남은 자리 0으로 채움, 소수부 2자리 출력
print('{:06.2f}'.format(3.141592))
