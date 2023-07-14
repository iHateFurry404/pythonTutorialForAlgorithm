try: # 일단 시도는 해보는 코드이다.
    print(4 / 0)
except: # 위의 코드가 에러가 생긴다면 실행한다. except는 여러번 쓸수있으며, 옆에 정확한 에러명을 적을수 있다.
    print('Error')
else: # else는 위의 코드가 에러가 없을때 실행한다.
    print('이게 되네')
finally: # 에러가 나더라도 실행한다. finally 뒤에는 except, else를 쓸수없다.
    print('do flip')

try:
    a = [1]
    print(a[2])
except IndexError as i: # 에러를 변수에 저장해 할수도 있다.
    print(i)

# 가끔씩 에러를 발생시켜야할때가 있는데, 그때 raise를 쓰면 된다.
# raise IndexError

# 클래스로 에러를 뜨개 만들수도 있다. 아직은 이해를 안해도 되고 아 이런게 있구나만 알면 된다.
class doError(Exception):
    pass

class Erorr(Exception):
    def __str__(self):
        return '어허...'

def checkName(coolName):
    if coolName == '탈모':
        raise doError() # 혹은 doError()
    print(coolName)

# checkName('탈모') # 이렇게 해서 문제를 이르킬수 있다.
try: # 이렇게 예외를 만들수도 있다.
    checkName('발모')
    checkName('탈모')
except: # as ~~~를 쓰면 에러가 생긴다. 쓰려면 Erorr클래스와 같이 작성해야한다.
    print('어허...')
