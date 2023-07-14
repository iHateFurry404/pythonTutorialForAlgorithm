# def 함수는 직접 함수를 만들수있으며, 값을 반환하거나 안해도 된다.
# 참고로 함수안에 함수를 선언할수 있으며, 함수안에 자기 자신을 쓸수있고, 다른 함수를 쓸수있다.
def fibonacci(n = 3): # 괄호 안에 들어가는것은 매개변수로, 함수안에서 쓰이는 변수이다. 매개변수는 받는 것이고, 없어도 된다. n = 3같이 초깃값을 쓸수도 있다.
    current, next = 0, 1 # current는 현재 항의 값, next는 다음 항의 값을 나타낸다.
    for _ in range(n): # n항까지의 피보나치 수열을 계산
        # 피보나치를 구하는 식 = 현재 항의 값 + 다음 항의 값이므로 아래 코드처럼 된다.
        current, next = next, current + next # current 값은 next가 되고 next는 current + next가 된다.
    return current # 값을 반환한다.
    # 값을 반환하지 않고도 print같은 것으로 기능을 할수있다.

print(f'{fibonacci(6)}') # 저기 안에 들어가는 숫자는 매개변수가 아니라 인수라고 한다.
