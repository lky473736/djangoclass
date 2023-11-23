'''
    dict : key-value pair
    고유 키를 특정 값에 배정
'''

dicti = {'chef' : 'amy', 'ceo' : 'jason', 'slist' : [1, 2, 3]} 
# key값은 언제나 string, 하지만 value값은 유동적임 (리스트, 문자열, 값, 튜플, 딕셔너리...)

print (dicti)
print (dicti['chef'].upper())
print (dicti['slist'])

dicti['daramji'] = 'naldaramji'
print (dicti)

# update value
dicti['chef'] = 'cinamoroll'
print (dicti)

print (dicti.keys()) # key 모음 리스트를 출력
print (dicti.values()) # value ''
print (dicti.items()) # tuple로 key-value 반환

print ('-' * 10)######################

# 중첩된 딕셔너리

mydict = {"PC" : {"notebook" : ['LG', 'SS', 'APPL'], 'tablet' : ['ipad', 'tab']}, "cat" : 'kitty'}

print (mydict['PC']['notebook'][0])