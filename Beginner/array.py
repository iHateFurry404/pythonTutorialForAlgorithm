from copy import deepcopy # copy라는 곳에서 deepcopy라는것을 가지고 와라

a = [True, 2, 3, '4', 5.0, [1, 2, 3, 4, 5]] # 진짜 다양한걸 넣을수 있다. 배열 안에 배열을 집어 넣을수도 있고, 튜플, int, float, 문자열 등등을 넣을 수 있다.
print(f'{a[0]}') # 이렇게 접근할수 있으며, 0부터 시작한다. 마지막 번호는 -1로 표현할수 있다. 저런 숫자를 인덱스라고 부른다.
print(f'{a[5][0]}') # 배열안에 있는 배열은 이렇게 접근할수 있다.

b = [[123, 456], [654, 321]] # 배열 안의 배열의 개수에 따라 n차원 배열이라 부른다. 이 배열은 2차원 배열이다.
d = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]] # 3차원 배열의 예

# 슬라이스는 배열을 잘라 나타낼수 있는 식(?)이다.
# 슬라이스는 배열[시작:목표:스텝(점프)] 으로 배열[시작]부터 배열[목표 - 1]까지를 나타낼 수 있다.
# 스텝은 몇칸씩 점프하는지 정할 수 있는 것이다. 기본 값은 1. 굳이 안써도 된다.
# 슬라이스에서 시작이나 목표가 비어있다면 처음부터/끝까지 라는 뜻이 된다.
print(f'{a[:]}') # 전부 다
print(f'{a[1:3]}') # a[1]부터 a[3 - 1]까지
print(f'{a[0:1]}') # a[0]부터 a[1 - 0]까지(처음)
print(f'{a[::2]}') # 처음부터 끝까지, 근데 2칸씩
# 참고로 a[slice(0, 0, 2)] 같이 함수로도 쓸 수 있다.

a.append('asdf') # append 메소드는 a에 요소를 넣을수 있게하는 메소드이다. 2개 이상의 값을 입력하면 오류가 생긴다.
a.extend(b) # 리스트를 추가할 수있다.
a.count(2) # 값의 개수를 셀수 있게 해준다.
a.index(5.0) # 입력한 값에 먼저 있는 그 값의 위치를 반환한다.
a.insert(3, '999') # 첫번째 값의 인덱스 뒤에 두번째 값을 넣는다. 
a.pop() # 해당 인덱스에 있는 요소를 삭제하고 삭제한 요소를 반환한다. 기본값은 -1이다.
a.remove('asdf') # 배열에서 값을 삭제한다. 하나만 입력할수있다.
a.reverse() # 배열을 뒤집는다.
# a.sort() # 배열을 정렬한다. 내림차순 하려면 a.sort(reverse = True)로 하면 된다. 숫자와 문자 둘다 섞여 있을때 쓴다면 에러가 생긴다.


e = a * 3 # 이렇게 리스트를 여러게 복사할 수도 있다.
f = a # 혹은 f = a[:]
print(f'{e}') # 그냥 리스트를 통째로 보고싶다면 이렇게 바꾸기도 한다.

# a[1] + a[2] 같이 덧셈도 할수 있다.
a[0] = 1 # 이렇게 변수를 바꿀수도 있다.
print(f'{e[0]}')
print(f'{f[0]}') # 어?  왜 f[0]은 바뀌는데 왜 e[0]은 왜 안 바뀌는 인걸까?
# e[0]이 안 바뀌는 이유는 a를 3번 e 리스트에 더했는데, 더이상 a와 연결되지 않고 독립적인 개체라 판단이 되어 바뀌지 않는 것이다.
# f[0]이 바뀌는 이유는 f가 '얕은 복사(Shallow copy)'를 했기 때문이다. 얕은 복사는 정말 최소한만 복사한다. 즉 id는 바뀌지 않고 계속 일방적 공유(그 말은 f에서 뭘 바꾼다 해도 a는 영향을 받지 않는다)를 하는 것이다.
# 이를 해결하려면 반댓말인 '깊은 복사(Deep copy)'를 하면 된다. 깊이 가 모든걸 복사하며 아예 독립적인 개체가 되게 된다.
deepCopiedF = deepcopy(a) # 깊은 복사를 한다.
a[0] = True
print(f'{deepCopiedF}') # 이제 더이상 방해를 받지 않게 된다.

t = (1, 2, 3, '4', '5') # 이 배열은 튜플인데, 바꾸거나 추가, 제거할수 없다. 그 외는 할수있다.
