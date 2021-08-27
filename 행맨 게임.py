# Hangman 미니 게임 제적

# 기본 프로그램 제작 및 테스트

import time
import csv
import random
import winsound

# 처음 인사
name = input("What is your name?")

print("Hi, " + name, "Time to play hangman game!")

print()

time.sleep(1) # 1초 딜레이

print("Start Loading . . .")

print()

time.sleep(0.5)

# CSV 단어 리스트
words = []

#문제 CSV 파일 로드
with open("./resource/word_list.csv", "r") as f :
    reader = csv.reader(f)
    # Header Skip
    next(reader)
    for c in reader :
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)



# 정답 단어
word = q[0].strip() # strip 공백 제거

# 추측 단어

guesses = ''

# 기회

turns = 10

# 동작 While Loop
# 기회가 남아있을 경우
while turns > 0 :
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word :
        #정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses :
            # 추측 단어 출력
            print(char, end = "")
        else :
            # 기본(처음엔 guesses가 ""이기 떄문에 else로 들어가기 때문), 틀린 경우 대시로 처리
            print("_", end = " ")
            failed += 1

    # 단어 추측이 성공 한 경우
    if failed == 0 :
        print()
        print()
        #성공 사운드
        winsound.PlaySound("./sounds/딩동댕동댕.wav", winsound.SND_FILENAME) # SND_FILENAME : 파일을 그대로 실행하기
        print("Congratulations! The Guesses is correct!")
        # while 탈출
        break
    print()

    # 추측 단어 글자 단위 입력
    print()
    print("Hint : {}".format(q[1].strip()))
    guess = input("guess a word.")

    # 단어 더하기
    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word :
        turns -= 1
        # 오류 메시지
        print("Ooup! Worong")
        print("You have", turns, "more guesses!")

        if turns == 0 :
            # 실패 메세지
            winsound.PlaySound("./sounds/땡.wav", winsound.SND_FILENAME)
            print("You failed hangman game!")
