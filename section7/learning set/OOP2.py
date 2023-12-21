# 파이썬 내에서 모든 것이 객체
num = 3.14
print (type(num))

# class와 instance, attribution
class sample : 
    # class object attribution 정의 (절대 속성)
    # 절대 속성은 초기 parameter에 영향을 미치지 않음 (self 안씀)
    state = 'living in earth' 
    
    def __init__ (self, name, age) : # attribution 정의 (사용자 정의 속성)
        self.name = name
        self.age = age
        
    def print_name(self) :
        print (self.name)
        
    def print_age(self) : 
        print (self.age)

obj1 = sample(name = "lky", age = 1) # instance 정의
obj1.print_name()
obj1.print_age()

obj2 = sample(name = "moraedooji", age = 0.5)
obj2.print_name()
obj2.print_age()

print (obj1.name, obj1.age)
print (obj2.name, obj2.age) # C언어 구조체 

print (obj1.state) # class object attribution 출력

# class 내에 있는 클래스 맴버도 출력 가능