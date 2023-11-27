# while : 반복문 (not having indexing)
'''# 직각삼각형 출력

n = int(input("직각삼각형의 층수 입력 : "))
i = 1

while n >= i :
    print ('*' * i)
    i += 1'''
    
# 정사각형 출력
n = int(input("정사각형의 한 변의 길이 입력 : "))
i = 1

for i in range (n + 1) : 
    p = 1
    
    while i >= p : 
        print ('*' * i)
        p += 1
        
    print ('현재 정사각형의 넓이 : ', i ** 2)
    i += 1