from abc import *

# 클래스 만들기
class person:
    classValue = 0 # 이게 클래스 속성이다.
    # 속성 만들기
    def __init__(self, name, age, iq): # self는 인스턴스를 말한다.
        self.name = name # 각각 설정한게 인스턴스 속성이고, 모든 인스턴스가 공유하는 값이 클래스 속성이다.
        self.age = age
        self.iq = iq
        self.__id = iq * 20 # 이건 비공개 속성이다. 클래스 메소드에서만 쓰일수 있다.
    
    # 클래스에 메소드를 만들수있다.
    def printInfo(self):
        print(f'name : {self.name} age : {self.age} iq : {self.iq} id : {self.__id}')

imGenius = person('ein sutain', 10, 1972) # 이게 인스턴스다.
imGenius.printInfo() # 메소드를 쓰는 예시

# 클래스 상속을 받으려면 ()안에 부모 클래스를 쓰면 된다.
class newPerson(person):
    # 부모 클래스의 메소드는 그대로 대물림받는다.
    def __init__(self, name, age, iq, birthday):
        self.name = name
        self.age = age
        self.iq = iq
        self.__id = iq * 20
        self.birthday = birthday
    # 메소드 오버라이딩은, 부모 클래스에 있는것을 재정의 하는것을 말한다. 부모 클래스에겐 영향을 미치진 못한다.
    def printInfo(self):
        print(f'name : {self.name} age : {self.age} iq : {self.iq} id : {self.__id} birthday : {self.birthday}')

imGenius2thGenReal = newPerson('ein sutain mr 2', 197, 32, 20771121)
imGenius2thGenReal.printInfo()

# 추상 클래스는 abc 모듈을 이용해 정말 정의만 하고 아무것도 안하고, 자식 클래스에게 재정의하도록 하는 이상한 클래스이다.
class newSuperMarioBrosPerson(metaclass = ABCMeta):
    """
    @property
    @abstractmethod
    def newSuperMarioBrosProperty(self):
        pass
    """
    @abstractmethod # 추상 메서드를 사용하려면 메서드를 쓰기전에 @abstractmethod를 쓴다.
    def printInfo(self):
        pass

# 이렇게 재정의 할수있다.
class newSuperMarioBrosPersonDeluxe(newSuperMarioBrosPerson):
    def printInfo(self):
        print('나는 사람이다 2023 우리들의 머리를 강타할 전설의 BLOCK버스터')

b = newSuperMarioBrosPersonDeluxe()
b.printInfo()
