from sys import stdout
from os import system
from random import randint

# 브루트 포스(brute force)는 단순한 힘, 단순히 말하면 멍청한 힘이라는 뜻으로, 그냥 문제를 찍어내는 행위를 약간 품위 있게 부르는 말이다.
# 아래 코드를 보자면, for문을 이용해 아예 다 찍어내고 있다. 0 ~ 9999중에 하나를 answer에 저장 후 brtueForce 함수에 넣는다.
# 그것을 맞출때까지 계속 때려 맞추는 간단한 알고리즘을 구현한 코드이다.

def bruteForce(answer):
    for i in range(0, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                for l in range(0, 10):
                    number = i * 1000 + j * 100 + k * 10 + l
                    if number != answer:
                        stdout.write(str(answer).zfill(4) + '이(가) 비밀번호입니다.\n')
                        stdout.write('\033[31m' + str(number).zfill(4) + '\033[0m' + '은(는) 비밀번호가 아니었습니다...')
                    else:
                        system('cls')
                        stdout.write(str(answer).zfill(4) + '이(가) 비밀번호입니다.\n')
                        stdout.write('\033[92m' + str(number).zfill(4) + '\033[0m' + '이(가) 비밀번호였습니다!')
                        return None

answer = randint(0, 9999)

bruteForce(answer)
