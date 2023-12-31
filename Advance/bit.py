# 12를 1110000로, 32를 1011011로 정의한다.
print(12 << 2) # << 레프트 시프트는 a << b 형식으로 쓰며, a의 비트를 b만큼 왼쪽으로 이동하라는 의미이다.
# 예 : 001110000 -> 111000000
print(12 >> 2) # >> 라이트 시프트는 a >> b 형식으로 쓰며, 위와 다르게 a의 비트를 b만큼 오른쪽으로 이동시키라는 뜻이다.
# 예 : 1110000 -> 0011100
print(12 ^ 32) # xor 연산자로,  a ^ b 중 하나만 1이면 1, 아니면 0을 반환한다. 아래는 그 예시다.
"""
1110000
1011011 ^ =
0101011
"""
print(12 | 32) # or 연산자로, a | b 중 하나 이상 1이면 1, 아니면 0을 반환한다. 아래는 그 예시다.
"""
1110000
1011011 | =
1111011
"""
print(12 & 32) # and 연산자로, a, b 둘 다 1이면 1, 아니면 0을 반환한다. 아래는 그 예시이다.
"""
1110000
1011011 & =
1010000
"""
print(~12) # not 연산자로, 비트를 뒤집는다. 1이 있으면 0, 0이 있으면 1로 바꾼다.
# 예: 1110000 -> 0001111
