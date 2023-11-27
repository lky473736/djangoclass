# for : 반복문 (indexing)
# 3차원 구구단

cube_list = [] # 세제곱

for i in range (9) : 
    print (f'단수 : {i+1}')
    for j in range (9) :
        for k in range (9) : 
            print (f"{i+1} * {j+1} * {k+1} == {(i+1)*(j+1)*(k+1)}")
            
            if i == j == k :
                cube_list.append ((i+1, (i+1)*(j+1)*(k+1)))

print ('-' * 10)
print ('<cube_list>')

for i in cube_list : 
    print (f"cube {i[0]} = {i[1]}")
        