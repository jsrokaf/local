#Q1. 양의 정수 1개를 입력한다. 그 수가
#    짝수인지 홀수인지 판별하여 출력한다.
a = int(input("정수 입력"))
if a%2 == 0 :
    print("짝수")
elif a == 0 :
    print("0입니다.")
else :
    print("홀수입니다.")

#Q2. 사용자로부터 하나의 값을 입력받은 후
#    해당 값에 20을 뺀 값을 출력하라.
#    단 출력 값의 범위는 0~255이다.
#    ex) 출력 값이 0보다 작은 값이되는 경우
#    0을 출력하고 255보다 큰 값이 되는 경우
#    255를 출력해야 한다.

#입력 : 200
#출력 : 180
#입력 : 15
#출력 : 0

a = int(input())
b = a - 20
if b<0:
    b = 0
elif b>255:
    b = 255
print(b)

#Q3. 사용자로부터 입력받은 시간이 정각인지 판별하라.
#   ex) 입력 02:00        
#       출력 정각입니다.
#       입력 05:15
#       출력 정각이 아닙니다.

# hint : 리스트 슬라이싱

t = input()
if t[3:] == "00":
    print("정각")
else:
    print("정각아님")

#Q4. 내가 입력한 단어가 fruit 리스트 안에 있는지
#    확인하라. 포함되어 있다면, 있음 출력
#    포함되지 않았다면 없음 출력
#    hint : in 연산자 - ~안에 있다.
#    ex) 입력 : 바나나
#        출력 : 있음

fruit = ["사과","바나나","포도"]
a = input()
if a in fruit :
    print("있음")
else :
    print("없음")



# 코딩도장 15.3

x = int(input())
if 11<=x<=20 :
    print("11~20")
elif 21<=x<=30 :
    print("21~30")
else :
    print("아무것도 해당하지 않음")

#Q7. 알파벳 한 개를 입력받고, 입력한 알파벳이
#    소문자라면, 대문자로 바꿔서 출력한다.
#    대문자라면, 소문자로 바꿔서 출력한다.
#    입력 : A
#    출력 : a

#    Hint : c = 'a'
#           c.upper() = A
#           c.lower() = a
#         c.isupper() = True or False
#         c.islower() = True or False

a = input()
if a.islower():
    print(a.upper())
else:
    print(a.lower())


#Q8. 숫자를 3개 입력받는다.
#    그 중 가장 큰 숫자만 출력한다.
#    ex) 입력 : 15 9 20
#        출력 : 20

a=int(input())
b=int(input()
c=int(input())
if a>b and a>c :
    print(a)
if b>c and b>a :
    print(b)
else :
    print(c)
      
#9. 주민등록번호 뒷자리 중 첫번째 자리는
#   성별을 나타낸다. 남자는 1,3 , 여자는 2,4
#   13자리의 주민등록번호를 입력받고
#   그 사람의 성별을 출력한다.

#   ex) 입력 : 821010-1687310
#       출력 : 남자
#       입력 : 051231-4133112
#       출력 : 여자


























