# CRUD Of List #

# Create #

# Empty list #
l1 = list()
l2 = []

# param (list) #
l3 = [1,2,3,7,8,9]
l4 = list(l3) # l4 = [1,2,3,7,8,9]
l5 = list([3,4,5]) #  l5= [3,4,5]

# 각자의 메모리를 가지고 있음.
# l3을 변경한다고 해서 l4가 변경되지는 않음.


# Read #
print(l3[4]) # var[index]로 접근
print(l3.index(3)) # param이 어떤 index에 위치하는지 출력


# Update #
l3[4] = 100
print(l3[4])
l4.clear() # 모두 비우기 l4 = list()를 재선언 하는 것과 동일

l4.append(5)    # C++ push_back()과 동일함.
l4.extend(l3)   # l4 += l3 과 동일하며, concat하는 함수
l4.insert(0,1000)   # first : index, second : value, first에 second값을 insert함. list에서는 지양해야할 연산


# Delete #
l3.pop()    # C++ vector.pop_back()과 동일
l3.pop(3)   # C++ vector.remove(index)와 동일
l3.remove(1) # param과 일치하는 값을 삭제. 없다면 value error



# etc #
# sorting #
l4.sort()   # ascending, sort(reverse = true)
print (l4)
l4.sort(reverse = True) # descending
print (l4)

l5 = sorted(l4) # l4 is not changed. it just returns sorted l4


'''
생성
=list()
=[]

읽기 (read/indexing)
[x]
.index(x)

추가
append(x)
insert(i,x)
extend(list)

삭제
pop()
pop(i)
remove(x)

정렬
.sort()
.sort(reverse=True)
.sorted(list)
'''


