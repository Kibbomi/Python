# C++ 에서 map과 개념이 거의 일치함 #
# C# 에서 dictionary와도 거의 일치 #

# Create #
d0 = dict()
d1 = {}
d2 = {1:'value1', 2:'value2',"key3":"value3"}
# key에는 변하지 않는 것들, string(Rvalue), int(Rvalue), tuple(Rvalue)들이 와야함. 

# Read #
print(d2[2])
print(d2.get(1))
print(d2.keys())    # key들을 dict_keys 객체로 반환
print(d2.values())  # value들을 list로 반환
print(d2.items())   # Key, Value Pair을 List<Tuple<key,value>>로 반환
print('key3' in d2) # 있으면 True, 없으면 False 반환



# Update #
d2[1] = 'value100'  # Dictionary 특정 Key의 값 변경하기
print(d2[1])
d2['Add'] = 'value10000'    # Dictionary에 추가하기
print(d2['Add'])


# Delete #
del d2['Add']
print(d2.get('Add'))    # get 함수는 없을 시 None을 반환


'''
생성
dict()
{}
{"key1":"value1", "key2" : 1, 100: "value3"}


읽기
['key']
.get('key')
.item()
.keys()
.values()


변경 & 추가
['key']= "newValue"

삭제
del d['key']
'''








