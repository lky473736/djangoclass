# control_flow : 비교 및 제어
# 비교나 조건을 만들 땐 boolean expression을 사용 or truth value를 사용 
# 두 boolean expression을 connect => logical operater (논리 연산자)

print ((3>2) and (4 == 1)) # False
print ((1) == True or (1) != True) # True
print (1 in [1, 2, 3, 4, 5]) # True
print ([0, 1] not in [0, 1, 2, 3, 4]) # True

# if, elif, else (조건문)
# indentation : 들여쓰기 (refactoring에 중요)

print ("로그인 시스템")
account_list = {}

while True :
    print ("계정이 있다면 1, 계정이 없다면 0을 입력")
    mode = int(input())

    if mode == 1 : 
        print ("아이디와 비밀번호를 공백으로 구분하여 입력")
        id, pw = input().split()
        
        if id in account_list.keys() and account_list[id] == pw :
            print ('로그인 성공')
            break
            
        else :
            print ('로그인 실패')
        
    elif mode == 0 : 
        print ("새로 만들 아이디와 비밀번호를 공백으로 구분하여 입력")
        newid, newpw = input().split()
        
        if newid in account_list.keys() : 
            while newid not in account_list.keys() : 
                print ('아이디가 이미 존재. 새로 만들 아이디 다시 입력.')
                newid = input()
                
                print ('새로 만들 비밀번호 입력.')
                newpw = input()
            
        print ('회원가입 성공')
        account_list[newid] = newpw
            
        
        
    else :
        print ("입력 오류. 시스템 종료.")
        exit()