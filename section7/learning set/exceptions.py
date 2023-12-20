# 에러와 예외 다루기
# try, except, finally문

# try문 : 말 그대로 한번 실행해보는 문
# except문 : try문에 오류가 있으면 실행됨 (에러를 지정해줄 수 있음)
# else문 : try문에서 오류가 없다면 실행됨
# finally문 : 오류와 상관없이 실행되는 마지막 문

try :
    i = 0
    arr = [1, 2, 3]
    
    while True :
        print (arr[i])
        i += 1
                  
except IndexError :
    print ("index error")
    
    try : 
        print ("daramji" + 10)
        
    except TypeError :
        print ("type error")
        
        try :
            print (1 + 1)
            
        except :
            print ("something error")
            
        else :
            print ('정상임')
        
finally : 
    print ("이건 항상 실행")