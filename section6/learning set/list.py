'''
list : component + indexing (다양한 자료형을 넣을 수 있음)
'''

var = 10
slist = [1, 2, 3, 4, 5, var]

print (slist[0 : 2]) # list도 슬라이싱 가능
print (slist[2 : 4])

'''
    append는 리스트 끝에 compo 추가 | slist.append(compo)
    insert는 리스트의 특정 위치에 compo 추가 | slist.insert(position, compo)
'''

slist.append (100)
print (slist)

slist.insert(2, 0) # 인덱싱 2에다가 0을 추가
print (slist)

'''
    pop은 특정 위치의 compo 없앰 | slist.pop(position) <- 비어있으면 마지막꺼 없앰
    remove는 compo가 처음으로 등장하는 compo를 지움 | slist.remove(compo)
'''

removing = slist.pop() # pop은 추후에 없앤 요소를 return함
print (slist, removing)

removing2 = slist.remove(3)
print (slist, removing2) # remove는 없앤 요소 return 안함