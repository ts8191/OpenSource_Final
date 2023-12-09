#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201801 이름 : 김태성

import os
import time
from functools import cmp_to_key

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):            # strung 오타-> string // my_string과 tsrget을 문자열로 인수를 받음
    n = len(target)                         # target의 길이를 n에 저장
    answer = 0                              # answer 0으로 초기화
    for i in range(len(my_string)):         # my_string 범위 내 비교 반복
        if my_string[i:i+n] == target:      # my_string의 i부터 타겟 길이만큼 타겟과 비교
            answer = 1                      # 비교 후 같을 경우 answer = 1
            break                           # 같으면 비교 반복 불필요하므로 반복문 나옴
    return answer                           # answer 값 반환

###### solution()

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution2(letter):                                              # 솔루션 2로 이름 변경
    morse = {                                                       # 모스 부호를 저장한 딕셔너리
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x', 
    '-.--':'y','--..':'z'}
    answer = ''                                                     # answer로 빈 문자열 생성  
    split_letter = letter.split(" ")                                # 입력으로 받은 letter를 공백으로 잘라 split_letter에 저장
    for i in range(len(split_letter)):                              # split_letter 길이 만큼, 즉 모스부호 해독 할 길이 만큼 반복
        answer += morse[split_letter[i]]                            # answer에 모스 딕셔너리에서 split_letter key 값으로 value(해독 값) 가져옴
    return answer                                                   # answer 반환

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution3(age):                                                 # 솔루션 3으로 이름 변경 
    s_age = str(age)                                                # 정수 age를 문자열 s_age로 변경
    answer = ''                                                     # 빈 answer로 문자열 생성
    for i in range(len(s_age)):                                     # s_age의 길이 만큼, age정수 자릿수 만큼 반복
        answer += chr(int(s_age[i])+96)                             # s_age의 각 요소를 자릿수 별로 정수로 변환함. 이후 아스키 코드로 변환함. 이 때 아스키코드 기준 97이 a이므로 1을 기준으로 96을 더함
                                                                    # chr() 함수는 정수를 아스키 코드로 변환 str 이 string이면 chr 은 character 
    return answer                                                   # 변환한 아스키코드를 합친 answer를 반환


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution4(r1, r2):                                                          # 솔루션 4로 이름 변경
    answer = 0                                                                  # answer 0으로 초기화
    for i in range(-r2, r2+1):                                                  # 큰 원인 r2 기준 반경내 정수 만큼 반복 이 떄 음수 및 r2 값도 포함하여 반복 
        for j in range(-r2, r2+1):                                              # y좌표 까지 구하기 위해 두번 반복
            if ((i**2 + j**2)>= r1**2) and ((i**2 + j**2)<= r2**2):             # 원의 공식 x^2 + y^2 = r^2를 이용하여 r1 반경 이상 또는 r2 반경 이하의 식을 만족하는 x y 좌표가 맞는지 연산   
                answer+=1                                                       # 조건을 만족하는 경우 두 원 사이의 좌표이므로(i, j = x, y좌표) answer 점 개수를 1 가산
                #print(i, j)                                                    # 디버깅 용
    return answer                                                               # answer 반환


# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution5(numbers):                                                         # 솔루션 5로 이름 변경
    answer = ''                                                                 # answer 문자열을 ''로 초기화
    tmp_list = []                                                               # tmp_list라는 배열 생성
    for i in range(len(numbers)):                                               # numbers 배열 길이 만큼 반복
        for j in range(len(numbers)):                                           # numbers 배열 길이 만큼 반복(sort 알고리즘에 따라 가장 큰 O(n)인 n^2로 가정) 
            numbers.sort(key = cmp_to_key(comp))                                # numbers comp 함수를 키 값으로 정렬 cmp_to_key를 이용하여 사용자 정의 정렬 함수 사용
    for i in range(len(numbers)):                                               # numbers 길이 만큼 반복
        answer += str(numbers[i])                                               # answer에 정렬된 numbers를 저장
    return answer                                                               # answer 반환

def comp (a, b):                                                                # comp의 정렬 함수 생성/ 합친 기준으로 큰 순으로 정렬하면, 결국 answer 또한 제일 큰 순으로 정렬 됨
    if int(str(a)+str(b)) < int(str(b)+str(a)):                                 # 문자열 a+b 가 b+a보다 작을 떄 ex) 12, 3이 있다면 123 이 312보다 작음
        return 1                                                                # 1반환
    elif int(str(a)+str(b)) == int(str(b)+str(a)):                              # 문자열 a+b 가 b+a와 같을 때 ex) 9, 99가 있다면 어떻게 문자열을 합치나 999로 같음
        return 0                                                                # 0반환
    else:                                                                       # 문자열 a+b 가 b+a보다 클 떄
        return -1                                                               # -1 반환


def main():                                                                                         # 실행을 위한 main()함수
    print(solution("asdfasdfaa", "asdfa"))                                                          # 임의의 두 문자열으로 solution2 호출 및 출력 
    print(solution2("-.- -. --- .-- -.-- --- ..- .-. ... . .-.. ..-."))                             # 모스부호 know your self 
    print(solution3(123456789))                                                                     # 1부터 9까지 영어로 변환
    print(solution4(2, 3))                                                                          # r1및 r2 반경 각각 2, 3으로 설정 
    print(solution5([95,92,945,6, 10, 2,351]))                                                      # 임의의 숫자 리스트 
if __name__ == '__main__':                                                                          # 프로그램의 시작점 확인하는 코드, 코드를 모듈이 아닌 메인 프로그램으로 사용
    main()                                                                                          # main 함수 출력

    