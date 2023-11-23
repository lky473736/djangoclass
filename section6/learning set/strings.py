'''
    문자열은 일종의 문자의 sequence -> 따라러 문자열을 인덱싱, 슬라이싱할 수도 있음
    python에서 모든 요소는 객체이기 때문에 직접 호출 및 변환이 가능
    python에서 작은 따옴표랑 큰 따옴표는 상관 없음 (C 기반이랑 다르게)
'''

# print ('i'm man') # 이럴 때는 작은 따옴표가 안에 있으니깐 상식상으로 안됨
print ("i'm man") # 큰따옴표로 캡슐화하거나
print ('i\'m man') # escape character처리 하거나

print ('-' * 10) ########################

myvar = "Hello I am very sleepy now" 
# 자기 자신을 객체로 하고, 객체에 대한 매소드 호출 가능
# 속성 (attribute) : 객체의 특성 (속성에는 괄호가 필요 없음)

print (myvar.upper()) # 모든 문자 대문자
print (myvar.capitalize()) # 첫 문자 대문자
print (myvar.split()) # parameter로 readline한 행을 분할한 리스트 return (parameter가 없으면 공백으로 분할 / return된 리스트엔 parameter가 없음)
print (myvar + " example of concatanate") # concatanate
print (f"{myvar} because i am an animal and this season is winter") # format