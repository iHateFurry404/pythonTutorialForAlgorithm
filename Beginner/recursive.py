from time import sleep

# 재귀(再歸)함수는 자신을 부르는 함수이다.
def countdown(n):
    # 이 함수는 for문 대신 재귀함수를 쓴 함수이다.
    if n == 0: # n이 0이라면 '끝!'이라고 말하고 아무것도 반환하지 않는다(끝낸다). 이것을 기저 조건이라한다.
        print('끝!')
        return
    print(f'{n}...')
    sleep(1) # 어우 근본없어;;
    # 자기 자신을 불러 함수를 실행한다.
    return countdown(n - 1) # countdown(n - 1)이라고 써도 된다.

def fibonacci(n):
    # 이 함수는 재귀 함수를 사용한 피보나치 수열이다.
    if n <= 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1) # 피보나치 수열의 정의에 따라 n번째 항은 (n-2)번째 항과 (n-1)번째 항을 더한 값이다.

# 재귀함수는 어떤때는 오히려 더 독이 될수 있으니 신중해서 쓰기를 바란다.
countdown(5)
print(f'{fibonacci(5)}')
