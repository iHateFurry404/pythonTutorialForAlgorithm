if 1 + 1 == 2: # if문 뒤에 나오는것은 조건식으로 True인 경우 아래 있는 명령문을 실행하고 아니라면 elif나 else로 보낸다. 참고로 모든 if, elif는 조건에 부합하다면 if문을 종료한다.
    # 참고로 조건문에 숫자를 넣어도 되는데, 0은 False, 그 외의 숫자는 True가 된다.
    print('당연한거 아니야?')
elif 1 + 1 == 1: # elif는 위에 if나 elif(elif는 여러개 쓸 수 있다.)가 참이 아닐때 실행하게 된다. 참이 아니면 아래로 가게 된다.
    print('절대 일어날일 없는곳')
else: # 모든 상황이 아닐때 온다. if문 안에서 딱 하나만 쓸 수 있다.
    print('히히')

a = 32
b = 1972

if a < b: # a가 b보다 작다면 True를 반환한다.
    print('A < B')
elif a > b: # a가 b보다 크다면 True를 반환한다.
     print('A > B')
elif a == b: # a와 b가 같다면 True를 반환한다.
     print('A == B')
elif a is b:  # a가 b라면 True를 반환한다. ==(!=포함)와 혼동하는 사람이 있는데, ==는 값을 비교하고 is는 객체를 비교한다.
    print('A is B')
elif a is not b: # a가 b와 같지 않다면 True를 반환한다.
    print('A is not B')
elif a != b: # a와 b가 다르다면 True를 반환한다.
     print('A != B')
elif a >= b: # a가 b 이상이면 True를 반환한다.
     print('A >= B')
elif a <= b: # a가 b 이하라면 True를 반환한다.
     print('A <= B')

if True and True: # and연산자는 양쪽 모두 참이면 True를 반환한다.
    print('Truly True')
elif True or False: # or연산자는 양쪽 중 하나만 참이여도 True를 반환한다.
    print('Truly False')
elif not True: # not 옆의 조건문의 결과를 뒤집는다 예: 참 -> 거짓, 거짓 -> 참
    print('Not True')
elif True ^ False: # xor연산자, 둘중 하나만 참이여야지 True를 반환한다.
    print('Xor True')


xorTest = True if True ^ True else False # 이렇게 더 간단히 쓸 수 있게 한다. 아래는 작성 방법이다. 이렇게 쓰게 된다면 더 가독성이 높아질수도 있다. + elif는 들어갈 수 없다.
# variableName = 조건문이 참일시 들어갈 값 if 조건문 else 아닐때 들어갈 값

match a: # match  뒤에는 식, 변수가 들어갈수 있으며, 여러개 넣을수 있다.
    case 32: # a의 값이 32면 아래 실행
        print('yipee')
    case 52:
        print('not yipee')
    case _: # 위의 것이 아니라면(모든 값) 실행, _는 모든 값을 의미한다.
        print('another')

match (a % 2, a % 3, a % 5):
    case (0, 0, 0): # 위의 식의 결괏값
        print(f'{a}은(는) 2의 배수이면서 3의 배수이면서 5의 배수이다.')
    case (0, 0, _): # _은 위의 값이 아닌 다른 값을 의미한다.
        print(f'{a}은(는) 2의 배수이면서 3의 배수입니다.')
    case (_, _, _):
        print('다 아닌데?')
