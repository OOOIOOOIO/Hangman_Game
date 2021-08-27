# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError(문법), TypeError(자료형), NameError(없는 변수), IndexError(없는 인덱스), ValueError, KeyError
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계) 발생하는 에러
# 1, 예외는 반드시 처리
# 2, 로그는 반드시 남긴다.
# 3, 예외는 던져진다. 처리를 위임할 수 있다.
# 4, 예외 무시


# SyntaxError : 문법 오류

# print("error)     ""
# print("error"))    ()
# if Ture           :
#    pass

#--------------------------------

# NameError : 참조 없음

# a = 10
# b = 15
# print(c)

#---------------------------------

# ZeroDivisionError

# print(100 / 0) : 0으로 못 나눔

#----------------------------------

# IndexError : 범위 벗어남

# x = [ 50, 70, 90]

# print(x[4]) # 없는 인덱스

# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # 빈 리스트기 때문에 에러 발생

#-----------------------------------------

# KeyError

# dic = {'name' : 'lee', 'age' : 25, 'adress' : 'seoul'}
# print(dic['hobby'])   #  키가 존재하지 않음
# print(dic.get('hobby'))  # get은 예외발생시키지 않고 none을 출력

#------------------권장사항---------------------------

# 예외가 없을 수가 없으니 예외가 없을 것이라고 가정하고 프로그램을 작성해라
# -> 런타임(실행할 떄) 예외 발생 처리 권장(EAFP)


#-----------------------------------------------------

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시

# import time
# print(time.time2()) : 존재하지 않을 때 발생

#---------------------------------------------------------

# ValueError : 시퀀스형 자료구조 안에서 존재하지 않을 떄

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

#----------------------------------------------------------

# FileNotFoundError

# f = open('test.txt') # 파일이 없다!

#------------------------------------------------------------

# TypeError : 자료형에 맞지 않는 연산을 사용할 경우

x = [1, 2]
y = (3, 4) # 튜플 불변형
z = 'test'

# print(x + y)
# print(x + z)
# print(x + list(y)) # 형 변환을 해줘야됨
# print(x + list(z)) # 문자열을 리스트로 바꿔주면 ['t', 'e', 's', 't']로 들어움

#-----------------------------------------------------------------

# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코 실행
# except 에러명1  -> 여러개 가능, 맞는 에러명을 써줘야
# except 에러명2
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 마지막에 실행

name = ['kim', 'lee', 'park']

# 예제 1
# try :
#     z = 'kk'
#     x = name.index(z)
#     print('{} found it! {} in name'.format(z, x + 1))
#
# except ValueError : # 예측해서 맞는 에러명을 써줘야됨
#     print('Not found it! - Occured ValueError')
#
# else :
#     print('Ok! else.')
#
# print()
#
# print('pass') # 예외 없이 다음 코드 실행되는 것을 보여 줌

#-------------------------------------------------------------------

# 예제 2

# try :
#     z = 'kk'
#     x = name.index(z)
#     print('{} found it! {} in name'.format(z, x + 1))
#
# except Exception :  # 모든 예외를 잡아줌 별로 권장은 x  or 그냥 except :
#     print('Not found it! - Occured ValueError')
#
# else :
#     print('Ok! else.')
#
# print()
#
# print('pass')

#---------------------------------------------------------------------------------

# 예제 3 : 애가 제일 좋음, Exception 대신 정확한 에러명 사용하기

# try :
#     z = 'kk'
#     x = name.index(z)
#     print('{} found it! {} in name'.format(z, x + 1))
#
# except Exception as e :  # as e를 붙여줌. 로그를 남길 떄 좋
#     print(e)             #에러의 내용을 출력해 줌
#     print('Not found it! - Occured ValueError')
#
# else :
#     print('Ok! else.') # 예외가 발생하지 않을 경우에만 실행
#
# finally :
#     print('Ok! finally') # 무조건 실행됨
#
# print()
#
# print('pass')

#------------------------------------------------------------------------------------

# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try :
    a = 'park'
    if a == 'kim' :  # kim 이새끼만 안들어왔구나
        print('ok! pass!')
    else :
        raise ValueError  # 강제로 ValueError를 발생시킴

except ValueError :
    print('Occureed Exception!')

else :
    print('ok good')
