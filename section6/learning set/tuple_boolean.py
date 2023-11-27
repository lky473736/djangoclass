# tuple : immutable <- not supporting item assignment
# tuple을 수동으로 정의하지 않음 (보통은 잘 안쓰임) 
# 하지만 많은 내장함수 및 라이브러리 함수가 tuple로 값을 반환하곤 함 (불변성 때문에)

tup = (1, 2, 3)
print (tup)
# 이게 안됨 -> tup[1] = "two"

# boolean expression : 조건식
# 조건문 안에서 참과 거짓을 판별할 때 사용

a = True

print (int(a)) # 1이 출력
print (int(~a)) # ~ : 부정 연산자 NOT
print (int(1<2)) # 1이 출력