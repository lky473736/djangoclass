# method 

# 함수 : 일반적으로 자체 내장된 함수거나 사용자 지정 함수 (def)를 의미
# 매소드 : 클래스 내부에서 정의된 함수 (객체의 속성)

class circle :
    pi = 3.14
    
    def __init__ (self, radius = 1) :
        self.radius = radius
        
    def peri (self) : # 매소드의 parameter을 self로 설정 == 이 매소드에 argument를 사용
        return round(self.pi * (self.radius ** 2))
    
        # return circle.pi * (self.radius ** 2)
        # pi는 인스턴스와 상관 없이 변경되지 않으니 circle.pi라 작성해도 무관
    
    def leng (self) :
        result = round(circle.pi * self.radius * 2) # leng 매소드에만 적용되는 지역변수
        return result
    
    def update_radius (self, new) :
        self.radius = new # 속성 업데이트
        
cir1 = circle(radius = 5)
print (cir1.radius)
print (cir1.pi)

# --------------

print (cir1.peri())
print (cir1.leng())

# --------------

cir1.update_radius(3)

print (cir1.radius)
print (cir1.peri())
print (cir1.leng())