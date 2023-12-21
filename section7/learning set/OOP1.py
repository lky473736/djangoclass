# 객체 지향 프로그래밍
# -> class로 객체 정의 가능 (조직화하기 위함)

class NameOfClass() :
    # init : 클래스에 대한 인스턴스와 또는 초기화 호출
    def __init__ (self, param1, param2) :
        self.param1 = param1
        self.param2 = param2
        # self 키워드 사용하여 클래스의 특정 인스턴스에 parameter 할당
        # 이때 self.~는 클래스 맴버, 클래스 안에 정의된 변수
        
    def func1 (self) : 
        # 클래스 매소드의 parameter에 self가 들어있음 => 클래스 인스턴스의 정보를 사용 가능
        # (만약 클래스 매소드에서 클래스 맴버를 사용하지 않을 경우에도 self를 넣는 게 정석)
        # 클래스 안의 함수 = 클래스 매소드, 클래스 액트
        print (self.param1)
        
    def func2 (self) : 
        print (self.param1 + self.param2)
        
    def func3 (self, a) :
        print (self.param1 + a)
        
    def func4 (self) :
        print()
        
objecting = NameOfClass(1, 2)

objecting.func1()
objecting.func2()
objecting.func3(10)
objecting.func4()