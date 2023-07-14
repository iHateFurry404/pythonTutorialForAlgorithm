import math # 이렇게 써도 되지만 이렇게 쓴다면 읽기가 불편하다. 
# import math as m이라 친다면 m.acos()이런식으로 써야한다.
from time import time # 특정 모듈만 뽑고싶다면 이렇게 쓴다. time모듈을 쓰고싶다면 time()만 치면 되지만, 함수 이름이 겹치는게 생기면 문제가 생기는 단점이 있다. time 대신 *를 쓰면 모두 가져온다는 뜻이다

acos1 = math.acos(1) # 이렇게 길게 써야한다.
print(time())

# 앞으로 pytorch, tenserflow, numpy, panda같은 라이브러리 튜토리얼도 만들 예정이다.
