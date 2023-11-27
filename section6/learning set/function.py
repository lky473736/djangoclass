'''
    def 함수명 (parameter) : 
        # 보통은 함수 정의 바로 다음 라인에 함수에 대한 설명을 쓰곤 함
        ~~~~~~~~
        ...
        return 리턴값
'''

def say_hello() : 
    print ('hello')
    
def return_hello() : 
    return 'hello'
        
helloval = return_hello()

print (helloval)
print (return_hello())
say_hello()

def cal(operator, p, q) : 
    match (operator) :
        case '+' : 
            return sum([p, q])
        
        case '-' :
            return max(p, q) - min(p, q) # show difference
        
        case '*' : 
            return p * q
        
        case '/' : 
            return int(p / q)

operator, p, q = input('operator, p, q : ').split()
print ('rst : ', cal(operator = operator, p = int(p), q = int(q)))
