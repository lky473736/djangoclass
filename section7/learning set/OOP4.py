# inheritance : 상속
# django 프레임워크를 상속을 통해 파생된 변형을 만드는 것

# 상속 : 기존 클래스를 새 커스텀 클래스로 전달
# 부모 클래스의 init 매소드나 이미 정의된 매소드의 사용을 그대로 물려받음

class person :
    def __init__ (self, firstname, lastname) :
        self.firstname = firstname 
        self.lastname = lastname
        
    def hello (self) :
        print ('hello!')
        
    def report (self) :
        print (f'I am {self.firstname} {self.lastname}')
        
class agent (person) : # person 클래스를 상속하겠다고 선언
    def reveal (self, passcode) :
        if passcode == self.firstname :
            print ("I am a secret agent")
            
        else :
            self.report() # report()를 상속받음
        
me = person ('daramji', 'hamster')
ag = agent ('daramji', 'hamster')

me.hello()
me.report()

ag.reveal ('daramji')