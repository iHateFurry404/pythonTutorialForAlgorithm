# 딕셔너리는 사전이라는 뜻이며, 사전처럼 찾을수있는 하나의 배열과 같다.
a = {1 : 2, '2' : 3} # a : b가 있으면, a는 키값, b는 밸류값이다.
print(a[1]) # 인덱스 할때는 키값으로 찾는다.
print(a['2'])
a['i broke the streak🗣️🗣️'] = 1972 # 키값, 밸류값은 무엇이 되도 상관이없다. 갑자기 1, 2, 3에서 19가 나올수도 있다는거다.
a[3] = 1234 # 이렇게 나중에 설정할수도 있다. 참고로 작성하는데 순서는 상관이 없다.
print(a['i broke the streak🗣️🗣️'])
print(a[3])

del a['i broke the streak🗣️🗣️'] # 이렇게 삭제할수도 있다. 리스트도 된다. 리스트는 삭제하고싶은 값의 인덱스를 입력하면 된다.

# 아래는 딕셔너리와 관련된 함수를 모아두었다.
print(a.keys()) # 키값만 뽑아낼수 있다.
print(a.values()) # 밸류값만 뽑아낼수 있다.
print(a.items()) # 둘다 뽑아낼수 있다.
print(a.get(3)) # 키에 맞는 밸류를 리턴한다. 찾으려는 키가 없을때 2번째 인수에 다른 인덱스를 써도 된다.
b = 'yes' if '1972' in a else 'sorry' # 이렇게 딕셔너리에 해당값이 있는지 찾아낼수 있다.
print(b)
a.clear() # a에 들어가있는것을 모두 삭제할수있다.
print(a)

# 리스트 컴프리헨션과 같이 딕셔너리 컴프리헨션이 있다. 그냥 for문에 값 몇개만 생기고 변수에 좀 생기는 수준이라 바로 이해가 될것이다.
c = {'김두한' : 1972, '심영' : 1121, '조병옥' : 112}
c = {name : death for name, death in c.items() if name != '조병옥'}
print(c)
c = {'김두한' : 1972, '심영' : 1121, '조병옥' : 112}
c = {name : 'Dead' if death > 1000 else 'not Dead' for name, death in c.items()}
print(c)
